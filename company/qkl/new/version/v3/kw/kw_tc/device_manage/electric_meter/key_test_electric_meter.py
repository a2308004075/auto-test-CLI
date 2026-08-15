from common.handlerKw.handlerKw import HandlerKw
from company.qkl.new.version.v3.ts.device_manage.electric_meter.test_electric_meter import TestElectricMeter

KeyTestElectricMeter = {
    "命令编码03，电表（高原/八费率）": HandlerKw.kw(TestElectricMeter.test_1),
}
