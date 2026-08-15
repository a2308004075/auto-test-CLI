from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.ncs.ncs_swap_common import NcsSwapCommon

KeyNcsSwapCommon = {
    "nacos获取swap-common": HandlerKw.kw(NcsSwapCommon.swap_common_get),
    "nacos配置swap-common：默认配置": HandlerKw.kw(NcsSwapCommon.swap_common_post_1),
}
