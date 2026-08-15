from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.ts.device_manage.main_heater.test_main_heater import TestMainHeater

KeyTestMainHeater = {
    "传感器数据：回内温度": HandlerKw.kw(TestMainHeater.test_8),
    "告警状态：回风温度传感器故障": HandlerKw.kw(TestMainHeater.test_5),
    "告警状态：柜内低温告警": HandlerKw.kw(TestMainHeater.test_7),
    "告警状态：柜内高温告警": HandlerKw.kw(TestMainHeater.test_6),
    "站点参数信息": HandlerKw.kw(TestMainHeater.test_1),
    "系统参数设置：低温告警温度值": HandlerKw.kw(TestMainHeater.test_12),
    "系统参数设置：制热停止回差值": HandlerKw.kw(TestMainHeater.test_10),
    "系统参数设置：制热启动温度": HandlerKw.kw(TestMainHeater.test_9),
    "系统参数设置：高温告警温度值": HandlerKw.kw(TestMainHeater.test_11),
    "设备状态：制热运行状态": HandlerKw.kw(TestMainHeater.test_3),
    "设备状态：机组运行状态": HandlerKw.kw(TestMainHeater.test_2),
    "设备状态：风机运行状态": HandlerKw.kw(TestMainHeater.test_4),
}
