from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.api.set_virtual_car_station import SetVirtualCarStation

KeySetVirtualCarStation = {
    "SetVirtualCarStation：0X129，高压互锁状态": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_set0X129),  # 参数：['hvil1State']
    "SetVirtualCarStation：0X129：默认值": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_set0X1292_0),
    "SetVirtualCarStation：0X12F-最严重故障码": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_set0X12F_bmsmostCriticalFltID),  # 参数：['bmsmostCriticalFltID']
    "SetVirtualCarStation：0X12F-最严重故障等级": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_set0X12F_3),  # 参数：['bmsmostCriticalFltLvl']
    "SetVirtualCarStation：0X12F：默认值": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_set0X12F),
    "SetVirtualCarStation：发送下低压执行结果：复位": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_closeLVContactorResult_0),
    "SetVirtualCarStation：发送下低压执行结果：执行完毕": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_closeLVContactorResult_2),
    "SetVirtualCarStation：发送下高压执行结果：复位": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_closeAndDisableHVContactorResult_0),
    "SetVirtualCarStation：发送下高压执行结果：执行完毕": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_closeAndDisableHVContactorResult_2),
    "SetVirtualCarStation：发送蓝牙扫描信息": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_scanBlueToothInfo_1),
    "SetVirtualCarStation：发送蓝牙扫描执行结果：成功": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_scanBlueToothInfoResult_1),
    "SetVirtualCarStation：发送蓝牙断开执行结果：复位": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_disConnectCarMbmuResult_0),
    "SetVirtualCarStation：发送蓝牙连接信息：已连接": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_blueToothInfo_1),
    "SetVirtualCarStation：发送蓝牙连接信息：未连接": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_blueToothInfo_0),
    "SetVirtualCarStation：发送蓝牙连接信息：正在连接中": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_blueToothInfo_3),
    "SetVirtualCarStation：发送蓝牙连接信息：重连中": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_blueToothInfo_2),
    "SetVirtualCarStation：发送蓝牙连接执行结果：复位": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_connectCarMbmuResult_0),
    "SetVirtualCarStation：发送蓝牙连接执行结果：执行成功": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_controlCommand_connectCarMbmuResult_2),
    "SetVirtualCarStation：发送车辆信息：电池包类别": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_carInfo_1),  # 参数：['packTypeOfPackage1']
    "SetVirtualCarStation：发送车辆信息：电池包类别，MBMU最严重故障等级": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_carInfo_2),  # 参数：['packTypeOfPackage1', 'supremeErrorLevelOfBattSys']
    "SetVirtualCarStation：发送车辆自由度信息：开车门": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_carFreedomStatusInfo_3),
    "SetVirtualCarStation：发送车辆自由度信息：方向盘调整": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_carFreedomStatusInfo_steeringTurnAngle),  # 参数：['steeringTurnAngle']
    "SetVirtualCarStation：发送车辆自由度信息：破坏所有自由度": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_carFreedomStatusInfo_2),
    "SetVirtualCarStation：发送车辆自由度信息：破坏非车门": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_carFreedomStatusInfo_4),
    "SetVirtualCarStation：发送车辆自由度信息：通过": HandlerKw.kw(SetVirtualCarStation.api_virtualCarStation_feign_v3_info_carFreedomStatusInfo_1),
    "SetVirtualCarStation：车机服务停发某一帧": HandlerKw.kw(SetVirtualCarStation.api_schedule_del),  # 参数：['code']
    "SetVirtualCarStation：车机服务恢复发某一帧": HandlerKw.kw(SetVirtualCarStation.api_schedule_addl),  # 参数：['code']
}
