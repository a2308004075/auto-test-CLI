from common.handlerKw.kwDecorator import KwDecorator
from common.utils.handlerWss import HandlerWss
from company.qkl.new.common.utils.qklWss import QKLWss


class NewWss:
    """
    新站wss
    """

    @staticmethod
    @KwDecorator("获取currentProcessData的wss消息")
    def current_process_data_wss():
        data = {"type": "currentProcessData"}
        return HandlerWss.Wss_New(QKLWss.ws(data))

    @staticmethod
    @KwDecorator("获取volume的wss消息")
    def volume_wss():
        data = {"type": "volume"}
        return HandlerWss.Wss_New(QKLWss.ws(data))

    @staticmethod
    @KwDecorator("获取fireMoveWarn的wss消息")
    def fire_move_warn_wss():
        data = {"type": "fireMoveWarn"}
        return HandlerWss.Wss_New(QKLWss.ws(data))

    @staticmethod
    @KwDecorator("获取underBox的wss消息")
    def under_box_wss():
        data = {"type": "underBox"}
        return HandlerWss.Wss_New(QKLWss.ws(data))
