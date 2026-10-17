# auto-test-CLI 项目文档

> 换电站自动化测试工具 | Python 3.6.8 | Git: refact-1.1

---

## 1. 项目概述

### 1.1 简介

auto-test-CLI 是面向乘用车换电站站控系统的自动化测试工具，服务于"时代电服"（CATL旗下）。项目核心能力包括：

1. **Swagger → API 客户端自动生成**：从 Swagger 2.0 JSON 文档生成 Python HTTP 客户端代码
2. **关键字字典自动生成**：将业务源文件（WSS/ACT/API/NCS/TC）通过 AST 解析转换为可复用的关键字字典
3. **HTTP/HTTPS 通信**：封装站控 API 请求，支持 Bearer Token 鉴权
4. **WebSocket 实时通信**：支持新站（/ws）和旧站（/manager/webSocketOfManager 等）的 WSS 消息收发
5. **Nacos 配置中心管理**：读写换电站各微服务的 Nacos 配置
6. **远程 Shell/SQL 执行**：通过 HTTP 接口调用测试服务执行预定义的 Shell 命令和 SQL 查询

### 1.2 技术栈

| 库 | 版本 | 用途 |
|---|---|---|
| loguru | latest | 日志记录（控制台 + 文件按日轮转） |
| pytest | latest | 单元测试框架 |
| pytz | latest | 时区处理（Asia/Shanghai） |
| requests | latest | HTTP 客户端 |
| websockets | latest | WebSocket 协议（sync.client） |

### 1.3 快速开始

```bash
# 创建虚拟环境（Python 3.6.8）
python -m venv .venv

# 激活虚拟环境
.venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 执行所有转换任务（Swagger + 5类关键字）
python convertAllFile.py
```

> **注意**：项目必须位于名为 `auto-test-CLI` 的目录中，`GetProject.get_project_path()` 通过向上查找该目录名定位项目根路径。

### 1.4 环境配置

编辑 `env.json`，修改 `useEnv` 字段切换当前环境：

| 环境 | 说明 |
|---|---|
| test | 主测试环境（默认） |
| test01 | test01 环境 |
| test03 | test03 环境 |
| him/him01/him03 | HIM 环境（配置待填充） |
| other | 其他环境（配置待填充） |

每个环境包含字段：`company`、`host`、`host_authorization`、`nacos`、`nacos_accessToken`、`wss`

---

## 2. 架构设计

### 2.1 分层架构

```
auto-test-CLI/
├── .venv/                     # 虚拟环境（Python 3.6.8）
├── convertAllFile.py          # 入口脚本（6个转换任务）
├── env.json                    # 多环境配置
├── requirements.txt            # 依赖声明
├── common/                     # 公共基础层
│   ├── handlerKw/              #   关键字处理引擎
│   ├── handlerSwagger/        #   Swagger → API 代码生成
│   ├── http/                   #   HTTP 请求封装
│   └── utils/                  #   工具函数库
├── company/
│   ├── qkl/new/                # 新站业务（v3 微服务架构）
│   │   ├── common/             #   API/NCS/WSS/SH/Utils 共享层
│   │   ├── kw/                 #   WSS 关键字字典
│   │   ├── source/swaggerApi/ #   Swagger JSON 源文件
│   │   └── version/v3/        #   业务版本层（act/dao/ts/kw）
│   ├── qkl/old/                # 旧站业务（v1 单体架构）
│   │   ├── common/             #   API/WSS/Utils 共享层
│   │   ├── kw/                 #   WSS 关键字字典
│   │   ├── source/swaggerApi/ #   Swagger JSON 源文件
│   │   └── version/v1/        #   业务版本层（act/dao/ts/kw）
│   └── qj/                     # 另一家公司占位（仅 __init__.py）
└── documents/                  # 项目文档
```

### 2.2 四层业务模型（version 层内）

