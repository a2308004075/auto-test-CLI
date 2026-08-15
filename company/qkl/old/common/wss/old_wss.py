from common.handlerKw.kwDecorator import KwDecorator
from common.utils.handlerWss import HandlerWss
from company.qkl.old.common.utils.qklWss import QKLWss


class OldWss:
    """
    旧站
    """

    @staticmethod
    @KwDecorator("获取newWebSocket的wss消息")
    def manager_newWebSocket():
        return HandlerWss.Wss_old(QKLWss.manager_newWebSocket())

    @staticmethod
    @KwDecorator("获取rbcWebSocket的wss消息")
    def rbc_webSocket():
        return HandlerWss.Wss_old(QKLWss.rbc_webSocket())

    @staticmethod
    @KwDecorator("获取webSocketOfManager的wss消息")
    def manager_webSocketOfManager():
        return HandlerWss.Wss_old(QKLWss.manager_webSocketOfManager())
