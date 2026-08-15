from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.common.ncs.swap_temp_common import SwapTempCommon


class NcsSwapTempCommon:
    """
    nacos操作swap-temp-common
    """

    @staticmethod
    @KwDecorator("nacos获取swap-temp-common")
    def swap_temp_common_get():
        return SwapTempCommon.swap_temp_common_get()

    @staticmethod
    @KwDecorator("nacos配置swap-temp-common：默认配置")
    def swap_temp_common_post_1():
        content = """caes:
  swap:
    collect:
      host: 10.100.2.24
    netty:
      clients:
        carStationNettyInitType31:
          - id: 2
            host: 0.0.0.0
            port: 4001
temp:
  bms:
    changeTemp: -20
    carFollow: true
    checkPackType: false
    autoGenSnAfterFail: false
        """
        return SwapTempCommon.swap_temp_common_post(content)
