from common.handlerKw.handlerKw import HandlerKw
from company.qkl.old.version.v1.dao.api.set_virtual_car_machine import SetVirtualCarMachine

KeySetVirtualCarMachine = {
    "SetVirtualCarMachine：抓拍车牌": HandlerKw.kw(SetVirtualCarMachine.api_swapSignalMock_captureCarPlate),  # 参数：['plateNo']
    "SetVirtualCarMachine：换电交互信息-自检失败、上高压失败": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_swapInteractionInfo_2),  # 参数：['vin']
    "SetVirtualCarMachine：换电交互信息-蓝牙断开": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_swapInteractionInfo_3),  # 参数：['vin']
    "SetVirtualCarMachine：换电交互信息，自检通过": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_swapInteractionInfo_1),  # 参数：['vin']
    "SetVirtualCarMachine：换电结束": HandlerKw.kw(SetVirtualCarMachine.api_swapSignalMock_swapFinished),
    "SetVirtualCarMachine：电池mac和sn信息：1-10": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_batteryCodeInfo_1),
    "SetVirtualCarMachine：电池mac和sn信息：闽H684349": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_batteryCodeInfo_1),
    "SetVirtualCarMachine：电池换电交互信息：1-10号仓": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_swapInteractionInfo_1),
    "SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_swapInteractionInfo_2),
    "SetVirtualCarMachine：电池换电交互信息：3、4仓断蓝牙": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_swapInteractionInfo_3),
    "SetVirtualCarMachine：电池换电交互信息：5、6仓断蓝牙": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_swapInteractionInfo_4),
    "SetVirtualCarMachine：电池数据信息-电压、电流、电阻，发0值": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_batteryDataInfo2_1),
    "SetVirtualCarMachine：电池数据信息-累计静置时间、无线通讯信号强度：无CBMU心跳": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_batteryDataInfo4_2),
    "SetVirtualCarMachine：电池数据信息-累计静置时间、无线通讯信号强度：有CBMU心跳": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_batteryDataInfo4_1),
    "SetVirtualCarMachine：电池数据信息：数据不为0": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_batteryDataInfo_2),
    "SetVirtualCarMachine：电池数据信息：数据为0": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_batteryDataInfo_1),
    "SetVirtualCarMachine：电池标志和状态信息": HandlerKw.kw(SetVirtualCarMachine.api_cbmuMock_batterySignOrStateInfo),
    "SetVirtualCarMachine：电池状态和标志信息：发0值": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_batterySignOrStateInfo_1),
    "SetVirtualCarMachine：电池状态和标志信息：电池包主负继电器状态、电池包主正继电器状态": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_batterySignOrStateInfo_3),  # 参数：['position', 'MainNegCnctrState', 'MainPosCnctrState']
    "SetVirtualCarMachine：车辆电池状态和标志信息：故障等级大于5": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_batterySignOrStateInfo_2),
    "SetVirtualCarMachine：车辆自由度信息：打开车门": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_carFreedomInfo_3),
    "SetVirtualCarMachine：车辆自由度信息：破坏非车门自由度": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_carFreedomInfo_2),
    "SetVirtualCarMachine：车辆自由度信息：通过": HandlerKw.kw(SetVirtualCarMachine.api_tbmuMock_carFreedomInfo_1),
    "SetVirtualCarMachine：车辆连接": HandlerKw.kw(SetVirtualCarMachine.api_swapSignalMock_carConnect),
}
