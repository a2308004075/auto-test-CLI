from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc


class MainAirConditioning:
    """
    主控室空调
    """

    @staticmethod
    @KwDecorator("主控室空调故障：温度上限报警")
    def action_1():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 183, 1)

    @staticmethod
    @KwDecorator("主控室空调故障：温度上限报警恢复")
    def action_2():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 183, 0)

    @staticmethod
    @KwDecorator("主控室空调故障：温度下限报警")
    def action_3():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 184, 1)

    @staticmethod
    @KwDecorator("主控室空调故障：温度下限报警恢复")
    def action_4():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 184, 0)

    @staticmethod
    @KwDecorator("主控室空调故障：第一路空调开关机失败")
    def action_5():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 181, 1)

    @staticmethod
    @KwDecorator("主控室空调故障：第一路空调开关机失败恢复")
    def action_6():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 181, 0)

    @staticmethod
    @KwDecorator("自动模式时，当当前温度≤制冷停止温度且电流真实值＞0且运行状态=制冷")
    def action_7():
        # 调度任务：空调自动模式任务

        # 站控：控制模式--自动

        # 当前温度≤制冷停止温度
        ## 站控：制冷停止温度
        ## PLC：当前温度
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 1, 200)

        # 电流真实值＞0
        ## PLC：电流真实值
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 113, 50)

        # PLC：运行状态=1：制冷
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 215, 1)

    @staticmethod
    @KwDecorator("自动模式时，当当前温度≥制热停止温度且电流真实值＞0且运行状态=制热")
    def action_8():
        # 调度任务：空调自动模式任务

        # 站控：控制模式--自动

        # 当前温度≥制热停止温度
        ## 站控：制热停止温度
        ## PLC：当前温度
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 1, 280)

        # 电流真实值＞0
        ## PLC：电流真实值
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 113, 50)

        # PLC：运行状态=2：制热
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，主控室空调', 215, 2)
