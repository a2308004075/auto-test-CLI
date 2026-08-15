from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.device_manage.main_heater.main_heater import MainHeater

KeyMainHeater = {
    "传感器数据：回内温度": HandlerKw.kw(MainHeater.action_8),  # 参数：['value']
    "告警状态：回风温度传感器故障": HandlerKw.kw(MainHeater.action_5),  # 参数：['value']
    "告警状态：柜内低温告警": HandlerKw.kw(MainHeater.action_7),  # 参数：['value']
    "告警状态：柜内高温告警": HandlerKw.kw(MainHeater.action_6),  # 参数：['value']
    "站点参数信息": HandlerKw.kw(MainHeater.action_1),  # 参数：['tempAdaptation']
    "系统参数设置：低温告警温度值": HandlerKw.kw(MainHeater.action_12),  # 参数：['value']
    "系统参数设置：制热停止回差值": HandlerKw.kw(MainHeater.action_10),  # 参数：['value']
    "系统参数设置：制热启动温度": HandlerKw.kw(MainHeater.action_9),  # 参数：['value']
    "系统参数设置：高温告警温度值": HandlerKw.kw(MainHeater.action_11),  # 参数：['value']
    "设备状态：制热运行状态": HandlerKw.kw(MainHeater.action_3),  # 参数：['value']
    "设备状态：机组运行状态": HandlerKw.kw(MainHeater.action_2),  # 参数：['value']
    "设备状态：风机运行状态": HandlerKw.kw(MainHeater.action_4),  # 参数：['value']
}
