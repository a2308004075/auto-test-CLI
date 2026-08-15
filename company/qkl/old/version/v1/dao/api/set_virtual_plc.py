from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.old.common.api.api_virtual_plc import ApiVirtualPlc


class SetVirtualPlc:
    @staticmethod
    @KwDecorator("SetVirtualPlc：更新寄存器值")
    def plcMock_updateRegisters(self, id, value):
        data = [{
            "id": id,
            'value': value
        }]
        return ApiVirtualPlc.plcMock_updateRegisters(data)
