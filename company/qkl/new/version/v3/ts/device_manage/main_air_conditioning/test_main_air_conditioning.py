from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_act.device_manage.main_air_conditioning.key_main_air_conditioning import KeyMainAirConditioning


class TestMainAirConditioning:
    @staticmethod
    @KwDecorator('主控室空调故障：温度上限报警')
    def test_1():
        RunKw.act_run(KeyMainAirConditioning, '主控室空调故障：温度上限报警')

    @staticmethod
    @KwDecorator('主控室空调故障：温度上限报警恢复')
    def test_2():
        RunKw.act_run(KeyMainAirConditioning, '主控室空调故障：温度上限报警恢复')

    @staticmethod
    @KwDecorator('主控室空调故障：温度下限报警')
    def test_3():
        RunKw.act_run(KeyMainAirConditioning, '主控室空调故障：温度下限报警')

    @staticmethod
    @KwDecorator('主控室空调故障：温度下限报警恢复')
    def test_4():
        RunKw.act_run(KeyMainAirConditioning, '主控室空调故障：温度下限报警恢复')

    @staticmethod
    @KwDecorator('主控室空调故障：第一路空调开关机失败')
    def test_5():
        RunKw.act_run(KeyMainAirConditioning, '主控室空调故障：第一路空调开关机失败')

    @staticmethod
    @KwDecorator('主控室空调故障：第一路空调开关机失败恢复')
    def test_6():
        RunKw.act_run(KeyMainAirConditioning, '主控室空调故障：第一路空调开关机失败恢复')

    @staticmethod
    @KwDecorator('自动模式时，当当前温度≤制冷停止温度且电流真实值＞0且运行状态=制冷')
    def test_7():
        RunKw.act_run(KeyMainAirConditioning, '自动模式时，当当前温度≤制冷停止温度且电流真实值＞0且运行状态=制冷')

    @staticmethod
    @KwDecorator('自动模式时，当当前温度≥制热停止温度且电流真实值＞0且运行状态=制热')
    def test_8():
        RunKw.act_run(KeyMainAirConditioning, '自动模式时，当当前温度≥制热停止温度且电流真实值＞0且运行状态=制热')
