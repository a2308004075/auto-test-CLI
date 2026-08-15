import time
from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc


class BatteryReturn:
    """
    电池一键入仓
    """

    @staticmethod
    @KwDecorator("电池一键入仓：执行中")
    def action_1():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：电池一键入仓：执行中')

    @staticmethod
    @KwDecorator("电池一键入仓：执行完毕")
    def action_2():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：电池一键入仓：执行中')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：电池一键入仓：执行完毕')

    @staticmethod
    @KwDecorator("电池一键入仓：执行错误")
    def action_3():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：电池一键入仓：执行中')
        time.sleep(2)

        faultReason = 0
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：电池一键入仓：执行错误', faultReason)