```
┌─────────────────────────────────────────────────────────┐
│  ts/（测试脚本层）                                        │
│  test_*.py → 导入 kw 字典 → RunKw.act_run() 执行关键字    │
├─────────────────────────────────────────────────────────┤
│  act/（业务动作层）                                       │
│  按模块组织 → @KwDecorator 标注 → RunKw.api_run() 调用API │
├─────────────────────────────────────────────────────────┤
│  dao/（数据访问层）                                       │
│  api/set_*.py → 封装业务请求数据                          │
│  ncs/ncs_*.py → 封装 Nacos 配置模板                      │
├─────────────────────────────────────────────────────────┤
│  kw/（关键字层，自动生成）                                 │
│  kw_act/ kw_api/ kw_ncs/ kw_tc/                         │
│  Key* = {"描述": HandlerKw.kw(Class.method), ...}       │
└─────────────────────────────────────────────────────────┘
```

### 2.3 新旧版本差异

| 特性 | 新站 v3 (company/qkl/new) | 旧站 v1 (company/qkl/old) |
|---|---|---|
| 架构 | 微服务，每个服务独立配置 | 单体，API 集中在 api_manager |
| API 客户端数 | 15 个（battery/camera/dcci/...） | 8 个（manager/cloud/rbc/...） |
| Nacos 配置 | 7 个配置文件 | 无（仅占位） |
| WSS 接口 | /ws（统一入口） | /manager/webSocketOfManager 等 3 个 |
| Shell/SQL | 通过 /autotest 服务执行 | 无（仅占位） |
| ACT 模块数 | 9 个 | 15 个 |
| TS 模块数 | 9 个 | 17 个 |
| 鉴权方式 | Bearer Token + MD5 动态密码 | Bearer Token |

---

## 3. 公共层详解（common/）

### 3.1 关键字处理引擎（handlerKw/）

#### KwDecorator 装饰器

为方法添加 `keyword_description` 属性，用于标记需要转换为关键字的方法。

```python
@staticmethod
@KwDecorator("获取currentProcessData的wss消息")
def current_process_data_wss():
    ...
```

- `@staticmethod` 放在 `@KwDecorator` **之前**（外层）
- 描述必须是中文字符串

#### ConvertKeyKw 转换器

使用 Python AST 解析源文件，提取 `@KwDecorator` 装饰的方法和参数，生成关键字字典文件。

**路径映射规则：**

| 源目录 | 输出目录 | 文件名规则 |
|---|---|---|
| common/wss/ | kw/ | xxx.py → key_xxx.py |
| version/*/act/ | version/*/kw/kw_act/ | xxx.py → key_xxx.py |
| version/*/dao/api/ | version/*/kw/kw_api/ | set_xxx.py → key_set_xxx.py |
| version/*/dao/ncs/ | version/*/kw/kw_ncs/ | ncs_xxx.py → key_ncs_xxx.py |
| version/*/ts/ | version/*/kw/kw_tc/ | test_xxx.py → key_test_xxx.py |

**生成的关键字字典格式：**

```python
from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.common.wss.new_wss import NewWss

KeyNewWss = {
    "获取currentProcessData的wss消息": HandlerKw.kw(NewWss.current_process_data_wss),
    "获取fireMoveWarn的wss消息": HandlerKw.kw(NewWss.fire_move_warn_wss),
    "获取underBox的wss消息": HandlerKw.kw(NewWss.under_box_wss),
    "获取volume的wss消息": HandlerKw.kw(NewWss.volume_wss),
}
```

#### HandlerKw 关键字封装

```python
HandlerKw.kw(func)  # 返回 lambda *args: func(*args)
```

#### RunKw 关键字执行器

```python
RunKw.ts_run(action_list, keyword, *args)    # 测试脚本执行
RunKw.act_run(action_list, keyword, *args)   # 业务动作执行
RunKw.api_run(action_list, keyword, *args)   # API 调用执行
RunKw.tools_run(action_list, keyword, *args) # 工具方法执行
```

所有方法内部调用 `__run(action_list, keyword, *args)` 查找关键字字典并执行。

### 3.2 Swagger 代码生成（handlerSwagger/）

解析 Swagger 2.0 JSON，为每个 API 服务生成 Python 客户端代码。

**生成流程：**

