from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_act.device_manage.electric_meter.key_electric_meter import KeyElectricMeter


class TestElectricMeter:
    @staticmethod
    @KwDecorator('命令编码03，电表（高原/八费率）')
    def test_1():
        # 1-八费率，2-高原版
        electricMeter_type = 2
        slaveId = 103
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,电表总电能度数', electricMeter_type, slaveId, 100000)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,交流侧有功功率', electricMeter_type, slaveId, 200)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,A相电流', electricMeter_type, slaveId, 30)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,B相电流', electricMeter_type, slaveId, 50)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,C相电流', electricMeter_type, slaveId, 60)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,A相电压', electricMeter_type, slaveId, 70)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,B相电压', electricMeter_type, slaveId, 80)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,C相电压', electricMeter_type, slaveId, 90)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,正向有功电能尖一次值', electricMeter_type, slaveId, 210000)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,正向有功电能峰一次值', electricMeter_type, slaveId, 220000)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,正向有功电能平一次值', electricMeter_type, slaveId, 230000)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,正向有功电能谷一次值', electricMeter_type, slaveId, 240000)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,正向有功电能深谷一次值', electricMeter_type, slaveId, 250000)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,总无功功率', electricMeter_type, slaveId, 150)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,A相有功功率', electricMeter_type, slaveId, 160)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,B相有功功率', electricMeter_type, slaveId, 170)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,C相有功功率', electricMeter_type, slaveId, 180)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,A相无功功率', electricMeter_type, slaveId, 190)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,B相无功功率', electricMeter_type, slaveId, 200)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,C相无功功率', electricMeter_type, slaveId, 210)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,AB线电压', electricMeter_type, slaveId, 220)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,BC线电压', electricMeter_type, slaveId, 230)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,CA线电压', electricMeter_type, slaveId, 240)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,总功率因数', electricMeter_type, slaveId, 250)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能一次值', electricMeter_type, slaveId, 260)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能尖一次值', electricMeter_type, slaveId, 270)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能峰一次值', electricMeter_type, slaveId, 280)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能平一次值', electricMeter_type, slaveId, 290)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能谷一次值', electricMeter_type, slaveId, 300)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能谷一次值', electricMeter_type, slaveId, 310)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能深谷一次值', electricMeter_type, slaveId, 320)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能6一次值', electricMeter_type, slaveId, 330)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能7一次值', electricMeter_type, slaveId, 340)  # 参数：['electricMeter_type', 'slaveId', 'value']
        RunKw.act_run(KeyElectricMeter, '命令编码03，电表（八费率/高原）,上月正向有功电能8一次值', electricMeter_type, slaveId, 350)  # 参数：['electricMeter_type', 'slaveId', 'value']
