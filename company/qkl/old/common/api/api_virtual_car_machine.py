from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiVirtualCarMachine:
    @staticmethod
    def _get_path(path):
        service = '/virtual-car-machine'
        return service + path

    @staticmethod
    def api_cbmuMock_batteryCodeInfo(data):
        """
        电池mac和sn信息
        请求参数:
            batteryCodeInfo: array [可选]
                        position: integer [可选] - 仓位号
                        sn: string [可选] - 电池包sn(407)
                        mac: string [可选] - 电池包mac(408)
        """
        path = f'/api/cbmuMock/batteryCodeInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_cbmuMock_batteryDataInfo1(data):
        """
        电池数据信息-能量、容量、soc、soh、soe
        请求参数:
            energyInfo: array [可选] - 电池包能量信息
                        position: integer [可选] - 仓位号
                        subTotalChrgEnergyInstation: number [可选] - 小计站内充电电量(40A)
                        subTotalChrgEnergyOutstation: number [可选] - 小计站外充电电量(40A)
                        hisAccumDisChrgEngy: number [可选] - 电池包累计放电总能量(411)
                        hisAccumChrgEngy: number [可选] - 电池包累计充电总能量(411)
                        thisTimeInDCEngyWh: integer [可选] - 本次小计换电站内充电能量(412)
                        thisTimeInstationDischrgEngyWh: integer [可选] - 本次小计换电站内充电能量(412)
                        instationHisAccumDisChrgEngy: number [可选] - 累计换电站内放电能量(413)
                        instationHisAccumChrgEngy: number [可选] - 累计换电站内充电能量(413)
            capacityInfo: array [可选] - 电池包容量信息
                        position: integer [可选] - 仓位号
                        sbMU_TotalChargeCap: number [可选] - 累计充电容量(40B)
                        sbMU_TotalDisChargeCap: number [可选] - 累计放电容量(40B)
                        sbMU_RatedCapacity: number [可选] - 标称容量(40D)
                        sysChrgCapCurrentAh: number [可选] - 本次充电容量(412)
            socSohSoeInfo: array [可选] - 电池包SocSohSoe信息
                        position: integer [可选] - 仓位号
                        sbMU_LCMSOCMax: number [可选] - LCM SOC上限(40C)
                        sbMU_LCMSOCMin: number [可选] - LCM SOC下限(40C)
                        sbMU_DisplaySOC: number [可选] - SBMU 显示SOC(404)
                        sbMU_SOCMax: number [可选] - SBMU 最大SOC(404)
                        sbMU_SOCMin: number [可选] - SBMU 最小SOC(404)
                        sbMU_SOH: number [可选] - SBMU SOH(404)
                        sbMU_RealSOC: number [可选] - SBMU 真实SOC(404)
                        sbMU_RemainEnergy: integer [可选] - SBMU SOE(406)
        """
        path = f'/api/cbmuMock/batteryDataInfo1'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_cbmuMock_batteryDataInfo2(data):
        """
        电池数据信息-电压、电流、电阻
        请求参数:
            voltageInfo: array [可选] - 电池包电压信息
                        position: integer [可选] - 仓位号
                        sbMU_CellVolt_Max: integer [可选] - SBMU 最大电芯电压(402)
                        sbMU_CellVolt_Min: integer [可选] - SBMU 最小电芯电压(402)
                        sbMU_CellVolt_Avg: integer [可选] - SBMU 平均电芯电压(402)
                        chargerVoltage_Output: number [可选] - ACDC输出电压(405)
                        sbMU_BattChrgReqVolt: number [可选] - SBMU充电请求电压(410)
            currentInfo: array [可选] - 电池包电流信息
                        position: integer [可选] - 仓位号
                        chargerCurrenr_Output: number [可选] - ACDC输出电流(405)
                        sbMU_BattCurr: number [可选] - SBMU母线电流(410)
                        sbMU_BattChrgReqCurr: number [可选] - SBMU充电请求电流(410)
            resistanceInfo: array [可选] - 电池包电阻信息
                        position: integer [可选] - 仓位号
                        sbMU_IsoMeasPosResKOhm: integer [可选] - 正极对地绝缘阻值(40E)
                        sbMU_IsoMeasNegResKOhm: integer [可选] - 负极对地绝缘阻值(40E)
                        sbMU_PackDCR: number [可选] - 电池包DCR(406)
        """
        path = f'/api/cbmuMock/batteryDataInfo2'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_cbmuMock_batteryDataInfo3(data):
        """
        电池数据信息-温度、次数统计、位置
        请求参数:
            temperatureInfo: array [可选] - 电池包温度信息
                        position: integer [可选] - 仓位号
                        sbMU_ModTmp_Max: integer [可选] - 模组最高温度(403)
                        sbMU_ModTmp_Min: integer [可选] - 模组最低温度(403)
                        sbMU_BatTmp_Avg: integer [可选] - 模组平均温度(403)
            countInfo: array [可选] - 电池包次数统计信息
                        position: integer [可选] - 仓位号
                        subTotalChrgTimeOutstation: integer [可选] - 小计站外充电次数(40A)
                        sbMU_MainPosCnctrOpenCnt: integer [可选] - 主正继电器断开次数(40D)
                        sbMU_MainNegCnctrOpenCnt: integer [可选] - 主负继电器断开次数(40D)
                        hisAccumDisChargeCycle: integer [可选] - 电池包累计放电总Cycle(414)
                        hisAccumChargeCycle: integer [可选] - 电池包累计充电总Cycle(414)
            positionInfo: array [可选] - 电池包位置信息
                        position: integer [可选] - 仓位号
                        sbMU_MaxCellVoltPos: integer [可选] - SBMU最大电芯电压位置(402)
                        sbMU_MinCellVoltPos: integer [可选] - SBMU最大电芯温度位置(402)
                        maxModuleTempPos: integer [可选] - 最高模组温度位置(403)
                        minModuleTempPos: integer [可选] - 最低模组温度位置(403)
        """
        path = f'/api/cbmuMock/batteryDataInfo3'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_cbmuMock_batteryDataInfo4(data):
        """
        电池数据信息-累计静置时间、无线通讯信号强度
        请求参数:
            otherInfo: array [可选] - 电池包其他信息
                        position: integer [可选] - 仓位号
                        sbMU_TotalStaticTime: integer [可选] - 累计静置时间(40C)
                        wirelessSignalStrength: integer [可选] - 无线通讯信号强度(401)
                        chargerStopReason: integer [可选] - 充电停止原因(405)
                        sbMU_MostCriticalFltLvl: integer [可选] - 电池包最高故障等级(406)
                        sbMU_FullChrgDeltaSOCError: integer [可选] - 满充SOC差异过大故障(406)
                        sbmuLive: integer [可选] - SBMU生命帧（0~15之间跳动）
                        cbmuLive: integer [可选] - CBMU生命帧（0~15之间跳动）
        """
        path = f'/api/cbmuMock/batteryDataInfo4'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_cbmuMock_batterySignOrStateInfo(data):
        """
        电池标志和状态信息
        请求参数:
            batterySignOrStateInfo: array [可选]
                        position: integer [可选] - 仓位号
                        s2C_BMSChrgAllowFlg: integer [可选] - 允许充电标志： 0-不允许，1-允许(401)
                        hvIL1State: integer [可选] - 高压互锁状态：0-Close，1-Open(401)
                        soCUnavailableFlg: integer [可选] - SOC不可信标志(404)
                        sbMU_FullChrgOneWeekRqstFlg: integer [可选] - 满充一周维护一次请求标志位(406)
                        sbMU_ChargeSts: integer [可选] - SBMU充电状态(410)
                        sbMU_ThermalSts: integer [可选] - SBMU热管理状态(410)
        """
        path = f'/api/cbmuMock/batterySignOrStateInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_cbmuMock_swapInteractionInfo(data):
        """
        电池换电交互信息
        请求参数:
            swapInteractionInfo: array [可选]
                        position: integer [可选] - 仓位号
                        c2S_WLDSts: integer [可选] - 蓝牙状态信息： 0-断开， 1-连接(401)
                        sbMU_SumCellVolt: number [可选] - 电芯电压累加和(403)
                        sbMU_RealSOC: number [可选] - SBMU 真实SOC(404)
                        charge_WorkingMode: integer [可选] - 充电机运行状态：0-空闲 1-参数配置中 2-充电中 3-停止充电 4-故障(405)
                        sbMU_MostCriticalFltID: integer [可选] - bms最严重故障码(406)
                        sbMU_MainNegCnctrState: integer [可选] - 主负继电器状态(406)
                        sbMU_MainPosCnctrState: integer [可选] - 主正继电器状态(406)
        """
        path = f'/api/cbmuMock/swapInteractionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_getAllAlive():
        """
        获取所有存活任务
        """
        path = f'/api/scheduleTask/getAllAlive'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_scheduleTask_getMessageCache():
        """
        按任务key获取消息缓存数据
        请求参数:
        """
        path = f'/api/scheduleTask/getMessageCache'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_scheduleTask_stopAllAlive():
        """
        停止所有存活任务
        """
        path = f'/api/scheduleTask/stopAllAlive'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_scheduleTask_stopTask():
        """
        按任务key停止任务
        请求参数:
        """
        path = f'/api/scheduleTask/stopTask'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_supportTest_batteryInfoList():
        """
        仓位电池信息
        请求参数:
        """
        path = f'/api/supportTest/batteryInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_supportTest_matchRuleDetails():
        """
        车包匹配规则明细
        """
        path = f'/api/supportTest/matchRuleDetails'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_supportTest_pullBatteryLabels():
        """
        拉取电池标签
        请求参数:
        """
        path = f'/api/supportTest/pullBatteryLabels'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_supportTest_resetBatteryTakeStrategy():
        """
        重置取电规则
        """
        path = f'/api/supportTest/resetBatteryTakeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_supportTest_setOutPackDisconnectBTResult():
        """
        设置出仓电池断蓝牙结果
        请求参数:
        """
        path = f'/api/supportTest/setOutPackDisconnectBTResult'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_swapSignalMock_captureCarPlate():
        """
        1.抓拍车牌
        请求参数:
        """
        path = f'/api/swapSignalMock/captureCarPlate'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_swapSignalMock_carConnect():
        """
        3.车辆连接
        """
        path = f'/api/swapSignalMock/carConnect'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_swapSignalMock_carGetIn():
        """
        2.车辆进站
        """
        path = f'/api/swapSignalMock/carGetIn'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_swapSignalMock_getSwapMode():
        """
        测试接口
        """
        path = f'/api/swapSignalMock/getSwapMode'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_swapSignalMock_offline_noticeStartOfflineSwap():
        """
        启动离线换电前参数设置
        """
        path = f'/api/swapSignalMock/offline/noticeStartOfflineSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_swapSignalMock_sendChangePowerType():
        """
        5.换电方式下发
        """
        path = f'/api/swapSignalMock/sendChangePowerType'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_swapSignalMock_swapConfirm():
        """
        6.启动换电
        """
        path = f'/api/swapSignalMock/swapConfirm'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_swapSignalMock_swapFinished():
        """
        8.换电结束
        """
        path = f'/api/swapSignalMock/swapFinished'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'GET', None))

    @staticmethod
    def api_tbmuMock_batteryCodeInfo(data):
        """
        电池mac和sn信息
        请求参数:
            macOfPackage1: string [可选] - 电池包1的mac(209)
            macOfPackage2: string [可选] - 电池包2的mac(209)
            snOfPackage1: string [可选] - 电池包1的sn(211)
            snOfPackage2: string [可选] - 电池包2的sn(212)
            macOfMBMU: string [可选] - mubmu的mac(209)
        """
        path = f'/api/tbmuMock/batteryCodeInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_tbmuMock_batteryDataInfo(data):
        """
        电池数据信息
        请求参数:
            mileageInfo: array [可选] - 电池包里程信息
                        position: integer [可选] - 电池包序号
                        toatlMilKm: number [可选] - 电池包总里程信息(20C)
                        tripMilKm: number [可选] - 电池包小计换电里程信息(20C)
            energyInfo: array [可选] - 电池包能量信息
                        position: integer [可选] - 电池包序号
                        hisAccumDisChrgEngy: number [可选] - 电池包累计放电总能量(20D)
                        hisAccumChrgEngy: number [可选] - 电池包累计充电总能量(20D)
                        outStationChargingEnergy: number [可选] - 两次换电间电池包小计站外插枪充电电量(20E)
                        energyTotalOutput: number [可选] - 两次换电间电池包小计站外放电电量(20E)
                        hisStaOutReChrgEngyWh: number [可选] - 两次换电间电池包小计站外回充能量(20F)
                        hisStaOutDisChrgEngy: number [可选] - 累计换电站外放电能量(20F)
                        sbMU_RemainEnergyBeforeExc: number [可选] - 进站时电池剩余能量(SOE)(204)
                        sbMU_RemainEnergyLastExc: number [可选] - 上次出站时电池剩余能量(204)
            socSohInfo: array [可选] - 电池包Soc和Soh信息
                        position: integer [可选] - 电池包序号
                        sbMU_DisplaySOCLastExc: number [可选] - 上次出站时显示SOC(204)
                        sbMU_RealSOCCLastExc: number [可选] - 上次出站时真实SOC(204)
                        battSts6_DisplaySOH: number [可选] - 显示SOH(206)
                        displaySOC: number [可选] - 显示SOC(206)
                        realSOC: number [可选] - 真实SOC(206)
        """
        path = f'/api/tbmuMock/batteryDataInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_tbmuMock_batterySignOrStateInfo(data):
        """
        电池状态和标志信息
        请求参数:
            batterySignOrStateInfo: array [可选]
                        position: integer [可选] - 电池包序号
                        m2S_WLDSts: integer [可选] - 蓝牙状态信息：0:未连接，1:连接，2:异常(204)
                        battSts6_MainNegCnctrState: integer [可选] - 电池包主负继电器状态(206)
                        battSts6_MainPosCnctrState: integer [可选] - 电池包主正继电器状态(206)
                        soCUnavailableFlg: integer [可选] - SOC不可信标志(206)
                        battSts6_FaultNum: integer [可选] - 最严重故障码(206)
                        mostCriticalFltLvl: integer [可选] - 电池包最高故障等级(206)
        """
        path = f'/api/tbmuMock/batterySignOrStateInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_tbmuMock_carFreedomInfo(data):
        """
        车辆自由度信息
        请求参数:
            gearSts: integer [可选] - 挡位状态，0：其它；1:N档，站控识别为为1时可以换电(201)
            vehPowerMode: integer [可选] - 车辆钥匙状态 0：熄火；1：Ready，站控识别为0时可以换电(201)
            epBWorkingSts: integer [可选] - 驻车制动状态，0：松开；1:制动，站控识别为0时可以换电(201)
            brakeSwitchSts: integer [可选] - 制动器状态，0：松开；1:制动，站控识别为为0时可以换电(201)
            doorSts: integer [可选] - 车门开关状态，0：全部车门关闭；1:未关闭全部车门，站控识别为为0时可以换电(201)
            steeringWheelAngle: number [可选] - 方向盘转向角角度，站控识别为≤30°时可以换电(201)
            vehHVState: integer [可选] - 高压连接状态，0：下高压；1:未下高压
        """
        path = f'/api/tbmuMock/carFreedomInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_tbmuMock_mockLock(data):
        """
        机械锁
        请求参数:
            packLock_Pack1lock: integer [可选] - PACK机械锁
            packLock_Pack1lock1: integer [可选] - PACK机械锁1
            packLock_Pack1lock2: integer [可选] - PACK机械锁2
            packLock_Pack1lock3: integer [可选] - PACK机械锁3
            packLock_Pack1lock4: integer [可选] - PACK机械锁4
            packLock_Pack1lock: integer [可选] - PACK机械锁
            packLock_Pack1lock1: integer [可选] - PACK机械锁1
            packLock_Pack1lock2: integer [可选] - PACK机械锁2
            packLock_Pack1lock3: integer [可选] - PACK机械锁3
            packLock_Pack1lock4: integer [可选] - PACK机械锁4
        """
        path = f'/api/tbmuMock/mockLock'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_tbmuMock_mockLockVolt(data):
        """
        机械锁电压
        请求参数:
            packLockVolt_Pack1lock1: integer [可选] - PACK机械锁电压1
            packLockVolt_Pack1lock2: integer [可选] - PACK机械锁电压2
            packLockVolt_Pack1lock3: integer [可选] - PACK机械锁电压3
            packLockVolt_Pack1lock4: integer [可选] - PACK机械锁电压4
            packLockVolt_Pack1lock1: integer [可选] - PACK机械锁电压1
            packLockVolt_Pack1lock2: integer [可选] - PACK机械锁电压2
            packLockVolt_Pack1lock3: integer [可选] - PACK机械锁电压3
            packLockVolt_Pack1lock4: integer [可选] - PACK机械锁电压4
        """
        path = f'/api/tbmuMock/mockLockVolt'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))

    @staticmethod
    def api_tbmuMock_swapInteractionInfo(data):
        """
        换电交互信息
        请求参数:
            vin: string [可选] - 车辆vin(214)
            vehHVState: integer [可选] - 高压连接状态：0-下高压，1-未下高压(201)
            packExcSts: integer [可选] - 换电状态：0-未换电，1-换电准备，2-换电中(201)
            blueDisconnectFailFlg: integer [可选] - 0-默认，1-请求蓝牙断开失败(201)
            allPackPwrDnSts: integer [可选] - 所有pack下高压状态： 0-默认，1-下高压成功，2-下高压失败(201)
            vhlAllowBatSwapFlg: integer [可选] - 车端换电允许标志位： 0-不允许，1-允许换电(201)
            pack1InstallSts: integer [可选] - 包1安装状态：0-未安装包；1-安装真包；2-安装假包；3-默认值
            pack2InstallSts: integer [可选] - 包2安装状态：0-未安装包；1-安装真包；2-安装假包；3-默认值
            m2T_WLDSts: integer [可选] - MBMU和TBMU蓝牙配对状态：0-未连接，1-连接，2-异常(203)
            excPackCheckFailFlg: integer [可选] - 自检失败标志位：0-正常，1-失败(203)
            packExcFailFlg: integer [可选] - 上高压失败标志位：0-正常，1-失败(203)
            waitBatterySwapMaxTimeOutFlg: integer [可选] - 换电超时请求退出换电标志位：0-正常，1-失败(203)
            vehTotalOdometer: integer [可选] - 车辆总里程信息(203)
            hisAccumChrgTimes: integer [可选] - 累计站外充电次数(207)
            subTotalChargeTimeOutStation: integer [可选] - 小计站外充电次数(207)
        """
        path = f'/api/tbmuMock/swapInteractionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualCarMachine._get_path(path), 'POST', data))
