from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_act.device_manage.main_heater.key_main_heater import KeyMainHeater


class TestMainHeater:
    @staticmethod
    @KwDecorator('站点参数信息')
    def test_1():
        RunKw.act_run(KeyMainHeater, '站点参数信息', 2)

    @staticmethod
    @KwDecorator('设备状态：机组运行状态')
    def test_2():
        RunKw.act_run(KeyMainHeater, '设备状态：机组运行状态', 1)

    @staticmethod
    @KwDecorator('设备状态：制热运行状态')
    def test_3():
        RunKw.act_run(KeyMainHeater, '设备状态：制热运行状态', 1)

    @staticmethod
    @KwDecorator('设备状态：风机运行状态')
    def test_4():
        RunKw.act_run(KeyMainHeater, '设备状态：风机运行状态', 1)

    @staticmethod
    @KwDecorator('告警状态：回风温度传感器故障')
    def test_5():
        RunKw.act_run(KeyMainHeater, '告警状态：回风温度传感器故障', 1)

    @staticmethod
    @KwDecorator('告警状态：柜内高温告警')
    def test_6():
        RunKw.act_run(KeyMainHeater, '告警状态：柜内高温告警', 1)

    @staticmethod
    @KwDecorator('告警状态：柜内低温告警')
    def test_7():
        RunKw.act_run(KeyMainHeater, '告警状态：柜内低温告警', 1)

    @staticmethod
    @KwDecorator('传感器数据：回内温度')
    def test_8():
        RunKw.act_run(KeyMainHeater, '传感器数据：回内温度', 20)

    @staticmethod
    @KwDecorator('系统参数设置：制热启动温度')
    def test_9():
        RunKw.act_run(KeyMainHeater, '系统参数设置：制热启动温度', 30)

    @staticmethod
    @KwDecorator('系统参数设置：制热停止回差值')
    def test_10():
        RunKw.act_run(KeyMainHeater, '系统参数设置：制热停止回差值', 400)

    @staticmethod
    @KwDecorator('系统参数设置：高温告警温度值')
    def test_11():
        RunKw.act_run(KeyMainHeater, '系统参数设置：高温告警温度值', 600)

    @staticmethod
    @KwDecorator('系统参数设置：低温告警温度值')
    def test_12():
        RunKw.act_run(KeyMainHeater, '系统参数设置：低温告警温度值', 100)
