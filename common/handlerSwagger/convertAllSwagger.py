import os
from common.utils.getProject import GetProject
from common.handlerSwagger.convertSwagger import convert_all_api_doc

# 定义常量
API_DOC_BASE_PATH = os.path.join(GetProject.get_project_path(), 'company')


def build_json_path(company, is_new=True):
    """构建 JSON 路径"""
    sub_path = 'new' if is_new else 'old'
    return os.path.join(API_DOC_BASE_PATH, company, sub_path, 'source', 'swaggerApi')


def convert_all_swagger():
    json_path_list = [
        build_json_path('qkl', is_new=True),
        build_json_path('qkl', is_new=False)
    ]

    try:
        for json_path in json_path_list:
            convert_all_api_doc(json_path)
    except Exception as e:
        print(f"处理 API 文档时发生错误: {e}")
