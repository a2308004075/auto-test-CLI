from common.utils.handlerNacos import HandlerNacos
from company.qkl.new.common.utils.qklNcsMethod import QKLNcsMethod


class SwapCommonStation:
    """
    nacos操作swap-common-station
    """

    @staticmethod
    def swap_common_station_get():
        """
        nacos获取swap-common-station
        """
        data = {
            "dataId": "swap-common-station.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station"
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.get(data))

    @staticmethod
    def swap_common_station_post(content):
        """
        nacos配置swap-common-station
        """
        data = {
            "dataId": "swap-common-station.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station",
            "type": "yaml",
            "content": content
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.post(data))
