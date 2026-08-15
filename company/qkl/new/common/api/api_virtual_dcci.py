from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiVirtualDcci:
    @staticmethod
    def _get_path(path):
        service = '/virtual-dcci'
        return service + path

    @staticmethod
    def api_dcci_schedule_getDcciScheduleList(data):
        """
        getDcciScheduleList
        请求参数:
            jobName: string [可选] - 任务名称
            scheduleBelongs: string [可选] - 任务所属
        """
        path = f'/api/dcci/schedule/getDcciScheduleList'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_getChargerSignIn(data):
        """
        getChargerSignIn
        """
        path = f'/api/dccoMock/feign/getChargerSignIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_getCurrentMagIdControlData(data):
        """
        getCurrentMagIdControlData
        请求参数:
            msgCommandId: string [可选] - 需要查询下控数据的命令ID，组合规则：0001 代表 协议的 0x00 0x01，必填
        """
        path = f'/api/dccoMock/feign/getCurrentMagIdControlData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_getHeartBeat(data):
        """
        getHeartBeat
        """
        path = f'/api/dccoMock/feign/getHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_initData(data):
        """
        initData
        """
        path = f'/api/dccoMock/feign/initData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_send4551(data):
        """
        send4551
        请求参数:
            acInputBreaker1Fault: integer [可选] - 充电桩交流输入断路器1故障
            acInputBreaker1Status: integer [可选] - 输入断路器1状态
            acInputBreaker2Fault: integer [可选] - 充电桩交流输入断路器2故障
            acInputBreaker2Status: integer [可选] - 输入断路器2状态
            avoltage: number [可选]
            bvoltage: number [可选]
            chargeInputVoltageOverFault: integer [可选] - 充电桩输入电压过压故障
            chargeInputVoltageUnderFault: integer [可选] - 充电桩输入电压欠压故障
            chargePileFanFault: integer [可选] - 充电桩风扇故障
            chargePileFanStatus: integer [可选] - 充电设备风扇状态
            chargePileOverTempFault: integer [可选] - 充电桩过温故障
            chargerNo: integer [可选] - 充电机编号
            cvoltage: number [可选]
            doorStatus: integer [可选] - 门禁状态
            emergencyStopStatus: integer [可选] - 急停状态
            entranceGuardFault: integer [可选] - 门禁故障
            envTemp: integer [可选] - 充电设备环境温度
            fault: integer [可选] - 总故障
            floodingFault: integer [可选] - 水浸故障
            floodingStatus: integer [可选] - 水浸状态
            gunNo: integer [可选] - 充电枪编号（1~12）
            lightningArresterFault: integer [可选] - 避雷器故障
            lightningArresterStatus: integer [可选] - 避雷器状态
            otherFault: integer [可选] - 其它故障
            otherWarn: integer [可选] - 其它告警
            position: integer [可选] - 仓位号
            scramButtonFault: integer [可选] - 急停按钮动作故障
            smokeDetectorFault: integer [可选] - 烟感故障
            smokeDetectorStatus: integer [可选] - 烟感状态
            syncTime: string [可选] - 同步时间 yyyy-MM-dd HH:mm:ss
            warn: integer [可选] - 总告警
            workStatus: integer [可选] - 工作状态
        """
        path = f'/api/dccoMock/feign/send4551'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_send4552(data):
        """
        send4552
        请求参数:
            acContactorState: integer [可选] - 充电桩交流接触器状态
            auxiliaryPowerFault: integer [可选] - 辅助电源故障
            batteryPackAuxiliaryPowerState: integer [可选] - 电池包辅助电源状态
            batteryPolarityReverseFault: integer [可选] - 电池极性反接故障
            bmsChargingElectricity: number [可选] - BMS充电电流测量值
            bmsChargingVoltage: number [可选] - BMS充电电压测量值
            bmsCommunicationFault: integer [可选] - BMS通信故障
            bmsDemandCurrent: number [可选] - BMS需求电流
            bmsDemandVoltage: number [可选] - BMS需求电压
            cc1State: integer [可选] - 电池连接状态
            chargeConnectElectromagneticLockFault: integer [可选] - 充电接口电磁锁故障
            chargeGuideVoltage: number [可选] - 充电导引电压
            chargeGunNotInPlaceWarn: integer [可选] - 充电枪未归位
            chargeGunOverTempFault: integer [可选] - 充电枪过温故障
            chargeModel: integer [可选] - 充电模式
            chargePortOverTempFault: integer [可选] - 充电接口过温
            chargeStatus: integer [可选] - 充电状态
            chargerNo: integer [可选] - 充电机编号
            chargingVehicleControlFault: integer [可选] - 充电中车辆控制导引故障
            circuitDcBusNegativeOutputFuseStatus: integer [可选] - 电池回路直流母线负极输出熔断器状态
            circuitDcBusPositiveOutputFuseStatus: integer [可选] - 电池回路直流母线正极输出熔断状态
            cloudFlowNo: string [可选] - 云端流水号
            cumulativeChargingTime: integer [可选] - 本次累计充电时间
            currentChargeElectricity: number [可选] - 本次充电电量
            currentChargePower: number [可选] - 当前充电功率
            currentSoc: number [可选] - 当前SOC
            currentVoltageVehiclePowerBattery: number [可选] - 整车动力蓄电池当前电压
            dc1Temp: integer [可选] - 充电接口温度 探头1温度(接1DC+
            dc2Temp: integer [可选] - 充电接口温度 探头2温度(接1DC+
            dcBusOutputOverCurrentFault: integer [可选] - 直流母线输出过流故障
            dcBusOutputOverVoltageFault: integer [可选] - 直流母线输出过压故障
            dcBusOutputUnderVoltageFault: integer [可选] - 直流母线输出欠压故障
            dcContactorInternalVoltage: number [可选] - 直流接触器内侧电压
            dcContactorOutVoltage: number [可选] - 直流接触器外侧电压
            dischargeCircuitFault: integer [可选] - 泄放回路故障
            electricMeterCommunicationFault: integer [可选] - 电表通信异常
            electricMeterDcCurrent: number [可选] - 电表直流电表电流
            electricMeterDcElectricity: number [可选] - 直流电表总电量
            electricMeterDcVoltage: number [可选] - 电表直流电表电压
            electricMeterDegreeFault: integer [可选] - 电表电度异常
            electronicLockState: integer [可选] - 充电接口电子锁状态
            exchangeInputAdhesionFault: integer [可选] - 充电桩交流输入接触器粘连故障
            exchangeInputMoveMistakeFault: integer [可选] - 充电桩交流输入接触器拒动/误动故障
            fault: integer [可选] - 总故障
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            insulationMonitorFault: integer [可选] - 绝缘监测故障
            insulationMonitorWarn: integer [可选] - 绝缘监测告警
            insulationResistance: number [可选] - 绝缘电阻
            maxAllowElectricity: number [可选] - 最高允许充电电流
            maxAllowableTemp: number [可选] - 最高允许温度
            maxAllowableTotalChargingVoltage: number [可选] - 最高允许充电总电压
            maxBatteryTemp: integer [可选] - 最高蓄电池温度
            maxSingleAllowVoltage: number [可选] - 单体最高允许充电电压
            maxSinglecellVoltage: number [可选] - 最高单体电池电压
            maxTempDetectionPointNumber: integer [可选] - 最高温度检测点编号
            minBatteryTemp: integer [可选] - 最低蓄电池温度
            minTempDetectionPointNumber: integer [可选] - 最低温度检测点编号
            moduleOutputConnectReverselyFault: integer [可选] - 模块输出反接故障
            negativeOutputMoveMistakeFault: integer [可选] - 终端回路负极直流输出接触器粘连/拒动/误动故障
            negativeStatus: integer [可选] - 终端回路负极直流输出接触器状态
            numberHighestSingleCellVoltage: integer [可选] - 最高单体电池电压所在编号
            otherFault: integer [可选] - 其它故障
            otherWarn: integer [可选] - 其它告警
            position: integer [可选] - 仓位号
            positiveOutputMoveMistakeFault: integer [可选] - 终端回路正极直流输出接触器粘连/拒动/误动故障
            positiveStatus: integer [可选] - 电终端回路正极直流输出接触器状态
            powerNegativeOutputMoveMistakeFault: integer [可选] - 功率分配负极接触器粘连/拒动/误动故障
            powerNegativeStatus: integer [可选] - 功率分配负极接触器状态
            powerPositiveOutputMoveMistakeFault: integer [可选] - 功率分配正极接触器粘连/拒动/误动故障
            powerPositiveStatus: integer [可选] - 功率分配正极接触器状态
            ratedCapacity: number [可选] - 整车动力蓄电池额定容量
            remainChargingTime: integer [可选] - 本次剩余充电时间
            startUpSoc: number [可选] - 启动时SOC
            startupMethod: integer [可选] - 启动方式 0：本地刷卡启动 1：后台启动 2: 本地管理员启动
            tcuCcuFault: integer [可选] - TCU-CCU故障
            totalRatedCapacity: number [可选] - 整车动力蓄电池标称容量
            totalRatedVoltage: number [可选] - 整车动力蓄电池额定总电压
            vin: string [可选] - 车辆VIN码
            warn: integer [可选] - 总告警
        """
        path = f'/api/dccoMock/feign/send4552'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_send4587(data):
        """
        send4587
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果
        """
        path = f'/api/dccoMock/feign/send4587'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendBatteryStatus(data):
        """
        sendBatteryStatus
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            status: integer [可选] - 电池(CC1）连接状态
        """
        path = f'/api/dccoMock/feign/sendBatteryStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendChargeAdjustParamResult(data):
        """
        sendChargeAdjustParamResult
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            cloudFlowNo: string [可选] - 云端流水号
            failedReason: integer [可选] - 失败原因  0:默认值；1:编码成功；2:编码失败
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果  0: 成功 1：失败
        """
        path = f'/api/dccoMock/feign/sendChargeAdjustParamResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendChargeRecord(data):
        """
        sendChargeRecord
        请求参数:
            cardBalanceAfterChager: number [可选] - 充电后卡余额 精确到0.01，单位是元
            cardBalanceBeforeCharge: number [可选] - 充电前卡余额 精确到0.01，单位是元
            chargeAmountOfMoney: number [可选] - 充电金额 精确到0.01，单位是元
            chargeEndTime: string [可选] - 充电结束时间
            chargePower: number [可选] - 充电电量 精确到0.01，单位是kwh
            chargeStartTime: string [可选] - 充电开始时间
            chargerNo: integer [可选] - 充电机编号
            cloudFlowNo: string [可选] - 云端流水号
            direction: integer [可选] - 充放电方向
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            newFailReason: integer [可选]
            oneElectricMeterAfterCharge: number [可选] - 1号枪充电后电能表数 精确到0.01，单位是kwh
            oneElectricMeterBeforeCharge: number [可选] - 1号枪充电前电能表数 精确到0.01，单位是kwh
            position: integer [可选] - 仓位号
            socAfterCharge: number [可选] - 充电后SOC
            socBeforeCharge: number [可选] - 充电前soc
            startupMethod: integer [可选] - 启动方式 0：本地刷卡启动 1：后台启动 2: 本地管理员启动
            stopReason: integer [可选] - 停止原因
            stopResult: integer [可选] - 停止类型  0x00:成功；0x01失败
            timePeriodChargingAmount: array [可选] - 时段充电量
            totalDeepValleyCharge: number [可选] - 深谷总充电量
            totalFlatCharge: number [可选] - 平总充电量
            totalPeakCharge: number [可选] - 峰总充电量
            totalSharpCharge: number [可选] - 尖总充电量
            totalValleyCharge: number [可选] - 谷总充电量
            vin: string [可选]
        """
        path = f'/api/dccoMock/feign/sendChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendHeartBeat(data):
        """
        sendHeartBeat
        请求参数:
            beatCount: integer [可选] - 心跳计数，范围:1-0xFF
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reserve: integer [可选] - 桩状态  固定 0xFF 255
        """
        path = f'/api/dccoMock/feign/sendHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendPeak(data):
        """
        sendPeak
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            times: array [可选] - 时段
                        periodType: integer [可选] - 时段尖峰标识
                        startTime: string [可选] - 时段开始时间
        """
        path = f'/api/dccoMock/feign/sendPeak'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendPeakCallback(data):
        """
        sendPeakCallback
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0成功 1失败
        """
        path = f'/api/dccoMock/feign/sendPeakCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendStartChargeCallback(data):
        """
        sendStartChargeCallback
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            cloudFlowNo: string [可选] - 云端流水号
            failedReason: integer [可选] - 失败原因
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 启动结果 0 成功 1 失败
        """
        path = f'/api/dccoMock/feign/sendStartChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendStartChargeReport(data):
        """
        sendStartChargeReport
        请求参数:
            batteryType: integer [可选] - 电池类型 0x01:铅酸电池；0x02:镍氢电池；0x03:磷酸铁锂电池；0x04:锰酸锂电池；0x05:钴酸锂电池；0x06:三元材料电池；0x07:聚合物锂电池；0x08:钛酸锂电池；0xFF:其他电池
            bmsToChargeVersion: string [可选] - BMS与充电桩通信协议版本号
            chargerNo: integer [可选] - 充电机编号
            cloudFlowNo: string [可选] - 云端流水号
            currentVoltage: number [可选] - 整车动力蓄电池当前电压 数据分辨率：0.1 V/位；0V 偏移
            failReason: integer [可选] - 失败原因 参考附录二充电启动完成帧失败原因(直流)
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            maxAllowElectric: number [可选] - 最高允许放电电量
            maxAllowElectricity: number [可选] - 最高允许充电电流 数据分辨率： 0.1 A /位；-400A 偏移； 数据范围：-400.0A~0.0A
            maxAllowTemp: integer [可选] - 最高允许温度 数据分辨率： 1ºC/位，-50 ºC 偏移量；数据范围：-50ºC~+200 ºC
            maxBMSAllowVoltage: number [可选] - BMS最高允许充电电压 数据分辨率： 0.1 V /位，0V 偏移量
            maxOutputElectric: number [可选] - 充电机最大输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            maxOutputVoltage: number [可选] - 充电机最高输出电压 数据分辨率:0.1 V/位；0V 偏移
            maxSingleAllowVoltage: number [可选] - 单体最高允许充电电压 数据分辨率：0.01 V/位，0 V 偏移量； 数据范围：0~24 V
            minAllowChargeStatus: integer [可选] - 最低允许动力蓄电池荷电状态
            minAllowElectric: number [可选] - 最低允许放电电量
            minAllowSinglelVoltage: number [可选] - 最低允许单体电池电压
            minOutputElectric: number [可选] - 充电机最小输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            minOutputVoltage: number [可选] - 充电机最低输出电压 数据分辨率:0.1 V/位；0V 偏移
            newFailReason: integer [可选] - 失败原因
            nominalEnergy: number [可选] - 整车动力蓄电池标称能量 数据分辨率：0.1 kWh/位，0 kWh 偏移量；数据范围：0~1000 kWh
            position: integer [可选] - 仓位号
            ratedCapacity: number [可选] - 整车动力蓄电池额定容量 0.1 Ah /位，0 Ah 偏移量
            result: integer [可选] - 成功标识 0x00:成功；0x01失败
            shakeHandResult: integer [可选] - 充电桩与BMS握手结果 00H:握手成功 01H:握手失败
            soc: integer [可选] - 整车动力蓄电池荷电状态 数据分辨率：1%/位，0%偏移量；数据范围：0~100%
            totalRatedVoltage: number [可选] - 整车动力蓄电池额定总电压 数据分辨率：0.1 V/位；0V 偏移
            vehicleIdentificationCode: string [可选] - 车辆识别码 ASCII 遵循 27930 最新协议标准
            vin: string [可选]
        """
        path = f'/api/dccoMock/feign/sendStartChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendStopChargeCallback(data):
        """
        sendStopChargeCallback
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            cloudFlowNo: string [可选] - 云端流水号
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果码 成功 1 设备已停机 0xFF 其他
        """
        path = f'/api/dccoMock/feign/sendStopChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_sendStopChargeReport(data):
        """
        sendStopChargeReport
        请求参数:
            batteryCellMaxVoltage: number [可选] - 动力蓄电池单体最高电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryCellMinVoltage: number [可选] - 动力蓄电池单体最低电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryMaxTemp: integer [可选] - 动力蓄电池最高温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            batteryMinTemp: integer [可选] - 动力蓄电池最低温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            chargerNo: integer [可选] - 充电机编号
            cloudFlowNo: string [可选] - 云端流水号
            failedReason: integer [可选] - 停止原因
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            newFailReason: integer [可选] - 失败原因
            position: integer [可选] - 仓位号
            result: integer [可选] - 成功标识  0x00:正常停止；0x01:异常停止
            suspendSoc: number [可选] - 中止荷电状态SOC(%) 数据分辨率:1%/位，0%偏移量；数据范围:0%~100%
            vin: string [可选]
        """
        path = f'/api/dccoMock/feign/sendStopChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_signIn(data):
        """
        signIn
        请求参数:
            ccuNum: integer [可选] - ccu数量
            chargeCode: string [可选] - 充电机code
            chargeGunCounts: integer [可选] - 充电枪口数目
            chargeHardwareVersion: string [可选] - 充电控制器硬件版本号
            chargeModuleCounts: integer [可选] - 充电模块数目
            chargeSoftwareVersion: string [可选] - 充电控制器软件版本
            chargerNo: integer [可选] - 充电机编号
            circuitBreakerNum: integer [可选] - 断路器数目
            code: string [可选] - 充电设备编码
            deviceModel: string [可选]
            equipmentAttr: integer [可选] - 设备属性
            equipmentProducer: integer [可选] - 设备厂商编号
            externalChargingNumber: integer [可选] - 站外充电桩绑定的站内充电机编号（充电模块群）
            gunNo: integer [可选] - 充电枪编号（1~12）
            maxChargeCurrent: number [可选] - 最大充电电流
            maxChargeVoltage: number [可选] - 最大充电电压
            maxCurrent: number [可选] - 最大输出电流
            maxDischargeCurrent: number [可选] - 最大放电电流
            maxDischargeVoltage: number [可选] - 最大放电电压
            maxVoltage: number [可选] - 最大输出电压
            minChargeCurrent: number [可选] - 最小充电电流
            minChargeVoltage: number [可选] - 最小充电电压
            minDischargeCurrent: number [可选] - 最小放电电流
            minDischargeVoltage: number [可选] - 最小放电电压
            monitorGateNo: integer [可选] - 监控网关编码
            position: integer [可选] - 仓位号
            power: integer [可选] - 当前功率
            protocolVersion: string [可选] - 通讯协议版本
            ratedPower: integer [可选] - 额定功率
            shuntRange: integer [可选] - 分流器量程
            sn: string [可选] - 充电设备出厂序列号
            supplierCode: integer [可选] - 充电机生产商
        """
        path = f'/api/dccoMock/feign/signIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoMock_feign_txt_download():
        """
        mockTxtDownload
        """
        path = f'/api/dccoMock/feign/txt/download'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'GET', None))

    @staticmethod
    def api_hot_dcciMock_feign_getChargerSignIn(data):
        """
        查看充电枪登录签到数据
        """
        path = f'/api/hot/dcciMock/feign/getChargerSignIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_getHeartBeat(data):
        """
        查看充电设备心跳
        """
        path = f'/api/hot/dcciMock/feign/getHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_initData(data):
        """
        初始化
        """
        path = f'/api/hot/dcciMock/feign/initData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4525(data):
        """
        充电设备应答鉴权认证4525
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reqNo: integer [可选] - 连接序号
            result: integer [可选] - 鉴权结果
        """
        path = f'/api/hot/dcciMock/feign/send4525'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4534(data):
        """
        充电设备响应升级请求4534
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果
        """
        path = f'/api/hot/dcciMock/feign/send4534'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4535(data):
        """
        充电设备上送升级状态4535
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            downLoadFailedReason: integer [可选] - 下载失败原因
            fileUrl: string [可选] - 文件URL
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            upgradeFailedReason: integer [可选] - 升级失败原因
            upgradeStatus: integer [可选] - 升级状态
            upgradeType: integer [可选] - 升级类型
        """
        path = f'/api/hot/dcciMock/feign/send4535'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4551(data):
        """
        充电设备数据上报4551(周期1s)
        请求参数:
            acInputBreaker1Fault: integer [可选] - 充电桩交流输入断路器1故障
            acInputBreaker1Status: integer [可选] - 输入断路器1状态
            acInputBreaker2Fault: integer [可选] - 充电桩交流输入断路器2故障
            acInputBreaker2Status: integer [可选] - 输入断路器2状态
            avoltage: number [可选]
            bvoltage: number [可选]
            chargeInputVoltageOverFault: integer [可选] - 充电桩输入电压过压故障
            chargeInputVoltageUnderFault: integer [可选] - 充电桩输入电压欠压故障
            chargePileFanFault: integer [可选] - 充电桩风扇故障
            chargePileFanStatus: integer [可选] - 充电设备风扇状态
            chargePileOverTempFault: integer [可选] - 充电桩过温故障
            chargerNo: integer [可选] - 充电机编号
            cvoltage: number [可选]
            doorStatus: integer [可选] - 门禁状态
            emergencyStopStatus: integer [可选] - 急停状态
            entranceGuardFault: integer [可选] - 门禁故障
            envTemp: integer [可选] - 充电设备环境温度
            fault: integer [可选] - 总故障
            floodingFault: integer [可选] - 水浸故障
            floodingStatus: integer [可选] - 水浸状态
            gunNo: integer [可选] - 充电枪编号（1~12）
            lightningArresterFault: integer [可选] - 避雷器故障
            lightningArresterStatus: integer [可选] - 避雷器状态
            otherFault: integer [可选] - 其它故障
            otherWarn: integer [可选] - 其它告警
            position: integer [可选] - 仓位号
            scramButtonFault: integer [可选] - 急停按钮动作故障
            smokeDetectorFault: integer [可选] - 烟感故障
            smokeDetectorStatus: integer [可选] - 烟感状态
            syncTime: string [可选] - 同步时间 yyyy-MM-dd HH:mm:ss
            warn: integer [可选] - 总告警
            workStatus: integer [可选] - 工作状态
        """
        path = f'/api/hot/dcciMock/feign/send4551'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4552(data):
        """
        充电枪数据上报4552(周期1s)
        请求参数:
            acContactorState: integer [可选] - 交流接触器状态
            auxiliaryPowerFault: integer [可选] - 辅助电源故障
            batteryPackAuxiliaryPowerState: integer [可选] - 电池包辅助电源状态
            batteryPolarityReverseFault: integer [可选] - 电池极性反接故障
            bmsChargingElectricity: number [可选] - BMS充电电流测量值
            bmsChargingVoltage: number [可选] - BMS充电电压测量值
            bmsCommunicationFault: integer [可选] - BMS通信故障
            bmsDemandCurrent: number [可选] - BMS需求电流
            bmsDemandVoltage: number [可选] - BMS需求电压
            chargeStatus: integer [可选] - 充电状态
            chargerNo: integer [可选] - 充电机编号
            chargingVehicleControlFault: integer [可选] - 加热中车辆控制导引故障
            circuitDcBusNegativeOutputFuseStatus: integer [可选] - 电池回路直流母线负极输出熔断器状态
            circuitDcBusPositiveOutputFuseStatus: integer [可选] - 电池回路直流母线正极输出熔断状态
            cumulativeChargingTime: integer [可选] - 本次累计充电时间
            currentChargePower: number [可选] - 当前功率
            currentSoc: number [可选] - 当前SOC
            currentVoltageVehiclePowerBattery: number [可选] - 整车动力蓄电池当前电压
            dcBusNegativeOutputFuseFault: integer [可选] - 电池回路直流母线负级输出熔断器故障
            dcBusNegativeOutputMoveMistakeFault: integer [可选] - 电池回路负极极直流输出接触器粘连/拒动/误动故障
            dcBusNegativeStatus: integer [可选] - 电池回路负极直流输出接触器状态
            dcBusOutputOverCurrentFault: integer [可选] - 直流母线输出过流故障
            dcBusOutputOverVoltageFault: integer [可选] - 直流母线输出过压故障
            dcBusOutputUnderVoltageFault: integer [可选] - 直流母线输出欠压故障
            dcBusPositiveOutputFuseFault: integer [可选] - 电池回路直流母线正级输出熔断器故障
            dcBusPositiveOutputMoveMistakeFault: integer [可选] - 电池回路正极直流输出接触器粘连/拒动/误动故障
            dcBusPositiveStatus: integer [可选] - 电池回路正极直流输出接触器状态
            dcContactorInternalVoltage: number [可选] - 直流接触器内侧电压
            dcContactorOutVoltage: number [可选] - 直流接触器外侧电压
            dischargeCircuitFault: integer [可选] - 泄放回路故障
            exchangeInputAdhesionFault: integer [可选] - 充电桩交流输入接触器粘连故障
            exchangeInputMoveMistakeFault: integer [可选] - 加热机交流输入接触器拒动
            fault: integer [可选] - 总故障
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            hotChargerCommunicationFault: integer [可选] - 加热机-充电机通信故障
            insulationMonitorFault: integer [可选] - 绝缘监测故障
            insulationMonitorWarn: integer [可选] - 绝缘监测告警
            insulationResistance: number [可选] - 绝缘电阻
            maxAllowElectricity: number [可选] - 最高允许充电电流
            maxAllowableTemp: number [可选] - 最高允许温度
            maxAllowableTotalChargingVoltage: number [可选] - 最高允许充电总电压
            maxBatteryTemp: number [可选] - 最高蓄电池温度
            maxSingleAllowVoltage: number [可选] - 单体最高允许充电电压
            maxSinglecellVoltage: number [可选] - 最高单体电池电压
            maxTempDetectionPointNumber: integer [可选] - 最高温度检测点编号
            minBatteryTemp: number [可选] - 最低蓄电池温度
            minTempDetectionPointNumber: integer [可选] - 最低温度检测点编号
            model: integer [可选] - 充电模式
            module1AirOutletTemp: number [可选] - 模块1出风口温度
            module1CommunicationFault: integer [可选]
            module1FanFault: integer [可选]
            module1InletTemp: number [可选] - 模块1进风口温度
            module1InputOverVoltage: integer [可选]
            module1InputUnderVoltage: integer [可选]
            module1OtherFault: integer [可选]
            module1OutCurrent: number [可选] - 模块1输出电流
            module1OutPower: number [可选] - 模块1输出功率
            module1OutVoltage: number [可选] - 模块1输出电压
            module1OutputOverCurrent: integer [可选]
            module1OutputOverVoltage: integer [可选]
            module1OverTemperatureProtection: integer [可选]
            module1WorkStatus: integer [可选] - 模块1站内外工作状态
            module2AirOutletTemp: number [可选] - 模块2出风口温度
            module2CommunicationFault: integer [可选]
            module2FanFault: integer [可选]
            module2InletTemp: number [可选] - 模块2进风口温度
            module2InputOverVoltage: integer [可选]
            module2InputUnderVoltage: integer [可选]
            module2OtherFault: integer [可选]
            module2OutCurrent: number [可选] - 模块2输出电流
            module2OutPower: number [可选] - 模块2输出电流
            module2OutVoltage: number [可选] - 模块2输出电压
            module2OutputOverCurrent: integer [可选]
            module2OutputOverVoltage: integer [可选]
            module2OverTemperatureProtection: integer [可选]
            module2WorkStatus: integer [可选] - 模块2站内外工作状态
            moduleOutputConnectReverselyFault: integer [可选] - 模块输出反接故障
            numberHighestSingleCellVoltage: integer [可选] - 最高单体电池电压所在编号
            otherFault: integer [可选] - 其它故障
            otherWarn: integer [可选] - 其它告警
            pos: integer [可选] - 绑定仓位号
            position: integer [可选] - 仓位号
            ratedCapacity: number [可选] - 整车动力蓄电池额定容量
            remainChargingTime: integer [可选] - 本次剩余充电时间
            startUpSoc: number [可选] - 启动时SOC
            tcuCcuFault: integer [可选] - TCU-CCU故障
            totalRatedCapacity: number [可选] - 整车动力蓄电池标称容量
            totalRatedVoltage: number [可选] - 整车动力蓄电池额定总电压
            vin: string [可选] - 车辆VIN码
            warn: integer [可选] - 总告警
        """
        path = f'/api/hot/dcciMock/feign/send4552'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4557(data):
        """
        充电设备上报历史故障4557
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            items: array [可选] - 故障列表
                        code: integer [可选] - 故障代码
                        gunNo: integer [可选] - 充电枪编号
                        ts: string [可选] - 故障时间 yyyy-MM-dd HH:mm:ss
        """
        path = f'/api/hot/dcciMock/feign/send4557'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4559(data):
        """
        充电设备上报历史订单4559
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            orders: array [可选] - 订单列表
                        chargeCapacity: number [可选] - 充电量
                        endSoc: number [可选] - 结束SOC
                        endTs: string [可选] - 结束时间 yyyy-MM-dd HH:mm:ss
                        flowNo: string [可选] - 流水号
                        gunNo: integer [可选] - 充电枪编号
                        startSoc: number [可选] - 启动SOC
                        startTs: string [可选] - 启动时间 yyyy-MM-dd HH:mm:ss
                        stopReson: integer [可选] - 停止原因
        """
        path = f'/api/hot/dcciMock/feign/send4559'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4562(data):
        """
        充放电设备回复电池包故障报警阈值(4562)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果 0成功 1失败
        """
        path = f'/api/hot/dcciMock/feign/send4562'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_send4587(data):
        """
        充电设备应答复位指令(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果
        """
        path = f'/api/hot/dcciMock/feign/send4587'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendBatteryStatus(data):
        """
        充电设备上报电池连接状态
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            status: integer [可选] - 电池(CC1）连接状态
        """
        path = f'/api/hot/dcciMock/feign/sendBatteryStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendChargeAdjustParamResult(data):
        """
        充电设备应答站功率/电流调节指令结果(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因  0:默认值；1:编码成功；2:编码失败
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果  0: 成功 1：失败
        """
        path = f'/api/hot/dcciMock/feign/sendChargeAdjustParamResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendChargeRecord(data):
        """
        充电设备主动上送充电记录(一次)
        请求参数:
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            chargerNo: integer [可选] - 充电机编号
            endSoc1: number [可选] - 加热机1号枪加热后SOC
            endSoc2: number [可选] - 加热机2号枪加热后SOC
            endSoc3: number [可选] - 加热机3号枪加热后SOC
            endSoc4: number [可选] - 加热机4号枪加热后SOC
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            module: integer [可选] - 加热模式
            num: integer [可选] - 加热电池个数
            pos1: integer [可选] - 加热机1号枪绑定仓位号
            pos2: integer [可选] - 加热机2号枪绑定仓位号
            pos3: integer [可选] - 加热机3号枪绑定仓位号
            pos4: integer [可选] - 加热机4号枪绑定仓位号
            position: integer [可选] - 仓位号
            startSoc1: number [可选] - 加热机1号枪加热前SOC
            startSoc2: number [可选] - 加热机2号枪加热前SOC
            startSoc3: number [可选] - 加热机3号枪加热前SOC
            startSoc4: number [可选] - 加热机4号枪加热前SOC
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            stopReason: integer [可选] - 停止原因
            stopResult: integer [可选] - 停止类型
        """
        path = f'/api/hot/dcciMock/feign/sendChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendHeartBeat(data):
        """
        充电设备心跳上报(周期10s)
        请求参数:
            beatCount: integer [可选] - 心跳计数，范围:1-0xFF
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reserve: integer [可选] - 桩状态  固定 0xFF 255
        """
        path = f'/api/hot/dcciMock/feign/sendHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendPeak(data):
        """
        充电设备上送尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            times: array [可选] - 时段
                        periodType: integer [可选] - 时段尖峰标识
                        startTime: string [可选] - 时段开始时间
        """
        path = f'/api/hot/dcciMock/feign/sendPeak'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendPeakCallback(data):
        """
        充电机响应尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0成功 1失败
        """
        path = f'/api/hot/dcciMock/feign/sendPeakCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendStartChargeCallback(data):
        """
        充电机响应远程启动(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reason1: integer [可选] - 1号枪拒绝原因
            reason2: integer [可选] - 2号枪拒绝原因
            reason3: integer [可选] - 3号枪拒绝原因
            reason4: integer [可选] - 4号枪拒绝原因
            result: integer [可选] - 启动结果
            result1: integer [可选] - 加热机1号枪启动结果
            result2: integer [可选] - 加热机2号枪启动结果
            result3: integer [可选] - 加热机3号枪启动结果
            result4: integer [可选] - 加热机4号枪启动结果
            startNum: integer [可选] - 接受启动的枪数
        """
        path = f'/api/hot/dcciMock/feign/sendStartChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendStartChargeReport(data):
        """
        充电机上送充电启动完成帧(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            pos1: integer [可选] - 加热机1号枪绑定仓位号
            pos2: integer [可选] - 加热机2号枪绑定仓位号
            pos3: integer [可选] - 加热机3号枪绑定仓位号
            pos4: integer [可选] - 加热机4号枪绑定仓位号
            position: integer [可选] - 仓位号
            reason1: integer [可选] - 1号枪拒绝原因
            reason2: integer [可选] - 2号枪拒绝原因
            reason3: integer [可选] - 3号枪拒绝原因
            reason4: integer [可选] - 4号枪拒绝原因
            result: integer [可选] - 启动结果
            result1: integer [可选] - 加热机1号枪启动结果
            result2: integer [可选] - 加热机2号枪启动结果
            result3: integer [可选] - 加热机3号枪启动结果
            result4: integer [可选] - 加热机4号枪启动结果
        """
        path = f'/api/hot/dcciMock/feign/sendStartChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendStopChargeCallback(data):
        """
        充电机响应停止充电(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果码 成功 1 设备已停机 0xFF 其他
        """
        path = f'/api/hot/dcciMock/feign/sendStopChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendStopChargeReport(data):
        """
        充电机上送充电停止完成帧(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 充电机交互流水号
            gun: integer [可选] - 停止来源枪号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 停止类型
            stoppedReason: integer [可选] - 停止原因
        """
        path = f'/api/hot/dcciMock/feign/sendStopChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_sendVersion(data):
        """
        充电设备版本号
        请求参数:
            ccuHardVersion: string [可选] - CCU硬件版本
            ccuProtocolVersion: string [可选] - CCU通讯协议版本号
            ccuSoftVersion: string [可选] - CCU软件版本
            chargerNo: integer [可选] - 充电机编号
            communicationProtocolVersion: string [可选]
            emuCommunicationProtocolVersion: string [可选]
            emuSoftwareVersion: string [可选]
            emuhardwareVersion: string [可选]
            gunNo: integer [可选] - 充电枪编号（1~12）
            hardwareVersion: string [可选]
            pduCommunicationProtocolVersion: string [可选]
            pduSoftwareVersion: string [可选]
            pduhardwareVersion: string [可选]
            position: integer [可选] - 仓位号
            softwareVersion: string [可选]
        """
        path = f'/api/hot/dcciMock/feign/sendVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_dcciMock_feign_signIn(data):
        """
        充电机登录签到
        请求参数:
            ccuNum: integer [可选] - ccu数量
            chargeGunCounts: integer [可选] - 充电枪口数目
            chargeHardwareVersion: string [可选] - 充电控制器硬件版本号
            chargeModuleCounts: integer [可选] - 充电模块数目
            chargeSoftwareVersion: string [可选] - 充电控制器软件版本
            chargerNo: integer [可选] - 充电机编号
            circuitBreakerNum: integer [可选] - 断路器数目
            code: string [可选] - 充电设备编码
            deviceModel: string [可选]
            equipmentAttr: integer [可选] - 设备属性
            equipmentProducer: integer [可选] - 设备厂商编号
            externalChargingNumber: integer [可选] - 站外充电桩绑定的站内充电机编号（充电模块群）
            gunNo: integer [可选] - 充电枪编号（1~12）
            maxChargeCurrent: number [可选] - 最大充电电流
            maxChargeVoltage: number [可选] - 最大充电电压
            maxCurrent: number [可选] - 最大输出电流
            maxDischargeCurrent: number [可选] - 最大放电电流
            maxDischargeVoltage: number [可选] - 最大放电电压
            maxVoltage: number [可选] - 最大输出电压
            minChargeCurrent: number [可选] - 最小充电电流
            minChargeVoltage: number [可选] - 最小充电电压
            minDischargeCurrent: number [可选] - 最小放电电流
            minDischargeVoltage: number [可选] - 最小放电电压
            monitorGateNo: integer [可选] - 监控网关编码
            position: integer [可选] - 仓位号
            power: integer [可选] - 当前功率
            protocolVersion: string [可选] - 通讯协议版本
            ratedPower: integer [可选] - 额定功率
            shuntRange: integer [可选] - 分流器量程
            sn: string [可选] - 充电设备出厂序列号
            supplierCode: integer [可选] - 充电机生产商
        """
        path = f'/api/hot/dcciMock/feign/signIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_getChargerRm(data):
        """
        查看遥测数据
        """
        path = f'/api/sc/dcciMock/feign/getChargerRm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_getChargerRs(data):
        """
        查看遥信数据
        """
        path = f'/api/sc/dcciMock/feign/getChargerRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_getChargerSignIn(data):
        """
        查看充电机登录签到数据
        """
        path = f'/api/sc/dcciMock/feign/getChargerSignIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_getChargerStatus(data):
        """
        查看充电状态
        """
        path = f'/api/sc/dcciMock/feign/getChargerStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_getHeartBeat(data):
        """
        查看充电设备心跳
        """
        path = f'/api/sc/dcciMock/feign/getHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_initData(data):
        """
        初始化充电机（充电设备心跳，充电设备遥信，充电枪遥信，充电枪遥测）
        """
        path = f'/api/sc/dcciMock/feign/initData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendChargeAdjustCallback(data):
        """
        充电机响应功率/电流调节(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 成功标识  0x00:成功；0x01:失败
        """
        path = f'/api/sc/dcciMock/feign/sendChargeAdjustCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendChargeRateCallback(data):
        """
        充电机响应充电速率调节(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果，0成功 1失败
        """
        path = f'/api/sc/dcciMock/feign/sendChargeRateCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendChargeRecord(data):
        """
        充电设备主动上送充电记录(一次)
        请求参数:
            averageElectricQuantity: number [可选] - 平电量
            cardBalanceAfterCharge: number [可选] - 充电后卡余额 精确到0.01，单位是元
            cardBalanceBeforeCharge: number [可选] - 充电前卡余额 精确到0.01，单位是元
            chargeAmountOfMoney: number [可选] - 充电金额 精确到0.01，单位是元
            chargeEndTime: string [可选] - 充电结束时间
            chargePower: number [可选] - 充电电量 精确到0.01，单位是kwh
            chargeStartTime: string [可选] - 充电开始时间
            chargerIdentity: string [可选] - 电池箱唯一编号
            chargerNo: integer [可选] - 充电机编号
            electricMeterAfterCharge: number [可选] - 充电枪充电后电能表数据 精确到0.01，单位是kwh
            electricMeterBeforeCharge: number [可选] - 充电枪充电前电能表数据 精确到0.01，单位是kwh
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            peakElectricQuantity: number [可选] - 峰电量
            position: integer [可选] - 仓位号
            reserve: integer [可选] - 预留
            socAfterCharge: integer [可选] - 充电后SOC
            socBeforeCharge: integer [可选] - 充电前soc
            tipCharge: number [可选] - 尖电量
            valleyElectricity: number [可选] - 谷电量
        """
        path = f'/api/sc/dcciMock/feign/sendChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendChargeUpgradeCallback(data):
        """
        充电机响应升级请求(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因 1：文件过大 2：文件类型不支持 3：分包字节数过大 4：充电设备充电中  5：充电设备升级中 0xFF：其他原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果，0成功 1失败
        """
        path = f'/api/sc/dcciMock/feign/sendChargeUpgradeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendChargeUpgradePack(data):
        """
        充电设备请求升级包(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            subcontractSeq: integer [可选] - 分包序号
        """
        path = f'/api/sc/dcciMock/feign/sendChargeUpgradePack'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendChargeUpgradeStatusCallback(data):
        """
        充电设备上送升级状态(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            downLoadFailedReason: integer [可选] - 下载失败原因 0：无 1：服务器连接失败 2：文件下载失败 3：校验失败 255：其它
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            upgradeFileType: integer [可选] - 升级文件类型 0：TCU固件 1：充电控制板固件 2：功率控制板固件
            upgradeStatus: integer [可选] - 升级状态 0：连接服务器 1：下载中 2：下载失败（详见下载失败原因） 3：下载成功 4：启动升级 5：升级中 6：升级失败 7：升级成功
            version: string [可选] - 版本号 如1.0.3
        """
        path = f'/api/sc/dcciMock/feign/sendChargeUpgradeStatusCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendChargerRs(data):
        """
        遥信数据上报(周期1s)
        请求参数:
            acContactorState: integer [可选] - 充电桩交流接触器状态 00H：分断 01H：吸合
            acInputAdhesionFault: integer [可选] - 充电桩交流输入接触器粘连故障(预留位置供其他适用) 0H：正常 1H：故障
            acInputBreakerFault: integer [可选] - 总告警 0H：正常 1H：故障
            acInputMoveMistakeFault: integer [可选] - 充电桩交流输入接触器据动/误动故(预留位置供其他适用) 0H：正常 1H：故障
            auxiliaryPowerFault: integer [可选] - 辅助电源故障 0H：正常 1H：故障
            batteryPackAuxiliaryPowerState: integer [可选] - 电池包辅助电源状态 0：辅助电源未给电池包供电 1：辅助电源正在给电池包供电
            batteryPolarityReverseFault: integer [可选] - 电池极性反接故障 0H：正常 1H：故障
            bmsCommunicationFault: integer [可选] - BMS通信故障 0H：正常 1H：故障
            chargeConnectElectromagneticLockFault: integer [可选] - 充电接口电磁锁故障 0H：正常 1H：故障
            chargeGunNotInPlaceWarn: integer [可选] - 充电枪未归位 0H：正常 1H：告警
            chargeGunOverTempWarn: integer [可选] - 充电枪过温告警 0H：正常 1H：故障
            chargeInputVoltageOverFault: integer [可选] - 充电桩输入电压过压故障 0H：正常 1H：故障
            chargeInputVoltageUnderFault: integer [可选] - 充电桩输入电压欠压故障 0H：正常 1H：故障
            chargePileFanFault: integer [可选] - 总告警 0H：正常 1H：故障
            chargePileOverTempFault: integer [可选] - 充电桩过温故障 0H：正常 1H：故障
            chargePileOverTempWarn: integer [可选] - 充电桩过温告警 0H：正常 1H：故障
            chargePortElectronicLockState: integer [可选] - 充电接口电子锁状态 0H：解锁 1H：锁止
            chargePortOverTempFault: integer [可选] - 充电接口过温故障 0H：正常 1H：故障
            chargerGunSeatStatus: integer [可选] - 充电桩充电枪座状态 0H：已连接 1H：未连接
            chargerNo: integer [可选] - 充电机编号
            chargingVehicleControlFault: integer [可选] - 充电中车辆控制导引故障 0H：正常 1H：故障
            dcBusNegativeOutputFuseFault: integer [可选] - 直流母线负级输出熔断器故障 0H：正常 1H：故障
            dcBusNegativeOutputMoveMistakeFault: integer [可选] - 直流母线负极输出接触器拒动/误动故障 0H：正常 1H：故障
            dcBusOutputOverCurrentFault: integer [可选] - 直流母线输出过流故障 0H：正常 1H：故障
            dcBusOutputOverVoltageFault: integer [可选] - 直流母线输出过压故障 0H：正常 1H：故障
            dcBusOutputUnderVoltageFault: integer [可选] - 直流母线输出欠压故障 0H：正常 1H：故障
            dcBusPositiveOutputFuseFault: integer [可选] - 直流母线正级输出熔断器故障 0H：正常 1H：故障
            dcBusPositiveOutputMoveMistakeFault: integer [可选] - 直流母线正极输出接触器拒动/误动故障 0H：正常 1H：故障
            dischargeCircuitFault: integer [可选] - 泄放回路故障 0H：正常 1H：故障
            electricMeterCommunicationFault: integer [可选] - 电表通信异常 0H：正常 1H：故障
            electricMeterDegreeFault: integer [可选] - 电表电度异常 0H：正常 1H：故障
            entranceGuardFault: integer [可选] - 门禁故障 0H：正常 1H：故障
            fault: integer [可选] - 总故障 0H：正常 1H：故障
            floodWarn: integer [可选] - 水浸告警 0H：正常 1H：故障
            gunNo: integer [可选] - 充电枪编号（1~12）
            insulationMonitorFault: integer [可选] - 绝缘监测故障 0H：正常 1H：故障
            insulationMonitorWarn: integer [可选] - 绝缘监测告警 0H：正常 1H：故障
            lightningArresterFault: integer [可选] - 避雷器故障 0H：正常 1H：故障
            moduleOutputConnectReversely: integer [可选] - 模块输出反接 0H：正常 1H：故障
            moduleStatusFour: string [可选] - 模块4状态 1：模块关机 0：模块运行
     * 1:模块故障 0模块正常
     * 1：模块恒流 0：模块恒压
     * 1：风扇故障 0：风扇正常
     * 1：输入过压 0：输入正常
     * 1：输入欠压 0：输入正常
     * 1：输出过压 0：输出正常
     * 1：输出欠压 0：输出正常
            moduleStatusFourS: string [可选] - 模块4状态 1:过流保护 0正常
     * 1过温保护 0正常
     * 1设置关机 0设置开机
     * 预留0
            moduleStatusOne: string [可选] - 模块1状态
     * 1：模块关机 0：模块运行
     * 1:模块故障 0模块正常
     * 1：模块恒流 0：模块恒压
     * 1：风扇故障 0：风扇正常
     * 1：输入过压 0：输入正常
     * 1：输入欠压 0：输入正常
     * 1：输出过压 0：输出正常
     * 1：输出欠压 0：输出正常
            moduleStatusOneS: string [可选] - 模块1状态
     * 1:过流保护 0正常
     * 1过温保护 0正常
     * 1设置关机 0设置开机
     * 预留0
            moduleStatusThree: string [可选] - 模块3状态
     * 1：模块关机 0：模块运行
     * 1:模块故障 0模块正常
     * 1：模块恒流 0：模块恒压
     * 1：风扇故障 0：风扇正常
     * 1：输入过压 0：输入正常
     * 1：输入欠压 0：输入正常
     * 1：输出过压 0：输出正常
     * 1：输出欠压 0：输出正常
            moduleStatusThreeS: string [可选] - 模块3状态
     * 1:过流保护 0正常
     * 1过温保护 0正常
     * 1设置关机 0设置开机
     * 预留0
            moduleStatusTwo: string [可选] - 模块2状态
     * 1：模块关机 0：模块运行
     * 1:模块故障 0模块正常
     * 1：模块恒流 0：模块恒压
     * 1：风扇故障 0：风扇正常
     * 1：输入过压 0：输入正常
     * 1：输入欠压 0：输入正常
     * 1：输出过压 0：输出正常
     * 1：输出欠压 0：输出正常
            moduleStatusTwoS: string [可选] - 模块2状态
     * 1:过流保护 0正常
     * 1过温保护 0正常
     * 1设置关机 0设置开机
     * 预留0
            negativeDcOutputContactorAdhesionFault: integer [可选] - 负极直流输出接触器粘连故故障 0H：正常 1H：故障
            negativeDcOutputContactorState: integer [可选] - 负极直流输出接触器状态 00H：分断 01H：闭合
            position: integer [可选] - 仓位号
            positiveDcOutputContactorAdhesionFault: integer [可选] - 正极直流输出接触器粘连故障 0H：正常 1H：故障
            positiveDcOutputContactorState: integer [可选] - 正极直流输出接触器状态 00H：分断 01H：闭合
            reversePowerAlarm: integer [可选] - 逆功率报警
            scramButtonFault: integer [可选] - 急停按钮动作故障 0H：正常 1H：故障
            smokeDetectorFault: integer [可选] - 烟感故障 0H：正常 1H：故障
            vehicleConnectState: integer [可选] - 车辆连接状态（CC1状态） 0H：未连接 1H：已连接
            warn: integer [可选] - 总告警 0H：正常 1H：告警
            workStatus: integer [可选] - 工作状态 00H：待机  01H：工作中  02H：工作完成  03H：充/放电暂停
        """
        path = f'/api/sc/dcciMock/feign/sendChargerRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendChargerStatus(data):
        """
        终端上报充电状态(周期1s)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            gunStatus: integer [可选] - 枪状态 00 空闲 01插枪 02充电 03 故障
            invokeModuleCount: integer [可选] - 已调用模块数量
            needModuleCount: integer [可选] - 需要模块数量
            position: integer [可选] - 仓位号
        """
        path = f'/api/sc/dcciMock/feign/sendChargerStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendGunRm(data):
        """
        遥测数据上报(周期1s)
        请求参数:
            bmsChargeElectricCurrent: number [可选] - BMS充电电流
            bmsChargeVoltage: number [可选] - BMS充电电压
            bmsDemandElectricCurrent: number [可选] - BMS需求电流
            bmsDemandVoltage: number [可选] - BMS需求电压
            chargeElectricCurrent: number [可选] - 充电电流（直流电表电流）
            chargeGuidanceVoltage: number [可选] - 充电导引电压
            chargeMode: integer [可选] - 充电模式 01H：恒压充电 02H：恒流充电 放电或其他模式填0
            chargePileInnerTemp: integer [可选] - 桩内部温度
            chargePortProbe1Temp: integer [可选] - 充电接口温度 探头1温度(接口 1DC+)
            chargePortProbe2Temp: integer [可选] - 充电接口温度 探头2温度(接口 1DC-)
            chargePortProbe3Temp: integer [可选] - 充电接口温度 探头3温度(接口 2DC+)
            chargePortProbe4Temp: integer [可选] - 充电接口温度 探头4温度(接口 2DC+)
            chargePower: number [可选] - 当前充电功率 数据分辨率：0.1 kw/位
            chargeTime: integer [可选] - 本次充电时间
            chargeVoltage: number [可选] - 充电电压（直流电表 电压）
            chargerAmbientTemp: integer [可选] - 充电机环境温
            chargerNo: integer [可选] - 充电机编号
            currentChargePower: number [可选] - 当前已充电量 精确到小数点后2位
            currentSoc: integer [可选] - 当前soc
            dcMeterCurrentPower: number [可选] - 直流电表当前电量
            estimateRemainingChargeTime: integer [可选] - 估算剩余充电时间
            gunNo: integer [可选] - 充电枪编号（1~12）
            highVoltageAcquisitionElectricCurent: number [可选] - 高压采集电流
            highVoltageAcquisitionVoltage: number [可选] - 高压采集电压
            maximumBatteryTemp: integer [可选] - 最高蓄电池为温度
            maximumTempMonitorPointNum: integer [可选] - 最高温度检测点编号
            minimumBatteryTemp: integer [可选] - 最低蓄电池为温度
            minimumTempMonitorPointNum: integer [可选] - 最低温度检测点编号
            moduleAirInletTemp: integer [可选] - 模块进风口温
            moduleAirOutletTemp: integer [可选] - 模块出风口温
            position: integer [可选] - 仓位号
            singleBatteryMaximumVoltage: number [可选] - 单体电池最高电压
            singleBatteryMinimumVoltage: number [可选] - 单体电池最低
        """
        path = f'/api/sc/dcciMock/feign/sendGunRm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendPeak(data):
        """
        充电设备上送尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            timesEightPeakIdentify: integer [可选] - 时段8尖峰标识
            timesEightStartTime: string [可选] - 时段8开始时间
            timesFivePeakIdentify: integer [可选] - 时段5尖峰标识
            timesFiveStartTime: string [可选] - 时段5开始时间
            timesFourPeakIdentify: integer [可选] - 时段4尖峰标识
            timesFourStartTime: string [可选] - 时段4开始时间
            timesNum: integer [可选] - 时段个数
            timesOnePeakIdentify: integer [可选] - 时段1尖峰标识
            timesOneStartTime: string [可选] - 时段1开始时间
            timesSevenPeakIdentify: integer [可选] - 时段7尖峰标识
            timesSevenStartTime: string [可选] - 时段7开始时间
            timesSixPeakIdentify: integer [可选] - 时段6尖峰标识
            timesSixStartTime: string [可选] - 时段6开始时间
            timesThreePeakIdentify: integer [可选] - 时段3尖峰标识
            timesThreeStartTime: string [可选] - 时段3开始时间
            timesTwoPeakIdentify: integer [可选] - 时段2尖峰标识
            timesTwoStartTime: string [可选] - 时段2开始时间
        """
        path = f'/api/sc/dcciMock/feign/sendPeak'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendPeakCallback(data):
        """
        充电机响应尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0成功 1失败
        """
        path = f'/api/sc/dcciMock/feign/sendPeakCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendRemoteStartChargeCheckCallback(data):
        """
        充电机响应远程启动命令，自检判断确认请求(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因 默认0
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果码 成功 1 设备已停机 0xFF 其他
        """
        path = f'/api/sc/dcciMock/feign/sendRemoteStartChargeCheckCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendStartChargeCallback(data):
        """
        充电机响应远程启动(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 启动结果 0 成功 1 失败
        """
        path = f'/api/sc/dcciMock/feign/sendStartChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendStartChargeReport(data):
        """
        充电机上送充电启动完成帧(一次)
        请求参数:
            batteryType: integer [可选] - 电池类型 0x01:铅酸电池；0x02:镍氢电池；0x03:磷酸铁锂电池；0x04:锰酸锂电池；0x05:钴酸锂电池；0x06:三元材料电池；0x07:聚合物锂电池；0x08:钛酸锂电池；0xFF:其他电池
            bmsToCVersion: string [可选] - BMS与充电桩通信协议版本号
            chargerNo: integer [可选] - 充电机编号
            currentVoltage: number [可选] - 整车动力蓄电池当前电压 数据分辨率：0.1 V/位；0V 偏移
            failReason: integer [可选] - 失败原因
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            maxAllowElectricity: number [可选] - 最高允许充电电流 数据分辨率:0.1 A/位；0A 偏移； 数据范围:0.0~850.0A
            maxAllowTemp: integer [可选] - 最高允许温度 数据分辨率： 1ºC/位，-50 ºC 偏移量；数据范围：-50ºC~+200 ºC
            maxBMSAllowVoltage: number [可选] - BMS最高允许充电电压 数据分辨率： 0.1 V /位，0V 偏移量
            maxOutputElectric: number [可选] - 充电机最大输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            maxOutputVoltage: number [可选] - 充电机最高输出电压 数据分辨率:0.1 V/位；0V 偏移
            maxSingleAllowVoltage: number [可选] - 单体最高允许充电电压 数据分辨率：0.01 V/位，0 V 偏移量； 数据范围：0~24 V
            minOutputElectric: number [可选] - 充电机最小输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            minOutputVoltage: number [可选] - 充电机最低输出电压 数据分辨率:0.1 V/位；0V 偏移
            nominalEnergy: number [可选] - 整车动力蓄电池标称能量 数据分辨率：0.1 kWh/位，0 kWh 偏移量；数据范围：0~1000 kWh
            position: integer [可选] - 仓位号
            ratedCapacity: number [可选] - 整车动力蓄电池额定容量 0.1 Ah /位，0 Ah 偏移量
            result: integer [可选] - 成功标识 0x00:成功；0x01失败
            shakeHandResult: integer [可选] - 充电桩与BMS握手结果 00H:握手成功 01H:握手失败
            soc: integer [可选] - 整车动力蓄电池荷电状态 数据分辨率：1%/位，0%偏移量；数据范围：0~100%
            totalRatedVoltage: number [可选] - 整车动力蓄电池额定总电压 数据分辨率：0.1 V/位；0V 偏移
            vehicleIdentificationCode: string [可选] - 车辆识别码 ASCII 遵循 27930 最新协议标准
        """
        path = f'/api/sc/dcciMock/feign/sendStartChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendStopChargeCallback(data):
        """
        充电机响应停止充电(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果码 成功 1 设备已停机 0xFF 其他
        """
        path = f'/api/sc/dcciMock/feign/sendStopChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendStopChargeReport(data):
        """
        充电机上送充电停止完成帧(一次)
        请求参数:
            batteryCellMaxVoltage: number [可选] - 动力蓄电池单体最高电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryCellMinVoltage: number [可选] - 动力蓄电池单体最低电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryMaxTemp: integer [可选] - 动力蓄电池最高温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            batteryMinTemp: integer [可选] - 动力蓄电池最低温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            bclTimeout: integer [可选] - 接收电池充电需求报文（BCL） 超时
            bcpTimeout: integer [可选] - 接收电池充电参数报文(BCP)超时
            bcsTimeout: integer [可选] - 接收电池充电总状态报文(BCS)超时
            bmsChargeFaultCause: string [可选] - BMS充电故障原因
            bmsSuspendCause: string [可选] - BMS中止充电原因
            bmsSuspendFaultCause: string [可选] - BMS中止错误原因
            brmTimeout: integer [可选] - 接收 BMS 和车辆的辨识报文(BRM)超时
            broTimeout: integer [可选] - 接收 BMS 完成充电准备报文(BRO)超时
            bsdTimeout: integer [可选] - 接收 BMS 充电统计报文(BSD)超时
            bstTimeout: integer [可选] - 接收 BMS 中止充电报文(BST)超时
            ccsTimeout: integer [可选] - 接收充电机充电状态报文(CCS)超时 <00>:=正常； <01>:=超时； <10>:=不可信状态
            chargerNo: integer [可选] - 充电机编号
            cmlTimeout: integer [可选] - 接收充电机的时间同步和充电机最大输出能力报文(CML)超时 <00>:=正常； <01>:=超时； <10>:=不可信状态
            cr0Timeout: integer [可选] - 接收充电机完成充电准备报文(CR0)超时 <00>:=正常； <01>:=超时； <10>:=不可信状态
            crm0x00Timeout: integer [可选] - 接收SPN2560=0x00的充电机辨识报文（CRM）超时  <00>:=正常； <01>:=超时； <10>:=不可信状态
            crm0xAATimeout: integer [可选] - 接收SPN2560=0xAA的充电机辨识报文（CRM）超时 <00>:=正常； <01>:=超时； <10>:=不可信状态
            csdTimeout: integer [可选] - 接收充电机充电统计报文(CSD)超时
            cstTimeout: integer [可选] - 接收充电机中止充电报文(CST)超时
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reserve21: integer [可选] - BMS检测到的其他错误
            reserve33: integer [可选] - 充电机检测到的其他错误
            result: integer [可选] - 成功标识  0x00:成功；0x01:失败
            stoppedReason: integer [可选] - 失败原因
            suspendSoc: integer [可选] - 中止荷电状态SOC(%) 数据分辨率:1%/位，0%偏移量；数据范围:0%~100%
        """
        path = f'/api/sc/dcciMock/feign/sendStopChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_sendVin(data):
        """
        站外终端上报VIN码至站控平台(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            vin: string [可选] - Vin码
        """
        path = f'/api/sc/dcciMock/feign/sendVin'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_sc_dcciMock_feign_signIn(data):
        """
        充电机登录签到
        请求参数:
            chargeGunCounts: integer [可选] - 充电枪口数目
            chargeHardwareVersion: string [可选] - 充电控制器硬件版本号
            chargeModuleCounts: integer [可选] - 充电模块数目
            chargeSoftwareVersion: string [可选] - 充电控制器软件版本
            chargerNo: integer [可选] - 充电机编号
            currentPower: integer [可选] - 当前功率
            currentRate: number [可选] - 当前速率
            equipmentAttr: integer [可选] - 设备属性
            equipmentProducer: integer [可选] - 设备厂商编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            monitorGateNo: integer [可选] - 监控网关编码
            position: integer [可选] - 仓位号
            protocolVersion: string [可选] - 通讯协议版本
            ratedPower: integer [可选] - 额定功率
            shuntRange: integer [可选] - 分流器量程
        """
        path = f'/api/sc/dcciMock/feign/signIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v10_demo_sendKeyonCallbacks(data):
        """
        sendKeyonCallbacks
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因 0:成功 1：电池包/或者充电枪未连接 2：正在充电中 0xFF：其他
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0: 成功 1：失败
        """
        path = f'/api/v1.0/demo/sendKeyonCallbacks'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v10_demo_startCharge(data):
        """
        sendStartCharge
        """
        path = f'/api/v1.0/demo/startCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v10_demo_stopCharge(data):
        """
        sendStopCharge
        """
        path = f'/api/v1.0/demo/stopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_getChargerRm(data):
        """
        查看遥测数据
        """
        path = f'/api/v1/dcciMock/feign/getChargerRm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_getChargerRs(data):
        """
        查看遥信数据
        """
        path = f'/api/v1/dcciMock/feign/getChargerRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_getChargerSignIn(data):
        """
        查看充电机登录签到数据
        """
        path = f'/api/v1/dcciMock/feign/getChargerSignIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_getHeartBeat(data):
        """
        查看充电设备心跳
        """
        path = f'/api/v1/dcciMock/feign/getHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_initData(data):
        """
        初始化充电机（充电设备心跳，充电设备遥信，充电枪遥信，充电枪遥测）
        """
        path = f'/api/v1/dcciMock/feign/initData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargeAdjustCallback(data):
        """
        充电机响应功率/电流调节(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 成功标识  0x00:成功；0x01:失败
        """
        path = f'/api/v1/dcciMock/feign/sendChargeAdjustCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargeRateCallback(data):
        """
        充电机响应充电速率调节(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果，0成功 1失败
        """
        path = f'/api/v1/dcciMock/feign/sendChargeRateCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargeRecord(data):
        """
        充电设备主动上送充电记录(一次)
        请求参数:
            averageElectricQuantity: number [可选] - 平电量
            cardBalanceAfterCharge: number [可选] - 充电后卡余额 精确到0.01，单位是元
            cardBalanceBeforeCharge: number [可选] - 充电前卡余额 精确到0.01，单位是元
            chargeAmountOfMoney: number [可选] - 充电金额 精确到0.01，单位是元
            chargeEndTime: string [可选] - 充电结束时间
            chargePower: number [可选] - 充电电量 精确到0.01，单位是kwh
            chargeStartTime: string [可选] - 充电开始时间
            chargerIdentity: string [可选] - 电池箱唯一编号
            chargerNo: integer [可选] - 充电机编号
            electricMeterAfterCharge: number [可选] - 充电枪充电后电能表数据 精确到0.01，单位是kwh
            electricMeterBeforeCharge: number [可选] - 充电枪充电前电能表数据 精确到0.01，单位是kwh
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            peakElectricQuantity: number [可选] - 峰电量
            position: integer [可选] - 仓位号
            socAfterCharge: integer [可选] - 充电后SOC
            socBeforeCharge: integer [可选] - 充电前soc
            stoppedReason: integer [可选] - 停止原因
            tipCharge: number [可选] - 尖电量
            valleyElectricity: number [可选] - 谷电量
        """
        path = f'/api/v1/dcciMock/feign/sendChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargeSoftVersion(data):
        """
        充放电机应答版本号(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            communicationProtocolVersion: string [可选] - 通讯协议版本号
            gunNo: integer [可选] - 充电枪编号（1~12）
            hardwareVersion: string [可选] - 硬件版本号
            position: integer [可选] - 仓位号
            softwareVersion: string [可选] - 软件版本号
        """
        path = f'/api/v1/dcciMock/feign/sendChargeSoftVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargeUpgradeCallback(data):
        """
        充电机响应升级请求(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因 1：文件过大 2：文件类型不支持 3：分包字节数过大 4：充电设备充电中  5：充电设备升级中 0xFF：其他原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果，0成功 1失败
        """
        path = f'/api/v1/dcciMock/feign/sendChargeUpgradeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargeUpgradePack(data):
        """
        充电设备请求升级包(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            subcontractSeq: integer [可选] - 分包序号
        """
        path = f'/api/v1/dcciMock/feign/sendChargeUpgradePack'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargeUpgradeStatusCallback(data):
        """
        充电设备上送升级状态(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            downLoadFailedReason: integer [可选] - 下载失败原因 0：无 1：服务器连接失败 2：文件下载失败 3：校验失败 255：其它
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            upgradeFileType: integer [可选] - 升级文件类型 0：TCU固件 1：充电控制板固件 2：功率控制板固件
            upgradeStatus: integer [可选] - 升级状态 0：连接服务器 1：下载中 2：下载失败（详见下载失败原因） 3：下载成功 4：启动升级 5：升级中 6：升级失败 7：升级成功
            version: string [可选] - 版本号 如1.0.3
        """
        path = f'/api/v1/dcciMock/feign/sendChargeUpgradeStatusCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargerModuleStatus(data):
        """
        充电设备上送模块状态(周期1s)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            moduleStatus: integer [可选] - 模块状态 0 空闲 1 站内使用 2 站外使用 3 故障
            position: integer [可选] - 仓位号
        """
        path = f'/api/v1/dcciMock/feign/sendChargerModuleStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendChargerRs(data):
        """
        遥信数据上报(周期1s)
        请求参数:
            acContactorState: integer [可选] - 充电桩交流接触器状态 00H：分断 01H：吸合
            acInputAdhesionFault: integer [可选] - 充电桩交流输入接触器粘连故障(预留位置供其他适用) 0H：正常 1H：故障
            acInputBreakerFault: integer [可选] - 总告警 0H：正常 1H：故障
            acInputMoveMistakeFault: integer [可选] - 充电桩交流输入接触器据动/误动故(预留位置供其他适用) 0H：正常 1H：故障
            auxiliaryPowerFault: integer [可选] - 辅助电源故障 0H：正常 1H：故障
            batteryPackAuxiliaryPowerState: integer [可选] - 电池包辅助电源状态 0：辅助电源未给电池包供电 1：辅助电源正在给电池包供电
            batteryPolarityReverseFault: integer [可选] - 电池极性反接故障 0H：正常 1H：故障
            bmsCommunicationFault: integer [可选] - BMS通信故障 0H：正常 1H：故障
            chargeConnectElectromagneticLockFault: integer [可选] - 充电接口电磁锁故障 0H：正常 1H：故障
            chargeGunNotInPlaceWarn: integer [可选] - 充电枪未归位 0H：正常 1H：告警
            chargeGunOverTempWarn: integer [可选] - 充电枪过温告警 0H：正常 1H：故障
            chargeInputVoltageOverFault: integer [可选] - 充电桩输入电压过压故障 0H：正常 1H：故障
            chargeInputVoltageUnderFault: integer [可选] - 充电桩输入电压欠压故障 0H：正常 1H：故障
            chargePileFanFault: integer [可选] - 总告警 0H：正常 1H：故障
            chargePileOverTempFault: integer [可选] - 充电桩过温故障 0H：正常 1H：故障
            chargePileOverTempWarn: integer [可选] - 充电桩过温告警 0H：正常 1H：故障
            chargePortElectronicLockState: integer [可选] - 充电接口电子锁状态 0H：解锁 1H：锁止
            chargePortOverTempFault: integer [可选] - 充电接口过温故障 0H：正常 1H：故障
            chargerGunSeatStatus: integer [可选] - 充电桩充电枪座状态 0H：已连接 1H：未连接
            chargerNo: integer [可选] - 充电机编号
            chargingVehicleControlFault: integer [可选] - 充电中车辆控制导引故障 0H：正常 1H：故障
            dcBusNegativeOutputFuseFault: integer [可选] - 直流母线负级输出熔断器故障 0H：正常 1H：故障
            dcBusNegativeOutputMoveMistakeFault: integer [可选] - 直流母线负极输出接触器拒动/误动故障 0H：正常 1H：故障
            dcBusOutputOverCurrentFault: integer [可选] - 直流母线输出过流故障 0H：正常 1H：故障
            dcBusOutputOverVoltageFault: integer [可选] - 直流母线输出过压故障 0H：正常 1H：故障
            dcBusOutputUnderVoltageFault: integer [可选] - 直流母线输出欠压故障 0H：正常 1H：故障
            dcBusPositiveOutputFuseFault: integer [可选] - 直流母线正级输出熔断器故障 0H：正常 1H：故障
            dcBusPositiveOutputMoveMistakeFault: integer [可选] - 直流母线正极输出接触器拒动/误动故障 0H：正常 1H：故障
            dischargeCircuitFault: integer [可选] - 泄放回路故障 0H：正常 1H：故障
            electricMeterCommunicationFault: integer [可选] - 电表通信异常 0H：正常 1H：故障
            electricMeterDegreeFault: integer [可选] - 电表电度异常 0H：正常 1H：故障
            entranceGuardFault: integer [可选] - 门禁故障 0H：正常 1H：故障
            fault: integer [可选] - 总故障 0H：正常 1H：故障
            floodWarn: integer [可选] - 水浸告警 0H：正常 1H：故障
            gunNo: integer [可选] - 充电枪编号（1~12）
            insulationMonitorFault: integer [可选] - 绝缘监测故障 0H：正常 1H：故障
            insulationMonitorWarn: integer [可选] - 绝缘监测告警 0H：正常 1H：故障
            lightningArresterFault: integer [可选] - 避雷器故障 0H：正常 1H：故障
            moduleCommunicationStatus: string [可选] - 模块通信状态 0x00000001：1号模块通信故障 0x00000002：2号模块通信故障 0x00000004：3号模块通信故障 0x00000008：4号模块通信故障
            moduleFaultStatus: string [可选] - 模块故障状态 0x00000001：1号模块故障 0x00000002：2号模块故障 0x00000004：3号模块故障 0x00000008：4号模块故障
            moduleOutputConnectReversely: integer [可选] - 模块输出反接 0H：正常 1H：故障
            negativeDcOutputContactorAdhesionFault: integer [可选] - 负极直流输出接触器粘连故故障 0H：正常 1H：故障
            negativeDcOutputContactorState: integer [可选] - 负极直流输出接触器状态 00H：分断 01H：闭合
            otherFault: integer [可选] - 其它故障
            position: integer [可选] - 仓位号
            positiveDcOutputContactorAdhesionFault: integer [可选] - 正极直流输出接触器粘连故障 0H：正常 1H：故障
            positiveDcOutputContactorState: integer [可选] - 正极直流输出接触器状态 00H：分断 01H：闭合
            scramButtonFault: integer [可选] - 急停按钮动作故障 0H：正常 1H：故障
            smokeDetectorFault: integer [可选] - 烟感故障 0H：正常 1H：故障
            vehicleConnectState: integer [可选] - 车辆连接状态（CC1状态） 0H：未连接 1H：已连接
            warn: integer [可选] - 总告警 0H：正常 1H：告警
            workStatus: integer [可选] - 工作状态 00H：待机  01H：站内工作  02H：站外工作  03H：工作完成 04H：站内充/放电暂停 05H：站外充/放电暂停 0FH：故障
        """
        path = f'/api/v1/dcciMock/feign/sendChargerRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendGunRm(data):
        """
        遥测数据上报(周期1s)
        请求参数:
            bmsChargeElectricCurrent: number [可选] - BMS充电电流
            bmsChargeVoltage: number [可选] - BMS充电电压
            bmsDemandElectricCurrent: number [可选] - BMS需求电流
            bmsDemandVoltage: number [可选] - BMS需求电压
            chargeElectricCurrent: number [可选] - 充电电流（直流电表电流）
            chargeGuidanceVoltage: number [可选] - 充电导引电压
            chargeMode: integer [可选] - 充电模式 01H：恒压充电 02H：恒流充电 放电或其他模式填0
            chargePileInnerTemp: integer [可选] - 桩内部温度
            chargePortProbe1Temp: integer [可选] - 充电接口温度 探头1温度(接口 1DC+)
            chargePortProbe2Temp: integer [可选] - 充电接口温度 探头2温度(接口 1DC-)
            chargePortProbe3Temp: integer [可选] - 充电接口温度 探头3温度(接口 2DC+)
            chargePortProbe4Temp: integer [可选] - 充电接口温度 探头4温度(接口 2DC+)
            chargePower: number [可选] - 当前充电功率
            chargeTime: integer [可选] - 本次充电时间
            chargeVoltage: number [可选] - 充电电压（直流电表 电压）
            chargerAmbientTemp: integer [可选] - 充电机环境温
            chargerNo: integer [可选] - 充电机编号
            currentSoc: integer [可选] - 当前soc
            dcMeterCurrentPower: number [可选] - 直流电表当前电量
            estimateRemainingChargeTime: integer [可选] - 估算剩余充电时间
            gunNo: integer [可选] - 充电枪编号（1~12）
            highVoltageAcquisitionElectricCurent: number [可选] - 高压采集电流
            highVoltageAcquisitionVoltage: number [可选] - 高压采集电压
            maximumBatteryTemp: integer [可选] - 最高蓄电池为温度
            maximumTempMonitorPointNum: integer [可选] - 最高温度检测点编号
            minimumBatteryTemp: integer [可选] - 最低蓄电池为温度
            minimumTempMonitorPointNum: integer [可选] - 最低温度检测点编号
            moduleAirInletTemp: integer [可选] - 模块进风口温
            moduleAirOutletTemp: integer [可选] - 模块出风口温
            position: integer [可选] - 仓位号
            singleBatteryMaximumVoltage: number [可选] - 单体电池最高电压
            singleBatteryMinimumVoltage: number [可选] - 单体电池最低
            vin: string [可选] - 车辆VIN码
        """
        path = f'/api/v1/dcciMock/feign/sendGunRm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendOfflineStopChargeCallback(data):
        """
        充电机响应监控平台掉线停止充电确认请求(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 失败原因 0：成功 1：失败
        """
        path = f'/api/v1/dcciMock/feign/sendOfflineStopChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendPeak(data):
        """
        充电设备上送尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            timesEightPeakIdentify: integer [可选] - 时段8尖峰标识
            timesEightStartTime: string [可选] - 时段8开始时间
            timesFivePeakIdentify: integer [可选] - 时段5尖峰标识
            timesFiveStartTime: string [可选] - 时段5开始时间
            timesFourPeakIdentify: integer [可选] - 时段4尖峰标识
            timesFourStartTime: string [可选] - 时段4开始时间
            timesNum: integer [可选] - 时段个数
            timesOnePeakIdentify: integer [可选] - 时段1尖峰标识
            timesOneStartTime: string [可选] - 时段1开始时间
            timesSevenPeakIdentify: integer [可选] - 时段7尖峰标识
            timesSevenStartTime: string [可选] - 时段7开始时间
            timesSixPeakIdentify: integer [可选] - 时段6尖峰标识
            timesSixStartTime: string [可选] - 时段6开始时间
            timesThreePeakIdentify: integer [可选] - 时段3尖峰标识
            timesThreeStartTime: string [可选] - 时段3开始时间
            timesTwoPeakIdentify: integer [可选] - 时段2尖峰标识
            timesTwoStartTime: string [可选] - 时段2开始时间
        """
        path = f'/api/v1/dcciMock/feign/sendPeak'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendPeakCallback(data):
        """
        充电机响应尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0成功 1失败
        """
        path = f'/api/v1/dcciMock/feign/sendPeakCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendRemoteStartChargeCheckCallback(data):
        """
        充电机响应远程启动命令，自检判断确认请求(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因 默认0
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果码 成功 1 设备已停机 0xFF 其他
        """
        path = f'/api/v1/dcciMock/feign/sendRemoteStartChargeCheckCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendStartChargeCallback(data):
        """
        充电机响应远程启动(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 启动结果 0 成功 1 失败
        """
        path = f'/api/v1/dcciMock/feign/sendStartChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendStartChargeReport(data):
        """
        充电机上送充电启动完成帧(一次)
        请求参数:
            batteryType: integer [可选] - 电池类型 0x01:铅酸电池；0x02:镍氢电池；0x03:磷酸铁锂电池；0x04:锰酸锂电池；0x05:钴酸锂电池；0x06:三元材料电池；0x07:聚合物锂电池；0x08:钛酸锂电池；0xFF:其他电池
            bmsChargerVersion: string [可选] - BMS与充电桩通信协议版本号
            chargerNo: integer [可选] - 充电机编号
            currentVoltage: number [可选] - 整车动力蓄电池当前电压 数据分辨率：0.1 V/位；0V 偏移
            failReason: integer [可选] - 失败原因
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            maxAllowElectricity: number [可选] - 最高允许充电电流 数据分辨率:0.1 A/位；0A 偏移； 数据范围:0.0~850.0A
            maxAllowTemp: integer [可选] - 最高允许温度 数据分辨率： 1ºC/位，-50 ºC 偏移量；数据范围：-50ºC~+200 ºC
            maxBMSAllowVoltage: number [可选] - BMS最高允许充电电压 数据分辨率： 0.1 V /位，0V 偏移量
            maxOutputElectric: number [可选] - 充电机最大输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            maxOutputVoltage: number [可选] - 充电机最高输出电压 数据分辨率:0.1 V/位；0V 偏移
            maxSingleAllowVoltage: number [可选] - 单体最高允许充电电压 数据分辨率：0.01 V/位，0 V 偏移量； 数据范围：0~24 V
            minOutputElectric: number [可选] - 充电机最小输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            minOutputVoltage: number [可选] - 充电机最低输出电压 数据分辨率:0.1 V/位；0V 偏移
            nominalEnergy: number [可选] - 整车动力蓄电池标称能量 数据分辨率：0.1 kWh/位，0 kWh 偏移量；数据范围：0~1000 kWh
            position: integer [可选] - 仓位号
            ratedCapacity: number [可选] - 整车动力蓄电池额定容量 0.1 Ah /位，0 Ah 偏移量
            result: integer [可选] - 成功标识 0x00:成功；0x01失败
            shakeHandResult: integer [可选] - 充电桩与BMS握手结果 00H:握手成功 01H:握手失败
            soc: integer [可选] - 整车动力蓄电池荷电状态 数据分辨率：1%/位，0%偏移量；数据范围：0~100%
            totalRatedVoltage: number [可选] - 整车动力蓄电池额定总电压 数据分辨率：0.1 V/位；0V 偏移
            vehicleIdentificationCode: string [可选] - 车辆识别码 ASCII 遵循 27930 最新协议标准
        """
        path = f'/api/v1/dcciMock/feign/sendStartChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendStopChargeCallback(data):
        """
        充电机响应停止充电(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果码 成功 1 设备已停机 0xFF 其他
        """
        path = f'/api/v1/dcciMock/feign/sendStopChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_sendStopChargeReport(data):
        """
        充电机上送充电停止完成帧(一次)
        请求参数:
            batteryCellMaxVoltage: number [可选] - 动力蓄电池单体最高电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryCellMinVoltage: number [可选] - 动力蓄电池单体最低电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryMaxTemp: integer [可选] - 动力蓄电池最高温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            batteryMinTemp: integer [可选] - 动力蓄电池最低温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            bmsChargeFaultCause: string [可选] - BMS充电故障原因
            bmsSuspendCause: string [可选] - BMS中止充电原因
            bmsSuspendFaultCause: string [可选] - BMS中止错误原因
            chargerNo: integer [可选] - 充电机编号
            failReason: integer [可选] - 失败原因
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 成功标识  0x00:成功；0x01:失败
            suspendSoc: integer [可选] - 中止荷电状态SOC(%) 数据分辨率:1%/位，0%偏移量；数据范围:0%~100%
        """
        path = f'/api/v1/dcciMock/feign/sendStopChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v1_dcciMock_feign_signIn(data):
        """
        充电机登录签到
        请求参数:
            chargeGunCounts: integer [可选] - 充电枪口数目
            chargeHardwareVersion: string [可选] - 充电控制器硬件版本号
            chargeModuleCounts: integer [可选] - 充电模块数目
            chargeSoftwareVersion: string [可选] - 充电控制器软件版本
            chargerNo: integer [可选] - 充电机编号
            currentRate: number [可选] - 当前速率
            equipmentAttr: integer [可选] - 设备属性
            equipmentProducer: integer [可选] - 设备厂商编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            monitorGateNo: integer [可选] - 监控网关编码
            position: integer [可选] - 仓位号
            protocolVersion: string [可选] - 通讯协议版本
            ratedPower: integer [可选] - 额定功率
            shuntRange: integer [可选] - 分流器量程
        """
        path = f'/api/v1/dcciMock/feign/signIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_getChargerRs(data):
        """
        查看充电设备遥信数据
        """
        path = f'/api/v2/dcciMock/feign/getChargerRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_getChargerSignIn(data):
        """
        查看充电枪登录签到数据
        """
        path = f'/api/v2/dcciMock/feign/getChargerSignIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_getCurrentMagIdControlData(data):
        """
        getCurrentMagIdControlData
        请求参数:
            msgCommandId: string [可选] - 需要查询下控数据的命令ID，组合规则：0001 代表 协议的 0x00 0x01，必填
        """
        path = f'/api/v2/dcciMock/feign/getCurrentMagIdControlData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_getGunRm(data):
        """
        查看充电枪遥测数据
        """
        path = f'/api/v2/dcciMock/feign/getGunRm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_getGunRs(data):
        """
        查看充电枪遥信数据
        """
        path = f'/api/v2/dcciMock/feign/getGunRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_getHeartBeat(data):
        """
        查看充电设备心跳
        """
        path = f'/api/v2/dcciMock/feign/getHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_initData(data):
        """
        初始化充电机（充电设备心跳，充电设备遥信，充电枪遥信，充电枪遥测）
        """
        path = f'/api/v2/dcciMock/feign/initData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendChargeAdjustParamResult(data):
        """
        充电设备应答站功率/电流调节指令结果(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因  0:默认值；1:编码成功；2:编码失败
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果  0: 成功 1：失败
        """
        path = f'/api/v2/dcciMock/feign/sendChargeAdjustParamResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendChargeEncodingResult(data):
        """
        充电设备上报电池包编码结果(一次)
        请求参数:
            batterySn: string [可选] - 电池包SN
            batterySnStatus: integer [可选] - 电池包SN状态 0：无效SN码 1：有效SN码
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 编码结果  0:默认值；1:编码成功；2:编码失败
        """
        path = f'/api/v2/dcciMock/feign/sendChargeEncodingResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendChargeRecord(data):
        """
        充电设备主动上送充电记录(一次)
        请求参数:
            cardBalanceAfterChager: number [可选] - 充电后卡余额 精确到0.01，单位是元
            cardBalanceBeforeCharge: number [可选] - 充电前卡余额 精确到0.01，单位是元
            chargeAmountOfMoney: number [可选] - 充电金额 精确到0.01，单位是元
            chargeEndTime: string [可选] - 充电结束时间
            chargePower: number [可选] - 充电电量 精确到0.01，单位是kwh
            chargeStartTime: string [可选] - 充电开始时间
            chargeTimesNum: integer [可选] - 充电时段数量
            chargerIdentity: string [可选] - 电池箱唯一编号
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            oneElectricMeterAfterCharge: number [可选] - 1号枪充电后电能表数 精确到0.01，单位是kwh
            oneElectricMeterBeforeCharge: number [可选] - 1号枪充电前电能表数 精确到0.01，单位是kwh
            position: integer [可选] - 仓位号
            socAfterCharge: integer [可选] - 充电后SOC
            socBeforeCharge: integer [可选] - 充电前soc
            stopReason: integer [可选] - 失败原因
            timesEightIdentify: integer [可选] - 时段8标识
            timesEightPower: number [可选] - 时段8电量
            timesEightStartTime: string [可选] - 时段8开始时间
            timesFiveIdentify: integer [可选] - 时段5标识
            timesFivePower: number [可选] - 时段5电量
            timesFiveStartTime: string [可选] - 时段5开始时间
            timesFourIdentify: integer [可选] - 时段4标识
            timesFourPower: number [可选] - 时段4电量
            timesFourStartTime: string [可选] - 时段4开始时间
            timesOneIdentify: integer [可选] - 时段1标识
            timesOnePower: number [可选] - 时段1电量
            timesOneStartTime: string [可选] - 时段1开始时间
            timesSevenIdentify: integer [可选] - 时段7标识
            timesSevenPower: number [可选] - 时段7电量
            timesSevenStartTime: string [可选] - 时段7开始时间
            timesSixIdentify: integer [可选] - 时段6标识
            timesSixPower: number [可选] - 时段6电量
            timesSixStartTime: string [可选] - 时段6开始时间
            timesThreeIdentify: integer [可选] - 时段3标识
            timesThreePower: number [可选] - 时段3电量
            timesThreeStartTime: string [可选] - 时段3开始时间
            timesTwoIdentify: integer [可选] - 时段2标识
            timesTwoPower: number [可选] - 时段2电量
            timesTwoStartTime: string [可选] - 时段2开始时间
            totalChargeTime: number [可选] - 充电仓累计充电时间（预留） 分辨率0.01h
        """
        path = f'/api/v2/dcciMock/feign/sendChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendChargerRs(data):
        """
        充电设备遥信数据上报(周期1s)
        请求参数:
            acInputBreakerFault: integer [可选] - 充电桩交流输入断路器故障 (系统供电断路器) 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            chargeInputVoltageOverFault: integer [可选] - 充电桩输入电压过压故障 该数据项为“故障”时，“总故障”置为“故障”状态。 00H：正常 01H：故障
            chargeInputVoltageUnderFault: integer [可选] - 充电桩输入电压欠压故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            chargePileFanFault: integer [可选] - 充电桩风扇故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            chargePileOverTempFault: integer [可选] - 充电桩过温故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            chargerNo: integer [可选] - 充电机编号
            entranceGuardFault: integer [可选] - 门禁故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            fault: integer [可选] - 总故障 0H：正常 1H：故障
            floodWarn: integer [可选] - 水浸告警 该数据项为“故障”时，“总故障”置为“故障”状态。 00H：正常 01H：故障
            gunNo: integer [可选] - 充电枪编号（1~12）
            lightningArresterFault: integer [可选] - 避雷器故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            moduleStatus: string [可选]
            position: integer [可选] - 仓位号
            scramButtonFault: integer [可选] - 急停按钮动作故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            smokeDetectorFault: integer [可选] - 烟感故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            warn: integer [可选] - 总告警 0H：正常 1H：告警
            workStatus: integer [可选] - 工作状态 00H：待机。无故障且所有充电枪不在充电 01H：工作中。有充电枪在工作(包含充电中，充电暂停，充电完成) 0EH：维护。正在维护中，暂时无法使用 0FH：故障。字段2总故障为故障时，状态为故障
        """
        path = f'/api/v2/dcciMock/feign/sendChargerRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendGunRm(data):
        """
        充电枪遥测数据上报(周期1s)
        请求参数:
            batterySn: string [可选] - 电池包SN
            bmsChargeElectricCurrent: number [可选] - BMS充电电流 测量值 数据分辨率：0.1 A/位；-400A偏移；数据 范围：-400.0 A~0.0A
            bmsChargeVoltage: number [可选] - BMS充电电压 测量值 数据分辨率：0.1 V/位，0 V偏移量；数据 范围：0.0 V~950.0V
            bmsDemandElectricCurrent: number [可选] - BMS需求电流 数据分辨率：0.1 A/位；-400A偏移；数据 范围：-400.0 A~0.0A
            bmsDemandVoltage: number [可选] - BMS需求电压 数据分辨率：0.1 V/位，0 V偏移量；数据 范围：0.0 V~950.0V
            chargeElectricCurrent: number [可选] - 充电电流（直流电表电流） 精确到小数点后 1位 如果有直流电表，为直流电表电流，放电时有可能为负数
            chargeGuidanceVoltage: number [可选] - 充电导引电压 数据分辨率：0.01V/位，0V偏移量；数据 范围 0.00 V~30.00V
            chargeMode: integer [可选] - 充电模式 01H：恒压充电 02H：恒流充电 放电或其他模式填0
            chargePortProbe1Temp: integer [可选] - 充电接口温度 探头1温度(接口 1DC+) 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +200.0℃
            chargePortProbe2Temp: integer [可选] - 充电接口温度 探头2温度(接口 1DC-) 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +200.0℃
            chargePortProbe3Temp: integer [可选] - 充电接口温度 探头3温度(接口 2DC+) 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +200.0℃
            chargePortProbe4Temp: integer [可选] - 充电接口温度 探头4温度(接口 2DC+) 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +200.0℃
            chargePower: number [可选] - 当前充电功率 数据分辨率：0.1 kw/位
            chargeTime: integer [可选] - 本次充电时间 精确度分钟
            chargeVoltage: number [可选] - 充电电压（直流电表 电压） 精确到小数点后 1位 如果有直流电表，为直流电表电压
            chargerAmbientTemp: integer [可选] - 充电机环境温 度 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +90.0℃
            chargerNo: integer [可选] - 充电机编号
            currentSoc: integer [可选] - 当前soc
            dcMeterCurrentPower: number [可选] - 直流电表当前电量 精确到小数点后2位
            estimateRemainingChargeTime: integer [可选] - 估算剩余充电时间 数据分辨率：1 min/位，0 min偏移量；数据范围：0~600min
            gunNo: integer [可选] - 充电枪编号（1~12）
            highVoltageAcquisitionElectricCurent: number [可选] - 高压采集电流 精确到小数点后 1位，放电时有可能为负数
            highVoltageAcquisitionVoltage: number [可选] - 高压采集电压 精确到小数点后 1位
            maximumBatteryTemp: integer [可选] - 最高蓄电池为温度 数据分辨率：1ºC/位，-50 ºC偏移量；数 据范围：-50ºC~+200ºC
            maximumTempMonitorPointNum: integer [可选] - 最高温度检测点编号 数据位1/位 数据范围1-128
            minimumBatteryTemp: integer [可选] - 最低蓄电池为温度 数据分辨率：1ºC/位，-50 ºC偏移量；数 据范围：-50ºC~+200ºC
            minimumTempMonitorPointNum: integer [可选] - 最低温度检测点编号 数据位1/位 数据范围1-128
            moduleAirInletTemp: integer [可选] - 模块进风口温 精度1℃
            moduleAirOutletTemp: integer [可选] - 模块出风口温 精度1℃
            position: integer [可选] - 仓位号
            reserve: integer [可选] - 预留
            singleBatteryMaximumVoltage: number [可选] - 单体电池最高电压 数据分辨率：0.01V/位，0V偏移量；数据 范围 0.00 V~24.00V
            singleBatteryMinimumVoltage: number [可选] - 单体电池最低 电压 数据分辨率：0.01V/位，0V偏移量；数据 范围 0.00 V~24.00V
            vehicleConnectState: integer [可选] - 车辆连接状态（CC1状态）0：未连接 1：真包已连接 （检测到1K）2：假包已连接 （检测到5K）
            vin: string [可选] - 车辆VIN码
        """
        path = f'/api/v2/dcciMock/feign/sendGunRm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendGunRs(data):
        """
        充电枪遥信数据上报(周期1s)
        请求参数:
            acContactorState: integer [可选] - 充电桩交流接触器状态 00H：分断 01H：吸合
            acInputAdhesionFault: integer [可选] - 充电桩交流输入接触器粘连故障(预留位置供其他适用) 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            acInputMoveMistakeFault: integer [可选] - 充电桩交流输入接触器据动/误动故(预留位置供其他适用) 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            auxiliaryPowerFault: integer [可选] - 辅助电源故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            batteryPackAuxiliaryPowerState: integer [可选] - 电池包辅助电源状态 0：辅助电源未给电池包供电 1：辅助电源正在给电池包供电
            batteryPolarityReverseFault: integer [可选] - 电池极性反接 故障 该数据项为“故障”时，“总故障”置为“故障”状态。无法判定该故障为设备自身硬件原因造成的故障时，在充电停止完成后恢复正常。00H：正常 01H：故障
            bmsCommunicationFault: integer [可选] - BMS通信故障 该数据项为“故障”时，“总故障”置为“故障”状态。无法判定该故障为设备自身硬件原因造成的故障时，在充电停止完成后恢复正常。 00H：正常 01H：故障
            chargeConnectElectromagneticLockFault: integer [可选] - 充电接口电磁锁故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            chargeGunNotInPlaceWarn: integer [可选] - 充电枪未归位 告警 该数据项为“告警”时，“总告警”置为“告警”状态。00H：正常 01H：告警
            chargeGunOverTempWarn: integer [可选] - 充电枪过温告警 该数据项为“故障”时，“总告警”置为“告警”状态。 00H：正常 01H：故障
            chargePortElectronicLockState: integer [可选] - 充电接口电子 锁状态 00H：解锁 01H：锁止
            chargePortOverTempFault: integer [可选] - 充电接口过温 故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            chargerNo: integer [可选] - 充电机编号
            chargingVehicleControlFault: integer [可选] - 充电中车辆控制导引故障 该数据项为“故障”时，“总故障”置为“故障”状态。无法判定该故障为设备自身硬件原因造成的故障时，在充电停止完成后恢复正常。00H：正常 01H：故障
            dcBusNegativeOutputFuseFault: integer [可选] - 直流母线负级输出 熔断器故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            dcBusNegativeOutputMoveMistakeFault: integer [可选] - 直流母线负极输出 接触器拒动/误动故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            dcBusOutputOverCurrentFault: integer [可选] - 直流母线输出过流故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            dcBusOutputOverVoltageFault: integer [可选] - 直流母线输出过压故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            dcBusOutputUnderVoltageFault: integer [可选] - 直流母线输出欠压故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            dcBusPositiveOutputFuseFault: integer [可选] - 直流母线正级输出 熔断器故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            dcBusPositiveOutputMoveMistakeFault: integer [可选] - 直流母线正极输出 接触器拒动/误动故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            dischargeCircuitFault: integer [可选] - 泄放回路故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            electricMeterCommunicationFault: integer [可选] - 电表通信异常 该数据项为“故障”时，“总告警”置为“告警”状态。00H：正常 01H：故障
            electricMeterDegreeFault: integer [可选] - 电表电度异常 该数据项为“故障”时，“总告警”置为“告警”状态。 00H：正常 01H：故障
            fault: integer [可选] - 总故障
            gunNo: integer [可选] - 充电枪编号（1~12）
            insulationMonitorFault: integer [可选] - 绝缘监测故障 该数据项为“故障”时，“总故障”置为“故障”状态。无法判定该故障为设备自身硬件原因造成的故障时，在充电停止完成后恢复正常。00H：正常 01H：故障
            insulationMonitorWarn: integer [可选] - 绝缘监测告警 该数据项为“告警”时，“总告警”置为“告警”状态。无法判定该故障为设备自身硬件原因造成的告警时，在充电停止完成后恢复正常。00H：正常 01H：告警
            keyonState: integer [可选] - KEYON状态 00H：电源断开 01H：电源导通
            moduleOutputConnectReversely: integer [可选] - 模块输出反接 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            moduleStatusOne: string [可选] - * 36.模块状态
     * 1：模块关机 0：模块运行
     * 1:模块故障 0模块正常
     * 1：模块恒流 0：模块恒压
     * 1：风扇故障 0：风扇正常
     * 1：输入过压 0：输入正常
     * 1：输入欠压 0：输入正常
     * 1：输出过压 0：输出正常
     * 1：输出欠压 0：输出正常
            moduleStatusTwo: string [可选] - * 37.模块状态
     * 1:过流保护 0正常
     * 1过温保护 0正常
     * 1设置关机 0设置开机
            negativeDcOutputContactorAdhesionFault: integer [可选] - 负极直流输出接触器粘连故故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            negativeDcOutputContactorState: integer [可选] - 负极直流输出接触器状态 00H：分断 01H：闭合
            position: integer [可选] - 仓位号
            positiveDcOutputContactorAdhesionFault: integer [可选] - 正极直流输出接触器粘连故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            positiveDcOutputContactorState: integer [可选] - 正极直流输出接触器状态 00H：分断 01H：闭合
            reserve: integer [可选] - 预留
            warn: integer [可选] - 总告警
            workMode: integer [可选] -      * 1.工作状态 站内单条充电机回路上的工作状态。对于站外终端，此字段暂无意义。
     * 00H：待机
     * 01H：站内工作(模块用于站内充电)
     * 02H：站外工作(模块用于站外充电)
     * 03H：工作完成(充电完成进入工作完成状态后，连续发完五帧工作完成状态，要回到待机状态)
     * 04H：站内充/放电暂停
     * 05H：站外充/放电暂停
     * 0FH：故障
        """
        path = f'/api/v2/dcciMock/feign/sendGunRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendHeartBeat(data):
        """
        充电设备心跳上报(周期10s)
        请求参数:
            beatCount: integer [可选] - 心跳计数，范围:1-0xFF
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reserve: integer [可选] - 桩状态  固定 0xFF 255
        """
        path = f'/api/v2/dcciMock/feign/sendHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendKeyonCallback(data):
        """
        充电设备应答KEYON控制(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因 0:成功 1：电池包/或者充电枪未连接 2：正在充电中 0xFF：其他
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0: 成功 1：失败
        """
        path = f'/api/v2/dcciMock/feign/sendKeyonCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendPeak(data):
        """
        充电设备上送尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            timesEightPeakIdentify: integer [可选] - 时段8尖峰标识
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            timesFivePeakIdentify: integer [可选] - 时段5尖峰标识
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            timesFourPeakIdentify: integer [可选] - 时段4尖峰标识
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            timesNum: integer [可选] - 时段个数
            timesOnePeakIdentify: integer [可选] - 时段1尖峰标识
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            timesSevenPeakIdentify: integer [可选] - 时段7尖峰标识
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            timesSixPeakIdentify: integer [可选] - 时段6尖峰标识
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            timesThreePeakIdentify: integer [可选] - 时段3尖峰标识
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            timesTwoPeakIdentify: integer [可选] - 时段2尖峰标识
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
        """
        path = f'/api/v2/dcciMock/feign/sendPeak'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendPeakCallback(data):
        """
        充电机响应尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0成功 1失败
        """
        path = f'/api/v2/dcciMock/feign/sendPeakCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendStartChargeCallback(data):
        """
        充电机响应远程启动(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 启动结果 0 成功 1 失败
        """
        path = f'/api/v2/dcciMock/feign/sendStartChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendStartChargeReport(data):
        """
        充电机上送充电启动完成帧(一次)
        请求参数:
            batteryType: integer [可选] - 电池类型 0x01:铅酸电池；0x02:镍氢电池；0x03:磷酸铁锂电池；0x04:锰酸锂电池；0x05:钴酸锂电池；0x06:三元材料电池；0x07:聚合物锂电池；0x08:钛酸锂电池；0xFF:其他电池
            bmsToChargeVersion: string [可选] - BMS与充电桩通信协议版本号
            chargerNo: integer [可选] - 充电机编号
            currentVoltage: number [可选] - 整车动力蓄电池当前电压 数据分辨率：0.1 V/位；0V 偏移
            failReason: integer [可选] - 失败原因 参考附录二充电启动完成帧失败原因(直流)
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            maxAllowElectricity: number [可选] - 最高允许充电电流 数据分辨率： 0.1 A /位；-400A 偏移； 数据范围：-400.0A~0.0A
            maxAllowTemp: integer [可选] - 最高允许温度 数据分辨率： 1ºC/位，-50 ºC 偏移量；数据范围：-50ºC~+200 ºC
            maxBMSAllowVoltage: number [可选] - BMS最高允许充电电压 数据分辨率： 0.1 V /位，0V 偏移量
            maxOutputElectric: number [可选] - 充电机最大输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            maxOutputVoltage: number [可选] - 充电机最高输出电压 数据分辨率:0.1 V/位；0V 偏移
            maxSingleAllowVoltage: number [可选] - 单体最高允许充电电压 数据分辨率：0.01 V/位，0 V 偏移量； 数据范围：0~24 V
            minOutputElectric: number [可选] - 充电机最小输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            minOutputVoltage: number [可选] - 充电机最低输出电压 数据分辨率:0.1 V/位；0V 偏移
            nominalEnergy: number [可选] - 整车动力蓄电池标称能量 数据分辨率：0.1 kWh/位，0 kWh 偏移量；数据范围：0~1000 kWh
            position: integer [可选] - 仓位号
            ratedCapacity: number [可选] - 整车动力蓄电池额定容量 0.1 Ah /位，0 Ah 偏移量
            result: integer [可选] - 成功标识 0x00:成功；0x01失败
            shakeHandResult: integer [可选] - 充电桩与BMS握手结果 00H:握手成功 01H:握手失败
            soc: integer [可选] - 整车动力蓄电池荷电状态 数据分辨率：1%/位，0%偏移量；数据范围：0~100%
            totalRatedVoltage: number [可选] - 整车动力蓄电池额定总电压 数据分辨率：0.1 V/位；0V 偏移
            vehicleIdentificationCode: string [可选] - 车辆识别码 ASCII 遵循 27930 最新协议标准
        """
        path = f'/api/v2/dcciMock/feign/sendStartChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendStopChargeCallback(data):
        """
        充电机响应停止充电(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果码 成功 1 设备已停机 0xFF 其他
        """
        path = f'/api/v2/dcciMock/feign/sendStopChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_sendStopChargeReport(data):
        """
        充电机上送充电停止完成帧(一次)
        请求参数:
            batteryCellMaxVoltage: number [可选] - 动力蓄电池单体最高电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryCellMinVoltage: number [可选] - 动力蓄电池单体最低电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryMaxTemp: integer [可选] - 动力蓄电池最高温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            batteryMinTemp: integer [可选] - 动力蓄电池最低温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 停止原因
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 成功标识  0x00:正常停止；0x01:异常停止
            suspendSoc: integer [可选] - 中止荷电状态SOC(%) 数据分辨率:1%/位，0%偏移量；数据范围:0%~100%
        """
        path = f'/api/v2/dcciMock/feign/sendStopChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v2_dcciMock_feign_signIn(data):
        """
        充电机登录签到
        请求参数:
            chargeGunCounts: integer [可选] - 充电枪口数目
            chargeHardwareVersion: string [可选] - 充电控制器硬件版本号
            chargeModuleCounts: integer [可选] - 充电模块数目
            chargeSoftwareVersion: string [可选] - 充电控制器软件版本
            chargerNo: integer [可选] - 充电机编号
            currentPower: integer [可选] - 当前功率
            currentRate: number [可选] - 当前速率
            equipmentAttr: integer [可选] - 设备属性
            equipmentProducer: integer [可选] - 设备厂商编号
            externalChargingNumber: integer [可选] - 站外充电桩绑定的站内充电机编号（充电模块群）
            gunNo: integer [可选] - 充电枪编号（1~12）
            monitorGateNo: integer [可选] - 监控网关编码
            position: integer [可选] - 仓位号
            protocolVersion: string [可选] - 通讯协议版本
            ratedPower: integer [可选] - 额定功率
            shuntRange: integer [可选] - 分流器量程
            supplierCode: integer [可选] - 充电机生产商
        """
        path = f'/api/v2/dcciMock/feign/signIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_getChargerRs(data):
        """
        查看充电设备遥信数据
        """
        path = f'/api/v3/dcciMock/feign/getChargerRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_getChargerSignIn(data):
        """
        查看充电枪登录签到数据
        """
        path = f'/api/v3/dcciMock/feign/getChargerSignIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_getCurrentMagIdControlData(data):
        """
        getCurrentMagIdControlData
        请求参数:
            msgCommandId: string [可选] - 需要查询下控数据的命令ID，组合规则：0001 代表 协议的 0x00 0x01，必填
        """
        path = f'/api/v3/dcciMock/feign/getCurrentMagIdControlData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_getGunRm(data):
        """
        查看充电枪遥测数据
        """
        path = f'/api/v3/dcciMock/feign/getGunRm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_getGunRs(data):
        """
        查看充电枪遥信数据
        """
        path = f'/api/v3/dcciMock/feign/getGunRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_getHeartBeat(data):
        """
        查看充电设备心跳
        """
        path = f'/api/v3/dcciMock/feign/getHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_initData(data):
        """
        初始化充电机（充电设备心跳，充电设备遥信，充电枪遥信，充电枪遥测）
        """
        path = f'/api/v3/dcciMock/feign/initData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4525(data):
        """
        充电设备应答鉴权认证4525
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reqNo: integer [可选] - 连接序号
            result: integer [可选] - 鉴权结果
        """
        path = f'/api/v3/dcciMock/feign/send4525'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4534(data):
        """
        充电设备响应升级请求4534
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果
        """
        path = f'/api/v3/dcciMock/feign/send4534'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4535(data):
        """
        充电设备上送升级状态4535
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            downLoadFailedReason: integer [可选] - 下载失败原因
            fileUrl: string [可选] - 文件URL
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            upgradeFailedReason: integer [可选] - 升级失败原因
            upgradeStatus: integer [可选] - 升级状态
            upgradeType: integer [可选] - 升级类型
        """
        path = f'/api/v3/dcciMock/feign/send4535'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4551(data):
        """
        充电设备数据上报4551(周期1s)
        请求参数:
            acInputBreaker1Fault: integer [可选] - 充电桩交流输入断路器1故障
            acInputBreaker1Status: integer [可选] - 输入断路器1状态
            acInputBreaker2Fault: integer [可选] - 充电桩交流输入断路器2故障
            acInputBreaker2Status: integer [可选] - 输入断路器2状态
            avoltage: number [可选]
            bvoltage: number [可选]
            chargeEquipFireWarn: integer [可选] - 充放电设备消防报警 -1：不存在 0：正常 1：故障
            chargeInputVoltageOverFault: integer [可选] - 充电桩输入电压过压故障
            chargeInputVoltageUnderFault: integer [可选] - 充电桩输入电压欠压故障
            chargePileFanFault: integer [可选] - 充电桩风扇故障
            chargePileFanStatus: integer [可选] - 充电设备风扇状态
            chargePileOverTempFault: integer [可选] - 充电桩过温故障
            chargerNo: integer [可选] - 充电机编号
            cvoltage: number [可选]
            doorStatus: integer [可选] - 门禁状态
            emergencyStopStatus: integer [可选] - 急停状态
            entranceGuardFault: integer [可选] - 门禁故障
            envTemp: integer [可选] - 充电设备环境温度
            equipBreakerFault: integer [可选] - 设备断路器故障 -1：不存在 0：正常 1：故障
            equipBreakerStatus: integer [可选] - 设备断路器状态 0:断开 1：闭合 2:故障脱扣
            fault: integer [可选] - 总故障
            floodingFault: integer [可选] - 水浸故障
            floodingStatus: integer [可选] - 水浸状态
            gunNo: integer [可选] - 充电枪编号（1~12）
            lightningArresterFault: integer [可选] - 避雷器故障
            lightningArresterStatus: integer [可选] - 避雷器状态
            otherFault: integer [可选] - 其它故障
            otherWarn: integer [可选] - 其它告警
            position: integer [可选] - 仓位号
            scramButtonFault: integer [可选] - 急停按钮动作故障
            smokeDetectorFault: integer [可选] - 烟感故障
            smokeDetectorStatus: integer [可选] - 烟感状态
            syncTime: string [可选] - 同步时间 yyyy-MM-dd HH:mm:ss
            warn: integer [可选] - 总告警
            workStatus: integer [可选] - 工作状态
        """
        path = f'/api/v3/dcciMock/feign/send4551'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4552(data):
        """
        充电枪数据上报4552(周期1s)
        请求参数:
            acContactorState: integer [可选] - 充电桩交流接触器状态
            acContactorState2: integer [可选] - 充电桩交流接触器2状态
            auxiliaryPowerFault: integer [可选] - 辅助电源故障
            batteryPackAuxiliaryPowerState: integer [可选] - 电池包辅助电源状态
            batteryPolarityReverseFault: integer [可选] - 电池极性反接故障
            bmsChargingElectricity: number [可选] - BMS充电电流测量值
            bmsChargingVoltage: number [可选] - BMS充电电压测量值
            bmsCommunicationFault: integer [可选] - BMS通信故障
            bmsDemandCurrent: number [可选] - BMS需求电流
            bmsDemandVoltage: number [可选] - BMS需求电压
            cc1State: integer [可选] - 电池连接状态
            ccuPduFault: integer [可选] - CCU-PDU通讯故障
            chargeConnectElectromagneticLockFault: integer [可选] - 充电接口电磁锁故障
            chargeGuideVoltage: number [可选] - 充电导引电压
            chargeGunNotInPlaceWarn: integer [可选] - 充电枪未归位
            chargeGunOverTempFault: integer [可选] - 充电枪过温故障
            chargeModel: integer [可选] - 充电模式
            chargePortOverTempFault: integer [可选] - 充电接口过温
            chargeStatus: integer [可选] - 充电状态
            chargerNo: integer [可选] - 充电机编号
            chargingVehicleControlFault: integer [可选] - 充电中车辆控制导引故障
            circuitDcBusNegativeOutputFuseStatus: integer [可选] - 电池回路直流母线负极输出熔断器状态
            circuitDcBusPositiveOutputFuseStatus: integer [可选] - 电池回路直流母线正极输出熔断状态
            cumulativeChargingTime: integer [可选] - 本次累计充电时间
            currentChargePower: number [可选] - 当前充电功率
            currentSoc: number [可选] - 当前SOC
            currentVoltageVehiclePowerBattery: number [可选] - 整车动力蓄电池当前电压
            dc1Temp: integer [可选] - 充电接口温度 探头1温度(接1DC+
            dc2Temp: integer [可选] - 充电接口温度 探头2温度(接1DC+
            dc3Temp: integer [可选] - 充电接口温度 探头3温度(接1DC+) 
            dc4Temp: integer [可选] - 充电接口温度 探头4温度(接1DC+)
            dcBusNegativeOutputFuseFault: integer [可选] - 电池回路直流母线负级输出熔断器故障
            dcBusNegativeOutputMoveMistakeFault: integer [可选] - 电池回路负极极直流输出接触器粘连/拒动/误动故障
            dcBusNegativeStatus: integer [可选] - 电池回路负极直流输出接触器状态
            dcBusOutputOverCurrentFault: integer [可选] - 直流母线输出过流故障
            dcBusOutputOverVoltageFault: integer [可选] - 直流母线输出过压故障
            dcBusOutputUnderVoltageFault: integer [可选] - 直流母线输出欠压故障
            dcBusPositiveOutputFuseFault: integer [可选] - 电池回路直流母线正级输出熔断器故障
            dcBusPositiveOutputMoveMistakeFault: integer [可选] - 电池回路正极直流输出接触器粘连/拒动/误动故障
            dcBusPositiveStatus: integer [可选] - 电池回路正极直流输出接触器状态
            dcContactorInternalVoltage: number [可选] - 直流接触器内侧电压
            dcContactorOutVoltage: number [可选] - 直流接触器外侧电压
            dischargeCircuitFault: integer [可选] - 泄放回路故障
            electricMeterCommunicationFault: integer [可选] - 电表通信异常
            electricMeterDcCurrent: number [可选] - 电表直流电表电流
            electricMeterDcElectricity: number [可选] - 直流电表总电量
            electricMeterDcVoltage: number [可选] - 电表直流电表电压
            electricMeterDegreeFault: integer [可选] - 电表电度异常
            electronicLockState: integer [可选] - 充电接口电子锁状态
            exchangeInputAdhesionFault1: integer [可选] - 充电桩交流输入接触器1粘连故障
            exchangeInputAdhesionFault2: integer [可选] - 充电桩交流输入接触器2粘连故障
            exchangeInputMoveMistakeFault1: integer [可选] - 充电桩交流输入接触器1拒动/误动故障
            exchangeInputMoveMistakeFault2: integer [可选] - 充电桩交流输入接触器2拒动/误动故障
            fault: integer [可选] - 总故障
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            insulationMonitorFault: integer [可选] - 绝缘监测故障
            insulationMonitorWarn: integer [可选] - 绝缘监测告警
            insulationResistance: number [可选] - 绝缘电阻
            keyonState: integer [可选] - KEYON状态
            maxAllowElectricity: number [可选] - 最高允许充电电流
            maxAllowableTemp: number [可选] - 最高允许温度
            maxAllowableTotalChargingVoltage: number [可选] - 最高允许充电总电压
            maxBatteryTemp: integer [可选] - 最高蓄电池温度
            maxSingleAllowVoltage: number [可选] - 单体最高允许充电电压
            maxSinglecellVoltage: number [可选] - 最高单体电池电压
            maxTempDetectionPointNumber: integer [可选] - 最高温度检测点编号
            minBatteryTemp: integer [可选] - 最低蓄电池温度
            minTempDetectionPointNumber: integer [可选] - 最低温度检测点编号
            module1AirOutletTemp: integer [可选] - 模块1出风口温度
            module1CommunicationFault: integer [可选] - 模块1 1：模块通信故障 0：模块通信正常
            module1FanFault: integer [可选] - 模块1 1：风扇故障 0：风扇正常
            module1InletTemp: integer [可选] - 模块1进风口温度
            module1InputOverVoltage: integer [可选] - 模块1 1：输入过压 0：输入正常
            module1InputUnderVoltage: integer [可选] - 模块1 1：输入欠压 0：输入正常
            module1OtherFault: integer [可选] - 模块1 1：其它故障 0：无其他故障该数据项不为0时，“总故障”置为“故障”状态。
            module1OutCurrent: number [可选] - 模块1输出电流
            module1OutPower: number [可选] - 模块1输出电流
            module1OutVoltage: number [可选] - 模块1输出电压
            module1OutputOverCurrent: integer [可选] - 模块1 1：输出过流 0：输出正常
            module1OutputOverVoltage: integer [可选] - 模块1 1：输出过压 0：输出正常
            module1OverTemperatureProtection: integer [可选] - 模块1 1：过温保护 0：温度正常
            module1WorkStatus: integer [可选] - 模块1站内外工作状态
            module2AirOutletTemp: integer [可选] - 模块2出风口温度
            module2CommunicationFault: integer [可选] - 模块2 1：模块通信故障 0：模块通信正常
            module2FanFault: integer [可选] - 模块2 1：风扇故障 0：风扇正常
            module2InletTemp: integer [可选] - 模块2进风口温度
            module2InputOverVoltage: integer [可选] - 模块2 1：输入过压 0：输入正常
            module2InputUnderVoltage: integer [可选] - 模块2 1：输入欠压 0：输入正常
            module2OtherFault: integer [可选] - 模块2 1：其它故障 0：无其他故障该数据项不为0时，“总故障”置为“故障”状态。
            module2OutCurrent: number [可选] - 模块2输出电流
            module2OutPower: number [可选] - 模块2输出电流
            module2OutVoltage: number [可选] - 模块2输出电压
            module2OutputOverCurrent: integer [可选] - 模块2 1：输出过流 0：输出正常
            module2OutputOverVoltage: integer [可选] - 模块2 1：输出过压 0：输出正常
            module2OverTemperatureProtection: integer [可选] - 模块2 1：过温保护 0：温度正常
            module2WorkStatus: integer [可选] - 模块2站内外工作状态
            moduleOutputConnectReverselyFault: integer [可选] - 模块输出反接故障
            negativeOutputMoveMistakeFault: integer [可选] - 终端回路负极直流输出接触器粘连/拒动/误动故障
            negativeStatus: integer [可选] - 终端回路负极直流输出接触器状态
            noModuleFault: integer [可选] - 无模块可用故障 0H：正常 1H：故障
            numberHighestSingleCellVoltage: integer [可选] - 最高单体电池电压所在编号
            otherFault: integer [可选] - 其它故障
            otherWarn: integer [可选] - 其它告警
            position: integer [可选] - 仓位号
            positiveOutputMoveMistakeFault: integer [可选] - 终端回路正极直流输出接触器粘连/拒动/误动故障
            positiveStatus: integer [可选] - 电终端回路正极直流输出接触器状态
            powerNegativeOutputMoveMistakeFault: integer [可选] - 功率分配负极接触器粘连/拒动/误动故障
            powerNegativeStatus: integer [可选] - 功率分配负极接触器状态
            powerPositiveOutputMoveMistakeFault: integer [可选] - 功率分配正极接触器粘连/拒动/误动故障
            powerPositiveStatus: integer [可选] - 功率分配正极接触器状态
            ratedCapacity: number [可选] - 整车动力蓄电池额定容量
            remainChargingTime: integer [可选] - 本次剩余充电时间
            startUpSoc: number [可选] - 启动时SOC
            tcuCcuFault: integer [可选] - TCU-CCU故障
            thisChargeAndDischargeAmount: number [可选] - 本次充放电量
            totalRatedCapacity: number [可选] - 整车动力蓄电池标称容量
            totalRatedVoltage: number [可选] - 整车动力蓄电池额定总电压
            vin: string [可选] - 车辆VIN码
            warn: integer [可选] - 总告警
        """
        path = f'/api/v3/dcciMock/feign/send4552'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4556(data):
        """
        充电设备上报设备参数
        请求参数:
            chargeDeviceOverTemperatureThreshold: number [可选] - 充电设备过温阈值
            chargerNo: integer [可选] - 充电机编号
            dcMeterAddress1: string [可选] - 电表地址1
            dcMeterAddress2: string [可选] - 电表地址2
            dcMeterAddress3: string [可选] - 电表地址3
            dcMeterAddress4: string [可选] - 电表地址4
            dcMeterBaudRate: integer [可选] - 直流电表型号
            doorQuote: integer [可选] - 门禁报警 0：关闭 1：打开
            gunNo: integer [可选] - 充电枪编号（1~12）
            inputOverVoltageThreshold: number [可选] - 输入过压阈值 V/位
            inputUnderVoltageThreshold: number [可选] - 输入欠压阈值 V/位
            limitSoc: integer [可选] - 本地SOC限制
            noEffectiveCurrentContinuouslyCharged: integer [可选] - 无有效电流可持续充电 0：关闭 1：打开
            offlineChargeTs: integer [可选] - 离线充电时间 min/位 0表示立马停止
            outOvervoltageThreshold: number [可选] - 输出过压阈值 V/位
            overcurrentFilterTs: number [可选] -  
            position: integer [可选] - 仓位号
            powerLossCompensationCoefficient: integer [可选] - 电损补偿系数
            simulatedCharged: integer [可选] - 模拟充电 0：关闭 1：打开
            singleOutputOvercurrentThreshold: number [可选] - 单路输出过流阈值 A/位
            stationChargeStrategy: integer [可选] - 站内外充放电策略
        """
        path = f'/api/v3/dcciMock/feign/send4556'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4557(data):
        """
        充电设备上报历史故障4557
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            items: array [可选] - 故障列表
                        code: integer [可选] - 故障代码
                        gunNo: integer [可选] - 充电枪编号
                        ts: string [可选] - 故障时间 yyyy-MM-dd HH:mm:ss
        """
        path = f'/api/v3/dcciMock/feign/send4557'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4559(data):
        """
        充放电设备上报充电BMS报文
        请求参数:
            canDatas: string [可选]
            canPackNum: integer [可选]
            chargerNo: integer [可选] - 充电机编号
        """
        path = f'/api/v3/dcciMock/feign/send4559'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4560(data):
        """
        充放电设备上报系统日志
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            log: string [可选]
        """
        path = f'/api/v3/dcciMock/feign/send4560'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_send4587(data):
        """
        充电设备应答复位指令(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果
        """
        path = f'/api/v3/dcciMock/feign/send4587'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendBatteryStatus(data):
        """
        充电设备上报电池连接状态
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            status: integer [可选] - 电池(CC1）连接状态
        """
        path = f'/api/v3/dcciMock/feign/sendBatteryStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendChargeAdjustParamResult(data):
        """
        充电设备应答站功率/电流调节指令结果(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因  0:默认值；1:编码成功；2:编码失败
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果  0: 成功 1：失败
        """
        path = f'/api/v3/dcciMock/feign/sendChargeAdjustParamResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendChargeEncodingResult(data):
        """
        充电设备上报电池包编码结果(一次)
        请求参数:
            batterySn: string [可选] - 电池包SN
            batterySnStatus: integer [可选] - 电池包SN状态 0：无效SN码 1：有效SN码
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 编码结果  0:默认值；1:编码成功；2:编码失败
        """
        path = f'/api/v3/dcciMock/feign/sendChargeEncodingResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendChargeRecord(data):
        """
        充电设备主动上送充电记录(一次)
        请求参数:
            cardBalanceAfterChager: number [可选] - 充电后卡余额 精确到0.01，单位是元
            cardBalanceBeforeCharge: number [可选] - 充电前卡余额 精确到0.01，单位是元
            chargeAmountOfMoney: number [可选] - 充电金额 精确到0.01，单位是元
            chargeEndTime: string [可选] - 充电结束时间
            chargePower: number [可选] - 充电电量 精确到0.01，单位是kwh
            chargeStartTime: string [可选] - 充电开始时间
            chargerNo: integer [可选] - 充电机编号
            direction: integer [可选]
            factoryStopReason: integer [可选]
            flowNo: string [可选] - 流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            newFailReason: integer [可选] - 失败原因 (新))
            oneElectricMeterAfterCharge: number [可选] - 1号枪充电后电能表数 精确到0.01，单位是kwh
            oneElectricMeterBeforeCharge: number [可选] - 1号枪充电前电能表数 精确到0.01，单位是kwh
            position: integer [可选] - 仓位号
            socAfterCharge: number [可选] - 充电后SOC
            socBeforeCharge: number [可选] - 充电前soc
            stopReason: integer [可选] - 停止原因
            stopResult: integer [可选] - 停止类型  0x00:成功；0x01失败
            totalDeepValleyCharge: number [可选] - 深谷总充电量
            totalFlatCharge: number [可选] - 平总充电量
            totalPeakCharge: number [可选] - 峰总充电量
            totalSharpCharge: number [可选] - 尖总充电量
            totalValleyCharge: number [可选] - 谷总充电量
        """
        path = f'/api/v3/dcciMock/feign/sendChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendChargerRs(data):
        """
        充电设备遥信数据上报(周期1s)
        请求参数:
            acInputBreakerFault: integer [可选] - 充电桩交流输入断路器故障 (系统供电断路器) 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            acInputCircuitBreakerStatus: integer [可选] - 交流输入断路器状态
            chargeInputVoltageOverFault: integer [可选] - 充电桩输入电压过压故障 该数据项为“故障”时，“总故障”置为“故障”状态。 00H：正常 01H：故障
            chargeInputVoltageUnderFault: integer [可选] - 充电桩输入电压欠压故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            chargePileFanWarn: integer [可选] - 充电桩风扇告警
            chargePileOverTempFault: integer [可选] - 充电桩过温故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            chargerNo: integer [可选] - 充电机编号
            entranceGuardFault: integer [可选] - 门禁故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            fault: integer [可选] - 总故障 0H：正常 1H：故障
            floodWarn: integer [可选] - 水浸告警 该数据项为“故障”时，“总故障”置为“故障”状态。 00H：正常 01H：故障
            gunNo: integer [可选] - 充电枪编号（1~12）
            lightningArresterFault: integer [可选] - 避雷器故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            otherFault: integer [可选] - 门禁故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            otherWarn: integer [可选] - 其它告警
            position: integer [可选] - 仓位号
            scramButtonFault: integer [可选] - 急停按钮动作故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            smokeDetectorFault: integer [可选] - 烟感故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            warn: integer [可选] - 总告警 0H：正常 1H：告警
            workStatus: integer [可选] - 工作状态 00H：待机。无故障且所有充电枪不在充电 01H：工作中。有充电枪在工作(包含充电中，充电暂停，充电完成) 0EH：维护。正在维护中，暂时无法使用 0FH：故障。字段2总故障为故障时，状态为故障
        """
        path = f'/api/v3/dcciMock/feign/sendChargerRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendGunRm(data):
        """
        充电枪遥测数据上报(周期1s)
        请求参数:
            batterySn: string [可选] - 电池包SN
            bmsChargeElectricCurrent: number [可选] - BMS充电电流 测量值 数据分辨率：0.1 A/位；-400A偏移；数据 范围：-400.0 A~0.0A
            bmsChargeVoltage: number [可选] - BMS充电电压 测量值 数据分辨率：0.1 V/位，0 V偏移量；数据 范围：0.0 V~950.0V
            bmsDemandElectricCurrent: number [可选] - BMS需求电流 数据分辨率：0.1 A/位；-400A偏移；数据 范围：-400.0 A~0.0A
            bmsDemandVoltage: number [可选] - BMS需求电压 数据分辨率：0.1 V/位，0 V偏移量；数据 范围：0.0 V~950.0V
            chargeElectricCurrent: number [可选] - 充电电流（直流电表电流） 精确到小数点后 1位 如果有直流电表，为直流电表电流，放电时有可能为负数
            chargeGuidanceVoltage: number [可选] - 充电导引电压 数据分辨率：0.01V/位，0V偏移量；数据 范围 0.00 V~30.00V
            chargeMode: integer [可选] - 充电模式 01H：恒压充电 02H：恒流充电 放电或其他模式填0
            chargePortProbe1Temp: integer [可选] - 充电接口温度 探头1温度(接口 1DC+) 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +200.0℃
            chargePortProbe2Temp: integer [可选] - 充电接口温度 探头2温度(接口 1DC-) 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +200.0℃
            chargePortProbe3Temp: integer [可选] - 充电接口温度 探头3温度(接口 2DC+) 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +200.0℃
            chargePortProbe4Temp: integer [可选] - 充电接口温度 探头4温度(接口 2DC+) 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +200.0℃
            chargePower: number [可选] - 当前充电功率 数据分辨率：0.1 kw/位
            chargeTime: integer [可选] - 本次充电时间 精确度分钟
            chargeVoltage: number [可选] - 充电电压（直流电表 电压） 精确到小数点后 1位 如果有直流电表，为直流电表电压
            chargerAmbientTemp: integer [可选] - 充电机环境温 度 数据分辨率：1℃/位，-50℃偏移量；数据范围：-50.0 ℃~ +90.0℃
            chargerNo: integer [可选] - 充电机编号
            currentSoc: integer [可选] - 当前soc
            dcMeterCurrentPower: number [可选] - 直流电表当前电量 精确到小数点后2位
            estimateRemainingChargeTime: integer [可选] - 估算剩余充电时间 数据分辨率：1 min/位，0 min偏移量；数据范围：0~600min
            gunNo: integer [可选] - 充电枪编号（1~12）
            highVoltageAcquisitionElectricCurent: number [可选] - 高压采集电流 精确到小数点后 1位，放电时有可能为负数
            highVoltageAcquisitionVoltage: number [可选] - 高压采集电压 精确到小数点后 1位
            maximumBatteryTemp: integer [可选] - 最高蓄电池为温度 数据分辨率：1ºC/位，-50 ºC偏移量；数 据范围：-50ºC~+200ºC
            maximumTempMonitorPointNum: integer [可选] - 最高温度检测点编号 数据位1/位 数据范围1-128
            minimumBatteryTemp: integer [可选] - 最低蓄电池为温度 数据分辨率：1ºC/位，-50 ºC偏移量；数 据范围：-50ºC~+200ºC
            minimumTempMonitorPointNum: integer [可选] - 最低温度检测点编号 数据位1/位 数据范围1-128
            moduleAirInletTemp: integer [可选] - 模块进风口温 精度1℃
            moduleAirOutletTemp: integer [可选] - 模块出风口温 精度1℃
            position: integer [可选] - 仓位号
            reserve: integer [可选] - 预留
            singleBatteryMaximumVoltage: number [可选] - 单体电池最高电压 数据分辨率：0.01V/位，0V偏移量；数据 范围 0.00 V~24.00V
            singleBatteryMinimumVoltage: number [可选] - 单体电池最低 电压 数据分辨率：0.01V/位，0V偏移量；数据 范围 0.00 V~24.00V
            vehicleConnectState: integer [可选] - 车辆连接状态（CC1状态）0：未连接 1：真包已连接 （检测到1K）2：假包已连接 （检测到5K）
            vin: string [可选] - 车辆VIN码
        """
        path = f'/api/v3/dcciMock/feign/sendGunRm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendGunRs(data):
        """
        充电枪遥信数据上报(周期1s)
        请求参数:
            acContactorState: integer [可选] - 充电桩交流接触器状态 00H：分断 01H：吸合
            acInputAdhesionFault: integer [可选] - 充电桩交流输入接触器粘连故障(预留位置供其他适用) 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            acInputMoveMistakeFault: integer [可选] - 充电桩交流输入接触器据动/误动故(预留位置供其他适用) 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            auxiliaryPowerFault: integer [可选] - 辅助电源故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            batteryPackAuxiliaryPowerState: integer [可选] - 电池包辅助电源状态 0：辅助电源未给电池包供电 1：辅助电源正在给电池包供电
            batteryPolarityReverseFault: integer [可选] - 电池极性反接 故障 该数据项为“故障”时，“总故障”置为“故障”状态。无法判定该故障为设备自身硬件原因造成的故障时，在充电停止完成后恢复正常。00H：正常 01H：故障
            bmsCommunicationFault: integer [可选] - BMS通信故障 该数据项为“故障”时，“总故障”置为“故障”状态。无法判定该故障为设备自身硬件原因造成的故障时，在充电停止完成后恢复正常。 00H：正常 01H：故障
            chargeConnectElectromagneticLockFault: integer [可选] - 充电接口电磁锁故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            chargeGunNotInPlaceWarn: integer [可选] - 充电枪未归位 告警 该数据项为“告警”时，“总告警”置为“告警”状态。00H：正常 01H：告警
            chargeGunOverTempWarn: integer [可选] - 充电枪过温告警 该数据项为“故障”时，“总告警”置为“告警”状态。 00H：正常 01H：故障
            chargePortElectronicLockState: integer [可选] - 充电接口电子 锁状态 00H：解锁 01H：锁止
            chargePortOverTempFault: integer [可选] - 充电接口过温 故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            chargeStatus: integer [可选] - 充电状态
            chargerNo: integer [可选] - 充电机编号
            chargingVehicleControlFault: integer [可选] - 充电中车辆控制导引故障 该数据项为“故障”时，“总故障”置为“故障”状态。无法判定该故障为设备自身硬件原因造成的故障时，在充电停止完成后恢复正常。00H：正常 01H：故障
            dcBusNegativeOutputFuseFault: integer [可选] - 直流母线负级输出 熔断器故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            dcBusNegativeOutputMoveMistakeFault: integer [可选] - 直流母线负极输出 接触器拒动/误动故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            dcBusOutputOverCurrentFault: integer [可选] - 直流母线输出过流故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            dcBusOutputOverVoltageFault: integer [可选] - 直流母线输出过压故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            dcBusOutputUnderVoltageFault: integer [可选] - 直流母线输出欠压故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            dcBusPositiveOutputFuseFault: integer [可选] - 直流母线正级输出 熔断器故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            dcBusPositiveOutputMoveMistakeFault: integer [可选] - 直流母线正极输出 接触器拒动/误动故障 该数据项为“故障”时，“总故障”置为“故障”状态。 0H：正常 1H：故障
            dischargeCircuitFault: integer [可选] - 泄放回路故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            electricMeterCommunicationFault: integer [可选] - 电表通信异常 该数据项为“故障”时，“总告警”置为“告警”状态。00H：正常 01H：故障
            electricMeterDegreeFault: integer [可选] - 电表电度异常 该数据项为“故障”时，“总告警”置为“告警”状态。 00H：正常 01H：故障
            fault: integer [可选] - 总故障
            gunNo: integer [可选] - 充电枪编号（1~12）
            insulationMonitorFault: integer [可选] - 绝缘监测故障 该数据项为“故障”时，“总故障”置为“故障”状态。无法判定该故障为设备自身硬件原因造成的故障时，在充电停止完成后恢复正常。00H：正常 01H：故障
            insulationMonitorWarn: integer [可选] - 绝缘监测告警 该数据项为“告警”时，“总告警”置为“告警”状态。无法判定该故障为设备自身硬件原因造成的告警时，在充电停止完成后恢复正常。00H：正常 01H：告警
            keyonState: integer [可选] - KEYON状态 00H：电源断开 01H：电源导通
            moduleOutputConnectReversely: integer [可选] - 模块输出反接 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            moduleStatusOne: string [可选] - 模块1状态
            moduleStatusTwo: string [可选] - 模块2状态
            negativeDcOutputContactorAdhesionFault: integer [可选] - 负极直流输出接触器粘连故故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            negativeDcOutputContactorState: integer [可选] - 负极直流输出接触器状态 00H：分断 01H：闭合
            otheWarn: integer [可选] - 其它告警
            otherFault: integer [可选] - 其它故障
            position: integer [可选] - 仓位号
            positiveDcOutputContactorAdhesionFault: integer [可选] - 正极直流输出接触器粘连故障 该数据项为“故障”时，“总故障”置为“故障”状态。00H：正常 01H：故障
            positiveDcOutputContactorState: integer [可选] - 正极直流输出接触器状态 00H：分断 01H：闭合
            reserve: integer [可选] - 预留
            warn: integer [可选] - 总告警
            workMode: integer [可选] -      * 1.工作状态 站内单条充电机回路上的工作状态。对于站外终端，此字段暂无意义。
     * 00H：待机
     * 01H：站内工作(模块用于站内充电)
     * 02H：站外工作(模块用于站外充电)
     * 03H：工作完成(充电完成进入工作完成状态后，连续发完五帧工作完成状态，要回到待机状态)
     * 04H：站内充/放电暂停
     * 05H：站外充/放电暂停
     * 0FH：故障
        """
        path = f'/api/v3/dcciMock/feign/sendGunRs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendHeartBeat(data):
        """
        充电设备心跳上报(周期10s)
        请求参数:
            beatCount: integer [可选] - 心跳计数，范围:1-0xFF
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reserve: integer [可选] - 桩状态  固定 0xFF 255
        """
        path = f'/api/v3/dcciMock/feign/sendHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendKeyonCallback(data):
        """
        充电设备应答KEYON控制(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因 0:成功 1：电池包/或者充电枪未连接 2：正在充电中 0xFF：其他
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0: 成功 1：失败
        """
        path = f'/api/v3/dcciMock/feign/sendKeyonCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendPeak(data):
        """
        充电设备上送尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            times: array [可选] - 时段
                        periodType: integer [可选] - 时段尖峰标识
                        startTime: string [可选] - 时段开始时间
        """
        path = f'/api/v3/dcciMock/feign/sendPeak'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendPeakCallback(data):
        """
        充电机响应尖峰评估设置(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果 0成功 1失败
        """
        path = f'/api/v3/dcciMock/feign/sendPeakCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendStartChargeCallback(data):
        """
        充电机响应远程启动(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 启动结果 0 成功 1 失败
        """
        path = f'/api/v3/dcciMock/feign/sendStartChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendStartChargeReport(data):
        """
        充电机上送充电启动完成帧(一次)
        请求参数:
            batteryType: integer [可选] - 电池类型 0x01:铅酸电池；0x02:镍氢电池；0x03:磷酸铁锂电池；0x04:锰酸锂电池；0x05:钴酸锂电池；0x06:三元材料电池；0x07:聚合物锂电池；0x08:钛酸锂电池；0xFF:其他电池
            bmsToChargeVersion: string [可选] - BMS与充电桩通信协议版本号
            chargerNo: integer [可选] - 充电机编号
            currentVoltage: number [可选] - 整车动力蓄电池当前电压 数据分辨率：0.1 V/位；0V 偏移
            failReason: integer [可选] - 失败原因 参考附录二充电启动完成帧失败原因(直流)
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            maxAllowElectric: number [可选] - 最高允许放电电量
            maxAllowElectricity: number [可选] - 最高允许充电电流 数据分辨率： 0.1 A /位；-400A 偏移； 数据范围：-400.0A~0.0A
            maxAllowTemp: integer [可选] - 最高允许温度 数据分辨率： 1ºC/位，-50 ºC 偏移量；数据范围：-50ºC~+200 ºC
            maxBMSAllowVoltage: number [可选] - BMS最高允许充电电压 数据分辨率： 0.1 V /位，0V 偏移量
            maxOutputElectric: number [可选] - 充电机最大输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            maxOutputVoltage: number [可选] - 充电机最高输出电压 数据分辨率:0.1 V/位；0V 偏移
            maxSingleAllowVoltage: number [可选] - 单体最高允许充电电压 数据分辨率：0.01 V/位，0 V 偏移量； 数据范围：0~24 V
            minAllowChargeStatus: integer [可选] - 最低允许动力蓄电池荷电状态
            minAllowElectric: number [可选] - 最低允许放电电量
            minAllowSinglelVoltage: number [可选] - 最低允许单体电池电压
            minOutputElectric: number [可选] - 充电机最小输出电流 数据分辨率:0.1 A/位；-400A 偏移数据范围:-400.0A~0.0A
            minOutputVoltage: number [可选] - 充电机最低输出电压 数据分辨率:0.1 V/位；0V 偏移
            newFailReason: integer [可选] - 失败原因 (新))
            nominalEnergy: number [可选] - 整车动力蓄电池标称能量 数据分辨率：0.1 kWh/位，0 kWh 偏移量；数据范围：0~1000 kWh
            position: integer [可选] - 仓位号
            ratedCapacity: number [可选] - 整车动力蓄电池额定容量 0.1 Ah /位，0 Ah 偏移量
            result: integer [可选] - 成功标识 0x00:成功；0x01失败
            shakeHandResult: integer [可选] - 充电桩与BMS握手结果 00H:握手成功 01H:握手失败
            soc: integer [可选] - 整车动力蓄电池荷电状态 数据分辨率：1%/位，0%偏移量；数据范围：0~100%
            totalRatedVoltage: number [可选] - 整车动力蓄电池额定总电压 数据分辨率：0.1 V/位；0V 偏移
            vehicleIdentificationCode: string [可选] - 车辆识别码 ASCII 遵循 27930 最新协议标准
        """
        path = f'/api/v3/dcciMock/feign/sendStartChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendStopChargeCallback(data):
        """
        充电机响应停止充电(一次)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 结果码 成功 1 设备已停机 0xFF 其他
        """
        path = f'/api/v3/dcciMock/feign/sendStopChargeCallback'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendStopChargeReport(data):
        """
        充电机上送充电停止完成帧(一次)
        请求参数:
            batteryCellMaxVoltage: number [可选] - 动力蓄电池单体最高电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryCellMinVoltage: number [可选] - 动力蓄电池单体最低电压(V) 数据分辨率:0.01 V/位，0 V 偏移量；数据范围:0 V~24 V
            batteryMaxTemp: integer [可选] - 动力蓄电池最高温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            batteryMinTemp: integer [可选] - 动力蓄电池最低温度(ºC) 数据分辨率:1ºC/位，-50ºC 偏移量；数据范围:-50 ºC~+200 ºC
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 停止原因
            flowNo: string [可选] - 充电机交互流水号
            gunNo: integer [可选] - 充电枪编号（1~12）
            newFailReason: integer [可选] - 失败原因 (新))
            position: integer [可选] - 仓位号
            result: integer [可选] - 成功标识  0x00:正常停止；0x01:异常停止
            suspendSoc: number [可选] - 中止荷电状态SOC(%) 数据分辨率:1%/位，0%偏移量；数据范围:0%~100%
        """
        path = f'/api/v3/dcciMock/feign/sendStopChargeReport'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_sendVersion(data):
        """
        充电设备版本号
        请求参数:
            ccuVersion: string [可选] - ccu版本数组
            chargerNo: integer [可选] - 充电机编号
            communicationProtocolVersion: string [可选] - tcu通讯协议版本号
            emuCommunicationProtocolVersion: string [可选] - emu通讯协议版本号
            emuSoftwareVersion: string [可选] - emu软件版本号
            emuhardwareVersion: string [可选] - emu硬件版本号
            gunNo: integer [可选] - 充电枪编号（1~12）
            hardwareVersion: string [可选] - tcu硬件版本号
            pduCommunicationProtocolVersion: string [可选] - pdu通讯协议版本号
            pduSoftwareVersion: string [可选] - pdu软件版本号
            pduhardwareVersion: string [可选] - pdu硬件版本号
            position: integer [可选] - 仓位号
            softwareVersion: string [可选] - tcu软件版本号
        """
        path = f'/api/v3/dcciMock/feign/sendVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_v3_dcciMock_feign_signIn(data):
        """
        充电机登录签到
        请求参数:
            ccuNum: integer [可选] - ccu数量
            chargeGunCounts: integer [可选] - 充电枪口数目
            chargeHardwareVersion: string [可选] - 充电控制器硬件版本号
            chargeModuleCounts: integer [可选] - 充电模块数目
            chargeSoftwareVersion: string [可选] - 充电控制器软件版本
            chargerNo: integer [可选] - 充电机编号
            circuitBreakerNum: integer [可选] - 断路器数目
            code: string [可选] - 充电设备编码
            deviceModel: string [可选] - 充电设备型号
            equipmentAttr: integer [可选] - 设备属性
            equipmentProducer: integer [可选] - 设备厂商编号
            externalChargingNumber: integer [可选] - 站外充电桩绑定的站内充电机编号（充电模块群）
            gunNo: integer [可选] - 充电枪编号（1~12）
            maxChargeCurrent: number [可选] - 最大充电电流
            maxChargeVoltage: number [可选] - 最大充电电压
            maxCurrent: number [可选] - 最大输出电流
            maxDischargeCurrent: number [可选] - 最大放电电流
            maxDischargeVoltage: number [可选] - 最大放电电压
            maxVoltage: number [可选] - 最大输出电压
            minChargeCurrent: number [可选] - 最小充电电流
            minChargeVoltage: number [可选] - 最小充电电压
            minDischargeCurrent: number [可选] - 最小放电电流
            minDischargeVoltage: number [可选] - 最小放电电压
            monitorGateNo: integer [可选] - 监控网关编码
            position: integer [可选] - 仓位号
            power: integer [可选] - 当前功率
            protocolVersion: string [可选] - 通讯协议版本
            ratedPower: integer [可选] - 额定功率
            shuntRange: integer [可选] - 分流器量程
            sn: string [可选] - 充电设备出厂序列号
            superchargeSupport: integer [可选] - 超充支持
            supplierCode: integer [可选] - 充电机生产商
        """
        path = f'/api/v3/dcciMock/feign/signIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))
