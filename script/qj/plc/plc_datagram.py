"""
解析PLC寄存器报文, 对照《重卡底盘-站控PLC-ModBus通用协议》Excel输出寄存器含义
Excel地址 = 40000 + 寄存器号
读取帧(PLC→站控): reg start=1040,length=120, value=[...], 表示站控收到从地址41040起的120个寄存器(41040~41159),
  value每元素为1个8bit字节, 相邻两元素合并为1个寄存器的16bit值(前元素为高字节, 寄存器值=前元素*256+后元素),
  length为寄存器数(value应有2*length个元素, 奇数个时忽略末尾多余字节), 逐位对照Excel定义解码
写入帧(站控→PLC): write reg 1 = 1, 表示向地址40001(心跳)写值1,
  数据说明列类型为int的寄存器(如40116 加解锁故障码/40117 加解锁尝试次数)写入值按int16有符号解读(65535即-1),
  值含义("N：含义"映射)优先于int16解读
read单帧(站控读取PLC): read reg=441,value=1080, 表示站控读取地址40441, 值为1080,
  备注含"参考PLC换电步序表单"的寄存器(如40441 RGV换电步序/40442 堆垛机换电步序)的值含义取自"PLC换电步序"表,
  如1080对应"码垛机步序-1080  升降缓存位低点",
  数据说明列类型为int的寄存器(如40342 螺丝枪加锁角度/40372 螺丝枪解锁次数/40478 RGV轴扭矩)值按int16有符号解读
  (报文按16bit无符号记录, 65535即-1, 值含义优先于int16解读), 备注含"乘于N/*N/除于N"缩放规则时换算实际值
read batch帧(站控批量读取PLC): read batch reg=140,value=[64511, 315, 0], 表示站控读取从地址40140起的3个寄存器(40140~40142),
  value第i个元素为寄存器(40140+i)的值(16个bit), 按数据说明列类型解码:
  "N-M号仓位/锁状态/状态位置/状态"类逐位输出编号状态(如"3号仓位在位"/"2号锁异常", 0/1状态词取备注"0正常，1异常"式说明),
  C列类型为int的寄存器(如40478 RGV轴扭矩)值为有符号整数(报文按16bit无符号记录, 65534即-2), 不逐位拆解,
  备注含"乘于N/*N/除于N"缩放规则时自动换算实际值(如扭矩值-2 -> 实际-0.02),
  C列类型为byte的寄存器(如40443 仓位水电连接头命令状态)值按位段拆字节分别解码: "byte,[N~M]位"标注的位段
  取对应8bit字节值(如258 -> 低字节2/高字节1), 每段按子行"N：含义"映射输出含义, 不逐位拆解,
  数据说明/备注含"N：含义"值映射的寄存器(如40130 PLC控制模式)输出值含义(如1000 -> 手动状态), 不逐位拆解

用法: result = parse_datagram(data, xlsx_path), data为报文字符串, xlsx_path为协议Excel文件路径(相对本脚本目录),
返回结构化解码结果(未收录定义时对应字段为None)
读取帧: {'type': 'read', 'start': 寄存器号, 'address_start'/'address_end': 起止地址, 'count': 寄存器数,
        'triggered': 触发位数, 'registers': [{'address': 地址, 'value': 寄存器值(相邻两字节合并: 前元素*256+后元素), 'bits': [{'bit': 位, 'state': 状态, 'desc': 定义}]}]}
写入帧: {'type': 'write', 'reg': 寄存器号, 'address': 地址, 'value': 写入值, 'int_value': int16值(非int型或命中值映射时为None), 'name': 功能, 'meaning': 值含义}
read单帧: {'type': 'read_reg', 'reg': 寄存器号, 'address': 地址, 'value': 值, 'int_value': int16值(非int型或命中值映射时为None), 'actual': 换算实际值(无缩放规则时为None), 'bytes': byte类位段子项列表(非byte类为None), 'name': 功能, 'meaning': 值含义, 'note': 说明}
read batch帧: {'type': 'batch', 'reg': 寄存器号, 'address_start'/'address_end': 起止地址, 'count': 寄存器数,
        'registers': [{'address': 地址, 'value': 值, 'name': 功能名, 'range': 范围说明, 'note': 值说明,
        'bits': [{'bit': 位, 'state': 状态, 'slot': 仓位号, 'desc': 仓位在位状态}]},
        int型寄存器项为{'address': 地址, 'value': 原始无符号值, 'int_value': 有符号值, 'actual': 换算实际值(无缩放规则时为None),
        'name': 功能名, 'range': 范围说明, 'note': 值说明, 'bits': None},
        byte类寄存器项为{'address': 地址, 'value': 寄存器值, 'bytes': [{'name': 子项名, 'range': 位段说明,
        'value': 字节值, 'meaning': 字节值含义(未收录时为None), 'note': 值说明}],
        'name': 功能名, 'range': 范围说明, 'note': 值说明, 'bits': None},
        值映射型寄存器项为{'address': 地址, 'value': 值, 'meaning': 值含义(未收录时为None),
        'name': 功能名, 'range': 范围说明, 'note': 值说明, 'bits': None}]}
"""
import os
import re
import zipfile
import xml.etree.ElementTree as ET

