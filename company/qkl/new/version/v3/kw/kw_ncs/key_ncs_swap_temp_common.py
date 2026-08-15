from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.dao.ncs.ncs_swap_temp_common import NcsSwapTempCommon

KeyNcsSwapTempCommon = {
    "nacos获取swap-temp-common": HandlerKw.kw(NcsSwapTempCommon.swap_temp_common_get),
    "nacos配置swap-temp-common：默认配置": HandlerKw.kw(NcsSwapTempCommon.swap_temp_common_post_1),
}
