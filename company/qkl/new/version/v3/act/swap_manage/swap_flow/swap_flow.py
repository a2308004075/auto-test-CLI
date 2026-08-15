import time
from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_manager import KeySetManager
from company.qkl.new.version.v3.kw.kw_api.key_set_swap_flow import KeySetSwapFlow
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_battery import KeySetVirtualBattery
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_car_station import KeySetVirtualCarStation
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_dcci import KeySetVirtualDcci
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc
from company.qkl.new.version.v3.kw.kw_ncs.key_ncs_virtual_car_station import KeyNcsVirtualCarStation


class SwapFlow:
    """
    换电流程监控
    """

    @staticmethod
    @KwDecorator("初始化车辆状态")
    def action_init_car(packTypeOfPackage1):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙连接执行结果：复位')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙断开执行结果：复位')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙连接执行结果：执行成功')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙连接信息：已连接')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送下高压执行结果：执行完毕')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送下低压执行结果：执行完毕')
        # RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送下高压执行结果：复位')
        # RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送下低压执行结果：复位')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆自由度信息：通过')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：0X12F：默认值')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：0X129：默认值')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆信息：电池包类别', packTypeOfPackage1)

    @staticmethod
    @KwDecorator("自检")
    def action_selfCheck(bmsmostCriticalFltID, hvil1State):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：0X12F-最严重故障码', bmsmostCriticalFltID)
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：0X129，高压互锁状态', hvil1State)

    @staticmethod
    @KwDecorator("初始化PLC")
    def action_init_plc():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：换电时PLC状态-换电时PLC状态、PLC的任务状态', 0, 22)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 2, 2, 2)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置PLC工作模式', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    @staticmethod
    @KwDecorator("抓拍车牌")
    def action_swap_cameraSendCarNo(carNo):
        RunKw.api_run(KeySetManager, 'SetManager：模拟上报车牌号', carNo)  # 闽DDE5917

    @staticmethod
    @KwDecorator("云端认证")
    def action_swap_cloudReceiveCloudValid(carNo, packType, ableToChange):
        SwapFlow.action_swap_cameraSendCarNo(carNo)
        time.sleep(2)

        RunKw.api_run(KeySetSwapFlow, 'SetSwapFlow：【云->站】云端发送检验结果：车牌号，是否允许抬杆', carNo, packType, ableToChange)

    @staticmethod
    @KwDecorator("PLC配方校验：通过")
    def action_swap_plcRecipeDigestVerify(carNo, packType):
        SwapFlow.action_swap_cloudReceiveCloudValid(carNo, packType, True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：PLC配方校验：执行完毕')

    @staticmethod
    @KwDecorator("驶入换电通道至PLC：通过")
    def action_swap_plcAllowVehicleEnter(carNo, packType):
        SwapFlow.action_swap_plcRecipeDigestVerify(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 1, 1, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行完毕')

    @staticmethod
    @KwDecorator("【云->站】车辆停稳应答：通过")
    def action_swap_cloudCarStoppedResp(carNo, packType):
        SwapFlow.action_swap_plcRecipeDigestVerify(carNo, packType)  # 换电配方通过
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 1, 1, 1)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行完毕')
        time.sleep(2)

        RunKw.api_run(KeySetSwapFlow, 'SetSwapFlow：【云->站】车辆停稳应答：闽DDE5917')

    @staticmethod
    @KwDecorator("同步仓位信息至PLC")
    def action_swap_plcSwapCampInfo(carNo, packType):
        SwapFlow.action_swap_plcRecipeDigestVerify(carNo, packType)  # 换电配方通过
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 1, 1, 1)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行完毕')
        time.sleep(6)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：同步仓位信息：执行完毕')
        time.sleep(2)

        RunKw.api_run(KeySetSwapFlow, 'SetSwapFlow：【云->站】车辆停稳应答：闽DDE5917')

    @staticmethod
    @KwDecorator("【云->站】云端发送开始换电：允许换电")
    def action_swap_cloudStartSwap(carNo, packType):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetSwapFlow, 'SetSwapFlow：【云->站】云端发送开始换电')

    @staticmethod
    @KwDecorator("归中举升：通过")
    def action_swap_plcBackCenterAndLift(carNo, packType):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行完毕')

    @staticmethod
    @KwDecorator("拆装电池包：通过")
    def action_swap_plcAllowDisassemblyBattery(carNo, packType):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：换电时PLC状态-换电时PLC状态、PLC的任务状态', 12, 1)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行完毕')

    @staticmethod
    @KwDecorator("拆装电池包：执行中")
    def action_swap_plcAllowDisassemblyBattery_ing(carNo, packType):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：换电时PLC状态-换电时PLC状态、PLC的任务状态', 12, 1)

    @staticmethod
    @KwDecorator("设备归位：通过")
    def action_swap_plcAllowReturnVehicle(carNo, packType):
        SwapFlow.action_swap_plcAllowDisassemblyBattery(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("车辆驶离：通过")
    def action_swap_plcAllowVehicleLeave(carNo, packType):
        SwapFlow.action_swap_plcAllowReturnVehicle(carNo, packType)
        time.sleep(2)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 2, 2, 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送车辆允许驶离指令到PLC：执行完毕')

    @staticmethod
    @KwDecorator("换电出仓清站外小计：未响应")
    def action_SubInfoOutClrSts_0(carNo, packType):
        SwapFlow.action_swap_cloudCarStoppedResp(carNo, packType)

    @staticmethod
    @KwDecorator("换电出仓清站外小计：失败")
    def action_SubInfoOutClrSts_1(carNo, packType):
        SwapFlow.action_swap_cloudCarStoppedResp(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18A2F980，站外小计信息清除控制执行结果', 1, 1)

    @staticmethod
    @KwDecorator("换电出仓清站外小计：成功")
    def action_SubInfoOutClrSts_2(carNo, packType):
        SwapFlow.action_swap_cloudCarStoppedResp(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18A2F980，站外小计信息清除控制执行结果', 1, 2)

    @staticmethod
    @KwDecorator("换电入仓清站内小计：未响应")
    def action_SubInfoInClrSts_0(carNo, packType):
        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电设备上报电池连接状态(4515)', 1, 1, 1, 1)

    @staticmethod
    @KwDecorator("换电入仓清站内小计：失败")
    def action_SubInfoInClrSts_1(carNo, packType):
        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电设备上报电池连接状态(4515)', 1, 1, 1, 1)
        time.sleep(2)
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18A2F980，站内小计信息清除控制执行结果', 1, 1)

    @staticmethod
    @KwDecorator("换电入仓清站内小计：成功")
    def action_SubInfoInClrSts_2(carNo, packType):
        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电设备上报电池连接状态(4515)', 1, 1, 1, 1)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18A2F980，站内小计信息清除控制执行结果', 1, 2)

    @staticmethod
    @KwDecorator("换电入仓，启动充电")
    def action_batteryIn_startCharge(carNo, packType):
        # 前置条件，电池满充充电

        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电设备上报电池连接状态(4515)', 1, 1, 1, 1)
        time.sleep(2)

    @staticmethod
    @KwDecorator("车机信息不全，车辆停稳失败")
    def action_swap_cloudCarStoppedResp_delCarInfo(code, carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', code)
        time.sleep(3)

        SwapFlow.action_swap_plcAllowVehicleEnter(carNo, packType)  # 驶入换电通道至PLC：通过

    @staticmethod
    @KwDecorator("车机信息不发【电池包SN】【车上电池真实SOC】【总里程信息】，车辆停稳失败")
    def action_swap_cloudCarStoppedResp_delAllCarInfo(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_244_command')  # 车上电池包SN
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_10B_command')  # 车辆总里程信息
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_123_command')  # 车上电池真实SOC
        time.sleep(3)

        SwapFlow.action_swap_plcAllowVehicleEnter(carNo, packType)  # 驶入换电通道至PLC：通过

    @staticmethod
    @KwDecorator("车机信息不全，10s内获收到车机信息，车辆停稳成功")
    def action_swap_cloudCarStoppedResp_delCarInfo_10s(code, carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', code)
        time.sleep(3)

        SwapFlow.action_swap_plcAllowVehicleEnter(carNo, packType)  # 驶入换电通道至PLC：通过
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆信息：电池包类别', packType)

    @staticmethod
    @KwDecorator("离线换电，车机信息不全，车辆停稳失败")
    def action_swap_cloudCarStoppedResp_offCloud_DelCarInfo_false(code):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', code)
        time.sleep(3)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：PLC配方校验：执行完毕')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 1, 1, 1)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行完毕')

    @staticmethod
    @KwDecorator("离线换电，车机信息不全，车辆停稳成功")
    def action_swap_cloudCarStoppedResp_offCloud_DelCarInfo(code, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', code)
        time.sleep(3)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：PLC配方校验：执行完毕')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 1, 1, 1)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行完毕')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆信息：电池包类别', packType)

    @staticmethod
    @KwDecorator("车机未发0x105，换电继续")
    def action_swap_closeAndDisableHVContactorBefor_carInfo(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_105_command')
        time.sleep(3)

        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)  # 归中举升：通过

    @staticmethod
    @KwDecorator("MBMU最高故障等级2、6、7、8")
    def action_swap_closeAndDisableHVContactor_supremeErrorLevelOfBattSys(carNo, packType, packTypeOfPackage1,
                                                                          supremeErrorLevelOfBattSys):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆信息：电池包类别，MBMU最严重故障等级',
                          packTypeOfPackage1, supremeErrorLevelOfBattSys)
        time.sleep(3)

        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)  # 归中举升：通过

    @staticmethod
    @KwDecorator("PLC暂停，PLC超时未响应【归中举升请求】2：执行成功")
    def action_swap_plcBackCenterAndLift_stop(carNo, packType, pauseStatus):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)
        time.sleep(2)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置PLC工作模式', 1, 1, 1, 1, 1, 1, pauseStatus, 1, 1, 1, 1, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行中')

    @staticmethod
    @KwDecorator("PLC暂停，PLC超时未响应【拆装电池包】2：执行成功")
    def action_swap_plcAllowDisassemblyBattery_stop(carNo, packType, pauseStatus):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置PLC工作模式', 1, 1, 1, 1, 1, 1, pauseStatus, 1, 1, 1, 1, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')

    @staticmethod
    @KwDecorator("PLC暂停，PLC超时未响应【设备归位】2：执行成功")
    def action_swap_plcAllowReturnVehicle_stop(carNo, packType, pauseStatus):
        SwapFlow.action_swap_plcAllowDisassemblyBattery(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置PLC工作模式', 1, 1, 1, 1, 1, 1, pauseStatus, 1, 1, 1, 1, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行中')

    @staticmethod
    @KwDecorator("PLC暂停，PLC超时未响应【车辆驶离】2：执行成功")
    def action_swap_plcAllowVehicleLeave_stop(carNo, packType, pauseStatus):
        SwapFlow.action_swap_plcAllowReturnVehicle(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置PLC工作模式', 1, 1, 1, 1, 1, 1, pauseStatus, 1, 1, 1, 1, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送车辆允许驶离指令到PLC：执行中')

    @staticmethod
    @KwDecorator("车机信息不全，拆安装包失败")
    def action_swap_plcAllowDisassemblyBattery_DelCarInfo_false(code, carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', code)
        time.sleep(3)

        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)

    @staticmethod
    @KwDecorator("车机信息不全，10s内获收到车机信息，拆装电池包成功")
    def action_swap_plcAllowDisassemblyBattery_DelCarInfo_10s(code, carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', code)
        time.sleep(3)

        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆信息：电池包类别', packType)

    @staticmethod
    @KwDecorator("车辆驶入到位前，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态")
    def action_swap_VehicleEnterBefor_SwapEquipmentStatus(carNo, packType, channelTopRadarStatus,
                                                          leftVSlotPositionSignal, rightVSlotPositionSignal):
        SwapFlow.action_swap_plcRecipeDigestVerify(carNo, packType)  # PLC配方校验：通过
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号',
                          channelTopRadarStatus, leftVSlotPositionSignal, rightVSlotPositionSignal)

    @staticmethod
    @KwDecorator("车辆驶入到位后，站控下控PLC归中举升前，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态")
    def action_swap_VehicleEnterAfter_plcBackCenterAndLiftBefor_SwapEquipmentStatus(carNo, packType,
                                                                                    channelTopRadarStatus,
                                                                                    leftVSlotPositionSignal,
                                                                                    rightVSlotPositionSignal):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号',
                          channelTopRadarStatus, leftVSlotPositionSignal, rightVSlotPositionSignal)

    @staticmethod
    @KwDecorator("PLC归中举升后，站控下控PLC归中举升后，顶部雷达状态，车辆左V槽在位信号不状态，车辆右V槽在位信号状态")
    def action_swap_plcBackCenterAndLiftAfter_SwapEquipmentStatus(carNo, packType, channelTopRadarStatus,
                                                                  leftVSlotPositionSignal, rightVSlotPositionSignal):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号',
                          channelTopRadarStatus, leftVSlotPositionSignal, rightVSlotPositionSignal)

    @staticmethod
    @KwDecorator("自复位，设备归位成功")
    def action_swap_selfReset_plcAllowReturnVehicle():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("自复位，设备归位成功，自检（最严重故障码，高压互锁状态）")
    def action_swap_selfReset_selfCheck(bmsmostCriticalFltID, hvil1State):
        SwapFlow.action_swap_selfReset_plcAllowReturnVehicle()  # 设备归位完成
        time.sleep(2)

        SwapFlow.action_selfCheck(bmsmostCriticalFltID, hvil1State)  # 自检

    @staticmethod
    @KwDecorator("无人值守，PLC归中举升失败，自复位，设备归位超时未响应执行中")
    def action_swap_plcBackCenterAndLift_selfReset_plcAllowReturnVehicle_timeout1(carNo, packType, faultReason):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行失败', faultReason)

    @staticmethod
    @KwDecorator("无人值守，PLC归中举升失败，自复位，设备归位超时未响应执行完成")
    def action_swap_plcBackCenterAndLift_selfReset_plcAllowReturnVehicle_timeout2(carNo, packType):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行失败', 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行中')

    @staticmethod
    @KwDecorator("无人值守，PLC归中举升失败，自复位，自检（最严重故障码，高压互锁状态）")
    def action_swap_plcBackCenterAndLift_selfReset_selfCheck_bmsmostCriticalFltID_hvil1State(carNo, packType,
                                                                                     bmsmostCriticalFltID,
                                                                                     hvil1State):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行失败', 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行中')
        time.sleep(2)

        SwapFlow.action_selfCheck(bmsmostCriticalFltID, hvil1State)  # 自检
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("无人值守，PLC归中举升失败，自复位，自检，车机停发129")
    def action_swap_plcBackCenterAndLift_selfReset_selfCheck_delV129(carNo, packType):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行失败', 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行中')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_129_command')

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("自检（最严重故障码，高压互锁状态）")
    def action_swap_selfCheck_bmsmostCriticalFltID_hvil1State(carNo, packType, bmsmostCriticalFltID, hvil1State):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')
        time.sleep(2)

        SwapFlow.action_selfCheck(bmsmostCriticalFltID, hvil1State)  # 自检
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行完毕')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("自检，车机停发129")
    def action_swap_selfCheck_delV129(carNo, packType):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_129_command')

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行完毕')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("自检，第二阶段12F心跳不变")
    def action_swap_selfCheck_heartNormal12F(carNo, packType):
        RunKw.api_run(KeyNcsVirtualCarStation, '配置virtual-car-station.yaml：默认配置')

        SwapFlow.action_swap_plcAllowDisassemblyBattery(carNo, packType)

        RunKw.api_run(KeyNcsVirtualCarStation, '配置virtual-car-station.yaml：修改heartNormal12F')

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("自检，前两次满足自检条件，第三次不满足自检条件")
    def action_swap_selfCheck_heartNormal12F_110(carNo, packType):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')
        time.sleep(2)

        SwapFlow.action_selfCheck(0, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行完毕')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')
        time.sleep(6.6)

        SwapFlow.action_selfCheck(0, 1)

    @staticmethod
    @KwDecorator("自检，前两次不满足自检条件，第三次满足自检条件")
    def action_swap_selfCheck_heartNormal12F_001(carNo, packType):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')
        time.sleep(2)

        SwapFlow.action_selfCheck(0, 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行完毕')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')
        time.sleep(6.2)

        SwapFlow.action_selfCheck(0, 0)

    @staticmethod
    @KwDecorator("自检，前两次不满足自检条件，第三次不满足满足自检条件")
    def action_swap_selfCheck_heartNormal12F_000(carNo, packType):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')
        time.sleep(2)

        SwapFlow.action_selfCheck(2, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行完毕')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("自检，第一次满足自检条件，第二次不满足自检条件，第三次满足自检条件")
    def action_swap_selfCheck_heartNormal12F_101(carNo, packType):
        SwapFlow.action_swap_plcBackCenterAndLift(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行中')
        time.sleep(2)

        SwapFlow.action_selfCheck(0, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许拆卸电池包指令：执行完毕')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')
        time.sleep(3)

        SwapFlow.action_selfCheck(2, 1)
        time.sleep(2.2)

        SwapFlow.action_selfCheck(0, 0)

    @staticmethod
    @KwDecorator("自复位，自检，前两次满足自检条件，第三次不满足自检条件")
    def action_swap_selfReset_selfCheck_heartNormal12F_110(carNo, packType):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行失败', 2)
        time.sleep(2)

        SwapFlow.action_selfCheck(0, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')
        time.sleep(6.6)

        SwapFlow.action_selfCheck(0, 1)

    @staticmethod
    @KwDecorator("自复位，自检，前两次不满足自检条件，第三次满足自检条件")
    def action_swap_selfReset_selfCheck_heartNormal12F_001(carNo, packType):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行失败', 2)
        time.sleep(2)

        SwapFlow.action_selfCheck(0, 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')
        time.sleep(6.2)

        SwapFlow.action_selfCheck(0, 0)

    @staticmethod
    @KwDecorator("自复位，自检，前两次不满足自检条件，第三次不满足满足自检条件")
    def action_swap_selfReset_selfCheck_heartNormal12F_000(carNo, packType):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行失败', 2)
        time.sleep(2)

        SwapFlow.action_selfCheck(2, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')

    @staticmethod
    @KwDecorator("自复位，自检，第一次满足自检条件，第二次不满足自检条件，第三次满足自检条件")
    def action_swap_selfReset_selfCheck_heartNormal12F_101(carNo, packType):
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 同步仓位信息至PLC
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行失败', 2)
        time.sleep(2)

        SwapFlow.action_selfCheck(0, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行完毕')
        time.sleep(3)

        SwapFlow.action_selfCheck(2, 1)
        time.sleep(2.2)

        SwapFlow.action_selfCheck(0, 0)

    @staticmethod
    @KwDecorator("车辆信息校验，缺少车辆电池SN")
    def action_swap_plcAllowVehicleLeave_delCarInfo_SN(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_244_command')
        time.sleep(2)

        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)

    @staticmethod
    @KwDecorator("车辆信息校验，缺少VBLE MAC")
    def action_swap_plcAllowVehicleLeave_delCarInfo_MAC(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_118_command')
        time.sleep(2)

        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)

    @staticmethod
    @KwDecorator("车辆信息校验，缺少packType")
    def action_swap_plcAllowVehicleLeave_delCarInfo_packType(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_13A_command')
        time.sleep(2)

        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)

    @staticmethod
    @KwDecorator("车辆信息校验，缺少车辆电池SN、VBLE MAC、packType")
    def action_swap_plcAllowVehicleLeave_delCarInfo(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_244_command')
        time.sleep(2)
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_118_command')
        time.sleep(2)
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_13A_command')
        time.sleep(2)

        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)

    @staticmethod
    @KwDecorator("车辆驶离条件判断，开合门未关到位")
    def action_swap_plcAllowVehicleLeave_openingClosingDoor(carNo, packType, openingClosingDoorStatus):
        SwapFlow.action_swap_plcAllowDisassemblyBattery(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态-开合门状态', openingClosingDoorStatus)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：允许车辆回位指令：执行中')

    @staticmethod
    @KwDecorator("车机停发13A，进行换电")
    def action_swap_delCarInfo_13A(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_13A_command')
        time.sleep(2)

        SwapFlow.action_swap_plcAllowReturnVehicle(carNo, packType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送车辆允许驶离指令到PLC：执行完毕')

    @staticmethod
    @KwDecorator("不同电池包，进行换电")
    def action_swap_packType(carNo, cloudpackType, carPackType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆信息：电池包类别', carPackType)
        time.sleep(2)

        SwapFlow.action_swap_plcAllowReturnVehicle(carNo, cloudpackType)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送车辆允许驶离指令到PLC：执行完毕')

    @staticmethod
    @KwDecorator("PLC响应【车辆驶入换电站且到位请求】执行完毕，自由度不满足")
    def action_swap_plcAllowVehicleEnter_carFreedom(carNo, packType):
        SwapFlow.action_swap_plcRecipeDigestVerify(carNo, packType)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行中')
        time.sleep(3)

        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆自由度信息：破坏所有自由度')

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 1, 1, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行完毕')
        time.sleep(3)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：同步仓位信息：执行完毕')

    @staticmethod
    @KwDecorator("PLC超时未响应【车辆驶入换电站且到位请求】执行中，换电通道顶部雷达")
    def action_swap_plcAllowVehicleEntering_timeout(carNo, packType, channelTopRadarStatus, leftVSlotPositionSignal,
                                                    rightVSlotPositionSignal):
        SwapFlow.action_swap_plcRecipeDigestVerify(carNo, packType)  # PLC配方校验：通过
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', channelTopRadarStatus, leftVSlotPositionSignal,
                          rightVSlotPositionSignal)
        time.sleep(3)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：同步仓位信息：执行完毕')

    @staticmethod
    @KwDecorator("PLC超时未响应【车辆驶入换电站且到位请求】执行结果，换电通道顶部雷达")
    def action_swap_plcAllowVehicleEntered_timeout(carNo, packType, channelTopRadarStatus, leftVSlotPositionSignal,
                                                   rightVSlotPositionSignal):
        SwapFlow.action_swap_plcRecipeDigestVerify(carNo, packType)  # PLC配方校验：通过
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', channelTopRadarStatus, leftVSlotPositionSignal,
                          rightVSlotPositionSignal)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行中')
        time.sleep(3)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：同步仓位信息：执行完毕')

    @staticmethod
    @KwDecorator("自由度监测阶段，自由度不满足")
    def action_swap_carFreedom(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆自由度信息：破坏所有自由度')
        time.sleep(2)
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)

    @staticmethod
    @KwDecorator("自由度监测阶段，方向盘")
    def action_swap_carFreedom_steeringTurnAngle(carNo, packType, steeringTurnAngle):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆自由度信息：方向盘调整', steeringTurnAngle)
        time.sleep(2)
        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)

    @staticmethod
    @KwDecorator("归中举升中，方向角不满足")
    def action_swap_plcBackCenterAndLift_carFreedom_steeringTurnAngle(carNo, packType, centeringStatus):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置归中状态', centeringStatus)
        time.sleep(2)

        SwapFlow.action_swap_plcSwapCampInfo(carNo, packType)  # 下低压成功
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：归中举升：执行中')

        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送车辆自由度信息：方向盘调整', 91)

    @staticmethod
    @KwDecorator("站内有车，进行换电")
    def action_swap_have_car(carNo, packType):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置换电设备状态：通道顶部雷达状态，车辆左V槽在位信号，车辆右V槽在位信号', 1, 1, 1)

        SwapFlow.action_swap_plcAllowVehicleLeave(carNo, packType)

    @staticmethod
    @KwDecorator("自由度超时，车机MBMU生命信号未发")
    def action_swap_delCarFreedom(carNo, packType):
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：车机服务停发某一帧', 'v3_112_command')
        time.sleep(2)

        SwapFlow.action_swap_plcAllowVehicleEnter(carNo, packType)
        time.sleep(4)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：同步仓位信息：执行完毕')

    @staticmethod
    @KwDecorator("车辆未驶入")
    def action_swap_VehicleEnter(carNo, packType):
        RunKw.api_run(KeySetManager, 'SetManager：模拟上报车牌号', carNo)  # 闽DDE5917
        time.sleep(2)

        RunKw.api_run(KeySetSwapFlow, 'SetSwapFlow：【云->站】云端发送检验结果：车牌号，是否允许抬杆', carNo, packType, True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：PLC配方校验：执行完毕')
        time.sleep(2)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行中')
        time.sleep(8)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：同步仓位信息：执行完毕')

    @staticmethod
    @KwDecorator("车辆蓝牙连接成功")
    def action_connect_ble_success():
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙连接执行结果：执行成功')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙连接信息：已连接')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙连接执行结果：复位')

    @staticmethod
    @KwDecorator("车辆蓝牙断开成功")
    def action_diconnect_ble_success():
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙连接执行结果：执行成功')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙连接信息：未连接')
        RunKw.api_run(KeySetVirtualCarStation, 'SetVirtualCarStation：发送蓝牙断开执行结果：复位')

    @staticmethod
    @KwDecorator("驶入换电通道至PLC：执行中")
    def action_swap_plcAllowVehicleEntering(carNo, packType):
        SwapFlow.action_swap_plcRecipeDigestVerify(carNo, packType)  # 换电配方通过
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：发送允许驶入换电通道至PLC：执行中')
        time.sleep(8)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：同步仓位信息：执行完毕')
