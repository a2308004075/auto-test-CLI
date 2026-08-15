from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.ncs.ncs_virtual_car_station import NcsVirtualCarStation

KeyNcsVirtualCarStation = {
    "nacos获取virtual-car-station": HandlerKw.kw(NcsVirtualCarStation.virtual_car_station_get),
    "nacos配置virtual-car-station：修改heartNormal12F": HandlerKw.kw(NcsVirtualCarStation.virtual_car_station_post_2),
    "nacos配置virtual-car-station：默认配置": HandlerKw.kw(NcsVirtualCarStation.virtual_car_station_post_1),
}
