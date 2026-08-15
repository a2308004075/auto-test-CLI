import ast
import os
from typing import List, Optional, Tuple

from common.utils.getProject import GetProject
from common.utils.handlerFile import HandlerFile


class ConvertKeyKw:
    """
    将带有 @KwDecorator 装饰器的源文件转换为关键字字典文件。

    支持多种源目录到输出目录的映射规则，例如：
    - wss: ``common/wss/xxx.py`` → ``kw/key_xxx.py``
    - act: ``version/v3/act/module/xxx.py`` → ``version/v3/kw/kw_act/module/key_xxx.py``
    - api: ``version/v3/dao/api/set_xxx.py`` → ``version/v3/kw/kw_api/key_xxx.py``
    - ncs: ``version/v3/dao/ncs/ncs_xxx.py`` → ``version/v3/kw/kw_ncs/key_ncs_xxx.py``
    - tc: ``version/v3/ts/test_xxx.py`` → ``version/v3/kw/kw_tc/key_test_xxx.py``

    源文件示例::

        class NewWss:
            @staticmethod
            @KwDecorator("获取currentProcessData的wss消息")
            def current_process_data_wss(carNo, packType):
                ...

    生成文件示例::

        from common.handlerKw.handlerKw import HandlerKw
        from company.qkl.new.common.wss.new_wss import NewWss

        KeyNewWss = {
            "获取currentProcessData的wss消息": HandlerKw.kw(NewWss.current_process_data_wss),  # 参数：['carNo', 'packType']
        }
    """

    @staticmethod
    def _extract_kw_description(func_node) -> Optional[str]:
        """
        从函数节点的装饰器列表中提取 @KwDecorator 的描述字符串。

        :param func_node: 函数 AST 节点（FunctionDef / AsyncFunctionDef）
        :return: 描述字符串，未找到则返回 None
        """
        for decorator in func_node.decorator_list:
            # 匹配 @KwDecorator("xxx") 形式
            if isinstance(decorator, ast.Call):
                func = decorator.func
                if isinstance(func, ast.Name) and func.id == 'KwDecorator':
                    if decorator.args:
                        arg = decorator.args[0]
                        # Python 3.6 使用 ast.Str，3.8+ 使用 ast.Constant
                        if isinstance(arg, ast.Str):
                            return arg.s
                        if hasattr(ast, 'Constant') and isinstance(arg, ast.Constant):
                            if isinstance(arg.value, str):
                                return arg.value
        return None

    @staticmethod
    def _extract_params(func_node) -> List[str]:
        """
        从函数节点中提取参数名列表（排除 self）。

        :param func_node: 函数 AST 节点
        :return: 参数名列表
        """
        return [
            arg.arg for arg in func_node.args.args
            if arg.arg != 'self'
        ]

    @staticmethod
    def _parse_source(file_path: str) -> Tuple[str, List[Tuple[str, str, List[str]]]]:
        """
        解析源文件，提取类名及被 @KwDecorator 装饰的方法信息。

        :param file_path: 源文件路径
        :return: (类名, [(描述, 方法名, 参数列表), ...])
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)

        class_name = None
        method_infos = []

        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        description = ConvertKeyKw._extract_kw_description(item)
                        if description:
                            params = ConvertKeyKw._extract_params(item)
                            method_infos.append((description, item.name, params))

        if class_name is None:
            raise ValueError(f"未在文件 {file_path} 中找到类定义")

        return class_name, method_infos

    @staticmethod
    def _to_module_path(file_path: str) -> str:
        """
        将文件路径转换为 Python 模块导入路径。

        :param file_path: 文件绝对路径
        :return: 模块路径，如 'company.qkl.new.common.wss.new_wss'
        """
        project_path = GetProject.get_project_path()
        relative_path = os.path.relpath(file_path, project_path)
        return relative_path.replace(os.sep, '.').replace('.py', '')

    @staticmethod
    def _generate_output_path(source_path: str, source_marker: str, output_marker: str) -> str:
        """
        根据源文件路径和目录映射规则推导输出路径。

        规则: ``.../<source_marker>/<source_prefix>xxx.py`` → ``.../<output_marker>/key_xxx.py``

        :param source_path: 源文件路径
        :param source_marker: 源目录中的标识片段，如 'common/wss'、'act' 或 'dao/api'
        :param output_marker: 输出目录中的标识片段，如 'kw'、'kw/kw_act' 或 'kw/kw_api'
        :param source_prefix: 源文件名前缀，如 'set_'；指定后会将该前缀替换为 'key_'，
                              未指定则直接在文件名前添加 'key_'
        :return: 输出文件路径
        """
        normalized = source_path.replace('\\', '/')
        source_dir_pattern = '/' + source_marker.strip('/') + '/'
        output_dir_pattern = '/' + output_marker.strip('/') + '/'
        output = normalized.replace(source_dir_pattern, output_dir_pattern)
        directory, filename = os.path.split(output)
        key_filename = 'key_' + filename
        return os.path.join(directory, key_filename)

    @staticmethod
    def convert(source_path: str, output_path: str = None,
                source_marker: str = 'common/wss', output_marker: str = 'kw') -> str:
        """
        转换单个源文件，生成关键字字典文件。

        :param source_path: 源文件路径
        :param output_path: 输出文件路径，为 None 时按映射规则自动推导
        :param source_marker: 源目录标识片段，默认 'common/wss'（兼容 wss 场景）
        :param output_marker: 输出目录标识片段，默认 'kw'
        :param source_prefix: 源文件名前缀，指定后替换为 'key_'（如 'set_' → 'key_'）
        :return: 实际生成的输出文件路径
        """
        source_path = os.path.normpath(os.path.abspath(source_path))
        class_name, method_infos = ConvertKeyKw._parse_source(source_path)
        module_path = ConvertKeyKw._to_module_path(source_path)

        if output_path is None:
            output_path = ConvertKeyKw._generate_output_path(
                source_path, source_marker, output_marker)
        output_path = os.path.normpath(os.path.abspath(output_path))

        # 按描述排序
        method_infos.sort(key=lambda x: x[0])

        # 构建文件内容
        lines = [
            "from common.handlerKw.handlerKw import HandlerKw",
            f"from {module_path} import {class_name}",
            "",
            f"Key{class_name} = {{",
        ]
        for description, method_name, params in method_infos:
            entry = f'    "{description}": HandlerKw.kw({class_name}.{method_name}),'
            if params:
                entry += f"  # 参数：{params}"
            lines.append(entry)
        lines.append("}")

        # 确保输出目录存在
        HandlerFile.create_dir(os.path.dirname(output_path))

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')

        return output_path


def convert_all(source_dirs: List[str], source_marker: str, output_marker: str) -> None:
    """
    批量转换指定目录下所有 .py 源文件为关键字字典文件。

    递归遍历每个 source_dir，跳过 __init__.py，对每个 .py 文件调用
    :func:`ConvertKeyKw.convert` 生成对应的关键字字典文件。

    :param source_dirs: 源目录列表（绝对路径）
    :param source_marker: 源目录标识片段，用于路径推导
    :param output_marker: 输出目录标识片段，用于路径推导
    :param source_prefix: 源文件名前缀，指定后替换为 'key_'（如 'set_' → 'key_'）
    """
    for source_dir in source_dirs:
        if not os.path.isdir(source_dir):
            continue
        for dir_path, _, file_list in os.walk(source_dir):
            for filename in file_list:
                if filename.endswith('.py') and filename != '__init__.py':
                    source_path = os.path.join(dir_path, filename)
                    output_path = ConvertKeyKw.convert(
                        source_path,
                        source_marker=source_marker,
                        output_marker=output_marker)
                    print(f"已生成: {output_path}")
