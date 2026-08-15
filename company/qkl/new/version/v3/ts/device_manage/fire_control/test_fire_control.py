from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_act.device_manage.fire_control.key_fire_control import KeyFireControl


class TestFireControl:
    @staticmethod
    @KwDecorator('系统状态-报警')
    def test_systemStatus_1():
        RunKw.act_run(KeyFireControl, '系统状态-报警', 0)  # 0-无报警，1-有报警

    @staticmethod
    @KwDecorator('系统状态-故障')
    def test_systemStatus_2():
        RunKw.act_run(KeyFireControl, '系统状态-故障', 0)  # 0-无故障，1-故障

    @staticmethod
    @KwDecorator('系统状态-消音')
    def test_systemStatus_3():
        RunKw.act_run(KeyFireControl, '系统状态-消音', 0)  # 0-未消音，1-消音中

    @staticmethod
    @KwDecorator('系统状态-自检')
    def test_systemStatus_4():
        RunKw.act_run(KeyFireControl, '系统状态-自检', 0)  # 0-自检完成，1-自检中

    @staticmethod
    @KwDecorator('系统状态-主电')
    def test_systemStatus_5():
        RunKw.act_run(KeyFireControl, '系统状态-主电', 1)  # 0-未使用市电，1-使用市电

    @staticmethod
    @KwDecorator('系统状态-备电')
    def test_systemStatus_6():
        RunKw.act_run(KeyFireControl, '系统状态-备电', 0)  # 0-未使用备电，1-使用备电

    @staticmethod
    @KwDecorator('系统状态-电源故障')
    def test_systemStatus_7():
        RunKw.act_run(KeyFireControl, '系统状态-电源故障', 0)  # 0-无故障，1-故障

    @staticmethod
    @KwDecorator('系统状态-自动模式')
    def test_systemStatus_8():
        RunKw.act_run(KeyFireControl, '系统状态-自动模式', 0)  # 0-非自动，1-自动

    @staticmethod
    @KwDecorator('系统状态-手动模式')
    def test_systemStatus_9():
        RunKw.act_run(KeyFireControl, '系统状态-手动模式', 0)  # 0-非手动，1-手动

    @staticmethod
    @KwDecorator('系统状态-手动启动信号')
    def test_systemStatus_10():
        RunKw.act_run(KeyFireControl, '系统状态-手动启动信号', 0)  # 0-无，1-有

    @staticmethod
    @KwDecorator('系统状态-手动急停信号')
    def test_systemStatus_11():
        RunKw.act_run(KeyFireControl, '系统状态-手动急停信号', 0)  # 0-无，1-有

    @staticmethod
    @KwDecorator('系统状态-声光报警状态')
    def test_systemStatus_12():
        RunKw.act_run(KeyFireControl, '系统状态-声光报警状态', 0)  # 0-无声光报警，1-声光报警

    @staticmethod
    @KwDecorator('系统状态-放气勿入状态')
    def test_systemStatus_13():
        RunKw.act_run(KeyFireControl, '系统状态-放气勿入状态', 0)  # 0-放气勿入灯未亮，1-放气勿入灯亮

    @staticmethod
    @KwDecorator('事件信息')
    def test_eventInformation():
        RunKw.act_run(KeyFireControl, '事件信息', [256, 113], [257, 256], [258, 256])

    @staticmethod
    @KwDecorator('传感器数据')
    def test_sensorData():
        RunKw.act_run(KeyFireControl, '传感器数据', 1, [2, 17], [3, 1], [4, 0], [5, 1], [6, 1], [7, 1], [8, 1])  # sensorNum, deviceType, sensorID, alarmLevel,temperature, COConcentration, VOC, smokeDensity

    @staticmethod
    @KwDecorator('灭火器状态')
    def test_FE():
        RunKw.act_run(KeyFireControl, '灭火器状态', -1, -1)
