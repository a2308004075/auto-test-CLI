from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.old.version.v1.kw.kw_act.battery_manage.battery_info.key_battery_info import KeyBatteryInfo


class TestBatteryInfo:
    @staticmethod
    @KwDecorator('电池初始化')
    def test_1():
        RunKw.act_run(KeyBatteryInfo, '电池初始化')
