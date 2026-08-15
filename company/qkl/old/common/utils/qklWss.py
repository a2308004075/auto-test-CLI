class QKLWss:
    """
    WebSocket相关操作
    """

    @staticmethod
    def manager_webSocketOfManager(data=None):
        """
        旧站WebSocket接口：/manager/webSocketOfManager
        """
        path = '/manager/webSocketOfManager'
        return path, data if data is not None else {}

    @staticmethod
    def manager_newWebSocket(data=None):
        """
        旧站WebSocket接口：/manager/newWebSocket
        """
        path = '/manager/newWebSocket'
        return path, data if data is not None else {}

    @staticmethod
    def rbc_webSocket(data=None):
        """
        旧站WebSocket接口：/rbc/webSocket
        """
        path = '/rbc/webSocket'
        return path, data if data is not None else {}
