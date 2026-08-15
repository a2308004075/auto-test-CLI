from common.utils.handlerNacos import HandlerNacos
from company.qkl.new.common.utils.qklNcsMethod import QKLNcsMethod


class VirtualBattery:
    """
    nacos操作virtual-battery
    """

    @staticmethod
    def virtual_battery_get():
        """
        nacos获取virtual-battery
        """
        data = {
            "dataId": "virtual-battery.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station"
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.get(data))

    @staticmethod
    def virtual_battery_post(content):
        """
        nacos配置virtual-battery
        """
        data = {
            "dataId": "	virtual-battery.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station",
            "type": "yaml",
            "content": content
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.post(data))