```
source/swaggerApi/*.json
  → ConvertApiDoc(json_file_path)
  → _extract_api_info() 解析 paths/methods/parameters
  → write_api() 生成 Python 代码
  → common/api/api_*.py
```

**生成代码结构：**

```python
from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod

class ApiXxx:
    @staticmethod
    def _get_path(path):
        service = '/xxx'
        return service + path

    @staticmethod
    def api_xxx_method(data):
        """API描述
        请求参数:
            param1: string [必填] - 参数说明
        """
        path = f'/api/xxx/method'
        return HttpRq.req(*HttpMethod.http_info(ApiXxx._get_path(path), 'POST', data))
```

### 3.3 HTTP 请求（http/）

#### HttpMethod

构建请求元组：`(path, method, data)`

#### HttpRq

执行 HTTP 请求，自动处理 Authorization 头和响应日志。

```python
HttpRq.req(path, method, data, other_authorization=None)
```

- 从 `HandleEnv` 读取 host 和 authorization
- 支持 GET（params）、POST/DELETE（json body）
- 自动检查响应 `code == 200` 判断成功
- `other_authorization` 参数可覆盖默认 Authorization（用于动态密码鉴权）

### 3.4 工具函数（utils/）

| 文件 | 类 | 核心方法 |
|---|---|---|
| handleEnv.py | HandleEnv | get_env_host() / get_env_authorization() / get_env_nacos() / get_env_wss() / get_env_company() |
| handlerNacos.py | HandlerNacos | NacosReq(path, method, data) — GET/POST/DELETE 请求 |
| handlerWss.py | HandlerWss | Wss_New(userId, path, data) / Wss_old(path) |
| handlerFile.py | HandlerFile | create_dir() / read_json() / get_env_path() |
| handlerAssert.py | HandlerAssert | equal / not_equal / include / not_include / true / not_true |
| logConfig.py | LogConfig | 日志配置，loguru 输出到控制台 + 文件（logs/{日期}.log） |
| getProject.py | GetProject | get_project_path() — 向上查找 'auto-test-CLI' 目录 |
| tools/handlerDataType.py | HandlerDataType | float_to_2shorts / uint16_to_2shorts / uint16_to_short / uint32_to_2shorts |
| tools/handlerEncrypt.py | HandlerEncrypt | md5_encrypt(text) |
| tools/handlerTime.py | HandlerTime | time_now_timestamp / time_now_time / get_now_date |

---

## 4. 新站业务层（company/qkl/new/）

### 4.1 API 客户端（common/api/）

由 Swagger JSON 自动生成，**不应手动修改**。共 15 个文件：

| 文件 | 类名 | 服务前缀 | 说明 |
|---|---|---|---|
| api_battery.py | ApiBattery | /battery | 电池管理服务 |
| api_camera.py | ApiCamera | /camera | 摄像头服务 |
| api_car_station.py | ApiCarStation | /car-station | 车机站服务 |
| api_dcci.py | ApiDcci | /dcci | 充电控制服务 |
| api_emu.py | ApiEmu | /emu | 能量管理服务 |
| api_energy.py | ApiEnergy | /energy | 能量监控服务 |
| api_fault.py | ApiFault | /fault | 故障管理服务 |
| api_manager.py | ApiManager | /manager | 站控管理服务（最大，5811行） |
| api_plc.py | ApiPlc | /plc | PLC 控制服务 |
| api_swap_flow.py | ApiSwapFlow | /swap-flow | 换电流程服务 |
| api_video.py | ApiVideo | /video | 视频服务 |
| api_virtual_battery.py | ApiVirtualBattery | /virtual-battery | 虚拟电池服务 |
| api_virtual_car_station.py | ApiVirtualCarStation | /virtual-car-station | 虚拟车机站服务 |
| api_virtual_dcci.py | ApiVirtualDcci | /virtual-dcci | 虚拟充电控制服务 |
| api_virtual_plc.py | ApiVirtualPlc | /virtual-plc | 虚拟 PLC 服务 |

### 4.2 Nacos 配置操作（common/ncs/）

