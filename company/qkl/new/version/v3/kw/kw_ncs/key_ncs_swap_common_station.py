from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.ncs.ncs_swap_common_station import NcsSwapCommonStation

KeyNcsSwapCommonStation = {
    "nacos获取swap-common-station": HandlerKw.kw(NcsSwapCommonStation.swap_common_station_get),
    "nacos配置swap-common-station：换电云接云平台测试环境": HandlerKw.kw(NcsSwapCommonStation.swap_common_station_post_2),
    "nacos配置swap-common-station：换电云接模拟器": HandlerKw.kw(NcsSwapCommonStation.swap_common_station_post_1),
}
