from common.handlerKw.handlerKw import HandlerKw
from company.qkl.old.version.v1.ts.swap_channel.test_swap_channel import TestSwapChannel

KeyTestSwapChannel = {
    "PLC换电流程状态": HandlerKw.kw(TestSwapChannel.test_9),
    "一次换电成功": HandlerKw.kw(TestSwapChannel.test_2),
    "下发两次云端校验结果": HandlerKw.kw(TestSwapChannel.test_4),
    "二次换电成功": HandlerKw.kw(TestSwapChannel.test_3),
    "初始化车辆状态：闽H684349": HandlerKw.kw(TestSwapChannel.test_1),
    "安装第二块成功-举升平台回落，自由度破坏变恢复": HandlerKw.kw(TestSwapChannel.test_7),
    "归中失败": HandlerKw.kw(TestSwapChannel.test_8),
    "断蓝牙成功": HandlerKw.kw(TestSwapChannel.test_5),
    "自检失败，无法二次换电：车上电池继电器": HandlerKw.kw(TestSwapChannel.test_6),
}
