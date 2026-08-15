from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.common.ncs.swap_common import SwapCommon


class NcsSwapCommon:
    """
    nacos操作swap-common
    """

    @staticmethod
    @KwDecorator("nacos获取swap-common")
    def swap_common_get():
        return SwapCommon.swap_common_get()

    @staticmethod
    @KwDecorator("nacos配置swap-common：默认配置")
    def swap_common_post_1():
        content = """test
        """
        return SwapCommon.swap_common_post(content)
