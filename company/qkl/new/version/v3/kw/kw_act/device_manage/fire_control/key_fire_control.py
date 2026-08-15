from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.device_manage.fire_control.fire_control import FireControl

KeyFireControl = {
    "事件信息": HandlerKw.kw(FireControl.action_eventInformation),  # 参数：['valueList1', 'valueList2', 'valueList3']
    "传感器数据": HandlerKw.kw(FireControl.action_sensorData),  # 参数：['sensorNum', 'deviceType', 'sensorID', 'alarmLevel', 'temperature', 'COConcentration', 'VOC', 'smokeDensity']
    "灭火器状态": HandlerKw.kw(FireControl.action_FE),  # 参数：['FE1', 'FE2']
    "系统状态-主电": HandlerKw.kw(FireControl.action_systemStatus_5),  # 参数：['value']
    "系统状态-声光报警状态": HandlerKw.kw(FireControl.action_systemStatus_12),  # 参数：['value']
    "系统状态-备电": HandlerKw.kw(FireControl.action_systemStatus_6),  # 参数：['value']
    "系统状态-手动启动信号": HandlerKw.kw(FireControl.action_systemStatus_10),  # 参数：['value']
    "系统状态-手动急停信号": HandlerKw.kw(FireControl.action_systemStatus_11),  # 参数：['value']
    "系统状态-手动模式": HandlerKw.kw(FireControl.action_systemStatus_9),  # 参数：['value']
    "系统状态-报警": HandlerKw.kw(FireControl.action_systemStatus_1),  # 参数：['value']
    "系统状态-放气勿入状态": HandlerKw.kw(FireControl.action_systemStatus_13),  # 参数：['value']
    "系统状态-故障": HandlerKw.kw(FireControl.action_systemStatus_2),  # 参数：['value']
    "系统状态-消音": HandlerKw.kw(FireControl.action_systemStatus_3),  # 参数：['value']
    "系统状态-电源故障": HandlerKw.kw(FireControl.action_systemStatus_7),  # 参数：['value']
    "系统状态-自动模式": HandlerKw.kw(FireControl.action_systemStatus_8),  # 参数：['value']
    "系统状态-自检": HandlerKw.kw(FireControl.action_systemStatus_4),  # 参数：['value']
}
