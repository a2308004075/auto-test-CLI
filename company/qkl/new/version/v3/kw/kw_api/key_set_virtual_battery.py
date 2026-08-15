from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.api.set_virtual_battery import SetVirtualBattery

KeySetVirtualBattery = {
    "SetVirtualBattery：18A2F980，站内小计信息清除控制执行结果": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18A2F980_1),  # 参数：['batteryPosition', 'subInfoInClrSts']
    "SetVirtualBattery：18A2F980，站外小计信息清除控制执行结果": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18A2F980_2),  # 参数：['batteryPosition', 'subInfoOutClrSts']
    "SetVirtualBattery：18F10180 基础参数1：1仓位，故障恢复": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F10180_2),
    "SetVirtualBattery：18F10180 基础参数1：1仓位，故障码6": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F10180_1),
    "SetVirtualBattery：18F10980Pack基础信息3：1-14号仓": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_18F10980_14),
    "SetVirtualBattery：18F10980Pack基础信息3：1-30号仓": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_18F10980_30),
    "SetVirtualBattery：18F10980Pack基础信息3：1号仓电池真实SOC=80": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_18F10980_2),
    "SetVirtualBattery：18F10980Pack基础信息3：SOC不可信标志": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_18F10980_batteryPosition_ForSOCUnavailableFlg),  # 参数：['batteryPosition', 'ForSOCUnavailableFlg']
    "SetVirtualBattery：18F10C80继电器状态，14个仓位": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_18F10C80_14),
    "SetVirtualBattery：18F10C80继电器状态，30个仓位": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_18F10C80_30),
    "SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=0": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_18F10C80_0),
    "SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=1": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_18F10C80_1),
    "SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=1": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F80180_3),
    "SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=3": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F80180_2),
    "SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=5": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F80180_4),
    "SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=6": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F80180_1),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=2.0": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_5),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=2.91": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_6),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.0": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_7),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.2": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_1),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.3": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_8),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.4": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_2),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.5": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_3),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.702": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_9),
    "SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.8": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_4),
    "SetVirtualBattery：18F82280 基础参数1：最大电压、最小电压": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82280_batteryPosition_s_MaxCellVoltMv_s_MinCellVoltMv),  # 参数：['batteryPosition', 's_MaxCellVoltMv', 's_MinCellVoltMv']
    "SetVirtualBattery：18F82380，温度检测点极值统计：最高温度-10，最低温度-2": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X118F82380_5),
    "SetVirtualBattery：18F82380，温度检测点极值统计：最高温度10，最低温度-15": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X118F82380_1),
    "SetVirtualBattery：18F82380，温度检测点极值统计：最高温度20，最低温度15": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X118F82380_3),
    "SetVirtualBattery：18F82380，温度检测点极值统计：最高温度35，最低温度-7": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X118F82380_2),
    "SetVirtualBattery：18F82380，温度检测点极值统计：最高温度40，最低温度25": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X118F82380_4),
    "SetVirtualBattery：18F82380，温度检测点极值统计：最高温度，最低温度": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X118F82380_batteryPosition_MaxModuleTempDegC_MinModuleTempDegC),  # 参数：['batteryPosition', 's_MaxModuleTempDegC', 's_MinModuleTempDegC']
    "SetVirtualBattery：18F82580输入电能量数据：1-14仓位": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F82580_14),
    "SetVirtualBattery：响应清除故障：1-失败": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_clearFaultResp_1),
    "SetVirtualBattery：响应清除故障：2-成功": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_clearFaultResp_21),
    "SetVirtualBattery：电池服务停发某一帧": HandlerKw.kw(SetVirtualBattery.api_schedule_del),  # 参数：['code']
    "SetVirtualBattery：电池服务恢复发送某一帧": HandlerKw.kw(SetVirtualBattery.api_schedule_add),  # 参数：['code']
    "SetVirtualBattery：设置sn：1-14号仓SN": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F80580_14),
    "SetVirtualBattery：设置sn：1-30号仓SN": HandlerKw.kw(SetVirtualBattery.api_batteryMock_v3_feign_do0X18F80580_30),
}
