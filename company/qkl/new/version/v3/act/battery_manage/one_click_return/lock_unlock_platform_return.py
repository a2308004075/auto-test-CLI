import time
from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc


class LockUnlockPlatformReturn:
    """
    加解锁平台回位
    """

    @staticmethod
    @KwDecorator("加解锁平台回位：执行中")
    def action_1():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：加解锁平台回位：执行中')

    @staticmethod
    @KwDecorator("加解锁平台回位：执行完毕")
    def action_2():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：加解锁平台回位：执行中')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：加解锁平台回位：执行完毕')

    @staticmethod
    @KwDecorator("加解锁平台回位：执行错误")
    def action_3():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：加解锁平台回位：执行中')
        time.sleep(2)

        faultReason = 0
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：加解锁平台回位：执行错误', faultReason)
