from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.api.set_swap_flow import SetSwapFlow

KeySetSwapFlow = {
    "SetSwapFlow：【云->站】云端发送开始换电": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_sendStartSwap),
    "SetSwapFlow：【云->站】云端发送检验结果：车牌号，是否允许抬杆": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_sendReceiveCloudValid_carNo_packType_ableToChange),  # 参数：['carNo', 'packType', 'ableToChange']
    "SetSwapFlow：【云->站】云端发送检验结果：车牌号，通过": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_sendReceiveCloudValid_carNo_packType),  # 参数：['carNo', 'packType']
    "SetSwapFlow：【云->站】云端发送检验结果：闽DDE5917，通过": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_sendReceiveCloudValid_packType),  # 参数：['packType']
    "SetSwapFlow：【云->站】云端返回电池标签": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_queryPackLabelResp),
    "SetSwapFlow：【云->站】换电站基本数据设置：换电站站点名称": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_downPowerStationBaseInfo),  # 参数：['stationName']
    "SetSwapFlow：【云->站】车辆停稳应答：闽DDE5917": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_carStoppedResp_1),
    "SetSwapFlow：【控制】断开mqtt": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_disconnect),
    "SetSwapFlow：【控制】重连mqtt": HandlerKw.kw(SetSwapFlow.api_cloudMqtt_reconnect),
}
