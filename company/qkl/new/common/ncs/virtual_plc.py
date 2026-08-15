from common.utils.handlerNacos import HandlerNacos
from company.qkl.new.common.utils.qklNcsMethod import QKLNcsMethod


class VirtualPlc:
    """
    nacos配置virtual-plc
    """

    @staticmethod
    def virtual_plc_get():
        """
        nacos获取virtual-plc.yaml
        """
        data = {
            "dataId": "virtual-plc.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station"
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.get(data))

    @staticmethod
    def virtual_plc_post(content):
        """
        nacos配置virtual-plc
        """
        data = {
            "dataId": "virtual-plc.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station",
            "type": "yaml",
            "content": content
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.post(data))
