from common.utils.handlerNacos import HandlerNacos
from company.qkl.new.common.utils.qklNcsMethod import QKLNcsMethod


class VirtualCarStation:
    """
    nacos操作virtual-car-station
    """

    @staticmethod
    def virtual_car_station_get():
        """
        nacos获取virtual-car-station
        """
        data = {
            "dataId": "virtual-car-station.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station"
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.get(data))

    @staticmethod
    def virtual_car_station_post(content):
        """
        nacos配置virtual-car-station
        """
        data = {
            "dataId": "virtual-car-station.yaml",
            "group": "DEFAULT_GROUP",
            "tenant": "swap-station",
            "type": "yaml",
            "content": content
        }
        return HandlerNacos.NacosReq(QKLNcsMethod.post(data))