每个 Nacos 配置类提供 `get()`（读取配置）和 `post(content)`（写入配置）方法。

| 文件 | 类名 | dataId | 说明 |
|---|---|---|---|
| swap_common.py | SwapCommon | swap-common.yaml | 通用换电配置 |
| swap_common_station.py | SwapCommonStation | swap-common-station.yaml | 站点级配置（MQTT/云登录） |
| swap_temp_common.py | SwapTempCommon | swap-temp-common.yaml | 温度相关配置 |
| virtual_battery.py | VirtualBattery | virtual-battery.yaml | 虚拟电池服务配置 |
| virtual_car_station.py | VirtualCarStation | virtual-car-station.yaml | 虚拟车机站配置 |
| virtual_dcci.py | VirtualDcci | virtual-dcci.yaml | 虚拟充电控制配置 |
| virtual_plc.py | VirtualPlc | virtual-plc.yaml | 虚拟 PLC 配置 |

所有配置使用统一参数：`group: DEFAULT_GROUP`、`tenant: swap-station`、`type: yaml`

### 4.3 WebSocket（common/wss/）

NewWss 类定义 4 种 WSS 消息类型，均使用 `@KwDecorator` 标注：

| 方法 | 描述 | type |
|---|---|---|
| current_process_data_wss() | 获取 currentProcessData 的 wss 消息 | currentProcessData |
| volume_wss() | 获取 volume 的 wss 消息 | volume |
| fire_move_warn_wss() | 获取 fireMoveWarn 的 wss 消息 | fireMoveWarn |
| under_box_wss() | 获取 underBox 的 wss 消息 | underBox |

### 4.4 Shell/SQL 执行（common/sh/）

ExecSh 通过 `/autotest` 服务执行远程命令：

```python
ExecSh.api_test_shell(cmd_id, params=None)  # 执行 Shell 命令
ExecSh.api_test_sql(cmd_id, params=None)    # 执行 SQL 查询
```

### 4.5 工具类（common/utils/）

| 文件 | 类 | 说明 |
|---|---|---|
| qklHttp.py | QKLHttp | 站控请求（自动添加 MD5 动态密码认证） |
| qklNcsMethod.py | QKLNcsMethod | Nacos HTTP 方法封装（GET/POST → /nacos/v1/cs/configs） |
| qklPwd.py | QKLPwd | Linux 密码生成：MD5(salt + 当前日期)[8:24]，盐值默认 '5ncp31' |
| qklSh.py | QKLSh | Shell 命令封装（current_time / get_log） |
| qklSql.py | QKLSQL | SQL 查询封装（get_timeout） |
| qklWss.py | QKLWss | WebSocket 路径定义（/ws） |

### 4.6 业务版本层（version/v3/）

#### ACT 业务动作模块（9 个）

| 模块 | 说明 | 代表性功能 |
|---|---|---|
| battery_manage | 电池管理 | 仓位信息初始化、充电/保温/加热控制、欠压补电、电池类型判断 |
| config_manage | 配置管理 | 调试配置、运营配置（变压器/设备/运营策略/体积/波浪能量）、站点配置、换电配置 |
| device_manage | 设备管理 | 电表、风机、消防、门禁、入侵检测、IPC、灯光、主控室空调/加热器、PLC、卷帘门 |
| energy_manage | 能量管理 | 能量相关业务 |
| event_manage | 事件管理 | 事件处理 |
| fault_diagnosis | 故障诊断 | 故障诊断与处理 |
| home | 首页/基本信息 | 换电站站点名称、识别代码、PLC 软件版本、云站状态 |
| software_ota | 软件 OTA | 软件升级 |
| swap_manage | 换电管理 | 换电流程控制 |

#### DAO 数据访问层

**API 层（set_*.py）**：13 个文件，封装业务请求数据

**NCS 层（ncs_*.py）**：7 个文件，封装 Nacos 配置操作模板

每个 NCS 文件包含 `get()` 和多个 `post_*()` 方法，post 方法内嵌 YAML 配置模板。

#### TS 测试脚本层

