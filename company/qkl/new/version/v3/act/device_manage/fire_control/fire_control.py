from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc


class FireControl:
    """
    消防
    """

    @staticmethod
    @KwDecorator("系统状态-报警")
    def action_systemStatus_1(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 0, value)  # 0-无报警，1-有报警

    @staticmethod
    @KwDecorator("系统状态-故障")
    def action_systemStatus_2(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 1, value)  # 0-无故障，1-故障

    @staticmethod
    @KwDecorator("系统状态-消音")
    def action_systemStatus_3(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 2, value)  # 0-未消音，1-消音中

    @staticmethod
    @KwDecorator("系统状态-自检")
    def action_systemStatus_4(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 3, value)  # 0-自检完成，1-自检中

    @staticmethod
    @KwDecorator("系统状态-主电")
    def action_systemStatus_5(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 4, value)  # 0-未使用市电，1-使用市电

    @staticmethod
    @KwDecorator("系统状态-备电")
    def action_systemStatus_6(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 5, value)  # 0-未使用备电，1-使用备电

    @staticmethod
    @KwDecorator("系统状态-电源故障")
    def action_systemStatus_7(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 6, value)  # 0-无故障，1-故障

    @staticmethod
    @KwDecorator("系统状态-自动模式")
    def action_systemStatus_8(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 7, value)  # 0-非自动，1-自动

    @staticmethod
    @KwDecorator("系统状态-手动模式")
    def action_systemStatus_9(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 8, value)  # 0-非手动，1-手动

    @staticmethod
    @KwDecorator("系统状态-手动启动信号")
    def action_systemStatus_10(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 9, value)  # 0-无，1-有

    @staticmethod
    @KwDecorator("系统状态-手动急停信号")
    def action_systemStatus_11(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 10, value)  # 0-无，1-有

    @staticmethod
    @KwDecorator("系统状态-声光报警状态")
    def action_systemStatus_12(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 15, value)  # 0-无声光报警，1-声光报警

    @staticmethod
    @KwDecorator("系统状态-放气勿入状态")
    def action_systemStatus_13(value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 16, value)  # 0-放气勿入灯未亮，1-放气勿入灯亮

    @staticmethod
    @KwDecorator("事件信息")
    def action_eventInformation(valueList1, valueList2, valueList3):
        # 防护区（高）：0x00
        # 设备类型（低）：0x71→113
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，消防设备', valueList1[0], valueList1[1])  # 防护区（高）、设备类型（低）

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，消防设备', valueList2[0], valueList2[1])  # 设备编号（高）、预留（低）

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，消防设备', valueList3[0], valueList3[1])  # 事件类型（高）、事件码（低）

    @staticmethod
    @KwDecorator("传感器数据")
    def action_sensorData(sensorNum, deviceType, sensorID, alarmLevel,
                          temperature, COConcentration, VOC, smokeDensity):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，消防设备', 3, sensorNum)  # 传感器数量
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', deviceType[0], deviceType[1])  # 设备类型。地址：0x0002、0x0012...0x07F2
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', sensorID[0], sensorID[1])  # 探测器ID，地址：0x0003、0x0013...0x07F3
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', alarmLevel[0], alarmLevel[1])  # 报警等级，地址：0x0004、0x0014...0x07F4
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', temperature[0], temperature[1])  # 温度，地址：0x0005、0x0015...0x07F5
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', COConcentration[0], COConcentration[1])  # 一氧化碳浓度，地址：0x0006、0x0016...0x07F6
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', VOC[0], VOC[1])  # VOC，地址：0x0007、0x0017...0x07F7
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', smokeDensity[0], smokeDensity[1])  # 烟雾报警，地址：0x0008、0x0018...0x07F8

    @staticmethod
    @KwDecorator("灭火器状态")
    def action_FE(FE1, FE2):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', 4096, FE1)  # 1#灭火器-灭火器状态
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', 4097, FE2)  # 2#灭火器-灭火器状态
