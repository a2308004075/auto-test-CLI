from common.handlerKw.handlerKw import HandlerKw
from company.qkl.old.version.v1.act.swap_channel.swap_channel import SwapChannel

KeySwapChannel = {
    "PLC换电流程状态": HandlerKw.kw(SwapChannel.action_9),
    "一次换电成功": HandlerKw.kw(SwapChannel.action_3),
    "下发两次云端校验结果": HandlerKw.kw(SwapChannel.action_4),
    "二次换电成功": HandlerKw.kw(SwapChannel.action_2),
    "初始化车辆状态：闽H684349": HandlerKw.kw(SwapChannel.action_1),
    "安装第二块成功-举升平台回落，自由度破坏变恢复": HandlerKw.kw(SwapChannel.action_7),
    "归中失败": HandlerKw.kw(SwapChannel.action_8),
    "断蓝牙成功": HandlerKw.kw(SwapChannel.action_5),
    "自检失败，无法二次换电：车上电池继电器": HandlerKw.kw(SwapChannel.action_6),
}
