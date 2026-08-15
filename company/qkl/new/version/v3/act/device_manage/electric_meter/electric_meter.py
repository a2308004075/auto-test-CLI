from common.handlerKw.runKw import RunKw
from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.version.v3.kw.kw_api.key_set_virtual_plc import KeySetVirtualPlc


class ElectricMeter:
    """
    电表
    """

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,电表总电能度数")
    def action_totalElectric(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE282, 'float_2', value)  # ['slaveId', 'start_id', 'value_type', 'value']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE302, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,交流侧有功功率")
    def action_realTimePower(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x201A, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,A相电流")
    def action_currentA(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x200C, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,B相电流")
    def action_currentB(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x200E, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,C相电流")
    def action_currentC(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2010, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,A相电压")
    def action_voltageA(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2000, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,B相电压")
    def action_voltageB(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2002, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,C相电压")
    def action_voltageC(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2004, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,正向有功电能尖一次值")
    def action_sharpTotalElectric(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE28E, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE31E, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,正向有功电能峰一次值")
    def action_peakTotalElectric(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE290, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE320, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,正向有功电能平一次值")
    def action_flatTotalElectric(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE292, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE322, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,正向有功电能谷一次值")
    def action_valleyTotalElectric(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE294, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE324, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,正向有功电能深谷一次值")
    def action_deepvalleyTotalElectric(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE296, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xE326, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,总无功功率")
    def action_totalReactivePower(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2022, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,A相有功功率")
    def action_activePowerA(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2014, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,B相有功功率")
    def action_activePowerB(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2016, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,C相有功功率")
    def action_activePowerC(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2018, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,A相无功功率")
    def action_reactivePowerA(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x201C, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,B相无功功率")
    def action_reactivePowerB(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x201E, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,C相无功功率")
    def action_reactivePowerC(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2020, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,AB线电压")
    def action_voltageAB(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2006, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,BC线电压")
    def action_voltageBC(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2008, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,CA线电压")
    def action_voltageCA(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x200A, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,总功率因数")
    def action_powerFactor(electricMeter_type, slaveId, value):
        RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0x2032, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能一次值")
    def action_activePowerTotalLastMonth(electricMeter_type, slaveId, value):
        # 1-八费率，2-高原版，3-四费率

        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc080, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc000, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能尖一次值")
    def action_activePowerSharpLastMonth(electricMeter_type, slaveId, value):
        # 1-八费率，2-高原版，3-四费率

        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc082, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc002, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能峰一次值")
    def action_activePowerPeakLastMonth(electricMeter_type, slaveId, value):
        # 1-八费率，2-高原版，3-四费率

        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc084, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc004, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能平一次值")
    def action_activePowerFlatLastMonth(electricMeter_type, slaveId, value):
        # 1-八费率，2-高原版，3-四费率

        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc086, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc006, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能谷一次值")
    def action_activePowerValleyLastMonth(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc088, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc008), 'float_2', value  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能深谷一次值")
    def action_activePowerDeepLastMonth(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc08A, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc00A, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能6一次值")
    def action_activePowerSixLastMonth(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc08C, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc00C, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能7一次值")
    def action_activePowerSevenLastMonth(electricMeter_type, slaveId, value):
        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc08E, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc00E, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']

    @staticmethod
    @KwDecorator("命令编码03，电表（八费率/高原）,上月正向有功电能8一次值")
    def action_activePowerEightLastMonth(electricMeter_type, slaveId, value):
        # 1-八费率，2-高原版，3-四费率

        if electricMeter_type == 1:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc090, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
        elif electricMeter_type == 2:
            RunKw.api_run(KeySetVirtualPlc, 'SetVirtualPlc：命令编码03，电表', slaveId, 0xc010, 'float_2', value)  # ['slaveId', 'start_id,'value_type', 'value'']