# 寄存器号与Excel地址的换算偏移
ADDRESS_OFFSET = 40000
# 读取帧(PLC→站控)与写入帧(站控→PLC)对应的寄存器定义工作表名
SHEET_NAME_READ = 'PLC→站控'
SHEET_NAME_WRITE = '站控→PLC'
# 换电步序值定义工作表名(40441 RGV换电步序/40442 堆垛机换电步序的值含义参考该表)
SHEET_NAME_STEP = 'PLC换电步序'
# 步序表索引备注标识: 备注含该标识的寄存器值含义参考"PLC换电步序"表, 该备注仅作解析依据不打印
STEP_NOTE_MARKER = '参考PLC换电步序表单'


# ============ 协议Excel解析 ============


def local_name(tag):
    """取XML标签的本地名(去掉命名空间)"""
    return tag.split('}')[-1]


def col_index(cell_ref):
    """单元格引用(如"C12")转为列下标(从0开始)"""
    letters = ''.join(ch for ch in cell_ref if ch.isalpha())
    index = 0
    for ch in letters:
        index = index * 26 + (ord(ch.upper()) - ord('A') + 1)
    return index - 1


def find_sheet_path(zip_file, sheet_name):
    """按工作表名在 workbook.xml 及其 rels 中定位对应的 sheet XML 路径"""
    workbook = ET.fromstring(zip_file.read('xl/workbook.xml'))
    rel_id = None
    for el in workbook.iter():
        # 表名比较忽略空格差异(如"站控 →PLC"与"站控→PLC")
        if local_name(el.tag) == 'sheet' and ''.join(el.attrib.get('name', '').split()) == ''.join(sheet_name.split()):
            rel_id = el.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            break
    if rel_id is None:
        raise KeyError('xlsx中未找到工作表: %s' % sheet_name)
    rels = ET.fromstring(zip_file.read('xl/_rels/workbook.xml.rels'))
    for rel in rels:
        if rel.attrib.get('Id') == rel_id:
            target = rel.attrib['Target'].lstrip('/')
            return target if target.startswith('xl/') else 'xl/' + target
    raise KeyError('xlsx中未找到工作表文件: %s' % sheet_name)


def load_shared_strings(zip_file):
    """读取共享字符串表(xlsx的文本单元格值统一存放在这里)"""
    strings = []
    if 'xl/sharedStrings.xml' in zip_file.namelist():
        root = ET.fromstring(zip_file.read('xl/sharedStrings.xml'))
        for si in root:
            strings.append(''.join(t.text or '' for t in si.iter() if local_name(t.tag) == 't'))
    return strings


def load_rows(zip_file, sheet_path, shared_strings):
    """读取工作表全部行, 返回二维文本列表(空单元格为'')"""
    rows = []
    root = ET.fromstring(zip_file.read(sheet_path))
    for el in root.iter():
        if local_name(el.tag) != 'row':
            continue
        cells = {}
        for cell in el:
            if local_name(cell.tag) != 'c':
                continue
            value = None
            for child in cell.iter():
                if local_name(child.tag) in ('v', 't'):
                    value = child.text
                    break
            if value is None:
                continue
            if cell.attrib.get('t') == 's':
                value = shared_strings[int(value)]
            cells[col_index(cell.attrib.get('r', 'A1'))] = value
        rows.append([cells.get(i, '') for i in range(max(cells) + 1)] if cells else [])
    return rows


