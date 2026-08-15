class QKLNcsMethod:
    """
    该类提供了与Nacos服务交互的静态方法。
    Nacos是一个动态服务发现、配置管理和服务管理平台。
    该类目前支持通过POST和GET方法与Nacos进行通信。
    """

    @staticmethod
    def post(data):
        """
        发送配置到Nacos的POST请求。

        参数:
        - data: 包含要发送的配置数据的字典。

        返回:
        - 一个元组，包含请求路径、HTTP方法和数据。
        """
        # 定义Nacos配置的POST请求路径
        path = "/nacos/v1/cs/configs"
        # 返回请求路径、方法和数据
        return path, 'post', data

    @staticmethod
    def get(data):
        """
        发送配置到Nacos的GET请求。

        参数:
        - data: 包含要获取的配置数据的字典。

        返回:
        - 一个元组，包含请求路径、HTTP方法和数据。
        """
        # 定义Nacos配置的GET请求路径
        path = "/nacos/v1/cs/configs"
        # 返回请求路径、方法和数据
        return path, 'get', data
