from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.ncs.ncs_virtual_plc import NcsVirtualPlc

KeyNcsVirtualPlc = {
    "nacos获取virtual-plc": HandlerKw.kw(NcsVirtualPlc.virtual_plc_get),
    "nacos配置virtual-plc：默认配置": HandlerKw.kw(NcsVirtualPlc.virtual_plc_post_1),
}
