from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_swap_flow import KeySetSwapFlow
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc


class StationBaseInfo:
    """
    换电站基本信息
    """

    @staticmethod
    @KwDecorator("换电站站点名称")
    def action_station_Name(stationName):
        RunKw.api_run(KeySetSwapFlow, 'SetSwapFlow：【云->站】换电站基本数据设置：换电站站点名称', stationName)

    @staticmethod
    @KwDecorator("换电站识别代码")
    def action_station_identification_code(code):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置站基本信息', code)

    @staticmethod
    @KwDecorator("PLC软件版本")
    def action_plc_software_version(aversion, bversion, cversion, dversion):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：PLC软件版本', aversion, bversion, cversion, dversion)

    @staticmethod
    @KwDecorator("云站状态")
    def action_cloud_status(status):
        if status == 0:
            RunKw.api_run(KeySetSwapFlow, 'SetSwapFlow：【控制】断开mqtt')
        if status == 1:
            RunKw.api_run(KeySetSwapFlow, 'SetSwapFlow：【控制】重连mqtt')
