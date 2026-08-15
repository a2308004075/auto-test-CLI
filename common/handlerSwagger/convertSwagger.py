import json
import re
from pathlib import Path
from typing import Dict, List, Optional


class ConvertApiDoc:
    """处理 Swagger API 文档，生成 Python 客户端代码"""

    def __init__(self, json_file_path: str):
        """
        初始化处理器

        :param json_file_path: Swagger JSON 文件路径
        """
        self.json_file_path = json_file_path
        with open(json_file_path, 'r', encoding='utf-8') as f:
            self._data: Dict = json.load(f)
        self.definitions: Dict = self._data.get('definitions', {})

    def _resolve_ref(self, ref: str) -> Optional[Dict]:
        """
        解析 $ref 引用

        :param ref: 引用路径，如 "#/definitions/AirAutoParamDTO"
        :return: 对应的定义字典，无法解析时返回 None
        """
        if not ref or not ref.startswith('#/definitions/'):
            return None
        return self.definitions.get(ref.replace('#/definitions/', ''))

    def _extract_field_info(
            self,
            field_name: str,
            field_schema: Dict,
            parent_path: str = '',
            required_fields: Optional[List[str]] = None
    ) -> List[Dict]:
        """
        递归提取字段信息，处理嵌套结构和数组

        :param field_name: 字段名称
        :param field_schema: 字段的架构信息
        :param parent_path: 父路径，用于构建字段的完整路径
        :param required_fields: 必需字段列表
        :return: 字段信息列表
        """
        if required_fields is None:
            required_fields = []

        # 处理 $ref 引用：递归展开被引用的定义
        if '$ref' in field_schema:
            ref_schema = self._resolve_ref(field_schema['$ref'])
            if ref_schema:
                ref_name = field_schema['$ref'].split('/')[-1]
                return self._extract_field_info(ref_name, ref_schema, parent_path, required_fields)
            return []

        field_type = field_schema.get('type', 'object')

        # 计算当前路径：非对象类型追加字段名，对象类型复用父路径
        if field_type != 'object':
            current_path = f"{parent_path}.{field_name}" if parent_path else field_name
        else:
            current_path = parent_path if parent_path else field_name

        fields: List[Dict] = []

        # 基本类型字段
        if field_type in {'string', 'number', 'integer', 'boolean'}:
            fields.append(self._create_field_info(
                current_path, field_name, field_type, field_schema, required_fields
            ))

        # 数组类型：记录数组字段本身，若数组项引用了 DTO 则展开其字段
        elif field_type == 'array':
            fields.append(self._create_field_info(
                current_path, field_name, 'array', field_schema, required_fields, is_array=True
            ))

            item_schema = field_schema.get('items', {})
            if '$ref' in item_schema:
                ref_schema = self._resolve_ref(item_schema['$ref'])
                if ref_schema:
                    ref_name = item_schema['$ref'].split('/')[-1]
                    array_fields = self._extract_field_info(
                        ref_name, ref_schema, f"{current_path}[]", required_fields
                    )
                    for af in array_fields:
                        af['level'] = af['field_path'].count('.')
                    fields.extend(array_fields)

        # 对象类型：递归展开属性
        elif field_type == 'object':
            properties = field_schema.get('properties', {})
            nested_required = field_schema.get('required', [])

            if properties:
                fields.append(self._create_field_info(
                    current_path, field_name, 'object', field_schema, required_fields
                ))

            for prop_name, prop_schema in properties.items():
                fields.extend(self._extract_field_info(
                    prop_name, prop_schema, current_path, nested_required
                ))

        return fields

    @staticmethod
    def _create_field_info(
            field_path: str,
            field_name: str,
            field_type: str,
            field_schema: Dict,
            required_fields: List[str],
            is_array: bool = False
    ) -> Dict:
        """创建字段信息字典"""
        return {
            'field_path': field_path,
            'field_name': field_name,
            'field_type': field_type,
            'format': field_schema.get('format', ''),
            'description': field_schema.get('description', ''),
            'required': field_name in required_fields,
            'level': field_path.count('.'),
            'is_array': is_array,
        }

    def _extract_api_info(self) -> List[Dict]:
        """提取详细的 API 信息"""
        valid_methods = {'get', 'post', 'put', 'delete', 'patch', 'head', 'options'}
        api_list = []

        for path, methods in self._data.get('paths', {}).items():
            for method, details in methods.items():
                if method in valid_methods:
                    api_list.append(self._create_api_info(path, method, details))

        return api_list

    def _create_api_info(self, path: str, method: str, details: Dict) -> Dict:
        """创建 API 信息字典"""
        api_info = {
            'api_name': details.get('summary', ''),
            'path': path,
            'method': method.upper(),
            'description': details.get('description', ''),
            'operation_id': details.get('operationId', ''),
            'tags': details.get('tags', []),
            'parameters': []
        }

        for param in details.get('parameters', []):
            api_info['parameters'].append(self._create_param_info(param))

        return api_info

    def _create_param_info(self, param: Dict) -> Dict:
        """创建参数信息字典"""
        param_in = param.get('in', '')
        param_info = {
            'name': param.get('name', ''),
            'location': param_in,
            'type': param.get('type', ''),
            'required': param.get('required', False),
            'description': param.get('description', ''),
            'fields': []
        }

        if param_in == 'body':
            self._process_body_schema(param.get('schema', {}), param_info)

        return param_info

    def _process_body_schema(self, schema: Dict, param_info: Dict) -> None:
        """处理 Body 参数的 schema，展开 DTO 字段"""
        if '$ref' in schema:
            dto_name = schema['$ref'].split('/')[-1]
            param_info['dto_name'] = dto_name
            ref_schema = self._resolve_ref(schema['$ref'])
            if ref_schema:
                required_fields = ref_schema.get('required', [])
                param_info['fields'] = self._extract_field_info(dto_name, ref_schema, '', required_fields)
        else:
            param_info['fields'] = self._extract_field_info(param_info['name'], schema, '', [])

    def write_api(self, output_path: str) -> None:
        """
        将详细的 API 文档写入到 Python 文件中

        :param output_path: 输出文件的路径
        """
        api_list = self._extract_api_info()

        output_file = Path(output_path)
        class_name = self._generate_class_name(output_file)
        service_name = self._extract_service_name(output_file)

        lines = [
            "from common.http.httpRq import HttpRq",
            "from common.http.httpMethod import HttpMethod",
            "",
            "",
            f"class {class_name}:",
            "    @staticmethod",
            "    def _get_path(path):",
            f"        service = '/{service_name}'",
            "        return service + path",
            "",
        ]

        for api_info in api_list:
            lines.extend(self._generate_method_lines(api_info, class_name))
            lines.append("")

        output_file.write_text('\n'.join(lines), encoding='utf-8')

    @staticmethod
    def _generate_class_name(output_file: Path) -> str:
        """生成类名：将下划线文件名转为 PascalCase（如 api_video → ApiVideo）"""
        return ''.join(word.capitalize() for word in output_file.stem.split('_') if word)

    @staticmethod
    def _extract_service_name(output_file: Path) -> str:
        """提取服务名：去掉 api_ 前缀，下划线转连字符"""
        file_stem = output_file.stem
        if file_stem.startswith('api_'):
            return file_stem[4:].replace('_', '-')
        return file_stem.replace('_', '-')

    def _generate_method_lines(self, api_info: Dict, class_name: str) -> List[str]:
        """生成单个 API 方法的代码行"""
        api_path = api_info.get('path', '')
        http_method = api_info.get('method', '')

        if not api_path or not http_method:
            raise ValueError("api_info must contain 'path' and 'method'")

        path_params = re.findall(r'{(\w+)}', api_path)
        method_name = self._generate_method_name(api_path)

        # 确定方法参数列表
        if path_params:
            param_list = ', '.join(path_params)
        elif http_method == 'GET':
            param_list = ''
        else:
            param_list = 'data'

        # 确定请求体参数：GET 或含路径参数时传 None，否则传 data
        data_arg = 'None' if http_method == 'GET' or path_params else 'data'

        # 构建方法签名和文档字符串
        signature = f"    def {method_name}({param_list}):" if param_list else f"    def {method_name}():"
        lines = [
            "    @staticmethod",
            signature,
            '        """',
            f"        {api_info.get('api_name', '')}",
        ]

        # 添加参数文档
        if api_info.get('parameters'):
            lines.append("        请求参数:")
            for param in api_info['parameters']:
                if param.get('fields'):
                    lines.extend(self._generate_param_docs(param['fields']))

        # 方法体
        lines.extend([
            '        """',
            f"        path = f'{api_path}'",
            f"        return HttpRq.req(*HttpMethod.http_info("
            f"{class_name}._get_path(path), '{http_method}', {data_arg}))",
        ])

        return lines

    @staticmethod
    def _generate_method_name(api_path: str) -> str:
        """从 API 路径生成方法名：替换路径参数、斜杠转下划线、移除点号"""
        method_name = re.sub(r'{(\w+)}', r'\1', api_path)
        method_name = method_name.replace('/', '_').replace('.', '')
        return method_name.lstrip('_')

    @staticmethod
    def _generate_param_docs(fields: List[Dict]) -> List[str]:
        """生成参数文档行"""
        lines = []
        for field in fields:
            if field['field_type'] == 'object':
                continue

            field_level = field.get('level', 0)
            if not field_level:
                continue

            req_mark = "必填" if field['required'] else "可选"
            desc = f" - {field['description']}" if field['description'] else ''
            parameter = field['field_path'].split('.')[-1]
            indent = "            " * field_level
            lines.append(f"{indent}{parameter}: {field['field_type']} [{req_mark}]{desc}")

        return lines


def convert_all_api_doc(json_dir: str) -> None:
    """
    处理指定目录下所有 API 文档

    :param json_dir: 包含 API 文档 .json 文件的目录路径
    """
    json_dir_path = Path(json_dir)

    for json_file in json_dir_path.glob('*.json'):
        # 文件名加 api_ 前缀，扩展名改为 .py
        output_file = json_file.with_name(f"api_{json_file.stem}.py")
        # 将路径中的 source/swaggerApi 替换为 common/api
        parts = ['common' if p == 'source' else 'api' if p == 'swaggerApi' else p
                 for p in output_file.parts]
        output_path = str(Path(*parts))

        handler = ConvertApiDoc(str(json_file))
        handler.write_api(output_path)
