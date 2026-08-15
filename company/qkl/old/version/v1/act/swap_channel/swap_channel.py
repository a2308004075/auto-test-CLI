import time
from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.old.version.v1.kw.kw_api.key_set_virtual_car_machine import KeySetVirtualCarMachine
from company.qkl.old.version.v1.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc
from company.qkl.old.version.v1.kw.kw_api.key_set_rbc import KeySetRbc


class SwapChannel:
    """
    换电通道
    """

    @staticmethod
    @KwDecorator('初始化车辆状态：闽H684349')
    def action_1():
        # 换电交互信息：闽H684349
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电交互信息，自检通过', 'LFP8C7PC7N1D28989')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池mac和sn信息：闽H684349')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池数据信息：数据为0')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池状态和标志信息：发0值')

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆自由度信息：通过')

    @staticmethod
    @KwDecorator('二次换电成功')
    def action_2():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：抓拍车牌', '闽H684349')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：云端换电结果下发：闽H984EC5，是否允许换电', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆连接')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙')
        time.sleep(15)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 5)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 7)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 15)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 17)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 8)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 16)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 1)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 18)
        time.sleep(20)

        # 换电交互信息：闽H684349
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电交互信息-自检失败、上高压失败', 'LFP8C7PC7N1D28989')
        time.sleep(5)

        # 车上电池包继电器状态
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池状态和标志信息：电池包主负继电器状态、电池包主正继电器状态', 2, 0, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：3、4仓断蓝牙')
        time.sleep(10)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 5)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 7)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 15)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 17)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 8)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 16)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 18)
        time.sleep(16)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电结束')
        time.sleep(4)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', False)

    @staticmethod
    @KwDecorator('一次换电成功')
    def action_3():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：抓拍车牌', '闽H684349')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：云端换电结果下发：闽H984EC5，是否允许换电', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆连接')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', True)
        time.sleep(5)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙')
        time.sleep(15)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 5)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 7)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 15)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 17)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 8)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 16)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 1)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 18)
        time.sleep(20)

        # 换电交互信息：闽H684349
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电交互信息，自检通过', 'LFP8C7PC7N1D28989')
        time.sleep(5)

        # 车上电池包继电器状态
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池状态和标志信息：电池包主负继电器状态、电池包主正继电器状态', 2, 0, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电结束')
        time.sleep(4)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', False)

    @staticmethod
    @KwDecorator('下发两次云端校验结果')
    def action_4():
        # 换电交互信息：闽H684349
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电交互信息-蓝牙断开', 'LFP8C7PC7N1D28989')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：抓拍车牌', '闽H684349')
        time.sleep(5)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙')
        time.sleep(6)

        RunKw.api_run(KeySetRbc, 'SetRbc：云端换电结果下发：闽H984EC5，是否允许换电', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆连接')
        time.sleep(2)
        # 换电交互信息：闽H684349
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电交互信息，自检通过', 'LFP8C7PC7N1D28989')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 1)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 5)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 7)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 15)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 17)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 8)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 16)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 18)
        time.sleep(20)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电结束')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', False)

    @staticmethod
    @KwDecorator('断蓝牙成功')
    def action_5():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆自由度信息：破坏非车门自由度')
        time.sleep(2)
        # 换电交互信息：闽H684349
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电交互信息-蓝牙断开', 'LFP8C7PC7N1D28989')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：抓拍车牌', '闽H684349')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙')
        time.sleep(6)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆连接')
        time.sleep(2)
        # 换电交互信息：闽H684349
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电交互信息，自检通过', 'LFP8C7PC7N1D28989')

    @staticmethod
    @KwDecorator('自检失败，无法二次换电：车上电池继电器')
    def action_6():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：抓拍车牌', '闽H684349')
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆连接')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙')
        time.sleep(15)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 5)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 7)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 15)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 17)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 8)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 16)
        time.sleep(2)

        # 40002=1
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 1)
        # 40011=6
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 6)
        time.sleep(2)
        # 车上电池包继电器状态
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池状态和标志信息：电池包主负继电器状态、电池包主正继电器状态', 2, 1, 1)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 18)
        time.sleep(20)

        # 自检失败
        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：换电交互信息-自检失败、上高压失败', 'LFP8C7PC7N1D28989')
        time.sleep(5)

    @staticmethod
    @KwDecorator('安装第二块成功-举升平台回落，自由度破坏变恢复')
    def action_7():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：抓拍车牌', '闽H684349')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：云端换电结果下发：闽H984EC5，是否允许换电', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆连接')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', True)
        time.sleep(5)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙')
        time.sleep(15)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 2)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 5)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 7)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 15)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 17)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 6)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 8)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 16)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 18)
        time.sleep(5)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆自由度信息：打开车门')
        time.sleep(1)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆自由度信息：通过')

    @staticmethod
    @KwDecorator('归中失败')
    def action_8():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：抓拍车牌', '闽H684349')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：云端换电结果下发：闽H984EC5，是否允许换电', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆连接')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', True)
        time.sleep(5)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙')
        time.sleep(15)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 1)  # 归中失败

    @staticmethod
    @KwDecorator('PLC换电流程状态')
    def action_9():
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 2, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 11, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 0)
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 0)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：抓拍车牌', '闽H684349')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：云端换电结果下发：闽H984EC5，是否允许换电', True)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：车辆连接')
        time.sleep(2)

        RunKw.api_run(KeySetRbc, 'SetRbc：车辆到位信号：是否到位', True)
        time.sleep(5)

        RunKw.api_run(KeySetVirtualCarMachine, 'SetVirtualCarMachine：电池换电交互信息：1、2仓断蓝牙')
        time.sleep(10)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 95, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 96, 1)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 98, 2)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 15)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 17)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 16)
        time.sleep(2)

        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：更新寄存器值', 6, 18)
