from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc


class Fan:
    """
    风机
    """

    @staticmethod
    @KwDecorator("命令编码01，风机")
    def action_1(slaveId, id, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码01，风机', slaveId, id, value)

    @staticmethod
    @KwDecorator("命令编码02，风机")
    def action_2(slaveId, id, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码02，风机', slaveId, id, value)

    @staticmethod
    @KwDecorator("命令编码03，风机")
    def action_3(slaveId, id, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，风机', slaveId, id, value)

    @staticmethod
    @KwDecorator("命令编码04，风机")
    def action_4(slaveId, id, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码04，风机', slaveId, id, value)
