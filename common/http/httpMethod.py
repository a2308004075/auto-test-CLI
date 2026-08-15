class HttpMethod:
    """
    获取http请求方法类型
    """

    @staticmethod
    def _validate_input(path, data):
        """
        验证输入参数

        :param path: 请求的路径
        :param data: 请求的数据
        :return: None
        :raises ValueError: 如果输入参数不合法
        """
        if not isinstance(path, str) or not path:
            raise ValueError("Path must be a non-empty string")
        if data is None:
            data = {}
        return path, data

    @staticmethod
    def _create_info(path, method, data):
        """
        创建响应元组

        :param path: 请求的路径
        :param data: 请求的数据
        :return: 返回一个包含路径、请求方法类型和数据的元组
        """
        return path, method, data

    @staticmethod
    def http_info(path, method, data):
        """
        处理HTTP响应

        :param path: 请求的路径
        :param method: 请求的方法类型
        :param data: 请求的数据
        :return: 返回一个包含路径、请求方法类型和数据的元组
        """
        path, data = HttpMethod._validate_input(path, data)
        return HttpMethod._create_info(path, method, data)
