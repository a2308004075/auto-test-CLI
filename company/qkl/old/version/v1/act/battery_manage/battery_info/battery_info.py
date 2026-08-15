import time
from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.old.version.v1.kw.kw_api.key_set_virtual_car_machine import KeySetVirtualCarMachine


class BatteryInfo:
    """
    电池信息
    """

    @staticmethod
    @KwDecorator('电池初始化')
    def action_1():
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池mac和sn信息：1-10')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1-10号仓')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualPlc：更新寄存器值', 20, 1023)
        time.sleep(2)
