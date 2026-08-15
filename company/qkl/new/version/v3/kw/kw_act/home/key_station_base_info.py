from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.act.home.station_base_info import StationBaseInfo

KeyStationBaseInfo = {
    "PLC软件版本": HandlerKw.kw(StationBaseInfo.action_plc_software_version),  # 参数：['aversion', 'bversion', 'cversion', 'dversion']
    "云站状态": HandlerKw.kw(StationBaseInfo.action_cloud_status),  # 参数：['status']
    "换电站站点名称": HandlerKw.kw(StationBaseInfo.action_station_Name),  # 参数：['stationName']
    "换电站识别代码": HandlerKw.kw(StationBaseInfo.action_station_identification_code),  # 参数：['code']
}
