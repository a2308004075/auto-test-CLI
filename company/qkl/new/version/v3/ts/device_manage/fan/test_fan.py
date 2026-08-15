from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_act.device_manage.fan.key_fan import KeyFan


class TestFan:
    @staticmethod
    @KwDecorator('风机，电池仓温度-0')
    def test_1():
        RunKw.act_run(KeyFan, '命令编码04，风机', 41, 0, 200)  # id,value
        RunKw.act_run(KeyFan, '命令编码04，风机', 42, 0, 200)  # id,value
        RunKw.act_run(KeyFan, '命令编码04，风机', 43, 0, 200)  # id,value
        RunKw.act_run(KeyFan, '命令编码04，风机', 44, 0, 200)  # id,value

    @staticmethod
    @KwDecorator('风机，工作状态-4')
    def test_2():
        RunKw.act_run(KeyFan, '命令编码01，风机', 41, 4, 0)  # slaveId,id,value
        RunKw.act_run(KeyFan, '命令编码01，风机', 42, 4, 0)  # slaveId,id,value
        RunKw.act_run(KeyFan, '命令编码01，风机', 43, 4, 0)  # slaveId,id,value
        RunKw.act_run(KeyFan, '命令编码01，风机', 44, 4, 0)  # slaveId,id,value

    @staticmethod
    @KwDecorator('风机，换电通道温度-1')
    def test_3():
        RunKw.act_run(KeyFan, '命令编码04，风机', 41, 1, 178)  # slaveId,id,value
        RunKw.act_run(KeyFan, '命令编码04，风机', 42, 1, 142)  # slaveId,id,value
        RunKw.act_run(KeyFan, '命令编码04，风机', 43, 1, 151)  # slaveId,id,value
        RunKw.act_run(KeyFan, '命令编码04，风机', 44, 1, 158)  # slaveId,id,value
