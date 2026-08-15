from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiVirtualCarStation:
    @staticmethod
    def _get_path(path):
        service = '/virtual-car-station'
        return service + path

    @staticmethod
    def api_virtualCarStation_feign_carStationInfo_blueToothInfo(data):
        """
        发送蓝牙连接信息
        请求参数:
            bluetoothScanStatus: integer [可选] - 蓝牙扫描状态 空闲：0   Rap连接扫描中：1   Rap重连扫描中:2   搜索扫描中:3
            connectedStatus: integer [可选] - SBLE和VBLE蓝牙连接状态：0-未连接，1-已连接
            signalStrengthOfS2V: integer [可选] - 未连接：0.0dbm 已连接：-128dbm ~ -1dbm
            signalStrengthOfV2S: integer [可选] - 未连接：0.0dbm 已连接：-128dbm ~ -1dbm
        """
        path = f'/api/virtualCarStation/feign/carStationInfo/blueToothInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_carStationInfo_carFreedomStatusInfo(data):
        """
        发送车辆自由度信息
        请求参数:
            carDoorStatus: integer [可选] - 车辆车门状态：1-车门全部关闭，2-车门未全部关闭
            footBrakeStatus: integer [可选] - 车辆刹车踏板状态：1-未制动，2-制动
            gearStatus: integer [可选] - 车辆档位状态:1-N档，2-非N档
            handBrakeStatus: integer [可选] - 车辆手刹/电子手刹状态：1-未制动，2-制动
            highVoltageStatusOf1BP: integer [可选] - 1号电池包高压状态：0-高压断开，7、18-高压闭合
            highVoltageStatusOf2BP: integer [可选] - 2号电池包高压状态：0-高压断开，7、18-高压闭合
            highVoltageStatusOfBS: integer [可选] - 电池系统高压状态：0-高压断开，1-高压闭合
            lowVoltageOfBS: integer [可选] - 电池系统低压输入电压 (KL30)：0~65534
            m2VAutoholdSts: integer [可选] - 自动驻车状态
            m2VBonnetSts: integer [可选] - 引擎盖状态
            m2VDoorSignal: integer [可选] - 判断门的区分（兼容）
            m2VDoorStsFL: integer [可选] - 左前门状态
            m2VDoorStsFR: integer [可选] - 右前门状态
            m2VDoorStsRL: integer [可选] - 左后门状态
            m2VDoorStsRR: integer [可选] - 右后门状态
            m2VMBMUPowerVoltage: integer [可选] - KL30电压
            m2VTrunkSts: integer [可选] - 后备箱状态
            steeringTurnAngle: number [可选] - 车辆方向盘转向角角度：0.0~6553.4
        """
        path = f'/api/virtualCarStation/feign/carStationInfo/carFreedomStatusInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_carStationInfo_carInfo(data):
        """
        发送车辆信息
        请求参数:
            accellRatedCapacityAh: number [可选]
            accellRatedCapacityAhOfPackage1: number [可选]
            actualSocOfPackage1: number [可选] - 1号电池可用荷电状态（真实）
            actualSocOfPackage2: number [可选] - 2号电池可用荷电状态（真实）
            bmstotalMilKm: number [可选]
            cellTypeOfPackage1: integer [可选] - 1号位电池包额定容量类别
            cellTypeOfPackage2: integer [可选] - 2号位电池包额定容量类别
            displayingSocOfPackage1: number [可选] - 1号电池可用荷电状态（表显）
            displayingSocOfPackage2: number [可选] - 2号电池可用荷电状态（表显）
            errorCodeOfBattSysList: array [可选] - 电池系统故障码
            errorCodeOfPackage1List: array [可选] - 1号电池包故障码
            errorCodeOfPackage2List: array [可选] - 2号电池包故障码
            hardVersionOfPackage1: string [可选] - 1号电池SBMU硬件版本号
            hardVersionOfPackage2: string [可选] - 2号电池SBMU硬件版本号
            hisStaOutAccumChrgerEngyOfPackage1: number [可选] - 1号累计站外插枪充电能量
            hisStaOutDisChrgEngyOfPackage1: number [可选] - 1号累计站外放电能量
            hisStaOutReChrgEngy: number [可选] - 电池包累计站外回充能量 kwh
            hvnegInterfaceTempOfPackage1: number [可选]
            hvposInterfaceTempOfPackage1: number [可选]
            mainCnctrCtrlStateOfPackage1: integer [可选] - 1号位电池包内主回路高压状态
            mbmuHardVersion: string [可选] - 车MBMU硬件版本号
            mbmuSoftVersion: string [可选] - 车MBMU软件版本号
            packTypeOfPackage1: integer [可选] - 1号位电池包类型识别码
            ratedPackVOLTOfPackage1: number [可选] - 1号电池额定电压
            sbleHardVersion: string [可选] - 站端通讯模块蓝牙硬件版本号
            sbleMac: string [可选] - 站端蓝牙通讯模块MAC
            sbleSoftVersion: string [可选] - 站端通讯模块蓝牙软件版本号
            signalStrengthOfV2S: integer [可选] - 未连接：0.0dbm 已连接：-128dbm ~ -1dbm
            snOfPackage1: string [可选] - 1号电池Sn码
            snOfPackage2: string [可选] - 2号电池Sn码
            socUnreliableFlagOfPackage1: integer [可选] - 1号电池包SOC不可信标志位
            socUnreliableFlagOfPackage2: integer [可选] - 2号电池包SOC不可信标志位
            soeOfPackage1: number [可选] - 1号电池电量
            soeOfPackage2: number [可选] - 2号电池电量
            softVersionOfPackage1: string [可选] - 1号电池SBMU软件版本号
            softVersionOfPackage2: string [可选] - 2号电池SBMU软件版本号
            sohOfPackage1: number [可选] - 1号电池健康度
            sohOfPackage2: number [可选] - 2号电池健康度
            statusOfPackage1: integer [可选] - BMS识别的1号电池包的状态
            statusOfPackage2: integer [可选] - BMS识别的2号电池包的状态
            subtotalMileageOfPackage1: number [可选] - 1号电池小计里程
            subtotalMileageOfPackage2: number [可选] - 2号电池小计里程
            subtotalOutsideChargingTimes: integer [可选] - 电池系统小计站外充电次数
            subtotalOutsideDischargingEnergyOfPackage1: number [可选] - 1号电池包小计站外放电能量
            subtotalOutsideDischargingEnergyOfPackage2: number [可选] - 2号电池包小计站外放电能量
            subtotalOutsideGunChargingEnergyOfPackage1: number [可选] - 1号电池包小计站外插枪充电能量
            subtotalOutsideGunChargingEnergyOfPackage2: number [可选] - 2号电池包小计站外插枪充电能量
            subtotalOutsideRechargingEnergyOfPackage1: number [可选] - 1号电池包小计站外回充能量
            subtotalOutsideRechargingEnergyOfPackage2: number [可选] - 2号电池包小计站外回充能量
            supremeErrorCodeOfBattSys: integer [可选] - 电池系统最高故障等级故障码
            supremeErrorCodeOfPackage1: integer [可选] - 1号电池包最高故障等级故障码
            supremeErrorCodeOfPackage2: integer [可选] - 2号电池包最高故障等级故障码
            supremeErrorLevelOfBattSys: integer [可选] - 电池系统最高故障等级
            supremeErrorLevelOfPackage1: integer [可选] - 1号电池包最高故障等级
            supremeErrorLevelOfPackage2: integer [可选] - 2号电池包最高故障等级
            tirePRSsignal: integer [可选] - 项目报警是用胎压值还是用报警信号
            tirePrsAlarm_FL: integer [可选] - 胎压报警信号 左前轮
            tirePrsAlarm_FR: integer [可选] - 胎压报警信号 右前轮
            tirePrsAlarm_RL: integer [可选] - 胎压报警信号 左后轮
            tirePrsAlarm_RR: integer [可选] - 胎压报警信号 右后轮
            tirePrs_FL: integer [可选] - 胎压值 左前轮
            tirePrs_FR: integer [可选] - 胎压值 右前轮
            tirePrs_RL: integer [可选] - 胎压值 左后轮
            tirePrs_RR: integer [可选] - 胎压值 右后轮
            totalChargingEnergyOfPackage1: number [可选] - 1号电池包累计充电能量
            totalChargingEnergyOfPackage2: number [可选] - 2号电池包累计充电能量
            totalDischargingEnergyOfPackage1: number [可选] - 1号电池包累计放电能量
            totalDischargingEnergyOfPackage2: number [可选] - 2号电池包累计放电能量
            totalMile: number [可选] - 车总里程数
            totalMileageOfPackage1: number [可选] - 1号电池总里程
            totalMileageOfPackage2: number [可选] - 2号电池总里程
            totalOutsideGunChargingTimes: integer [可选] - 电池系统累计站外插枪充电次数
            vbleHardVersion: string [可选] - 车蓝牙通讯模块硬件版本号
            vbleMac: string [可选] - 车蓝牙通讯模块MAC
            vbleSoftVersion: string [可选] - 车蓝牙通讯模块软件版本号
            vehSpeed: number [可选] - 车速
            vin: string [可选] - 车辆vin码
        """
        path = f'/api/virtualCarStation/feign/carStationInfo/carInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_carStationInfo_fastChangeLockStatus(data):
        """
        发送1号电池包和2号电池包的快换锁状态
        请求参数:
            num1_Package1: integer [可选] - 1号电池包1号快换锁状态:0-无效状态,1-锁止状态,2-解锁状态,3-异常状态
            num1_Package2: integer [可选] - 2号电池包1号快换锁状态:0-无效状态,1-锁止状态,2-解锁状态,3-异常状态
            num2_Package1: integer [可选] - 1号电池包2号快换锁状态:0-无效状态,1-锁止状态,2-解锁状态,3-异常状态
            num2_Package2: integer [可选] - 2号电池包2号快换锁状态:0-无效状态,1-锁止状态,2-解锁状态,3-异常状态
            num3_Package1: integer [可选] - 1号电池包3号快换锁状态:0-无效状态,1-锁止状态,2-解锁状态,3-异常状态
            num3_Package2: integer [可选] - 2号电池包3号快换锁状态:0-无效状态,1-锁止状态,2-解锁状态,3-异常状态
            num4_Package1: integer [可选] - 1号电池包4号快换锁状态:0-无效状态,1-锁止状态,2-解锁状态,3-异常状态
            num4_Package2: integer [可选] - 2号电池包4号快换锁状态:0-无效状态,1-锁止状态,2-解锁状态,3-异常状态
        """
        path = f'/api/virtualCarStation/feign/carStationInfo/fastChangeLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_carStationInfo_scanBlueToothInfo(data):
        """
        发送蓝牙扫描信息
        请求参数:
            sbleMac: string [可选] - 扫描蓝牙MAC
            signalStrengthOfV2S: integer [可选] - 未连接：0.0dbm 已连接：-128dbm ~ -1dbm
        """
        path = f'/api/virtualCarStation/feign/carStationInfo/scanBlueToothInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_allAliveTask():
        """
        所有存活的任务
        """
        path = f'/api/virtualCarStation/feign/controlCommand/allAliveTask'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'GET', None))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_cancelAll(data):
        """
        取消所有模拟命令
        """
        path = f'/api/virtualCarStation/feign/controlCommand/cancelAll'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_clearSubtotalOfBS(data):
        """
        发送清除电池系统小计信息结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/controlCommand/clearSubtotalOfBS'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_clientLogin(data):
        """
        客户端请求通信登录
        请求参数:
            requestCode: integer [可选] - 默认值：全F 未请求登录：0 请求登录：1
        """
        path = f'/api/virtualCarStation/feign/controlCommand/clientLogin'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_closeAndDisableHVContactorResult(data):
        """
        发送下高压执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/controlCommand/closeAndDisableHVContactorResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_closeLVContactorResult(data):
        """
        发送下低压执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/controlCommand/closeLVContactorResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_connectCarMbmu(data):
        """
        发送蓝牙连接执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/controlCommand/connectCarMbmu'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_disConnectCarMbmuResult(data):
        """
        发送蓝牙断开执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/controlCommand/disConnectCarMbmuResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_scanBlueToothInfoResult(data):
        """
        发送蓝牙扫描执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/controlCommand/scanBlueToothInfoResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_selfCheckResult(data):
        """
        发送自检执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/controlCommand/selfCheckResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_startBeatCount(data):
        """
        启动SBLE心跳
        """
        path = f'/api/virtualCarStation/feign/controlCommand/startBeatCount'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_controlCommand_stopBeatCount(data):
        """
        停止SBLE心跳
        """
        path = f'/api/virtualCarStation/feign/controlCommand/stopBeatCount'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v1_carStationInfo_batteryCodeInfo(data):
        """
        电池mac和sn信息
        请求参数:
            macOfPackage0: string [可选] - 车机的mac(209)
            macOfPackage1: string [可选] - 电池包1的mac(209)
            macOfPackage2: string [可选] - 电池包2的mac(209)
            snOfPackage1: string [可选] - 电池包1的sn(211)
            snOfPackage2: string [可选] - 电池包2的sn(211)
        """
        path = f'/api/virtualCarStation/feign/v1/carStationInfo/batteryCodeInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v1_carStationInfo_batteryDataInfo(data):
        """
        电池数据信息
        请求参数:
            batteryLockInfoList: array [可选] - 电池包lock信息
                        batterySwapSelfCheckFailReason: integer [可选] - SBMU3换电失败原因
                        packDetailLock1Sts: integer [可选] - 电池包内第1个机械锁的状态
                        packDetailLock2Sts: integer [可选] - 电池包内第2个机械锁的状态
                        packDetailLock3Sts: integer [可选] - 电池包内第3个机械锁的状态
                        packDetailLock4Sts: integer [可选] - 电池包内第4个机械锁的状态
                        packLockSts: integer [可选] - 电池包机械锁状态（0：无效，1：lock，2：unlock，3：abnormal)
                        packPollID: integer [可选] - 电池包序号
                        pollId: integer [可选] - 电池包序号
                        wirelessSignalStrength: integer [可选] - TMU与MBMU的无线通讯信号强度
            energyInfo: array [可选] - 电池包能量信息
                        energyTotalOutput: number [可选] - 两次换电间电池包小计站外放电电量(20E)
                        hisAccumChrgEngy: number [可选] - 电池包累计充电总能量(20D)
                        hisAccumDisChrgEngy: number [可选] - 电池包累计放电总能量(20D)
                        hisStaOutAccumChrgerEngy: number [可选] - 累计换电站外插枪充电能量(210)
                        hisStaOutDisChrgEngy: number [可选] - 累计换电站外放电能量(20F)
                        hisStaOutReChrgEngy: number [可选] - 累计换电站外回充能量(210)
                        hisStaOutReChrgEngyWh: number [可选] - 两次换电间电池包小计站外回充能量(20F)
                        outStationChargingEnergy: number [可选] - 两次换电间电池包小计站外插枪充电电量(20E)
                        pollId: integer [可选] - 电池包序号
                        sbMU_RemainEnergyBeforeExc: number [可选] - 进站时电池剩余能量(SOE)(204)
                        sbMU_RemainEnergyLastExc: number [可选] - 上次出站时电池剩余能量(204)
            mileageInfo: array [可选] - 电池包里程信息
                        pollId: integer [可选] - 电池包序号
                        toatlMilKm: number [可选] - 电池包总里程信息(20C)
                        tripMilKm: number [可选] - 电池包小计换电里程信息(20C)
            socSohInfo: array [可选] - 电池包Soc和Soh信息
                        battSts6_DisplaySOH: number [可选] - 显示SOH(206)
                        displaySOC: number [可选] - 显示SOC(206)
                        pollId: integer [可选] - 电池包序号
                        realSOC: number [可选] - 真实SOC(206)
                        sbMU_DisplaySOCLastExc: number [可选] - 上次出站时显示SOC(204)
                        sbMU_RealSOCCLastExc: number [可选] - 上次出站时真实SOC(204)
        """
        path = f'/api/virtualCarStation/feign/v1/carStationInfo/batteryDataInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v1_carStationInfo_batterySignOrStateInfo(data):
        """
        电池状态和标志信息
        请求参数:
            batterySignOrStateInfo: array [可选]
                        battSts6_FaultNum: integer [可选] - 最严重故障码(206)
                        battSts6_MainNegCnctrState: integer [可选] - 电池包主负继电器状态(206)
                        battSts6_MainPosCnctrState: integer [可选] - 电池包主正继电器状态(206)
                        m2S_WLDSts: integer [可选] - 蓝牙状态信息：0:未连接，1:连接，2:异常(204)
                        mostCriticalFltLvl: integer [可选] - 电池包最高故障等级(206)
                        pollId: integer [可选] - 电池包序号
                        soCUnavailableFlg: integer [可选] - SOC不可信标志(206)
        """
        path = f'/api/virtualCarStation/feign/v1/carStationInfo/batterySignOrStateInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v1_carStationInfo_carFreedomInfo(data):
        """
        车辆自由度信息
        请求参数:
            brakeSwitchSts: integer [可选] - 制动器状态，0：松开；1:制动，站控识别为为0时可以换电(201)
            doorSts: integer [可选] - 车门开关状态，0：全部车门关闭；1:未关闭全部车门，站控识别为为0时可以换电(201)
            epBWorkingSts: integer [可选] - 驻车制动状态，0：松开；1:制动，站控识别为0时可以换电(201)
            gearSts: integer [可选] - 挡位状态，0：其它；1:N档，站控识别为为1时可以换电(201)
            steeringWheelAngle: number [可选] - 方向盘转向角角度，站控识别为≤30°时可以换电(201)
            vehHVState: integer [可选] - 高压连接状态(页面上展示为熄火)，0：下高压；1:未下高压(201)
            vehPowerMode: integer [可选] - 车辆钥匙状态(没有用) 0：熄火；1：Ready，站控识别为0时可以换电(201)
        """
        path = f'/api/virtualCarStation/feign/v1/carStationInfo/carFreedomInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v1_carStationInfo_swapAndSelfCheckInfo(data):
        """
        电池换电失败原因、电池自我检测换电失败原因
        请求参数:
            bmsFalutCodeBit0: integer [可选] - MBMU未发送SBMU2上高压指令
            bmsFalutCodeBit1: integer [可选] - SBMU2蓝牙通信故障无法上高压
            bmsFalutCodeBit11: integer [可选] - MBMU未发送SBMU1上高压指令
            bmsFalutCodeBit12: integer [可选] - SBMU1蓝牙通信故障无法上高压
            bmsFalutCodeBit13: integer [可选] - SBMU1未收到MBMU上高压指令
            bmsFalutCodeBit14: integer [可选] - SBMU1未响应上高压指令
            bmsFalutCodeBit15: integer [可选] - SBMU1接触器开路故障
            bmsFalutCodeBit16: integer [可选] - 进入换电后10min内未收到"换电指令"跳转
            bmsFalutCodeBit17: integer [可选] - 自检失败后处理超时
            bmsFalutCodeBit18: integer [可选] - 站控发送SBMU1的MAC地址为0
            bmsFalutCodeBit19: integer [可选] - 站控发送SBMU2的MAC地址为0
            bmsFalutCodeBit2: integer [可选] - SBMU2未收到MBMU上高压指令
            bmsFalutCodeBit20: integer [可选] - SBMU1的蓝牙连接失败
            bmsFalutCodeBit21: integer [可选] - SBMU2的蓝牙连接失败
            bmsFalutCodeBit22: integer [可选] - 自检失败
            bmsFalutCodeBit24: integer [可选] - SBMU1未收到下高压指令
            bmsFalutCodeBit25: integer [可选] - SBMU2未收到下高压指令
            bmsFalutCodeBit26: integer [可选] - SBMU1收到下高压指令但未反馈下高压完成
            bmsFalutCodeBit27: integer [可选] - SBMU2收到下高压指令但未反馈下高压完成
            bmsFalutCodeBit28: integer [可选] - SBMU1接触器粘连故障
            bmsFalutCodeBit29: integer [可选] - SBMU2接触器粘连故障
            bmsFalutCodeBit3: integer [可选] - SBMU2未响应上高压指令
            bmsFalutCodeBit30: integer [可选] - SBMU1蓝牙断不开
            bmsFalutCodeBit31: integer [可选] - SBMU2蓝牙断不开
            bmsFalutCodeBit4: integer [可选] - SBMU2接触器开路故障
            bmsFalutCodeBit41: integer [可选] - SBMU2的累加和电压无效
            bmsFalutCodeBit42: integer [可选] - SBMU2有禁止继电器闭合故障
            bmsFalutCodeBit43: integer [可选] - SBMU2有继电器延迟断开故障
            bmsFalutCodeBit44: integer [可选] - SBMU2有继电器强制断开故障
            bmsFalutCodeBit5: integer [可选] - 上高压失败后处理超时
            bmsFalutCodeBit56: integer [可选] - 自检失败触发存储
            bmsFalutCodeBit57: integer [可选] - 电池包压差过大
            bmsFalutCodeBit58: integer [可选] - SBMU1的累加和电压无效
            bmsFalutCodeBit59: integer [可选] - SBMU1有禁止继电器闭合故障
            bmsFalutCodeBit6: integer [可选] - 所有蓝牙都连不上
            bmsFalutCodeBit60: integer [可选] - SBMU1有继电器延迟断开故障
            bmsFalutCodeBit61: integer [可选] - SBMU1有继电器强制断开故障
            bmsFalutCodeBit9: integer [可选] - 绝缘禁止上高压
            sbmu1FaultCode: integer [可选] - sbmu1故障码
            sbmu2FaultCode: integer [可选] - sbmu2故障码
        """
        path = f'/api/virtualCarStation/feign/v1/carStationInfo/swapAndSelfCheckInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v1_carStationInfo_swapInteractionInfo(data):
        """
        换电交互信息
        请求参数:
            allPackPwrDnSts: integer [可选] - 所有pack下高压状态： 0-默认，1-下高压成功，2-下高压失败(201)
            blueDisconnectFailFlg: integer [可选] - 0-默认，1-请求蓝牙断开失败(201)
            excPackCheckFailFlg: integer [可选] - 自检失败标志位：0-正常，1-失败(203)
            hisAccumChrgTimes: integer [可选] - 累计站外充电次数(207)
            m2T_WLDSts: integer [可选] - MBMU和TBMU蓝牙配对状态：0-未连接，1-连接，2-异常(203)
            packExcFailFlg: integer [可选] - 上高压失败标志位：0-正常，1-失败(203)
            packExcSts: integer [可选] - 换电状态：0-未换电，1-换电准备，2-换电中(201)
            subTotalChargeTimeOutStation: integer [可选] - 小计站外充电次数(207)
            vehSubTotalOdometer: integer [可选] - 车辆小计换电里程信息(203)
            vehTotalOdometer: integer [可选] - 车辆总里程信息(203)
            vhlAllowBatSwapFlg: integer [可选] - 车端换电允许标志位： 0-不允许，1-允许换电(201)
            vin: string [可选] - 车辆vin(214)
            waitBatterySwapMaxTimeOutFlg: integer [可选] - 换电超时请求退出换电标志位：0-正常，1-失败(203)
        """
        path = f'/api/virtualCarStation/feign/v1/carStationInfo/swapInteractionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v1_carStationInfo_tbmuMbmuVersionInfo(data):
        """
        Tbmu Mbmu版本信息
        请求参数:
            mbmuAppVersion: string [可选] - mbmu app版本号
            mbmuBleBootVersion: string [可选] - mbmu 蓝牙 boot版本号
            mbmuBleSoftVersion: string [可选] - mbmu 蓝牙软件版本号
            mbmuBootVersion: string [可选] - mbmu boot版本号
            mbmuHardwareVersion: string [可选] - mbmu 硬件版本号
            tbmuAppVersion: string [可选] - tbmu app版本号
            tbmuBleBootVersion: string [可选] - tbmu 蓝牙 boot版本号
            tbmuBleSoftVersion: string [可选] - tbmu 蓝牙软件版本号
            tbmuBootVersion: string [可选] - tbmu boot版本号
            tbmuHardwareVersion: string [可选] - tbmu 硬件版本号
        """
        path = f'/api/virtualCarStation/feign/v1/carStationInfo/tbmuMbmuVersionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v1_carStationInfo_virtualCarStationInit(data):
        """
        换电开始初始化模拟器
        """
        path = f'/api/virtualCarStation/feign/v1/carStationInfo/virtualCarStationInit'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_controlCommand_closeAndDisableHVContactorResult(data):
        """
        发送下高压执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/v3/controlCommand/closeAndDisableHVContactorResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_controlCommand_closeLVContactorResult(data):
        """
        发送下低压执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/v3/controlCommand/closeLVContactorResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_controlCommand_connectCarMbmuResult(data):
        """
        发送蓝牙连接执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
            rpa: string [可选] - rpa
        """
        path = f'/api/virtualCarStation/feign/v3/controlCommand/connectCarMbmuResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_controlCommand_disConnectCarMbmuResult(data):
        """
        发送蓝牙断开执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/v3/controlCommand/disConnectCarMbmuResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_controlCommand_scanBlueToothInfoResult(data):
        """
        发送蓝牙扫描执行结果
        请求参数:
            errorCode: integer [可选] - 默认值：全F 无故障/无法识别故障：0 故障码：1~254
            resultCode: integer [可选] - 默认值：全F 执行失败：1 执行成功：2
        """
        path = f'/api/virtualCarStation/feign/v3/controlCommand/scanBlueToothInfoResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_controlCommand_set0X129(data):
        """
        0X129
        请求参数:
            cnctrPwrSplyVolt: integer [可选]
            cnctrPwrSplyVoltVldBySafety: integer [可选]
            hvil1State: integer [可选]
            kl30Volt: integer [可选]
            kl30VoltVldBySafety: integer [可选]
            voltInfo_CRC: integer [可选]
            voltInfo_SBMU_AlIV: integer [可选]
            wakeUpSourceState: integer [可选]
        """
        path = f'/api/virtualCarStation/feign/v3/controlCommand/set0X129'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_controlCommand_set0X12F(data):
        """
        0X12F
        请求参数:
            allMainCnctrOpenedFlg: integer [可选] - 所有主回路的继电器断开标志
            bmsfaultDisposeSignal: integer [可选]
            bmsinitStatus: integer [可选]
            bmsmostCriticalFltID: integer [可选]
            bmsmostCriticalFltLvl: integer [可选]
            cellOverVoltALvl4Flt: integer [可选] - 功能安全单体极限过压
            cellUnderVoltALvl4Flt: integer [可选] - 功能安全单体极限欠压
            cellVoltSamplingLineOpenWireFlt: integer [可选] - 模组温度采样线开路故障
            faultCat: integer [可选] - 未锁存故障等级
            fltInfo2_CRC: integer [可选] - PACK信息3报文的CRC
            fltInfo2_SBMU_AlIV: integer [可选] - SBMU生命信号,0~15循环
            mainNegCnctrCtrlHighSideCmd: integer [可选] - 主负继电器高边控制命令
            mainNegCnctrCtrlLowSideCmd: integer [可选] - 主负继电器低边控制命令
            mainPosCnctrCtrlHighSideCmd: integer [可选] - 主正继电器低边控制命令
            mainPosCnctrCtrlLowSideCmd: integer [可选] - 主正继电器高边控制命令
            moduleOTALvl4Flt: integer [可选] - 功能安全过温四级故障标志位
            powerOnCmdFeedBack: integer [可选] - SBMU反馈收到MBMU/VCU的上高压指令
            preCnctrCtrlHighSideCmd: integer [可选] - 预充继电器高边控制命令
            preCnctrCtrlLowSideCmd: integer [可选] - 预充继电器低边控制命令
            tempSamplingLineOpenWireFlt: integer [可选]
            tempSensorSeriousFlt: integer [可选] - 温度传感器严重故障标志
        """
        path = f'/api/virtualCarStation/feign/v3/controlCommand/set0X12F'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_controlCommand_stopJob(data):
        """
        停止定时任务
        请求参数:
            code: string [可选] - 停止任务:v3_244_command-sn任务,v3_123_command-真实soc
        """
        path = f'/api/virtualCarStation/feign/v3/controlCommand/stopJob'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_info_blueToothInfo(data):
        """
        发送蓝牙连接信息
        请求参数:
            bluetoothScanStatus: integer [可选] - 蓝牙扫描状态 空闲：0   Rap连接扫描中：1   Rap重连扫描中:2   搜索扫描中:3
            connectedStatus: integer [可选] - SBLE和VBLE蓝牙连接状态：0-未连接，1-已连接
            signalStrengthOfS2V: integer [可选] - 未连接：0.0dbm 已连接：-128dbm ~ -1dbm
            signalStrengthOfV2S: integer [可选] - 未连接：0.0dbm 已连接：-128dbm ~ -1dbm
        """
        path = f'/api/virtualCarStation/feign/v3/info/blueToothInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_info_carFreedomStatusInfo(data):
        """
        发送车辆自由度信息
        请求参数:
            carDoorStatus: integer [可选] - 车辆车门状态：1-车门全部关闭，2-车门未全部关闭
            footBrakeStatus: integer [可选] - 车辆刹车踏板状态：1-未制动，2-制动
            gearStatus: integer [可选] - 车辆档位状态:1-N档，2-非N档
            handBrakeStatus: integer [可选] - 车辆手刹/电子手刹状态：1-未制动，2-制动
            highVoltageStatusOf1BP: integer [可选] - 1号电池包高压状态：0-高压断开，7、18-高压闭合
            highVoltageStatusOf2BP: integer [可选] - 2号电池包高压状态：0-高压断开，7、18-高压闭合
            highVoltageStatusOfBS: integer [可选] - 电池系统高压状态：0-高压断开，1-高压闭合
            lowVoltageOfBS: integer [可选] - 电池系统低压输入电压 (KL30)：0~65534
            m2VAutoholdSts: integer [可选] - 自动驻车状态
            m2VBonnetSts: integer [可选] - 引擎盖状态
            m2VDoorSignal: integer [可选] - 判断门的区分（兼容）
            m2VDoorStsFL: integer [可选] - 左前门状态
            m2VDoorStsFR: integer [可选] - 右前门状态
            m2VDoorStsRL: integer [可选] - 左后门状态
            m2VDoorStsRR: integer [可选] - 右后门状态
            m2VMBMUPowerVoltage: integer [可选] - KL30电压
            m2VTrunkSts: integer [可选] - 后备箱状态
            steeringTurnAngle: number [可选] - 车辆方向盘转向角角度：0.0~6553.4
        """
        path = f'/api/virtualCarStation/feign/v3/info/carFreedomStatusInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_info_carInfo(data):
        """
        发送车辆信息
        请求参数:
            accellRatedCapacityAh: number [可选]
            accellRatedCapacityAhOfPackage1: number [可选]
            actualSocOfPackage1: number [可选] - 1号电池可用荷电状态（真实）
            actualSocOfPackage2: number [可选] - 2号电池可用荷电状态（真实）
            bmstotalMilKm: number [可选]
            cellTypeOfPackage1: integer [可选] - 1号位电池包额定容量类别
            cellTypeOfPackage2: integer [可选] - 2号位电池包额定容量类别
            displayingSocOfPackage1: number [可选] - 1号电池可用荷电状态（表显）
            displayingSocOfPackage2: number [可选] - 2号电池可用荷电状态（表显）
            errorCodeOfBattSysList: array [可选] - 电池系统故障码
            errorCodeOfPackage1List: array [可选] - 1号电池包故障码
            errorCodeOfPackage2List: array [可选] - 2号电池包故障码
            hardVersionOfPackage1: string [可选] - 1号电池SBMU硬件版本号
            hardVersionOfPackage2: string [可选] - 2号电池SBMU硬件版本号
            hisStaOutAccumChrgerEngyOfPackage1: number [可选] - 1号累计站外插枪充电能量
            hisStaOutDisChrgEngyOfPackage1: number [可选] - 1号累计站外放电能量
            hisStaOutReChrgEngy: number [可选] - 电池包累计站外回充能量 kwh
            hvnegInterfaceTempOfPackage1: number [可选]
            hvposInterfaceTempOfPackage1: number [可选]
            mainCnctrCtrlStateOfPackage1: integer [可选] - 1号位电池包内主回路高压状态
            mbmuHardVersion: string [可选] - 车MBMU硬件版本号
            mbmuSoftVersion: string [可选] - 车MBMU软件版本号
            packTypeOfPackage1: integer [可选] - 1号位电池包类型识别码
            ratedPackVOLTOfPackage1: number [可选] - 1号电池额定电压
            sbleHardVersion: string [可选] - 站端通讯模块蓝牙硬件版本号
            sbleMac: string [可选] - 站端蓝牙通讯模块MAC
            sbleSoftVersion: string [可选] - 站端通讯模块蓝牙软件版本号
            signalStrengthOfV2S: integer [可选] - 未连接：0.0dbm 已连接：-128dbm ~ -1dbm
            snOfPackage1: string [可选] - 1号电池Sn码
            snOfPackage2: string [可选] - 2号电池Sn码
            socUnreliableFlagOfPackage1: integer [可选] - 1号电池包SOC不可信标志位
            socUnreliableFlagOfPackage2: integer [可选] - 2号电池包SOC不可信标志位
            soeOfPackage1: number [可选] - 1号电池电量
            soeOfPackage2: number [可选] - 2号电池电量
            softVersionOfPackage1: string [可选] - 1号电池SBMU软件版本号
            softVersionOfPackage2: string [可选] - 2号电池SBMU软件版本号
            sohOfPackage1: number [可选] - 1号电池健康度
            sohOfPackage2: number [可选] - 2号电池健康度
            statusOfPackage1: integer [可选] - BMS识别的1号电池包的状态
            statusOfPackage2: integer [可选] - BMS识别的2号电池包的状态
            subtotalMileageOfPackage1: number [可选] - 1号电池小计里程
            subtotalMileageOfPackage2: number [可选] - 2号电池小计里程
            subtotalOutsideChargingTimes: integer [可选] - 电池系统小计站外充电次数
            subtotalOutsideDischargingEnergyOfPackage1: number [可选] - 1号电池包小计站外放电能量
            subtotalOutsideDischargingEnergyOfPackage2: number [可选] - 2号电池包小计站外放电能量
            subtotalOutsideGunChargingEnergyOfPackage1: number [可选] - 1号电池包小计站外插枪充电能量
            subtotalOutsideGunChargingEnergyOfPackage2: number [可选] - 2号电池包小计站外插枪充电能量
            subtotalOutsideRechargingEnergyOfPackage1: number [可选] - 1号电池包小计站外回充能量
            subtotalOutsideRechargingEnergyOfPackage2: number [可选] - 2号电池包小计站外回充能量
            supremeErrorCodeOfBattSys: integer [可选] - 电池系统最高故障等级故障码
            supremeErrorCodeOfPackage1: integer [可选] - 1号电池包最高故障等级故障码
            supremeErrorCodeOfPackage2: integer [可选] - 2号电池包最高故障等级故障码
            supremeErrorLevelOfBattSys: integer [可选] - 电池系统最高故障等级
            supremeErrorLevelOfPackage1: integer [可选] - 1号电池包最高故障等级
            supremeErrorLevelOfPackage2: integer [可选] - 2号电池包最高故障等级
            tirePRSsignal: integer [可选] - 项目报警是用胎压值还是用报警信号
            tirePrsAlarm_FL: integer [可选] - 胎压报警信号 左前轮
            tirePrsAlarm_FR: integer [可选] - 胎压报警信号 右前轮
            tirePrsAlarm_RL: integer [可选] - 胎压报警信号 左后轮
            tirePrsAlarm_RR: integer [可选] - 胎压报警信号 右后轮
            tirePrs_FL: integer [可选] - 胎压值 左前轮
            tirePrs_FR: integer [可选] - 胎压值 右前轮
            tirePrs_RL: integer [可选] - 胎压值 左后轮
            tirePrs_RR: integer [可选] - 胎压值 右后轮
            totalChargingEnergyOfPackage1: number [可选] - 1号电池包累计充电能量
            totalChargingEnergyOfPackage2: number [可选] - 2号电池包累计充电能量
            totalDischargingEnergyOfPackage1: number [可选] - 1号电池包累计放电能量
            totalDischargingEnergyOfPackage2: number [可选] - 2号电池包累计放电能量
            totalMile: number [可选] - 车总里程数
            totalMileageOfPackage1: number [可选] - 1号电池总里程
            totalMileageOfPackage2: number [可选] - 2号电池总里程
            totalOutsideGunChargingTimes: integer [可选] - 电池系统累计站外插枪充电次数
            vbleHardVersion: string [可选] - 车蓝牙通讯模块硬件版本号
            vbleMac: string [可选] - 车蓝牙通讯模块MAC
            vbleSoftVersion: string [可选] - 车蓝牙通讯模块软件版本号
            vehSpeed: number [可选] - 车速
            vin: string [可选] - 车辆vin码
        """
        path = f'/api/virtualCarStation/feign/v3/info/carInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualCarStation_feign_v3_info_scanBlueToothInfo(data):
        """
        发送蓝牙扫描信息
        请求参数:
            sbleMac: string [可选] - 扫描蓝牙MAC
            signalStrengthOfV2S: integer [可选] - 未连接：0.0dbm 已连接：-128dbm ~ -1dbm
        """
        path = f'/api/virtualCarStation/feign/v3/info/scanBlueToothInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarStation._get_path(path), 'POST', data))
