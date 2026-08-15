from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.ts.home.test_station_base_info import TestStationBaseInfo

KeyTestStationBaseInfo = {
    "校验PLC软件版本": HandlerKw.kw(TestStationBaseInfo.test_plc_software_version),
    "校验云站状态": HandlerKw.kw(TestStationBaseInfo.test_cloud_status),
    "校验换电站站点名称": HandlerKw.kw(TestStationBaseInfo.test_station_name),
    "校验换电站识别代码": HandlerKw.kw(TestStationBaseInfo.test_station_identification_code),
}
