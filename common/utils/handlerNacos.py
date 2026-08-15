import requests
import json
from common.utils.logConfig import log
from common.utils.handleEnv import HandleEnv


# 定义一个处理Nacos请求的类
class HandlerNacos:
    """
    nacos请求
    """

    # 定义一个静态方法，用于发送Nacos请求
    @staticmethod
    def NacosReq(*kwargs):
        """
        http请求
        """
        path, method, data = kwargs
        nacos, accessToken = HandleEnv.get_env_nacos()

        url = nacos + path

        get_headers = {
            'accessToken': accessToken
        }
        post_headers = {
            'Content-Type': 'application/x/www-form-urlencoded',
            'accessToken': accessToken
        }

        resp = None
        method = method.upper()
        if method == 'GET':
            resp = requests.request(method=method, url=url, headers=get_headers, params=data)
        if method == 'POST' or method == 'DELETE':
            resp = requests.request(method=method, url=url, headers=post_headers, data=data)
        code = resp.status_code
        if code == 200:
            if 'GET' in resp.request.method:
                try:
                    log.info(f'params：{resp.request.url.split("?")[1]}')
                    return resp
                except Exception as e:
                    log.error(f'处理GET请求参数时发生错误: {e}')
                    return resp
            elif 'POST' in resp.request.method:
                log.info(f'body：{json.loads(resp.request.body)}')
                return resp
            elif 'DELETE' in resp.request.method:
                log.info(f'body：{json.loads(resp.request.body)}')
                return resp
        else:
            if 'GET' in resp.request.method:
                try:
                    log.error(f'http下控失败=={code}\t{resp.url}\tparams：{resp.request.url.split("?")[1]}')
                    return resp
                except Exception as e:
                    log.error(f'处理GET请求参数时发生错误: {e}')
                    return resp
            elif 'POST' in resp.request.method:
                log.error(f'http下控失败=={code}\t{resp.url}\tbody：{json.loads(resp.request.body)}')
                return resp
            elif 'DELETE' in resp.request.method:
                log.error(f'http下控失败=={code}\t{resp.url}\tbody：{json.loads(resp.request.body)}')
                return resp
            else:
                return resp
