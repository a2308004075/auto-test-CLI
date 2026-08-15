import os
from common.utils.getProject import GetProject
from common.handlerKw.convertKw import convert_all


def convert_all_wss_kw() -> None:
    """
    批量转换所有 wss 源文件（new 和 old）为关键字字典文件。
    """
    project_path = GetProject.get_project_path()
    source_dirs = [
        os.path.join(project_path, 'company', 'qkl', 'new', 'common', 'wss'),
        os.path.join(project_path, 'company', 'qkl', 'old', 'common', 'wss'),
    ]
    convert_all(source_dirs, source_marker='common/wss', output_marker='kw')


def convert_all_act_kw() -> None:
    """
    批量转换所有 act 源文件（new 和 old 的各版本）为关键字字典文件。
    """
    project_path = GetProject.get_project_path()
    source_dirs = [
        os.path.join(project_path, 'company', 'qkl', 'new', 'version', 'v3', 'act'),
        os.path.join(project_path, 'company', 'qkl', 'old', 'version', 'v1', 'act'),
    ]
    convert_all(source_dirs, source_marker='act', output_marker='kw/kw_act')


def convert_all_api_kw() -> None:
    """
    批量转换所有 dao/api 源文件（new 和 old 的各版本）为关键字字典文件。

    文件名转换规则: ``set_xxx.py`` → ``key_xxx.py``
    """
    project_path = GetProject.get_project_path()
    source_dirs = [
        os.path.join(project_path, 'company', 'qkl', 'new', 'version', 'v3', 'dao', 'api'),
        os.path.join(project_path, 'company', 'qkl', 'old', 'version', 'v1', 'dao', 'api'),
    ]
    convert_all(source_dirs, source_marker='dao/api', output_marker='kw/kw_api')


def convert_all_ncs_kw() -> None:
    """
    批量转换所有 dao/ncs 源文件（new 和 old 的各版本）为关键字字典文件。
    """
    project_path = GetProject.get_project_path()
    source_dirs = [
        os.path.join(project_path, 'company', 'qkl', 'new', 'version', 'v3', 'dao', 'ncs'),
        os.path.join(project_path, 'company', 'qkl', 'old', 'version', 'v1', 'dao', 'ncs'),
    ]
    convert_all(source_dirs, source_marker='dao/ncs', output_marker='kw/kw_ncs')


def convert_all_tc_kw() -> None:
    """
    批量转换所有 ts 源文件（new 和 old 的各版本）为关键字字典文件。
    """
    project_path = GetProject.get_project_path()
    source_dirs = [
        os.path.join(project_path, 'company', 'qkl', 'new', 'version', 'v3', 'ts'),
        os.path.join(project_path, 'company', 'qkl', 'old', 'version', 'v1', 'ts'),
    ]
    convert_all(source_dirs, source_marker='ts', output_marker='kw/kw_tc')
