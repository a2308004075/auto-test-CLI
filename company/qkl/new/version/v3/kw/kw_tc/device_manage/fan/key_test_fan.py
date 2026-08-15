from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.ts.device_manage.fan.test_fan import TestFan

KeyTestFan = {
    "风机，工作状态-4": HandlerKw.kw(TestFan.test_2),
    "风机，换电通道温度-1": HandlerKw.kw(TestFan.test_3),
    "风机，电池仓温度-0": HandlerKw.kw(TestFan.test_1),
}
