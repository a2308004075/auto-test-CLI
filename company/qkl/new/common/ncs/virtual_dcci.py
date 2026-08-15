from common.utils.handlerNacos import HandlerNacos
from company.qkl.new.common.utils.qklNcsMethod import QKLNcsMethod


class VirtualDcci:
    """
    nacos操作virtual-dcci
    """

    @staticmethod
    def virtual_dcci_get():
        """
        nacos获取virtual-dcci.
        """
        data = {
            "dataId": "virtual-dcci.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station"
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.get(data))

    @staticmethod
    def virtual_dcci_post(content):
        """
        nacos配置virtual-dcci
        """
        data = {
            "dataId": "virtual-dcci.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station",
            "type": "yaml",
            "content": content
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.post(data))
