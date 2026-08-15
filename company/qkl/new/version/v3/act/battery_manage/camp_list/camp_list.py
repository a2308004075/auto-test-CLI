import time
from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_dcci import KeySetVirtualDcci
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_battery import KeySetVirtualBattery


class CampList:
    @staticmethod
    @KwDecorator("仓位信息初始化")
    def action_1():
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1-14号仓keyon断开、cc1断开')
        time.sleep(10)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1-14号仓keyon连接、cc1连接')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：设置sn：1-14号仓SN')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10980Pack基础信息3：1-14号仓')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80继电器状态，14个仓位')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置仓位信息')

    @staticmethod
    @KwDecorator("调整充电功率/电流")
    def action_2():
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电设备应答站功率/电流调节指令结果：0-成功', '')

    @staticmethod
    @KwDecorator("启动充电：响应4900")
    def action_3():
        flowNo = ''
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电机响应远程启动（4900）：0-成功', flowNo)
        time.sleep(2)

    @staticmethod
    @KwDecorator("启动充电")
    def action_4():
        flowNo = ""
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电机响应远程启动（4900）：0-成功', flowNo)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电机上送充电启动完成帧（4501）：0-成功', flowNo)

    @staticmethod
    @KwDecorator("停止充电")
    def action_5():
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：0')

        flowNo = ""
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电机响应停止充电（5000）：0-成功', flowNo)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电机上送充电停止完成帧（4503）：1-正常停止', flowNo)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电设备主动上送充电记录（4200）：正常停止', flowNo)

    @staticmethod
    @KwDecorator("充电设备主动上送充电记录（4200）：正常停止")
    def action_6():
        flowNo = "2025020514070000101"
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电设备主动上送充电记录（4200）：正常停止', flowNo)

    @staticmethod
    @KwDecorator("充电枪数据上报4552：修改1号仓参数")
    def action_7():
        flowNo = "2025020514070000101"
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：修改1号仓参数', flowNo)

    @staticmethod
    @KwDecorator("充电设备上报历史订单4559")
    def action_8():
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电设备上报历史订单4559')

    @staticmethod
    @KwDecorator("响应清除故障：1-失败")
    def action_9():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualDcci：响应清除故障：1-失败')

    @staticmethod
    @KwDecorator("响应清除故障：2-成功")
    def action_10():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：响应清除故障：2-成功')

    @staticmethod
    @KwDecorator("充电后保温：1号仓，成功")
    def action_11():
        # Tmin≤-10 且Tmax≤25
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：0')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度10，最低温度-15')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=1')

    @staticmethod
    @KwDecorator("充电后保温：1号仓，失败")
    def action_12():
        # Tmin≤-10 且Tmax≤25
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：0')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度10，最低温度-15')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=0')

    @staticmethod
    @KwDecorator("充电后退出保温：1号仓，失败")
    def action_13():
        # Tmin≤-5 且Tmax≤30
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：0')
        time.sleep(2)
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度35，最低温度-7')
        time.sleep(2)
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=1')

    @staticmethod
    @KwDecorator("充电后退出保温：1号仓，成功")
    def action_14():
        # Tmin≤-5 且Tmax≤30
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：0')
        time.sleep(2)
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度35，最低温度-7')
        time.sleep(2)
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=0')

    @staticmethod
    @KwDecorator("充电中加热（非极低温）：1号仓，成功")
    def action_15():
        # Tmin≤17 且Tmax≤30
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度20，最低温度15')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=1')

    @staticmethod
    @KwDecorator("充电中加热（非极低温）：1号仓，失败")
    def action_16():
        # Tmin≤17 且Tmax≤30
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度20，最低温度15')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=0')

    @staticmethod
    @KwDecorator("充电中退出加热：1号仓，成功")
    def action_17():
        # Tmin≤20 且Tmax≤35
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度40，最低温度25')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=0')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：0')
        time.sleep(2)

    @staticmethod
    @KwDecorator("充电中退出加热：1号仓，失败")
    def action_18():
        # Tmin≤20 且Tmax≤35
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度40，最低温度25')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：0')
        time.sleep(2)

    @staticmethod
    @KwDecorator("充电中加热（极低温-20）：1号仓，成功")
    def action_19():
        # Tmin≤17 且Tmax≤30
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度-10，最低温度-22')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=1')

    @staticmethod
    @KwDecorator("充电中加热（极低温-20）：1号仓，失败")
    def action_20():
        # Tmin≤17 且Tmax≤30
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1号仓充电状态：1')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度-10，最低温度-22')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80，继电器状态：1号仓，加热继电器状态=0')

    @staticmethod
    @KwDecorator("电池类型为三元里，0.5V<电池包最小电压<开启电压，触发欠压补电")
    def action_21():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=6')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.2')

    @staticmethod
    @KwDecorator("电池类型为三元里，欠压补电中，SBMU最小电压（NCM）>截止电压，站控下控停止充电")
    def action_22():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=6')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.8')

    @staticmethod
    @KwDecorator("电池类型为三元里，电池包最小电压=开启电压，触发欠压补电")
    def action_23():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=6')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.4')

    @staticmethod
    @KwDecorator("电池类型为三元里，开启电压<电池包最小电压（NCM）<截止电压，不触发欠压补电")
    def action_24():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=6')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.5')

    @staticmethod
    @KwDecorator("电池类型为三元里，欠压补电中，SBMU最小电（NCM）压=截止电压，站控下控停止充电")
    def action_25():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=6')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.702')

    @staticmethod
    @KwDecorator("电池类型为磷酸铁锂电池，0.5V<电池包最小电压<开启电压，触发欠压补电")
    def action_26():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=3')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=2.0')

    @staticmethod
    @KwDecorator("电池类型为磷酸铁锂电池，电池包最小电压=开启电压，触发欠压补电")
    def action_27():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=3')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=2.91')

    @staticmethod
    @KwDecorator("电池类型为磷酸铁锂电池，开启电压<电池包最小电压<截止电压，不触发欠压补电")
    def action_28():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=3')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.0')

    @staticmethod
    @KwDecorator("电池类型为磷酸铁锂电池，欠压补电中，SBMU最小电压（LFP）>截止电压，站控下控停止充电")
    def action_29():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=3')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.3')

    @staticmethod
    @KwDecorator("电池类型为磷酸铁锂电池，欠压补电中，SBMU最小电压（LFP）=截止电压，站控下控停止充电")
    def action_30():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=3')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.2')

    @staticmethod
    @KwDecorator("电池类型为铅酸电池，0.5V<电池包最小电压<开启电压，触发欠压补电")
    def action_31():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=1')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=2.0')

    @staticmethod
    @KwDecorator("电池类型为铅酸电池，电池包最小电压=开启电压，触发欠压补电")
    def action_32():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=1')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=2.91')

    @staticmethod
    @KwDecorator("电池类型为铅酸电池，开启电压<电池包最小电压<截止电压，不触发欠压补电")
    def action_33():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=1')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.0')

    @staticmethod
    @KwDecorator("电池类型为铅酸电池，欠压补电中，SBMU最小电压>截止电压，站控下控停止充电")
    def action_34():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=1')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.3')

    @staticmethod
    @KwDecorator("电池类型为铅酸电池，欠压补电中，SBMU最小电压=截止电压，站控下控停止充电")
    def action_35():
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F80180 基础参数1：1号仓，s_CellType=1')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：1号仓，s_MinCellVoltMv=3.2')

    @staticmethod
    @KwDecorator("30个仓位信息初始化")
    def action_36():
        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1-30号仓keyon断开、cc1断开')
        time.sleep(10)

        RunKw.api_run(KeySetVirtualDcci, 'SetVirtualDcci：充电枪数据上报4552：1-30号仓keyon连接、cc1连接')
        time.sleep(5)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：设置sn：1-30号仓SN')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10980Pack基础信息3：1-30号仓')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F10C80继电器状态，30个仓位')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：设置仓位信息')

    @staticmethod
    @KwDecorator("触发站控诊断故障48")
    def action_37():
        # 1、消防报警级别2
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', 3330, 0)  # 默认
        # RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', 3330, 1)  # 消防报警级别1
        # RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，消防设备', 3330, 2)  # 消防报警级别2

        # 2、站内电池包电压、温度均为无效值
        # 最大温度=205℃ or -50℃ and 最小温度=205℃  or -50℃
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82380，温度检测点极值统计：最高温度，最低温度', 1, 200, 200)
        # 最大电压>5V or最大电压=0V and 最小电压>5V or 最小电压=0V
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：18F82280 基础参数1：最大电压、最小电压', 1, 4, 4)

        # 3、电池在位且有心跳
        # （1）电池在位
        # （2）keyon连接
        # （3）0X18F10680 心跳为空
        # RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：电池服务停发某一帧', 'V3_0X18F10680_COMMAND')
        RunKw.api_run(KeySetVirtualBattery, 'SetVirtualBattery：电池服务恢复发送某一帧', 'V3_0X18F10680_COMMAND')

    @staticmethod
    @KwDecorator("消防系统长时间消音")
    def action_38():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，消防设备', 2, 0)
