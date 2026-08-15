from common.utils.handlerNacos import HandlerNacos
from company.qkl.new.common.utils.qklNcsMethod import QKLNcsMethod


class SwapTempCommon:
    """
    nacos操作swap-temp-common
    """

    @staticmethod
    def swap_temp_common_get():
        """
        nacos获取swap-temp-common
        """
        data = {
            "dataId": "swap-temp-common.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station"
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.get(data))

    @staticmethod
    def swap_temp_common_post(content):
        """
        nacos配置swap-temp-common
        """
        data = {
            "dataId": "swap-temp-common.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station",
            "type": "yaml",
            "content": content
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.post(data))