def load_bit_defs(rows):
    """
    解析位图型寄存器定义, 返回 {Excel地址: [bit0~bit15描述]}, 未定义位为None
    行格式: 地址行(A列=地址, B列=0, C列=描述) + 后续各bit行(B列=1~15)
    """
    defs = {}
    current = None
    for row in rows:
        col_a = row[0].strip() if len(row) > 0 else ''
        col_b = row[1].strip() if len(row) > 1 else ''
        col_c = row[2].strip() if len(row) > 2 else ''
        if col_a.isdigit() and len(col_a) == 5:
            current = int(col_a)
            defs.setdefault(current, [None] * 16)
        elif col_a:
            # A列为其他文字(如分区标题行)时, 结束当前寄存器块
            current = None
        if current is not None and col_b.isdigit() and 0 <= int(col_b) <= 15:
            defs[current][int(col_b)] = col_c
    return defs


def parse_value_map(text):
    """
    解析"N：含义"式值映射文本, 返回 {值: 含义}, 全角/半角冒号均可,
    支持一行多个映射(如"0:无动作，1:下压中，2：抬起中，3：未知"/"0：无人 1：有人闯入")
    """
    values = {}
    if not text:
        return values
    matches = list(re.finditer(r'(\d+)\s*[：:]', text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        meaning = text[m.end():end].strip(' ，,、；;\n\t')
        if meaning:
            values[m.group(1)] = meaning
    return values


def load_value_defs(rows):
    """
    解析值映射型寄存器定义, 返回 {Excel地址: {'name': 功能, 'values': {值: 含义}, 'range': 数据说明}},
    行格式: 地址行(A列=地址, B列=功能, C列=数据说明) + 后续行(C/D列为值说明),
    值映射优先取C列(数据说明), D列(备注)中的映射一并收录(如40440流程回退的映射在D列),
    range为地址行C列原文(int/高字节等数据类型说明, 供int16解读判断)
    """
    defs = {}
    current = None
    for row in rows:
        col_a = row[0].strip() if len(row) > 0 else ''
        col_b = row[1].strip() if len(row) > 1 else ''
        col_c = row[2].strip() if len(row) > 2 else ''
        col_d = row[3].strip() if len(row) > 3 else ''
        if col_a.isdigit() and len(col_a) == 5:
            current = int(col_a)
            defs[current] = {'name': col_b, 'values': {}, 'range': col_c}
        elif col_a:
            # A列为其他文字(如分区标题行)时, 结束当前寄存器块
            current = None
        if current is None:
            continue
        if col_b and not defs[current]['name']:
            defs[current]['name'] = col_b
        defs[current]['values'].update(parse_value_map(col_c))
        defs[current]['values'].update(parse_value_map(col_d))
    return defs


def load_step_defs(rows):
    """
    解析"PLC换电步序"表的步序定义, 返回 {分区名: {步序值: B列原文}}, B列原文如"码垛机步序-1080  升降缓存位低点"
    行格式: 分区标题行(A列=分区名, 如"堆垛机换电步序") + 步序行(B列如"码垛机步序-1080  升降缓存位低点")
    """
    defs = {}
    current = None
    for row in rows:
        col_a = row[0].strip() if len(row) > 0 else ''
        col_b = row[1].strip() if len(row) > 1 else ''
        if col_a:
            current = col_a
            defs.setdefault(current, {})
        if current is None:
            continue
        m = re.match(r'^(\S*步序)\s*-\s*(\d+)\s+(.*)$', col_b)
        if m:
            defs[current][int(m.group(2))] = col_b
    return defs


def load_word_defs(rows):
    """
    解析单行寄存器定义(PLC→站控表), 返回 {Excel地址: {'name': 功能名, 'range': 范围说明, 'note': 值说明,
    'bytes': byte位段子行列表(如40443 仓位水电连接头命令状态下的仓位2子行, 无子行时为[])}}
    行格式: 地址 | 功能名 | 范围/bit说明 | 值说明, 如 40140|电池在位信号|1-16号仓位|每个bit位代表一个仓位...
    C列为"byte,[N~M]位"位段标注的寄存器下含多个byte位段子行(A列为空/B列为子项功能名/C列为位段标注),
    子行依次收集到'bytes'列表(如主行byte,[0~7]位取低8bit/子行byte,[8~15]位取高8bit)
    """
    defs = {}
    current = None
    for row in rows:
        col_a = row[0].strip() if len(row) > 0 else ''
        col_b = row[1].strip() if len(row) > 1 else ''
        col_c = row[2].strip() if len(row) > 2 else ''
        col_d = row[3].strip() if len(row) > 3 else ''
        # 地址行且B列为功能名文字(非bit号数字)时, 视为单行定义
        if col_a.isdigit() and len(col_a) == 5 and col_b and not col_b.isdigit():
            current = int(col_a)
            defs[current] = {'name': col_b, 'range': col_c, 'note': col_d, 'bytes': []}
        elif col_a:
            # A列为其他文字(如分区标题行)时, 结束当前寄存器块
            current = None
        elif current is not None and col_b and re.match(r'^byte', col_c, re.IGNORECASE):
            # byte位段子行(A列为空): C列为位段标注时, 收集到当前寄存器定义的'bytes'列表
            defs[current]['bytes'].append({'name': col_b, 'range': col_c, 'note': col_d})
    return defs


# ============ 报文解析与解码 ============

# 已解析的寄存器定义缓存, key为(帧类型, Excel绝对路径), 首次调用时加载
DEFS_CACHE = {}


def load_defs(kind, xlsx_path):
    """
    按帧类型懒加载协议Excel寄存器定义并缓存, 缓存按(帧类型, Excel路径)隔离
    kind: 'read'读取帧位图定义 / 'write'写入帧值映射定义(站控→PLC表)
          'word'单行寄存器定义 / 'read_value'值映射定义(均为PLC→站控表)
          'step'换电步序值定义(PLC换电步序表)
    xlsx_path: 协议Excel文件路径
    """
    cache_key = (kind, os.path.abspath(xlsx_path))
    if cache_key in DEFS_CACHE:
        return DEFS_CACHE[cache_key]
    if not os.path.isfile(xlsx_path):
        raise ValueError('未找到协议Excel: %s' % xlsx_path)
    if kind == 'write':
        sheet_name = SHEET_NAME_WRITE
    elif kind == 'step':
        sheet_name = SHEET_NAME_STEP
    else:
        sheet_name = SHEET_NAME_READ
    with zipfile.ZipFile(xlsx_path) as zf:
        shared_strings = load_shared_strings(zf)
        sheet_rows = load_rows(zf, find_sheet_path(zf, sheet_name), shared_strings)
    if kind == 'write':
        defs = load_value_defs(sheet_rows)
    elif kind == 'word':
        defs = load_word_defs(sheet_rows)
    elif kind == 'read_value':
        defs = load_value_defs(sheet_rows)
    elif kind == 'step':
        defs = load_step_defs(sheet_rows)
    else:
        defs = load_bit_defs(sheet_rows)
    DEFS_CACHE[cache_key] = defs
    return defs


def to_int16(value):
    """16bit无符号值按int16有符号解读, 高位置1时按补码转负数(65535即-1)"""
    return value - 0x10000 if value > 0x7FFF else value


def parse_scale_factor(note):
    """解析备注中"乘于N/*N/除于N"式缩放规则, 返回倍数N(无规则时为None)"""
    if not note:
        return None
    m = re.search(r'(?:乘于|\*)\s*(\d+)|除于\s*(\d+)', note)
    return int(m.group(1) or m.group(2)) if m else None


def build_byte_items(value, word):
    """
    拆分byte类寄存器值(如40443 仓位水电连接头命令状态)为位段子项列表, 非byte类寄存器返回None:
    'range'为"byte,[N~M]位"式位段标注(如byte,[0~7]位取低8bit/byte,[8~15]位取高8bit),
    子项取寄存器值对应位段的字节值, 并按该子项'note'的"N：含义"映射换算含义(未收录时为None),
    子项列表 = 主行定义(如仓位1) + 'bytes'中各子行定义(如仓位2)
    """
    if not word or not word['range'].strip().lower().startswith('byte'):
        return None
    items = []
    for sub in [{'name': word['name'], 'range': word['range'],
                 'note': word['note']}] + word['bytes']:
        m = re.search(r'[\[［]\s*(\d+)\s*[~～]\s*(\d+)\s*[\]］]', sub['range'])
        if not m:
            continue
        low_bit, high_bit = int(m.group(1)), int(m.group(2))
        sub_value = (value >> low_bit) & ((1 << (high_bit - low_bit + 1)) - 1)
        items.append({'name': sub['name'], 'range': sub['range'],
                      'value': sub_value,
                      'meaning': parse_value_map(sub['note']).get(str(sub_value)),
                      'note': sub['note']})
    return items or None


def build_read_result(data_address, data_body, bit_defs):
    """
    构建读取帧(PLC→站控)结构化解码结果: value每元素为1个8bit字节, 相邻两元素合并为1个
    16bit寄存器值(前元素为高字节, 寄存器值=前元素*256+后元素), 第i个寄存器对应地址(起始地址+i),
    length为寄存器数(value元素个数为其2倍, 奇数个时忽略末尾多余字节), 逐位对照Excel位图定义,
    未收录定义时desc为None
    """
    start = ADDRESS_OFFSET + data_address
    count = len(data_body) // 2
    end = start + count - 1
    triggered = 0
    registers = []
    for i in range(count):
        value = data_body[2 * i] * 0x100 + data_body[2 * i + 1]
        reg = start + i
        bits = bit_defs.get(reg)
        bit_list = []
        for bit in range(16):
            state = (value >> bit) & 1
            if state:
                triggered += 1
            bit_list.append({'bit': bit, 'state': state,
                             'desc': bits[bit] if bits and bits[bit] else None})
        registers.append({'address': reg, 'value': value, 'bits': bit_list})
    return {'type': 'read', 'start': data_address, 'address_start': start,
            'address_end': end, 'count': count, 'triggered': triggered,
            'registers': registers}


def build_write_result(data_address, value, value_defs):
    """
    构建写入帧(站控→PLC)结构化解码结果: 寄存器功能名与写入值的含义, 未收录时为None,
    数据说明列类型为int的寄存器(如40116 加解锁故障码/40117 加解锁尝试次数)写入值按int16
    有符号解读(65535即-1), 值含义("N：含义"映射)优先于int16解读
    """
    reg = ADDRESS_OFFSET + data_address
    info = value_defs.get(reg)
    meaning = info['values'].get(str(value)) if info else None
    int_value = None
    if meaning is None and info and info['range'].strip().lower().startswith('int'):
        # int型寄存器: 写入值为有符号int16, 高位置1时按补码转负数(65535即-1)
        int_value = to_int16(value)
    return {'type': 'write', 'reg': data_address, 'address': reg, 'value': value,
            'int_value': int_value,
            'name': info['name'] if info else None,
            'meaning': meaning}


def build_batch_result(data_address, data_body, word_defs, value_defs):
    """
    构建 read batch 帧结构化解码结果: 站控批量读取PLC寄存器,
    value每元素为一个寄存器(16bit)的值, 第i个元素对应地址(起始地址+i), 按数据说明列类型解码:
    C列类型为int的寄存器(如40478 RGV轴扭矩)值为有符号整数(报文按16bit无符号记录, 65534即-2),
    不逐位拆解, 备注含"乘于N/*N/除于N"缩放规则时换算实际值(如扭矩-2 -> -0.02), bits为None;
    C列类型为byte的寄存器(如40443 仓位水电连接头命令状态)值按位段拆字节分别解码, 子项列表在'bytes'字段, bits为None;
    数据说明/备注含"N：含义"值映射的寄存器(如40130 PLC控制模式)输出值含义, bits为None;
    "N-M号仓位/锁状态/状态位置/状态"类逐位输出编号状态(slot为编号), 0/1状态词取备注"0正常，1异常"式说明;
    其余寄存器逐位输出, desc为Excel说明
    """
    start = ADDRESS_OFFSET + data_address
    end = start + len(data_body) - 1
    triggered = 0
    registers = []
    for i, value in enumerate(data_body):
        reg = start + i
        info = word_defs.get(reg)
        range_text = info['range'] if info else None
        note = info['note'] if info else None
        if range_text and range_text.strip().lower().startswith('int'):
            # int型寄存器: 值为有符号int16, 高位置1时按补码转负数(65534即-2)
            int_value = to_int16(value)
            factor = parse_scale_factor(note)
            actual = int_value / factor if factor else None
            registers.append({'address': reg, 'value': value, 'int_value': int_value,
                              'actual': actual,
                              'name': info['name'] if info else None,
                              'range': range_text, 'note': note, 'bits': None})
            continue
        byte_items = build_byte_items(value, info)
        if byte_items:
            # byte类寄存器(如40443 仓位水电连接头命令状态): 值按位段拆字节分别解码
            registers.append({'address': reg, 'value': value, 'bytes': byte_items,
                              'name': info['name'] if info else None,
                              'range': range_text, 'note': note, 'bits': None})
            continue
        value_info = value_defs.get(reg)
        if value_info and value_info['values']:
            # 值映射型寄存器(如40130 PLC控制模式): 值含义取"N：含义"映射, 不逐位拆解
            registers.append({'address': reg, 'value': value,
                              'meaning': value_info['values'].get(str(value)),
                              'name': value_info['name'] or (info['name'] if info else None),
                              'range': range_text, 'note': note, 'bits': None})
            continue
        slot_start = None
        slot_word = None
        off_word, on_word = '正常', '异常'
        if range_text:
            for pattern, word in ((r'(\d+)\s*-\s*\d+号仓位', '号仓位'),
                                  (r'(\d+)\s*-\s*\d+锁状态', '号锁'),
                                  (r'(\d+)\s*-\s*\d+状态位置', '号位置'),
                                  (r'(\d+)\s*-\s*\d+状态', '号位')):
                m = re.match(pattern, range_text)
                if m:
                    slot_start = int(m.group(1))
                    slot_word = word
                    break
        if slot_start is not None and slot_word != '号仓位' and note:
            # 位图说明"0正常，1异常"式: 提取0/1状态词(如"0关闭，1打开")
            m = re.search(r'0\s*(\S+?)[，,]\s*1\s*(\S+)', note)
            if m:
                off_word, on_word = m.group(1), m.group(2)
        bit_list = []
        for bit in range(16):
            state = (value >> bit) & 1
            if state:
                triggered += 1
            if slot_start is not None:
                if slot_word == '号仓位':
                    desc = '%d%s%s' % (slot_start + bit, slot_word,
                                       '在位' if state else '不在位')
                else:
                    desc = '%d%s%s' % (slot_start + bit, slot_word,
                                       on_word if state else off_word)
            else:
                desc = note
            bit_list.append({'bit': bit, 'state': state,
                             'slot': slot_start + bit if slot_start is not None else None,
                             'desc': desc})
        registers.append({'address': reg, 'value': value,
                          'name': info['name'] if info else None,
                          'range': range_text, 'note': note, 'bits': bit_list})
    return {'type': 'batch', 'reg': data_address, 'address_start': start,
            'address_end': end, 'count': len(data_body), 'triggered': triggered,
            'registers': registers}


def build_read_reg_result(data_address, value, word_defs, read_value_defs, step_defs=None):
    """
    构建 read 单帧结构化解码结果: 站控读取单个PLC寄存器, 功能名/值含义/说明未收录时为None,
    值含义优先取值映射定义, 无映射且备注含"参考PLC换电步序表单"时取step_defs中指定分区的
    步序定义(备注如"参考PLC换电步序表单——RGV步序", 指定分区未收录时回退唯一分区);
    数据说明列类型为int的寄存器(如40342 螺丝枪加锁角度/40372 螺丝枪解锁次数/40478 RGV轴扭矩)
    值按int16有符号解读(报文按16bit无符号记录, 65535即-1, 值含义优先于int16解读),
    备注含"乘于N/*N/除于N"缩放规则时换算实际值(如扭矩-2 -> -0.02);
    byte类寄存器(如40443 仓位水电连接头命令状态)值按位段拆字节解码, 子项列表在'bytes'字段
    """
    reg = ADDRESS_OFFSET + data_address
    word = word_defs.get(reg)
    value_info = read_value_defs.get(reg)
    note = word['note'] if word else None
    byte_items = build_byte_items(value, word)
    meaning = None
    int_value = None
    actual = None
    if byte_items is None:
        meaning = value_info['values'].get(str(value)) if value_info else None
        if meaning is None and step_defs is not None and note:
            section = note.split('——')[-1].strip()
            steps = step_defs.get(section)
            if steps is None and len(step_defs) == 1:
                steps = list(step_defs.values())[0]
            meaning = steps.get(value) if steps else None
        if meaning is None and word and word['range'].strip().lower().startswith('int'):
            # int型寄存器: 值为有符号int16, 高位置1时按补码转负数(65535即-1)
            int_value = to_int16(value)
            factor = parse_scale_factor(note)
            actual = int_value / factor if factor else None
    return {'type': 'read_reg', 'reg': data_address, 'address': reg, 'value': value,
            'int_value': int_value, 'actual': actual, 'bytes': byte_items,
            'name': (value_info or word or {}).get('name'),
            'meaning': meaning,
            'note': note}


def parse_datagram(data, xlsx_path):
    """
    解析PLC寄存器报文帧(入口), data为报文字符串, xlsx_path为协议Excel文件路径,
    自动识别帧类型并返回结构化解码结果:
    读取帧(PLC→站控) "reg start=1040,length=120, value=[...]"      -> build_read_result 结果
    写入帧(站控→PLC) "write reg 1 = 1"                            -> build_write_result 结果
    read单帧(站控读PLC) "read reg=441,value=1080"                 -> build_read_reg_result 结果
    read batch帧(站控批量读PLC) "read batch reg=140,value=[...]"  -> build_batch_result 结果
    """
    xlsx_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), xlsx_path)

    if data.startswith('write reg'):
        # 写入帧(站控写入PLC): write reg 1 = 1, 表示站控把值1写入寄存器1
        # data_address 为 data 中的寄存器号, value 为 data 中的写入值
        data_address = int(data.replace('write reg', '').split('=')[0].strip())
        value = int(data.split('=')[1].strip())
        return build_write_result(data_address, value, load_defs('write', xlsx_path))
    if data.startswith('read batch reg='):
        # read batch帧(站控批量读取PLC): read batch reg=140,value=[64511, 315, 0]
        # data_address 为 data 中的 reg(起始寄存器号), data_body 为 data 中的 value
        data_address = int(data.split('reg=')[1].split(',')[0])
        data_body = [int(x) for x in data.split('value=')[1].strip('[]').split(',')]
        return build_batch_result(data_address, data_body, load_defs('word', xlsx_path),
                                  load_defs('read_value', xlsx_path))
    if data.startswith('read reg='):
        # read单帧(站控读取PLC): read reg=441,value=1080, 表示站控读取地址40441
        # data_address 为 data 中的寄存器号, value 为 data 中的读取值
        data_address = int(data.split('reg=')[1].split(',')[0])
        value = int(data.split('value=')[1])
        word_defs = load_defs('word', xlsx_path)
        # 备注含"参考PLC换电步序表单"的寄存器(40441 RGV换电步序/40442 堆垛机换电步序),
        # 值含义从"PLC换电步序"表的步序定义解析
        step_defs = None
        word = word_defs.get(ADDRESS_OFFSET + data_address)
        if word and STEP_NOTE_MARKER in word['note']:
            step_defs = load_defs('step', xlsx_path)
        return build_read_reg_result(data_address, value, word_defs,
                                     load_defs('read_value', xlsx_path), step_defs)
    # 读取帧(PLC→站控): reg start=1040,length=120, value=[...]
    # data_address 为 data 中的 start, data_body 为 data 中的 value
    data_address = int(data.split("start=")[1].split(",")[0])
    data_body = [int(x) for x in data.split("value=")[1].strip("[]").split(",")]
    return build_read_result(data_address, data_body, load_defs('read', xlsx_path))


