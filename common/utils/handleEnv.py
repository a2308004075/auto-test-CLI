from typing import Optional, Dict, Tuple
from common.utils.logConfig import logger
from common.utils.handlerFile import HandlerFile


class HandleEnv:

    @staticmethod
    def _get_env_config() -> Optional[Dict]:
        """
        获取环境配置

        Returns:
            当前使用的环境配置字典，失败返回None
        """
        env_path = HandlerFile.get_env_path()
        env_json = HandlerFile.read_json(env_path)
        if not env_json or 'useEnv' not in env_json:
            logger.error("环境配置无效或缺少useEnv字段")
            return None

        use_env = env_json['useEnv']
        if use_env not in env_json:
            logger.error(f"指定的环境'{use_env}'不存在于配置中")
            return None

        return env_json[use_env]

    @staticmethod
    def get_env_host() -> Tuple[Optional[str], Optional[str]]:
        """
        获取host信息

        Returns:
            (host, authorization)元组，失败返回(None, None)
        """
        # 调用私有方法获取环境配置
        env_json = HandleEnv._get_env_config()
        # 如果环境配置为空，返回(None, None)
        if not env_json:
            return None, None
        # 从环境配置中获取host信息
        return env_json.get('host')

    @staticmethod
    def get_env_authorization() -> Tuple[Optional[str], Optional[str]]:
        """
        获取host、authorization信息

        Returns:
            (host, authorization)元组，失败返回(None, None)
        """
        # 调用私有方法获取环境配置信息
        env_json = HandleEnv._get_env_config()
        # 如果环境配置为空，则返回(None, None)
        if not env_json:
            return None, None
        # 从环境配置中获取host和authorization信息
        return env_json.get('host_authorization')

    @staticmethod
    def get_env_nacos() -> Tuple[Optional[str], Optional[str]]:
        """
        获取nacos信息

        Returns:
            (nacos, nacos_accessToken)元组，失败返回(None, None)
        """
        env_json = HandleEnv._get_env_config()
        if not env_json:
            return None, None
        return env_json.get('nacos'), env_json.get('nacos_accessToken')

    @staticmethod
    def get_env_wss() -> Optional[str]:
        """
        获取wss信息

        Returns:
            wss配置字符串，失败返回None
        """
        env_json = HandleEnv._get_env_config()
        if not env_json:
            return None
        return env_json.get('wss')

    @staticmethod
    def get_env_company() -> Optional[str]:
        """
        获取公司

        Returns:
            公司id，失败返回None
        """
        env_json = HandleEnv._get_env_config()
        if not env_json:
            return None
        return env_json.get('company')
