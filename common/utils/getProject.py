import os
from typing import Optional


class GetProject:
    @staticmethod
    def get_project_path() -> Optional[str]:
        _PROJECT_NAME = 'scs-postman-tool'
        """
        获取项目路径

        Args:
            project_name: 项目名称，默认为'postman-tool'

        Returns:
            项目根路径，失败返回None
        """
        try:
            name = _PROJECT_NAME
            current_file_path = os.path.abspath(__file__)
            # 获取当前文件所在目录
            current_dir = os.path.dirname(current_file_path)
            # 逐级向上查找项目根目录
            while not os.path.basename(current_dir) == name:
                current_dir = os.path.dirname(current_dir)
                if current_dir == os.path.dirname(current_dir):  # 已到达根目录
                    raise FileNotFoundError(f"项目 {name} 未找到")
            project_root = current_dir
            return os.path.normpath(project_root)
        except Exception as e:
            raise e


if __name__ == '__main__':
    print(GetProject.get_project_path())
