import json
import os
from typing import List, Optional, Any
from common.utils.getProject import GetProject
from common.utils.logConfig import log


class HandlerFile:
    @staticmethod
    def create_dir(dir_path: str) -> None:
        """
        若文件夹不存在，则创建

        Args:
            dir_path: 目录路径
        """
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

    @staticmethod
    def get_env_path() -> Optional[str]:
        """
        获取env.json路径

        Returns:
            env.json文件路径，失败返回None
        """
        project_path = GetProject.get_project_path()
        if not project_path or not os.path.isdir(project_path):
            log.error("项目路径无效")
            return None
        return os.path.join(project_path, 'env.json')

    @staticmethod
    def read_json(json_path: str, encoding: str = 'utf-8') -> Optional[Any]:
        """
        读取Json文件内容

        Args:
            json_path: JSON文件路径
            encoding: 文件编码，默认为utf-8

        Returns:
            JSON解析后的数据，如果读取失败则返回None
        """
        # 验证文件路径
        if not os.path.exists(json_path):
            log.error(f"文件未找到：{json_path}")
            return None

        # 检查文件是否可读
        if not os.access(json_path, os.R_OK):
            log.error(f"文件不可读：{json_path}")
            return None

        try:
            with open(json_path, 'r', encoding=encoding) as file:
                data = json.load(file)
                return data
        except IOError as e:
            log.error(f"文件读取失败：{e}")
            return None
        except json.JSONDecodeError as e:
            log.error(f"JSON解析失败：{e}")
            return None
