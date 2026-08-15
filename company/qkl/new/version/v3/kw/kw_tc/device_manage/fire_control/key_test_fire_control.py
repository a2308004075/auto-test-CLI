from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.ts.device_manage.fire_control.test_fire_control import TestFireControl

KeyTestFireControl = {
    "事件信息": HandlerKw.kw(TestFireControl.test_eventInformation),
    "传感器数据": HandlerKw.kw(TestFireControl.test_sensorData),
    "灭火器状态": HandlerKw.kw(TestFireControl.test_FE),
    "系统状态-主电": HandlerKw.kw(TestFireControl.test_systemStatus_5),
    "系统状态-声光报警状态": HandlerKw.kw(TestFireControl.test_systemStatus_12),
    "系统状态-备电": HandlerKw.kw(TestFireControl.test_systemStatus_6),
    "系统状态-手动启动信号": HandlerKw.kw(TestFireControl.test_systemStatus_10),
    "系统状态-手动急停信号": HandlerKw.kw(TestFireControl.test_systemStatus_11),
    "系统状态-手动模式": HandlerKw.kw(TestFireControl.test_systemStatus_9),
    "系统状态-报警": HandlerKw.kw(TestFireControl.test_systemStatus_1),
    "系统状态-放气勿入状态": HandlerKw.kw(TestFireControl.test_systemStatus_13),
    "系统状态-故障": HandlerKw.kw(TestFireControl.test_systemStatus_2),
    "系统状态-消音": HandlerKw.kw(TestFireControl.test_systemStatus_3),
    "系统状态-电源故障": HandlerKw.kw(TestFireControl.test_systemStatus_7),
    "系统状态-自动模式": HandlerKw.kw(TestFireControl.test_systemStatus_8),
    "系统状态-自检": HandlerKw.kw(TestFireControl.test_systemStatus_4),
}
