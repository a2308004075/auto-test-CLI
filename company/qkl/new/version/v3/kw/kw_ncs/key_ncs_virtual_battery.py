from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.ncs.ncs_virtual_battery import NcsVirtualBattery

KeyNcsVirtualBattery = {
    "nacos获取virtual-battery": HandlerKw.kw(NcsVirtualBattery.virtual_battery_get),
    "nacos配置virtual-battery：默认配置": HandlerKw.kw(NcsVirtualBattery.virtual_battery_post_1),
}
