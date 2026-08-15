class HandlerKw:
    @staticmethod
    def kw(func):
        """
        封装关键字
        """
        return lambda *args: func(*args)