def print_byte_items(byte_items, indent=''):
    """打印byte类寄存器(如40443 仓位水电连接头命令状态)的位段子项: 子项名 = 字节值 (含义)"""
    for item in byte_items:
        line = '%s%s = %d' % (indent, item['name'], item['value'])
        if item['meaning']:
            line += ' (%s)' % item['meaning']
        else:
            line += ' （未收录该值说明）'
        print(line)


def print_result(result):
    """打印 parse_datagram 的结构化结果(调试用), 读取帧逐寄存器输出全部16位"""
    if result['type'] == 'write':
        print('\n寄存器帧: write reg %d = %d -> 地址%d'
              % (result['reg'], result['value'], result['address']))
        if result['name'] is None:
            print('%d = %d   未收录寄存器定义' % (result['address'], result['value']))
            return
        display = result['int_value'] if result['int_value'] is not None else result['value']
        line = '%d %s = %d' % (result['address'], result['name'], display)
        if result['int_value'] is not None and result['int_value'] != result['value']:
            # 负数由16bit无符号原始值按补码转换而来, 附注原始值
            line += ' (原始值%d)' % result['value']
        if result['meaning']:
            line += ' (%s)' % result['meaning']
        elif result['int_value'] is None:
            line += ' （未收录该值说明）'
        print(line)
        return
    if result['type'] == 'read_reg':
        print('\n寄存器帧: read reg %d = %d -> 地址%d'
              % (result['reg'], result['value'], result['address']))
        if result['name'] is None:
            print('%d = %d   未收录寄存器定义' % (result['address'], result['value']))
            return
        if result['bytes']:
            # byte类寄存器: 值按位段拆字节解码, 输出寄存器整体值后逐位段输出子项
            print('%d %s = %d' % (result['address'], result['name'], result['value']))
            print_byte_items(result['bytes'], indent='  ')
            return
        display = result['int_value'] if result['int_value'] is not None else result['value']
        line = '%d %s = %d' % (result['address'], result['name'], display)
        if result['int_value'] is not None and result['int_value'] != result['value']:
            # 负数由16bit无符号原始值按补码转换而来, 附注原始值
            line += ' (原始值%d)' % result['value']
        if result['meaning']:
            line += ' (%s)' % result['meaning']
        elif result['actual'] is not None:
            line += '  实际值 %s' % ('%g' % result['actual'])
        # 步序表索引类备注(如"参考PLC换电步序表单——RGV步序")仅作解析依据, 不打印
        if result['note'] and STEP_NOTE_MARKER not in result['note']:
            line += '   %s' % result['note']
        print(line)
        return
    if result['type'] == 'batch':
        print('\n寄存器帧: read batch reg=%d -> 地址%d, 寄存器数量%d (地址%d~%d)'
              % (result['reg'], result['address_start'], result['count'],
                 result['address_start'], result['address_end']))
        for register in result['registers']:
            if register['bits'] is None:
                if 'int_value' in register:
                    # int型寄存器: 输出有符号值与换算后的实际值, 不逐位拆解
                    line = '地址%d = %d' % (register['address'], register['int_value'])
                    if register['int_value'] != register['value']:
                        # 负数由16bit无符号原始值按补码转换而来, 附注原始值
                        line += ' (原始值%d)' % register['value']
                    if register['name']:
                        line += '  %s' % register['name']
                    if register['actual'] is not None:
                        line += '  实际值 %s' % ('%g' % register['actual'])
                    if register['note']:
                        line += '  %s' % register['note']
                    print(line)
                elif 'bytes' in register:
                    # byte类寄存器: 值按位段拆字节解码, 输出寄存器整体值后逐位段输出子项
                    line = '地址%d = %d' % (register['address'], register['value'])
                    if register['name']:
                        line += '  %s' % register['name']
                    print(line)
                    print_byte_items(register['bytes'], indent='  ')
                else:
                    # 值映射型寄存器: 输出值含义(备注即映射来源, 不重复输出)
                    line = '地址%d = %d' % (register['address'], register['value'])
                    if register['name']:
                        line += '  %s' % register['name']
                    if register['meaning']:
                        line += ' (%s)' % register['meaning']
                    else:
                        line += ' （未收录该值说明）'
                    print(line)
                continue
            line = '地址%d = %d' % (register['address'], register['value'])
            if register['name']:
                line += '  %s' % register['name']
            if register['range']:
                line += ' %s' % register['range']
            print(line)
            for bit_info in register['bits']:
                desc = bit_info['desc'] if bit_info['desc'] else '（Excel中无此位定义）'
                print('  第%2d位: %d  %s' % (bit_info['bit'], bit_info['state'], desc))
        tail = '其中 %d 位为1' % result['triggered'] if result['triggered'] else '无'
        print('共 %d 个寄存器 (地址%d~%d), %s'
              % (result['count'], result['address_start'], result['address_end'], tail))
        return
    print('\n寄存器帧: %d -> 地址%d, 寄存器数量%d (地址%d~%d)'
          % (result['start'], result['address_start'], result['count'],
             result['address_start'], result['address_end']))
    for register in result['registers']:
        print('地址%d = %d' % (register['address'], register['value']))
        for bit_info in register['bits']:
            desc = bit_info['desc'] if bit_info['desc'] else '（Excel中无此位定义）'
            print('  第%2d位: %d  %s' % (bit_info['bit'], bit_info['state'], desc))
    tail = '其中 %d 位触发' % result['triggered'] if result['triggered'] else '无触发'
    print('共 %d 个寄存器 (地址%d~%d), %s'
          % (result['count'], result['address_start'], result['address_end'], tail))


if __name__ == '__main__':
    xlsx_path = '重卡底盘-站控PLC-ModBus通用协议 - V3.0站 -V1.10-20260901.xlsx'

    # data = "write reg 1 = 1"

    # data = "write reg 116 = 65535"

    # data = "reg start=1040,length=2, value=[0, 3, 1, 0]"

    # data = "read batch reg=140,value=[64511, 315, 0]"

    # data = "read reg=441,value=1080"

    # data = "read reg=342,value=65535"

    # data = "read reg=443,value=258"

    data = "read batch reg=443,value=[258]"
    # data = "read batch reg=478,value=[2, 0, 3, 0, 1, 3, 0, 65534, 1, 3, 65534, 3, 7, 8, 8, 19, 23, 22, 24, 19, 22, 0, 0, 2, 4, 0, 0, 86, 0, 0, 0]"

    print_result(parse_datagram(data, xlsx_path))



