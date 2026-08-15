"""
转换入口脚本

该脚本是整个项目的代码生成入口，用于将 Swagger 接口文档和各类源文件
自动转换为可执行的关键字字典文件，供后续自动化测试调用。

转换流程按以下顺序执行：
1. Swagger 文档转换：将 source/swaggerApi 目录下的 JSON 接口文档转换为 Python API 文件
2. 关键字转换：将 wss、act、api、ncs、ts 等源文件统一转换为关键字字典文件

覆盖范围：company/qkl/new（v3 版本）和 company/qkl/old（v1 版本）
"""
from common.handlerSwagger.convertAllSwagger import convert_all_swagger
from common.handlerKw.convertAllKw import convert_all_wss_kw, convert_all_act_kw, convert_all_api_kw, \
    convert_all_ncs_kw, convert_all_tc_kw

# ==================== Swagger 接口文档转换 ====================
# 将 Swagger JSON 接口文档转换为 Python API 文件，生成各模块的接口调用方法
convert_all_swagger()

# ==================== 关键字字典转换 ====================
# 将 WSS（WebSocket）相关源文件转换为关键字字典文件
convert_all_wss_kw()
# 将 ACT（动作）相关源文件转换为关键字字典文件
convert_all_act_kw()
# 将 API 接口相关源文件转换为关键字字典文件
convert_all_api_kw()
# 将 NCS 相关源文件转换为关键字字典文件
convert_all_ncs_kw()
# 将 TC（测试用例）相关源文件转换为关键字字典文件
convert_all_tc_kw()
