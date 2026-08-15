from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.api.set_virtual_plc import SetVirtualPlc

KeySetVirtualPlc = {
    "SetVirtualPlc：PLC软件版本": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getPlcCommunicationVersion),  # 参数：['aversion', 'bversion', 'cversion', 'dversion']
    "SetVirtualPlc：PLC配方校验": HandlerKw.kw(SetVirtualPlc.api_swap_plc_virtual_plcRecipeDigestVerify),  # 参数：['result', 'faultReason', 'faultReasonDetail', 'batteryCompartmentRecipeDigest', 'swapCommonRecipeDigest', 'swapDeltaRecipeDigest']
    "SetVirtualPlc：PLC配方校验：执行中": HandlerKw.kw(SetVirtualPlc.api_swap_plc_virtual_plcRecipeDigestVerify_1),
    "SetVirtualPlc：PLC配方校验：执行失败": HandlerKw.kw(SetVirtualPlc.api_swap_plc_virtual_plcRecipeDigestVerify_3),  # 参数：['faultReason']
    "SetVirtualPlc：PLC配方校验：执行完毕": HandlerKw.kw(SetVirtualPlc.api_swap_plc_virtual_plcRecipeDigestVerify_2),
    "SetVirtualPlc：允许车辆回位指令：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowReturnVehicle_1),
    "SetVirtualPlc：允许车辆回位指令：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowReturnVehicle_2),
    "SetVirtualPlc：允许车辆回位指令：执行错误毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowReturnVehicle_3),  # 参数：['faultReason']
    "SetVirtualPlc：加解锁平台上升：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_rgvDriveChannel_1),
    "SetVirtualPlc：加解锁平台上升：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_rgvDriveChannel_2),
    "SetVirtualPlc：加解锁平台上升：执行错误": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_rgvDriveChannel_3),  # 参数：['faultReason']
    "SetVirtualPlc：加解锁平台回位：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_rgvReturn_1),
    "SetVirtualPlc：加解锁平台回位：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_rgvReturn_2),
    "SetVirtualPlc：加解锁平台回位：执行错误": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_rgvReturn_3),  # 参数：['faultReason']
    "SetVirtualPlc：发送允许拆卸电池包指令：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowDisassemblyBattery_1),
    "SetVirtualPlc：发送允许拆卸电池包指令：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowDisassemblyBattery_2),
    "SetVirtualPlc：发送允许拆卸电池包指令：执行错误": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowDisassemblyBattery_3),  # 参数：['faultReason']
    "SetVirtualPlc：发送允许驶入换电通道至PLC：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowVehicleEnter_1),
    "SetVirtualPlc：发送允许驶入换电通道至PLC：执行失败": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowVehicleEnter_3),  # 参数：['faultReason']
    "SetVirtualPlc：发送允许驶入换电通道至PLC：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowVehicleEnter_2),
    "SetVirtualPlc：发送车辆允许驶离指令到PLC：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowVehicleLeave_1),
    "SetVirtualPlc：发送车辆允许驶离指令到PLC：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowVehicleLeave_2),
    "SetVirtualPlc：发送车辆允许驶离指令到PLC：执行错误": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_allowVehicleLeave_3),  # 参数：['faultReason']
    "SetVirtualPlc：同步仓位信息：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_startSwap_1),
    "SetVirtualPlc：同步仓位信息：执行失败": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_startSwap_3),  # 参数：['faultReason', 'failCamp1', 'failCamp2']
    "SetVirtualPlc：同步仓位信息：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_startSwap_2),
    "SetVirtualPlc：命令编码01，主控室加热器": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadCoils_mainHeater_01),  # 参数：['point_id', 'value']
    "SetVirtualPlc：命令编码01，消防设备": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadCoils_firControl_01),  # 参数：['point_id', 'value']
    "SetVirtualPlc：命令编码01，风机": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadCoils_fan_01),  # 参数：['slaveId', 'point_id', 'value']
    "SetVirtualPlc：命令编码02，主控室加热器": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadDiscreteInputs_mainHeater_02),  # 参数：['point_id', 'value']
    "SetVirtualPlc：命令编码02，风机": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadDiscreteInputs_fan_02),  # 参数：['slaveId', 'point_id', 'value']
    "SetVirtualPlc：命令编码03，主控室加热器": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadHoldingRegisters_mainHeater_03),  # 参数：['point_id', 'value']
    "SetVirtualPlc：命令编码03，主控室空调": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadHoldingRegisters_mainAirConditioning_03),  # 参数：['point_id', 'value']
    "SetVirtualPlc：命令编码03，消防设备": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadHoldingRegisters_firControl_03),  # 参数：['point_id', 'value']
    "SetVirtualPlc：命令编码03，电表": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadHoldingRegisters_electricMeter_03),  # 参数：['slaveId', 'point_id', 'value']
    "SetVirtualPlc：命令编码03，风机": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadHoldingRegisters_fan_03),  # 参数：['slaveId', 'point_id', 'value']
    "SetVirtualPlc：命令编码04，主控室加热器": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadInputRegisters_mainHeater_04),  # 参数：['point_id', 'value']
    "SetVirtualPlc：命令编码04，消防设备": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadInputRegisters_firControl_04),  # 参数：['point_id', 'value']
    "SetVirtualPlc：命令编码04，风机": HandlerKw.kw(SetVirtualPlc.modbusVirtual_updateReadInputRegisters_fan_04),  # 参数：['slaveId', 'point_id', 'value']
    "SetVirtualPlc：归中举升：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_backCenterAndLift_1),
    "SetVirtualPlc：归中举升：执行失败": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_backCenterAndLift_3),  # 参数：['faultReason']
    "SetVirtualPlc：归中举升：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_backCenterAndLift_2),
    "SetVirtualPlc：换电时PLC状态-换电时PLC状态、PLC的任务状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getPlcStatusFeedBack),  # 参数：['electricChannelPlcStatus', 'plcGeneralStatus']
    "SetVirtualPlc：电池一键入仓：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_controlBatteryReturn_1),
    "SetVirtualPlc：电池一键入仓：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_controlBatteryReturn_2),
    "SetVirtualPlc：电池一键入仓：执行错误": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_controlBatteryReturn_3),  # 参数：['faultReason']
    "SetVirtualPlc：电池一键出仓：执行中": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_controlBatteryOut_1),
    "SetVirtualPlc：电池一键出仓：执行完毕": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_controlBatteryOut_2),
    "SetVirtualPlc：电池一键出仓：执行错误": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_controlBatteryOut_3),  # 参数：['faultReason']
    "SetVirtualPlc：站点参数上报050B": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_reportStationParamInfo),  # 参数：['tempAdaptation']
    "SetVirtualPlc：设置PLC工作模式": HandlerKw.kw(SetVirtualPlc.api_swap_plc_virtual_getPlcWorkingMode),  # 参数：['batteryDetectionAlarmStatus', 'communicationType', 'controlMode', 'debugStatus', 'faultStatus', 'motionModuleStatus', 'pauseStatus', 'scapegoatDetectionAlarmStatus', 'scramStatus', 'servoAlarmStatus', 'attendedSafetyAlarmStatus', 'unattendedSafetyAlarmStatus']
    "SetVirtualPlc：设置仓位信息": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getPositionInfo),
    "SetVirtualPlc：设置仓位信息-仓位故障信息": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getPositionInfo_3),  # 参数：['positionNo', 'positionFaultStatus']
    "SetVirtualPlc：设置仓位信息-电推杆状态信息": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getPositionInfo_2),  # 参数：['positionNo', 'electricPutterStatus']
    "SetVirtualPlc：设置仓位信息-电池在位信息状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getPositionInfo_1),  # 参数：['positionNo', 'batteryPlaceStatus']
    "SetVirtualPlc：设置归中状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getCenteringStatus),  # 参数：['centeringStatus']
    "SetVirtualPlc：设置换电设备状态-RGV加热模式": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_4),  # 参数：['rgvHeatingMode']
    "SetVirtualPlc：设置换电设备状态-主控室侧安全门状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_6),  # 参数：['mainControlSafetyDoorStatus']
    "SetVirtualPlc：设置换电设备状态-充电仓侧安全门状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_7),  # 参数：['chargeCampSafetyDoorStatus']
    "SetVirtualPlc：设置换电设备状态-入口道闸状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_3),  # 参数：['entranceRoadStatus']
    "SetVirtualPlc：设置换电设备状态-入口雷达状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_1),  # 参数：['entranceRadarStatus']
    "SetVirtualPlc：设置换电设备状态-出口雷达状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_2),  # 参数：['exitRadarStatus']
    "SetVirtualPlc：设置换电设备状态-开合门状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_5),  # 参数：['openingClosingDoorStatus']
    "SetVirtualPlc：设置换电设备状态-集装箱侧安全门状态": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_8),  # 参数：['containerSafetyDoorStatus']
    "SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getSwapEquipmentStatus_channelTopRadarStatus_leftVSlotPositionSignal_rightVSlotPositionSignal),  # 参数：['channelTopRadarStatus', 'leftVSlotPositionSignal', 'rightVSlotPositionSignal']
    "SetVirtualPlc：设置站基本信息": HandlerKw.kw(SetVirtualPlc.api_virtual_feign_getStationBaseInfo),  # 参数：['hardwareVersion']
}
