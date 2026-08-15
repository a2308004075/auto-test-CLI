import json
import websockets.sync.client as client
from common.utils.handleEnv import HandleEnv


class HandlerWss:
    """
    Wss请求
    """

    @staticmethod
    def Wss_New(userId: str = '567', *kwargs):
        """
        新站websocket请求
        该方法用于处理新的websocket请求，接收路径和数据作为参数，发送数据并接收响应
        参数:
            *kwargs: 可变长度的参数列表，预期包含两个元素，第一个是路径，第二个是发送的数据
        返回:
            wss_recv_json: 接收到的websocket响应数据，已转换为字典格式
        """
        # 解析传入的参数，分别赋值给路径和数据变量
        path, data = kwargs
        # 获取环境对应的websocket主机地址
        host = HandleEnv.get_env_wss()
        # 拼接完整的请求URL
        base_url = f'{host}{path}'
        # 使用with语句确保websocket连接能够正确关闭
        with client.connect(base_url) as websocket:
            # 发送用户ID信息
            websocket.send(json.dumps({"userId": userId}))
            # 发送实际数据
            websocket.send(json.dumps(data))
            # 接收websocket响应，并转换为字典格式
            wss_recv_json = json.loads(websocket.recv())
            # 返回接收到的响应数据
            return wss_recv_json

    @staticmethod
    def Wss_old(*kwargs):
        """
        旧站websocket请求
        该方法用于向旧网站的websocket接口发送请求，并接收处理响应数据
        参数:
            *kwargs: 可变长度的参数列表，用于指定websocket请求的路径
        返回:
            msg_json: 解析后的响应数据，以字典形式返回
        """
        # 获取websocket请求的路径
        path = kwargs
        # 获取环境对应的websocket主机地址
        host = HandleEnv.get_env_wss()
        # 拼接完整的请求URL
        base_url = f'{host}{path}'
        # 使用with语句确保websocket连接能够正确关闭
        with client.connect(base_url) as websocket:
            # 接收websocket响应的消息并解析为JSON格式
            msg_json = json.loads(websocket.recv())
            # 返回解析后的消息
            return msg_json
