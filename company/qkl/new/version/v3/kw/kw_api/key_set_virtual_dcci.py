from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.api.set_virtual_dcci import SetVirtualDcci

KeySetVirtualDcci = {
    "SetVirtualDcci：充电机上送充电停止完成帧（4503）：1-正常停止": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_sendStopChargeReport_1),  # 参数：['flowNo']
    "SetVirtualDcci：充电机上送充电启动完成帧（4501）：0-成功": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_sendStartChargeReport_0),  # 参数：['flowNo']
    "SetVirtualDcci：充电机响应停止充电（5000）：0-成功": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_sendStopChargeCallback_0),  # 参数：['flowNo']
    "SetVirtualDcci：充电机响应远程启动（4900）：0-成功": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_sendStartChargeCallback_0),  # 参数：['flowNo']
    "SetVirtualDcci：充电机响应远程启动（4900）：1-失败": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_sendStartChargeCallback_1),  # 参数：['flowNo']
    "SetVirtualDcci：充电枪数据上报4552：1-14号仓keyon断开、cc1断开": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_2),
    "SetVirtualDcci：充电枪数据上报4552：1-14号仓keyon连接、cc1连接": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_1),
    "SetVirtualDcci：充电枪数据上报4552：1-30号仓keyon断开、cc1断开": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_10),
    "SetVirtualDcci：充电枪数据上报4552：1-30号仓keyon连接、cc1连接": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_11),
    "SetVirtualDcci：充电枪数据上报4552：1号仓CC1状态：断开": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_7),
    "SetVirtualDcci：充电枪数据上报4552：1号仓CC1状态：连接": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_6),
    "SetVirtualDcci：充电枪数据上报4552：1号仓keyon断开": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_4),
    "SetVirtualDcci：充电枪数据上报4552：1号仓keyon连接": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_3),
    "SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：0": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_5),
    "SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_9),
    "SetVirtualDcci：充电枪数据上报4552：修改1号仓参数": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4552_8),  # 参数：['flowNo']
    "SetVirtualDcci：充电设备上报历史订单4559": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4559_0),
    "SetVirtualDcci：充电设备上报电池连接状态(4515)": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_sendBatteryStatus_0),  # 参数：['chargerNo', 'gunNo', 'position', 'status']
    "SetVirtualDcci：充电设备主动上送充电记录（4200）：正常停止": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_sendChargeRecord_0),  # 参数：['flowNo']
    "SetVirtualDcci：充电设备应答站功率/电流调节指令结果：0-成功": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_sendChargeAdjustParamResult_0),  # 参数：['flowNo']
    "SetVirtualDcci：充电设备数据上报4551：烟感故障：0": HandlerKw.kw(SetVirtualDcci.api_v3_dcciMock_feign_send4551_1),
}
