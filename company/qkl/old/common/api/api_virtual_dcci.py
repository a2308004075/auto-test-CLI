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
    def api_v10_demo_clientInfos(data):
        """
        clientInfos
        """
        path = f'/api/v1.0/demo/clientInfos'
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
    def api_v10_demo_sendMsg(data):
        """
        sendMsg
        请求参数:
        """
        path = f'/api/v1.0/demo/sendMsg'
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
            gunNo: integer [可选] - 充电枪编号（1~12）
            peakElectricQuantity: number [可选] - 峰电量
            position: integer [可选] - 仓位号
            reserve: integer [可选] - 预留
            socAfterCharge: integer [可选] - 充电后SOC
            socBeforeCharge: integer [可选] - 充电前soc
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
            btoCVersion: string [可选]
            chargerNo: integer [可选] - 充电机编号
            currentVoltage: number [可选] - 整车动力蓄电池当前电压 数据分辨率：0.1 V/位；0V 偏移
            failReason: integer [可选] - 失败原因
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
            failReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            reserve21: string [可选] - BMS检测到的其他错误
            reserve33: integer [可选] - 充电机检测到的其他错误
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
            fieldsComputed: integer [可选]
            fieldsNormalized: integer [可选]
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            zoneShared: boolean [可选]
            timesFivePeakIdentify: integer [可选] - 时段5尖峰标识
            fieldsComputed: integer [可选]
            fieldsNormalized: integer [可选]
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            zoneShared: boolean [可选]
            timesFourPeakIdentify: integer [可选] - 时段4尖峰标识
            fieldsComputed: integer [可选]
            fieldsNormalized: integer [可选]
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            zoneShared: boolean [可选]
            timesNum: integer [可选] - 时段个数
            timesOnePeakIdentify: integer [可选] - 时段1尖峰标识
            fieldsComputed: integer [可选]
            fieldsNormalized: integer [可选]
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            zoneShared: boolean [可选]
            timesSevenPeakIdentify: integer [可选] - 时段7尖峰标识
            fieldsComputed: integer [可选]
            fieldsNormalized: integer [可选]
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            zoneShared: boolean [可选]
            timesSixPeakIdentify: integer [可选] - 时段6尖峰标识
            fieldsComputed: integer [可选]
            fieldsNormalized: integer [可选]
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            zoneShared: boolean [可选]
            timesThreePeakIdentify: integer [可选] - 时段3尖峰标识
            fieldsComputed: integer [可选]
            fieldsNormalized: integer [可选]
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            zoneShared: boolean [可选]
            timesTwoPeakIdentify: integer [可选] - 时段2尖峰标识
            fieldsComputed: integer [可选]
            fieldsNormalized: integer [可选]
            firstDayOfWeek: integer [可选]
            lenient: boolean [可选]
            minimalDaysInFirstWeek: integer [可选]
            time: string [可选]
            timeInMillis: integer [可选]
            id: string [可选]
            rawOffset: integer [可选]
            zoneShared: boolean [可选]
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
            reserve1: integer [可选] - 预留1 固定0x00
            reserve2: integer [可选] - 预留2 固定0x00
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
        """
        path = f'/api/v2/dcciMock/feign/signIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualDcci._get_path(path), 'POST', data))
