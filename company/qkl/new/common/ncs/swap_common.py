from common.utils.handlerNacos import HandlerNacos
from company.qkl.new.common.utils.qklNcsMethod import QKLNcsMethod


class SwapCommon:
    """
    nacos操作swap-common
    """

    @staticmethod
    def swap_common_get():
        """
        nacos获取swap-common
        """
        data = {
            "dataId": "swap-common.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station"
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.get(data))

    @staticmethod
    def swap_common_post(content):
        """
        nacos配置swap-common
        """
        data = {
            "dataId": "swap-common.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station",
            "type": "yaml",
            "content": content
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.post(data))