与 ACT 模块一一对应，每个 test_*.py 文件：
1. 导入对应的 KW 字典
2. 使用 `RunKw.act_run(KeyDict, '关键字名称')` 执行

```python
class TestCampList:
    @staticmethod
    @KwDecorator('启动充电')
    def test_1():
        RunKw.act_run(KeyCampList, '启动充电')
```

---

## 5. 旧站业务层（company/qkl/old/）

### 5.1 API 客户端（common/api/）

共 8 个文件：

| 文件 | 类名 | 服务前缀 | 说明 |
|---|---|---|---|
| api_cloud.py | ApiCloud | /cloud | 云端交互（电池拍照/OSS/站基信息） |
| api_dcc_pdu.py | ApiDccPdu | /dcc-pdu | DCC PDU 服务 |
| api_manager.py | ApiManager | /manager | 站控管理（4229行，全业务线） |
| api_rbc.py | ApiRbc | /rbc | 换电控制中心（换电认证/信号确认） |
| api_virtual_car_machine.py | ApiVirtualCarMachine | /virtual-car-machine | 虚拟车机 |
| api_virtual_dcci.py | ApiVirtualDcci | /virtual-dcci | 虚拟充电控制 |
| api_virtual_modbus.py | ApiVirtualModbus | /virtual-modbus | 虚拟 Modbus |
| api_virtual_plc.py | ApiVirtualPlc | /virtual-plc | 虚拟 PLC |

### 5.2 WebSocket（common/wss/）

OldWss 类定义 3 种 WSS 连接：

| 方法 | 描述 | 路径 |
|---|---|---|
| manager_newWebSocket() | 获取 newWebSocket 的 wss 消息 | /manager/newWebSocket |
| rbc_webSocket() | 获取 rbcWebSocket 的 wss 消息 | /rbc/webSocket |
| manager_webSocketOfManager() | 获取 webSocketOfManager 的 wss 消息 | /manager/webSocketOfManager |

### 5.3 ACT 业务模块（15 个）

battery_manage / charger_manage / data_statistics / device_control / device_manage / event_manage / fault_manage / file_manage / software_ota / station_maintenance / station_manage / strategy_manage / swap_channel / swap_manage / ups

---

## 6. 核心工作流

### 6.1 入口脚本执行流程

```python
# convertAllFile.py
# ==================== Swagger 接口文档转换 ====================
convert_all_swagger()      # Swagger JSON → API 客户端代码

# ==================== 关键字字典转换 ====================
convert_all_wss_kw()       # WSS 源文件 → 关键字字典
convert_all_act_kw()       # ACT 源文件 → 关键字字典
convert_all_api_kw()       # DAO/API 源文件 → 关键字字典
convert_all_ncs_kw()       # DAO/NCS 源文件 → 关键字字典
convert_all_tc_kw()        # TS 源文件 → 关键字字典
```

### 6.2 HTTP 请求链路

```
业务方法 (act/*.py)
  → RunKw.api_run(KeySetXxx, '关键字名称', *args)
    → HandlerKw.kw(SetXxx.api_xxx)(*args)
      → ApiXxx.api_xxx(data)  [自动生成的客户端]
        → HttpRq.req(*HttpMethod.http_info(path, method, data))
          → HandleEnv.get_env_host() + get_env_authorization()
          → requests.request()
```

### 6.3 WebSocket 链路

```
NewWss.current_process_data_wss()
  → QKLWss.ws(data) → (path='/ws', data)
  → HandlerWss.Wss_New(userId='567', path, data)
    → HandleEnv.get_env_wss()
    → websockets.sync.client.connect(wss://host/ws)
    → send(userId) + send(data) + recv()
```

### 6.4 Nacos 配置链路

```
NcsSwapCommonStation.swap_common_station_get()
  → SwapCommonStation.swap_common_station_get()
    → QKLNcsMethod.get(data) → (path, 'get', data)
  → HandlerNacos.NacosReq(path, method, data)
    → HandleEnv.get_env_nacos() → (nacos_url, accessToken)
    → requests.request()
```

