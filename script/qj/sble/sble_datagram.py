from script.qj.sble.sble_messages import messages

data = "0C0141EF0000008000000000"

data_head = data[0:8]
data_body = data[8:]

# 每两个字符为1个字节,切分为十六进制字符串列表
data_body_bytes = [data_body[i:i + 2] for i in range(0, len(data_body), 2)]

# 每个字节转为8位二进制字符串,高位在前
data_body_binary = [f'{int(byte, 16):08b}' for byte in data_body_bytes]

print(data_head)

# 报文位定义在 sble_messages.py 的 messages 字典中, 新增报文只需在该模块追加

# 匹配报文: MsgID 去前导0后精确匹配
msg = messages.get(data_head.upper().lstrip("0"))
if msg is None and len(data_head) == 8:
    # (4A~4D) 类报文的 MsgID 末字节随 SBMU 序号变化, 去掉末字节再匹配
    msg = messages.get(data_head[:6].upper().lstrip("0"))

if msg is not None:
    msg_name, sender, cycle, signals = msg
    print(f"\n报文ID: {data_head} = {msg_name} (发送方{sender}, 周期{cycle}ms, DLC=8)")
    # data_body_binary 每字节反转为 bit0 为最低位的位流(bit_stream[k] = bit k),
    # 按信号段切片后再反转(高位在前), 即得该信号的自然二进制值
    bit_stream = ''.join(byte[::-1] for byte in data_body_binary)
    for name, cn_name, start, length, factor, offset, val_table in signals:
        seg_bits = bit_stream[start:start + length][::-1]
        raw = int(seg_bits, 2)
        bit_range = f"bit{start}" if length == 1 else f"bit{start}~{start + length - 1}"
        line = f"{bit_range:<9}: {seg_bits:<32} {name:<33} {cn_name} = {raw}"
        if factor != 1 or offset != 0:
            # 物理值 = 原始值 * Factor + Offset
            phys = raw * factor + offset
            line += f" -> {f'{phys:.4f}'.rstrip('0').rstrip('.')}"
        if val_table is not None and raw in val_table:
            line += f" ({val_table[raw]})"
        print(line)
else:
    print(f"\n报文ID: {data_head} 未收录位定义")
