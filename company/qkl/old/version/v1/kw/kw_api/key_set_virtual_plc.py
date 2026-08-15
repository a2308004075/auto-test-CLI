from common.handlerKw.handlerKw import HandlerKw
from company.qkl.old.version.v1.dao.api.set_virtual_plc import SetVirtualPlc

KeySetVirtualPlc = {
    "SetVirtualPlc：更新寄存器值": HandlerKw.kw(SetVirtualPlc.plcMock_updateRegisters),  # 参数：['id', 'value']
}
