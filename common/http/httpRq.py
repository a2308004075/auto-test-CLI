import requests
import json
from common.utils.logConfig import log
from common.utils.handleEnv import HandleEnv


class HttpRq:
    """
    站控请求
    """

    @staticmethod
    def req(path: str = None, method: str = None, data=None, other_authorization: str = None):
        """
        http请求
        """

        authorization = HandleEnv.get_env_authorization()
        host = HandleEnv.get_env_host()
        if not host:
            raise ValueError("环境变量中的主机地址不能为空")

        if other_authorization:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {other_authorization}'
            }
        else:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': authorization
            }
        method = method.upper()
        try:
            if method == 'GET':
                resp = requests.request(method=method, url=f"{host}{path}", headers=headers, params=data)
            elif method in ['POST', 'DELETE']:
                resp = requests.request(method=method, url=f"{host}{path}", headers=headers, json=data)
            else:
                raise ValueError(f"不支持的请求方法: {method}")
        except requests.exceptions.RequestException as e:
            log.error(f"请求失败: {e}")
            return None

        if resp is None:
            log.error("请求响应为 None")
            return None

        if 'code' in resp.text:
            code = resp.json().get("code")
            if code == 200:
                return HttpRq.log_response(resp, method, True)
            else:
                return HttpRq.log_response(resp, method, False)
        else:
            return resp

    @staticmethod
    def log_response(resp, method, success):
        if success:
            if method == 'GET':
                try:
                    log.info(f'params：{resp.request.url.split("?")[1]}')
                except (ValueError, IndexError):
                    log.info(f'params：无')
            elif method in ['POST', 'DELETE']:
                try:
                    log.info(f'body：{json.loads(resp.request.body)}')
                except (ValueError, TypeError):
                    log.info(f'body：无')
        else:
            if method == 'GET':
                try:
                    log.error(f'{resp.url}\tparams：{resp.request.url.split("?")[1]}')
                except (ValueError, IndexError):
                    log.error(f'{resp.url}\tparams：无')
            elif method in ['POST', 'DELETE']:
                try:
                    log.error(f'{resp.url}\t{resp.json().get("code")}\tbody：{json.loads(resp.request.body)}')
                except (ValueError, TypeError):
                    log.error(f'{resp.url}\t{resp.json().get("code")}\tbody：无')
        return resp
