from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.ncs.ncs_virtual_dcci import NcsVirtualDcci

KeyNcsVirtualDcci = {
    "nacos获取virtual-dcci": HandlerKw.kw(NcsVirtualDcci.virtual_dcci_get),
    "nacos配置virtual-dcci：默认配置": HandlerKw.kw(NcsVirtualDcci.virtual_dcci_post_1),
}
