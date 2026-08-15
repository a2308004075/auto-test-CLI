from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.old.version.v1.kw.kw_act.swap_channel.key_swap_channel import KeySwapChannel


class TestSwapChannel:
    @staticmethod
    @KwDecorator('初始化车辆状态：闽H684349')
    def test_1():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')

    @staticmethod
    @KwDecorator('一次换电成功')
    def test_2():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')
        RunKw.act_run(KeySwapChannel, '一次换电成功')

    @staticmethod
    @KwDecorator('二次换电成功')
    def test_3():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')
        RunKw.act_run(KeySwapChannel, '二次换电成功')

    @staticmethod
    @KwDecorator('下发两次云端校验结果')
    def test_4():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')
        RunKw.act_run(KeySwapChannel, '下发两次云端校验结果')

    @staticmethod
    @KwDecorator('断蓝牙成功')
    def test_5():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')
        RunKw.act_run(KeySwapChannel, '断蓝牙成功')

    @staticmethod
    @KwDecorator('自检失败，无法二次换电：车上电池继电器')
    def test_6():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')
        RunKw.act_run(KeySwapChannel, '自检失败，无法二次换电：车上电池继电器')

    @staticmethod
    @KwDecorator('安装第二块成功-举升平台回落，自由度破坏变恢复')
    def test_7():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')
        RunKw.act_run(KeySwapChannel, '安装第二块成功-举升平台回落，自由度破坏变恢复')

    @staticmethod
    @KwDecorator('归中失败')
    def test_8():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')
        RunKw.act_run(KeySwapChannel, '归中失败')

    @staticmethod
    @KwDecorator('PLC换电流程状态')
    def test_9():
        RunKw.act_run(KeySwapChannel, '初始化车辆状态：闽H684349')
        RunKw.act_run(KeySwapChannel, 'PLC换电流程状态')
