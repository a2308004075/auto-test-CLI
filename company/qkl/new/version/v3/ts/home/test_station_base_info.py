from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_act.home.key_station_base_info import KeyStationBaseInfo


class TestStationBaseInfo:
    @staticmethod
    @KwDecorator('校验换电站站点名称')
    def test_station_name():
        RunKw.act_run(KeyStationBaseInfo, '换电站站点名称', "测试站01")

    @staticmethod
    @KwDecorator('校验换电站识别代码')
    def test_station_identification_code():
        RunKw.act_run(KeyStationBaseInfo, '换电站识别代码', "*PRO-V3.0-14-C-SLRTB-00000000-0325030002")

    @staticmethod
    @KwDecorator('校验PLC软件版本')
    def test_plc_software_version():
        RunKw.act_run(KeyStationBaseInfo, 'PLC软件版本', 3, 1, 6, 50)

    @staticmethod
    @KwDecorator('校验云站状态')
    def test_cloud_status():
        RunKw.act_run(KeyStationBaseInfo, '云站状态', 0)