### 6.5 Shell/SQL 执行链路

```
QKLSh.current_time()
  → ExecSh.api_test_shell(cmd_id=1)
    → HttpRq.req(path='/autotest/api/test/shell', method='POST', data={id:1})
    → 远程测试服务执行预定义 Shell 命令
```

### 6.6 鉴权机制

| 场景 | 机制 | 实现 |
|---|---|---|
| 站控 API | Bearer Token（JWT） | env.json → host_authorization |
| 测试服务（/autotest） | MD5 动态密码 | QKLPwd: MD5('5ncp31:' + 日期)[8:24] |
| Nacos | accessToken | env.json → nacos_accessToken |

---

## 7. 代码规范

### 7.1 类设计

- 所有业务类使用 `@staticmethod`，不使用实例方法
- 类不使用 `__init__`，纯静态工具类模式

### 7.2 装饰器使用

```python
@staticmethod              # 外层（上方）
@KwDecorator("中文描述")    # 内层（下方）
def method_name(param1, param2):
    ...
```

### 7.3 命名规范

| 类型 | 文件名 | 类名 | 示例 |
|---|---|---|---|
| API 客户端 | api_*.py | Api* (PascalCase) | api_battery.py → ApiBattery |
| NCS 配置 | ncs_*.py | Ncs* | ncs_swap_common.py → NcsSwapCommon |
| DAO/API | set_*.py | Set* | set_battery.py → SetBattery |
| WSS | *_wss.py | *Wss | new_wss.py → NewWss |
| 关键字字典 | key_*.py | Key* | key_new_wss.py → KeyNewWss |
| ACT 动作 | 按模块组织 | 描述功能 | camp_list.py → CampList |
| 测试脚本 | test_*.py | Test* | test_camp_list.py → TestCampList |

### 7.4 自动生成文件

以下文件由代码生成器自动产生，**不应手动修改**：

- `common/api/api_*.py` — 由 Swagger JSON 自动生成
- `kw/key_*.py` — 由 AST 解析自动生成

以下文件为**手写业务代码**：

- `version/*/act/*.py` — 业务动作
- `version/*/dao/api/set_*.py` — API 数据访问
- `version/*/dao/ncs/ncs_*.py` — Nacos 配置模板
- `version/*/ts/*.py` — 测试脚本

### 7.5 文件编码

所有 Python 文件使用 UTF-8 编码。

---

## 8. 附录

### 8.1 Nacos 配置 dataId 列表

| dataId | 说明 |
|---|---|
| swap-common.yaml | 通用换电配置 |
| swap-common-station.yaml | 站点级配置（MQTT URL/云登录/RSA密钥） |
| swap-temp-common.yaml | 温度配置（BMS 温度策略/netty 客户端） |
| virtual-battery.yaml | 虚拟电池（心跳/Redis/Swagger/命令结果） |
| virtual-car-station.yaml | 虚拟车机站（netty 服务器/客户端/下控命令结果） |
| virtual-dcci.yaml | 虚拟充电控制（Redis/Swagger/回调/认证） |
| virtual-plc.yaml | 虚拟 PLC（Redis/netty/Modbus/回调延迟） |

### 8.2 新站 WSS 消息类型

| type | 说明 |
|---|---|
| currentProcessData | 当前换电流程数据 |
| volume | 体积信息 |
| fireMoveWarn | 消防移动告警 |
| underBox | 底箱信息 |

### 8.3 外部服务接口

| 服务 | 路径 | 说明 |
|---|---|---|
| 站控 API | /manager/api/*, /battery/api/* 等 | 换电站各微服务 REST API |
| 测试服务 Shell | /autotest/api/test/shell | 远程 Shell 命令执行 |
| 测试服务 SQL | /autotest/api/test/sql | 远程 SQL 查询 |
| Nacos | /nacos/v1/cs/configs | 配置读写 |
| 新站 WSS | /ws | WebSocket 实时消息 |
| 旧站 WSS | /manager/webSocketOfManager, /manager/newWebSocket, /rbc/webSocket | 旧站 WebSocket |
