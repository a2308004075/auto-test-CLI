class QKLWss:
    """
    WebSocket相关操作
    """

    @staticmethod
    def ws(data):
        """
        新站WebSocket接口：/ws
        """
        path = '/ws'
        return path, data
