from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_act.battery_manage.camp_list.key_camp_list import KeyCampList


class TestCampList:
    @staticmethod
    @KwDecorator('启动充电')
    def test_1():
        RunKw.act_run(KeyCampList, '启动充电')

    @staticmethod
    @KwDecorator('仓位信息初始化')
    def test_2():
        RunKw.act_run(KeyCampList, '仓位信息初始化')

    @staticmethod
    @KwDecorator('充电设备主动上送充电记录（4200）：正常停止')
    def test_3():
        RunKw.act_run(KeyCampList, '充电设备主动上送充电记录（4200）：正常停止')

    @staticmethod
    @KwDecorator('充电枪数据上报4552：修改1号仓参数')
    def test_4():
        RunKw.act_run(KeyCampList, '充电枪数据上报4552：修改1号仓参数')

    @staticmethod
    @KwDecorator('充电设备上报历史订单4559')
    def test_5():
        RunKw.act_run(KeyCampList, '充电设备上报历史订单4559')

    @staticmethod
    @KwDecorator('响应清除故障：1-失败')
    def test_6():
        RunKw.act_run(KeyCampList, '响应清除故障：1-失败')

    @staticmethod
    @KwDecorator('响应清除故障：2-成功')
    def test_7():
        RunKw.act_run(KeyCampList, '响应清除故障：2-成功')

    @staticmethod
    @KwDecorator('充电后保温：1号仓，成功')
    def test_8():
        RunKw.act_run(KeyCampList, '充电后保温：1号仓，成功')

    @staticmethod
    @KwDecorator('充电后保温：1号仓，失败')
    def test_9():
        RunKw.act_run(KeyCampList, '充电后保温：1号仓，失败')

    @staticmethod
    @KwDecorator('充电后退出保温：1号仓，成功')
    def test_11():
        RunKw.act_run(KeyCampList, '充电后退出保温：1号仓，成功')

    @staticmethod
    @KwDecorator('充电后退出保温：1号仓，失败')
    def test_12():
        RunKw.act_run(KeyCampList, '充电后退出保温：1号仓，失败')

    @staticmethod
    @KwDecorator('充电中加热（非极低温）：1号仓，成功')
    def test_13():
        RunKw.act_run(KeyCampList, '充电中加热（非极低温）：1号仓，成功')

    @staticmethod
    @KwDecorator('充电中加热（非极低温）：1号仓，失败')
    def test_14():
        RunKw.act_run(KeyCampList, '充电中加热（非极低温）：1号仓，失败')

    @staticmethod
    @KwDecorator('充电中退出加热：1号仓，成功')
    def test_15():
        RunKw.act_run(KeyCampList, '充电中退出加热：1号仓，成功')

    @staticmethod
    @KwDecorator('充电中退出加热：1号仓，失败')
    def test_16():
        RunKw.act_run(KeyCampList, '充电中退出加热：1号仓，失败')

    @staticmethod
    @KwDecorator('充电中加热（极低温-20）：1号仓，成功')
    def test_17():
        RunKw.act_run(KeyCampList, '充电中加热（极低温-20）：1号仓，成功')

    @staticmethod
    @KwDecorator('充电中加热（极低温-20）：1号仓，失败')
    def test_18():
        RunKw.act_run(KeyCampList, '充电中加热（极低温-20）：1号仓，失败')

    @staticmethod
    @KwDecorator('电池类型为三元里，0.5V<电池包最小电压<开启电压，触发欠压补电')
    def test_19():
        RunKw.act_run(KeyCampList, '电池类型为三元里，0.5V<电池包最小电压<开启电压，触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为三元里，欠压补电中，SBMU最小电压（NCM）>截止电压，站控下控停止充电')
    def test_20():
        RunKw.act_run(KeyCampList, '电池类型为三元里，欠压补电中，SBMU最小电压（NCM）>截止电压，站控下控停止充电')

    @staticmethod
    @KwDecorator('电池类型为三元里，电池包最小电压=开启电压，触发欠压补电')
    def test_21():
        RunKw.act_run(KeyCampList, '电池类型为三元里，电池包最小电压=开启电压，触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为三元里，开启电压<电池包最小电压<截止电压，不触发欠压补电')
    def test_22():
        RunKw.act_run(KeyCampList, '电池类型为三元里，开启电压<电池包最小电压<截止电压，不触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为三元里，欠压补电中，SBMU最小电（NCM）压=截止电压，站控下控停止充电')
    def test_23():
        RunKw.act_run(KeyCampList, '电池类型为三元里，欠压补电中，SBMU最小电（NCM）压=截止电压，站控下控停止充电')

    @staticmethod
    @KwDecorator('电池类型为磷酸铁锂电池，0.5V<电池包最小电压<开启电压，触发欠压补电')
    def test_24():
        RunKw.act_run(KeyCampList, '电池类型为磷酸铁锂电池，0.5V<电池包最小电压<开启电压，触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为磷酸铁锂电池，电池包最小电压=开启电压，触发欠压补电')
    def test_25():
        RunKw.act_run(KeyCampList, '电池类型为磷酸铁锂电池，电池包最小电压=开启电压，触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为磷酸铁锂电池，开启电压<电池包最小电压<截止电压，不触发欠压补电')
    def test_26():
        RunKw.act_run(KeyCampList, '电池类型为磷酸铁锂电池，开启电压<电池包最小电压<截止电压，不触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为磷酸铁锂电池，欠压补电中，SBMU最小电压（LFP）>截止电压，站控下控停止充电')
    def test_27():
        RunKw.act_run(KeyCampList, '电池类型为磷酸铁锂电池，欠压补电中，SBMU最小电压（LFP）>截止电压，站控下控停止充电')

    @staticmethod
    @KwDecorator('电池类型为磷酸铁锂电池，欠压补电中，SBMU最小电（LFP）压=截止电压，站控下控停止充电')
    def test_28():
        RunKw.act_run(KeyCampList, '电池类型为磷酸铁锂电池，欠压补电中，SBMU最小电（LFP）压=截止电压，站控下控停止充电')

    @staticmethod
    @KwDecorator('电池类型为铅酸电池，0.5V<电池包最小电压<开启电压，触发欠压补电')
    def test_29():
        RunKw.act_run(KeyCampList, '电池类型为铅酸电池，0.5V<电池包最小电压<开启电压，触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为铅酸电池，电池包最小电压=开启电压，触发欠压补电')
    def test_30():
        RunKw.act_run(KeyCampList, '电池类型为铅酸电池，电池包最小电压=开启电压，触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为铅酸电池，开启电压<电池包最小电压<截止电压，不触发欠压补电')
    def test_31():
        RunKw.act_run(KeyCampList, '电池类型为铅酸电池，开启电压<电池包最小电压<截止电压，不触发欠压补电')

    @staticmethod
    @KwDecorator('电池类型为铅酸电池，欠压补电中，SBMU最小电压>截止电压，站控下控停止充电')
    def test_32():
        RunKw.act_run(KeyCampList, '电池类型为铅酸电池，欠压补电中，SBMU最小电压>截止电压，站控下控停止充电')

    @staticmethod
    @KwDecorator('电池类型为铅酸电池，欠压补电中，SBMU最小电压=截止电压，站控下控停止充电')
    def test_33():
        RunKw.act_run(KeyCampList, '电池类型为铅酸电池，欠压补电中，SBMU最小电压=截止电压，站控下控停止充电')

    @staticmethod
    @KwDecorator('30个仓位信息初始化')
    def test_34():
        RunKw.act_run(KeyCampList, '30个仓位信息初始化')

    @staticmethod
    @KwDecorator('触发站控诊断故障48')
    def test_35():
        RunKw.act_run(KeyCampList, '触发站控诊断故障48')

    @staticmethod
    @KwDecorator('消防系统长时间消音')
    def test_36():
        RunKw.act_run(KeyCampList, '消防系统长时间消音')
