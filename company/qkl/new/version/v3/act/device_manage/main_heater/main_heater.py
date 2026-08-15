from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc


class MainHeater:
    """
    主控室加热器
    """

    @staticmethod
    @KwDecorator("站点参数信息")
    def action_1(tempAdaptation):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：站点参数上报050B', tempAdaptation)

    @staticmethod
    @KwDecorator("设备状态：机组运行状态")
    def action_2(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，主控室加热器', 0, value)

    @staticmethod
    @KwDecorator("设备状态：制热运行状态")
    def action_3(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，主控室加热器', 3, value)

    @staticmethod
    @KwDecorator("设备状态：风机运行状态")
    def action_4(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，主控室加热器', 4, value)

    @staticmethod
    @KwDecorator("告警状态：回风温度传感器故障")
    def action_5(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码02，主控室加热器', 0, value)

    @staticmethod
    @KwDecorator("告警状态：柜内高温告警")
    def action_6(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码02，主控室加热器', 12, value)

    @staticmethod
    @KwDecorator("告警状态：柜内低温告警")
    def action_7(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码02，主控室加热器', 13, value)

    @staticmethod
    @KwDecorator("传感器数据：回内温度")
    def action_8(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，主控室加热器', 0, value)

    @staticmethod
    @KwDecorator("系统参数设置：制热启动温度")
    def action_9(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室加热器', 2, value)

    @staticmethod
    @KwDecorator("系统参数设置：制热停止回差值")
    def action_10(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室加热器', 3, value)

    @staticmethod
    @KwDecorator("系统参数设置：高温告警温度值")
    def action_11(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室加热器', 4, value)

    @staticmethod
    @KwDecorator("系统参数设置：低温告警温度值")
    def action_12(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室加热器', 5, value)
