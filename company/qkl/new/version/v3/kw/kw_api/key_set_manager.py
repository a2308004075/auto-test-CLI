from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.api.set_manager import SetManager

KeySetManager = {
    "SetManager：下控蓝牙断开": HandlerKw.kw(SetManager.api_swapFlowTask_manualSendBluetoothStatus_2),
    "SetManager：下控蓝牙连接": HandlerKw.kw(SetManager.api_swapFlowTask_manualSendBluetoothStatus_1),  # 参数：['vbleMac', 'mbmuIrk']
    "SetManager：模拟上报车牌号": HandlerKw.kw(SetManager.api_swapFlowTask_cameraSendCarNo),  # 参数：['carNo']
}
