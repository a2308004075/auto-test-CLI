from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiVirtualBattery:
    @staticmethod
    def _get_path(path):
        service = '/virtual-battery'
        return service + path

    @staticmethod
    def api_batteryMock_feign_v1_batteryCodeInfo(data):
        """
        电池mac和sn信息
        请求参数:
            batteryCodeInfo: array [可选]
                        mac: string [可选] - 电池包mac(408)
                        position: integer [可选] - 仓位号
                        sn: string [可选] - 电池包sn(407)
        """
        path = f'/api/batteryMock/feign/v1/batteryCodeInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_feign_v1_batteryDataInfo1(data):
        """
        电池数据信息-能量、容量、soc、soh、soe
        请求参数:
            capacityInfo: array [可选] - 电池包容量信息
                        position: integer [可选] - 仓位号
                        sbMU_RatedCapacity: number [可选] - 标称容量(40D)
                        sbMU_TotalChargeCap: number [可选] - 累计充电容量(40B)
                        sbMU_TotalDisChargeCap: number [可选] - 累计放电容量(40B)
                        subTotalChrgCapInstation: number [可选] - 小计站内充电容量（40F)
                        subTotalChrgCapOutstation: number [可选] - 小计站外充电容量(40F)
                        sysChrgCapCurrentAh: number [可选] - 本次充电容量(412)
            energyInfo: array [可选] - 电池包能量信息
                        hisAccumChrgEngy: number [可选] - 电池包累计充电总能量(411)
                        hisAccumDisChrgEngy: number [可选] - 电池包累计放电总能量(411)
                        instationHisAccumChrgEngy: number [可选] - 累计换电站内充电能量(413)
                        instationHisAccumDisChrgEngy: number [可选] - 累计换电站内放电能量(413)
                        position: integer [可选] - 仓位号
                        subTotalChrgEnergyInstation: number [可选] - 小计站内充电电量(40A)
                        subTotalChrgEnergyOutstation: number [可选] - 小计站外充电电量(40A)
                        thisTimeInDCEngyWh: number [可选] - 本次小计换电站内充电能量(412)
                        thisTimeInstationDischrgEngyWh: number [可选] - 本次小计换电站内放电能量(412)
            socSohSoeInfo: array [可选] - 电池包SocSohSoe信息
                        position: integer [可选] - 仓位号
                        sbMU_DisplaySOC: number [可选] - SBMU 显示SOC(404)
                        sbMU_LCMSOCMax: number [可选] - LCM SOC上限(40C)
                        sbMU_LCMSOCMin: number [可选] - LCM SOC下限(40C)
                        sbMU_RemainEnergy: integer [可选] - SBMU SOE(406)
                        sbMU_SOCMax: number [可选] - SBMU 最大SOC(404)
                        sbMU_SOCMin: number [可选] - SBMU 最小SOC(404)
                        sbMU_SOH: number [可选] - SBMU SOH(404)
        """
        path = f'/api/batteryMock/feign/v1/batteryDataInfo1'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_feign_v1_batteryDataInfo2(data):
        """
        电池数据信息-电压、电流、电阻
        请求参数:
            currentInfo: array [可选] - 电池包电流信息
                        chargerCurrenr_Output: number [可选] - ACDC输出电流(405)
                        position: integer [可选] - 仓位号
                        sbMU_BattChrgReqCurr: number [可选] - SBMU充电请求电流(410)
                        sbMU_BattCurr: number [可选] - SBMU母线电流(410)
            resistanceInfo: array [可选] - 电池包电阻信息
                        position: integer [可选] - 仓位号
                        sbMU_IsoMeasNegResKOhm: integer [可选] - 负极对地绝缘阻值(40E)
                        sbMU_IsoMeasPosResKOhm: integer [可选] - 正极对地绝缘阻值(40E)
                        sbMU_PackDCR: number [可选] - 电池包DCR(406)
            voltageInfo: array [可选] - 电池包电压信息
                        chargerVoltage_Output: number [可选] - ACDC输出电压(405)
                        position: integer [可选] - 仓位号
                        sbMU_BattChrgReqVolt: number [可选] - SBMU充电请求电压(410)
                        sbMU_CellVolt_Avg: integer [可选] - SBMU 平均电芯电压(402)
                        sbMU_CellVolt_Max: integer [可选] - SBMU 最大电芯电压(402)
                        sbMU_CellVolt_Min: integer [可选] - SBMU 最小电芯电压(402)
        """
        path = f'/api/batteryMock/feign/v1/batteryDataInfo2'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_feign_v1_batteryDataInfo3(data):
        """
        电池数据信息-温度、次数统计、位置
        请求参数:
            countInfo: array [可选] - 电池包次数统计信息
                        hisAccumChargeCycle: integer [可选] - 电池包累计充电总Cycle(414)
                        hisAccumDisChargeCycle: integer [可选] - 电池包累计放电总Cycle(414)
                        position: integer [可选] - 仓位号
                        sbMU_MainNegCnctrOpenCnt: integer [可选] - 主负继电器断开次数(40D)
                        sbMU_MainPosCnctrOpenCnt: integer [可选] - 主正继电器断开次数(40D)
                        subTotalChrgTimeOutstation: integer [可选] - 小计站外充电次数(40A)
            positionInfo: array [可选] - 电池包位置信息
                        maxModuleTempPos: integer [可选] - 最高模组温度位置(403)
                        minModuleTempPos: integer [可选] - 最低模组温度位置(403)
                        position: integer [可选] - 仓位号
                        sbMU_MaxCellVoltPos: integer [可选] - SBMU最大电芯电压位置(402)
                        sbMU_MinCellVoltPos: integer [可选] - SBMU最大电芯温度位置(402)
            temperatureInfo: array [可选] - 电池包温度信息
                        position: integer [可选] - 仓位号
                        sbMU_BatTmp_Avg: integer [可选] - 模组平均温度(403)
                        sbMU_ModTmp_Max: integer [可选] - 模组最高温度(403)
                        sbMU_ModTmp_Min: integer [可选] - 模组最低温度(403)
        """
        path = f'/api/batteryMock/feign/v1/batteryDataInfo3'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_feign_v1_batteryDataInfo4(data):
        """
        电池数据信息-累计静置时间、无线通讯信号强度
        请求参数:
            otherInfo: array [可选] - 电池包其他信息
                        chargerStopReason: integer [可选] - 充电停止原因(405)
                        position: integer [可选] - 仓位号
                        s2C_BMSChrgAllowFlg: integer [可选] - 允许充电标志(401)
                        sbMU_FaultNum: integer [可选] - 故障码(406)
                        sbMU_FullChrgDeltaSOCError: integer [可选] - 满充SOC差异过大故障(406)
                        sbMU_MostCriticalFltLvl: integer [可选] - 电池包最高故障等级(406)
                        sbMU_TotalStaticTime: integer [可选] - 累计静置时间(40C)
                        wirelessSignalStrength: integer [可选] - 无线通讯信号强度(401)
        """
        path = f'/api/batteryMock/feign/v1/batteryDataInfo4'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_feign_v1_batterySignOrStateInfo(data):
        """
        电池标志和状态信息
        请求参数:
            batterySignOrStateInfo: array [可选]
                        hvIL1State: integer [可选] - 高压互锁状态：0-Close，1-Open(401)
                        position: integer [可选] - 仓位号
                        s2C_BMSChrgAllowFlg: integer [可选] - 允许充电标志： 0-不允许，1-允许(401)
                        sbMU_ChargeSts: integer [可选] - SBMU充电状态(410)
                        sbMU_FullChrgOneWeekRqstFlg: integer [可选] - 满充一周维护一次请求标志位(406)
                        sbMU_ThermalSts: integer [可选] - SBMU热管理状态(410)
                        soCUnavailableFlg: integer [可选] - SOC不可信标志(404)
        """
        path = f'/api/batteryMock/feign/v1/batterySignOrStateInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_feign_v1_mockCbmuSbmuVersion(data):
        """
        电池包版本信息
        请求参数:
            batteryVersionInfoList: array [可选] - 电池包版本信息
                        appBootVersion: string [可选] - app boot版本号
                        appSoftVersion: string [可选] - app软件版本号
                        bleSoftwareVersion: string [可选] - 蓝牙软件版本号
                        hardwareVersion: string [可选] - 硬件版本号
                        position: integer [可选] - 仓位号
        """
        path = f'/api/batteryMock/feign/v1/mockCbmuSbmuVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_feign_v1_swapInteractionInfo(data):
        """
        电池换电交互信息
        请求参数:
            swapInteractionInfo: array [可选] - 仓内换电交互信息
                        c2S_WLDSts: integer [可选] - 蓝牙状态信息： 0-断开， 1-连接(401)
                        charge_WorkingMode: integer [可选] - 充电机运行状态：0-空闲 1-参数配置中 2-充电中 3-停止充电 4-故障(405)
                        position: integer [可选] - 仓位号
                        sbMU_MainNegCnctrState: integer [可选] - 主负继电器状态(406)
                        sbMU_MainPosCnctrState: integer [可选] - 主正继电器状态(406)
                        sbMU_MostCriticalFltID: integer [可选] - bms最严重故障码(406)
                        sbMU_RealSOC: number [可选] - SBMU 真实SOC(404)
                        sbMU_SumCellVolt: number [可选] - 电芯电压累加和(403)
        """
        path = f'/api/batteryMock/feign/v1/swapInteractionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_18F10980(data):
        """
        18F10980 Pack基础信息3
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_ForSOCUnavailableFlg: integer [可选] - 电池包真实SOC不可信标志位
            s_PackAvailEngyKwh: number [可选] - SOE
            s_PackRealSOCPct: number [可选] - 电池包真实SOC
            s_SysMaxSOCPct: number [可选] - 电池包最大真实SOC
            s_SysMinSOCPct: number [可选] - 电池包最小真实SOC
        """
        path = f'/api/batteryMock/v3/feign/18F10980'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_18F10C80(data):
        """
        18F10C80 继电器状态
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_HeatRelayState: integer [可选] - 加热继电器状态
            s_MainCnctrCtrlState: integer [可选] - 包内主回路高压状态
            s_MainNegCnctrSts: integer [可选] - 主负继电器状态
            s_MainPosCnctrSts: integer [可选] - 主正继电器状态
            s_PreChgRelayState: integer [可选] - 预充继电器状态
        """
        path = f'/api/batteryMock/v3/feign/18F10C80'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_clearFaultResp(data):
        """
        响应清除故障
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            resaon: integer [可选] - 原因
            result: integer [可选] - 结果 1:失败 2:成功
        """
        path = f'/api/batteryMock/v3/feign/clearFaultResp'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X118F82380(data):
        """
        18F82380 温度检测点极值统计
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_AvgModuleTempDegC: integer [可选]
            s_MaxConnectorPosTempDegC: integer [可选]
            s_MaxConnectorPosTempPstn: integer [可选]
            s_MaxModuleTempDegC: integer [可选]
            s_MaxModuleTempPstn: integer [可选]
            s_MinConnectorNegTempDegC: integer [可选]
            s_MinConnectorNegTempPstn: integer [可选]
            s_MinModuleTempDegC: integer [可选]
            s_MinModuleTempPstn: integer [可选]
        """
        path = f'/api/batteryMock/v3/feign/do0X118F82380'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X1871F980(data):
        """
        1871F980 电池箱充电中止信息
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_BMSChrgStopErrReason: integer [可选] - 电池箱 BMS 中止充电错误原因
            s_BMSChrgStopFltReason: integer [可选] - 电池箱 BMS 中止充电故障原因
            s_BMSChrgStopReason: integer [可选] - 电池箱 BMS 中止充电原因
        """
        path = f'/api/batteryMock/v3/feign/do0X1871F980'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18A2F980(data):
        """
        18A2F980 信息清除请求结果反馈
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_FltClearingSts: integer [可选] - 故障清除控制执行结果
            s_SubInfoInClrSts: integer [可选] - 站内小计信息清除控制执行结果
            s_SubInfoOutClrSts: integer [可选] - 站外小计信息清除控制执行结果
        """
        path = f'/api/batteryMock/v3/feign/do0X18A2F980'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F10180(data):
        """
        18F10180 基础参数1
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_PACKFaultID_N1: integer [可选]
            s_PACKFaultID_N2: integer [可选]
            s_PACKFaultID_N3: integer [可选]
            s_PACKFault_FrameNo: integer [可选]
        """
        path = f'/api/batteryMock/v3/feign/do0X18F10180'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F10680(data):
        """
        18F10680 电池包故障信息
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_BMSMostCriticalFltID: integer [可选] - 包内最高故障等级ID
            s_BMSMostCriticalFltLvl: integer [可选] - 包内最高故障等级
            s_FltInfo2_SBMU_AlIV: integer [可选] - SBMU生命信号
            s_ThermalRunawayFltReason: integer [可选] - 热失控故障原因
        """
        path = f'/api/batteryMock/v3/feign/do0X18F10680'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F40180(data):
        """
        18F40180
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_HISTInstatHisAccumDisChrgEngy: number [可选] - 累计站内放电能量
            s_HisStaOutDisChrgEngy: number [可选] - 累计换电站外放电能量
        """
        path = f'/api/batteryMock/v3/feign/do0X18F40180'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F40280(data):
        """
        18F40280
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_HISTInstatHisAccumChrgEngy: number [可选] - 累计站内充电能量
            s_HisStaOutChrgEngy: number [可选] - 电池包累计站外充电能量
        """
        path = f'/api/batteryMock/v3/feign/do0X18F40280'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F40480(data):
        """
        18F40480
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_BMSTripMilKm: number [可选] - 电池箱小计里程
            s_HisStaOutDisChrgEngyWh: number [可选] - 小计换电站外放电能量
            s_ThisTimeInstatDischrgEngyWh: number [可选] - 小计站内放电能量
        """
        path = f'/api/batteryMock/v3/feign/do0X18F40480'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F40580(data):
        """
        18F40580
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_BMSOffStationChargingEnergy: number [可选] - 小计换电站外插枪充电输入能量
            s_HisStaOutReChrgEngyWh: number [可选] - 小计换电站外回充充电能量
            s_ThisTimeInDCEngyWh: number [可选] - 小计站内充电输入能量
        """
        path = f'/api/batteryMock/v3/feign/do0X18F40580'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F80180(data):
        """
        18F80180 基础参数1
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_CellRatedCapacityAh: number [可选] - 额定容量（1C的容量） Ah
            s_CellType: integer [可选] - 电池类型
            s_NumOfAllModulesTemp: integer [可选] - 温度检测点数量
            s_NumOfCellParalleling: integer [可选] - 电池并联数
            s_NumOfCellSeriesConnection: integer [可选] - 电池串联数
            s_RatedPackVOLT: number [可选] - 额定电压
        """
        path = f'/api/batteryMock/v3/feign/do0X18F80180'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F80580(data):
        """
        设置sn
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            sn: string [可选] - 24位sn
        """
        path = f'/api/batteryMock/v3/feign/do0X18F80580'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F80680(data):
        """
        设置BMS硬件版本
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            version: string [可选] - 24位版本号
        """
        path = f'/api/batteryMock/v3/feign/do0X18F80680'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F80780(data):
        """
        设置BMS软件版本
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            version: string [可选] - 24位版本号
        """
        path = f'/api/batteryMock/v3/feign/do0X18F80780'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F81280(data):
        """
        18F81280 电压电流SOC数据
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_BatteryToG0VoltRelTim: number [可选] - Pack电压
            s_DischrgCurrRelTim: number [可选] - Pack电流
            s_DispSOHCPct: integer [可选] - 显示SOH
            s_PackReportedSOCPct: number [可选] - 显示SOC
        """
        path = f'/api/batteryMock/v3/feign/do0X18F81280'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F82280(data):
        """
        18F82280 基础参数1
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_MaxCellVoltMv: number [可选]
            s_MaxCellVoltPstn: integer [可选]
            s_MinCellVoltMv: number [可选]
            s_MinCellVoltPstn: integer [可选]
        """
        path = f'/api/batteryMock/v3/feign/do0X18F82280'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F82580(data):
        """
        18F82580 输入电能量数据
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_HisAccumChrgEngyWh: number [可选] - 累计充电电能量值
            s_HisAccumChrgTimes: integer [可选] - 电池累计充电cycle
            s_HisThisTimChrgEngyWh: number [可选] - 本次充电能量值
        """
        path = f'/api/batteryMock/v3/feign/do0X18F82580'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F82680(data):
        """
        18F82680
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_HisAccumDisChrgCap: number [可选] - 累计充电容量值
            s_HisThisTimDisChrgCap: number [可选] - 本次放电容量值
        """
        path = f'/api/batteryMock/v3/feign/do0X18F82680'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do0X18F82780(data):
        """
        18F82780 输入容量数据
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_CalibrationCap: number [可选] - 电池箱额定容量
            s_HisAccumChrgCap: number [可选] - 累计充电容量值
            s_HisThisTimChrgCap: number [可选] - 本次充电容量值
        """
        path = f'/api/batteryMock/v3/feign/do0X18F82780'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do18F10880(data):
        """
        18F10880 Pack基础信息2
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            packType: integer [可选] - 电池包类型识别码
            s_AvgCellVolt: integer [可选] - 电芯平均电压 mV
            s_HVIL1State: integer [可选] - 高压互锁状态
            s_KL30Volt: number [可选] - KL30电压值 V
            s_KL30VoltVldBySafety: integer [可选] - KL30电压有效性
            s_TotalSumVoltV: number [可选] - 包内单体累加和电压 V
            s_TotalSumVoltVld: integer [可选] - 包内单体累加和电压有效性
        """
        path = f'/api/batteryMock/v3/feign/do18F10880'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do18F10D80(data):
        """
        18F10D80 绝缘信息
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_ExtIsoMeasNegResKOhm: integer [可选] - 负对地绝缘阻值 kΩ
            s_ExtIsoMeasPosResKOhm: integer [可选] - 正对地绝缘阻值 kΩ
            s_IsoMeasEnFlg: integer [可选] - 绝缘检测标志
            s_IsoMeasResVldBySafety: integer [可选] - 绝缘阻值有效性
            s_IsoMeasStatus: integer [可选] - 绝缘检测状态
        """
        path = f'/api/batteryMock/v3/feign/do18F10D80'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do18F20180(data):
        """
        18F20180 Pack详细电压信息1
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_CellVoltMv_N1: integer [可选] - N+1电池单体电压
            s_CellVoltMv_N2: integer [可选] - N+2电池单体电压
            s_CellVoltMv_N3: integer [可选] - N+3电池单体电压
            s_CellVoltMv_N4: integer [可选] - N+4电池单体电压
            s_CellVoltVld_N1: integer [可选] - N+1电池单体电压有效性
            s_CellVoltVld_N2: integer [可选] - N+2电池单体电压有效性
            s_CellVoltVld_N3: integer [可选] - N+3电池单体电压有效性
            s_CellVoltVld_N4: integer [可选] - N+4电池单体电压有效性
            s_volt_FrameNo: integer [可选] - 单体电压帧序号N，N从0开始，N最大到28
        """
        path = f'/api/batteryMock/v3/feign/do18F20180'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do18F30180(data):
        """
        18F30180 Pack详细温度信息1
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_ModuleTempDegCBranch_N1: number [可选]
            s_ModuleTempDegCBranch_N2: number [可选]
            s_ModuleTempDegCBranch_N3: number [可选]
            s_ModuleTempDegCBranch_N4: number [可选]
            s_ModuleTempDegCBranch_N5: number [可选]
            s_ModuleTempVldBranch_N1: integer [可选]
            s_ModuleTempVldBranch_N2: integer [可选]
            s_ModuleTempVldBranch_N3: integer [可选]
            s_ModuleTempVldBranch_N4: integer [可选]
            s_ModuleTempVldBranch_N5: integer [可选]
            s_ModuleTemp_FrameNo: integer [可选]
        """
        path = f'/api/batteryMock/v3/feign/do18F30180'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_do18F82480(data):
        """
        18F82480 输出电能量数据
        请求参数:
            batteryPosition: integer [可选] - 仓位号
            s_HisAccumDisChrgEngyWh: number [可选] - 累计放电电能量值
            s_HisThisTimDisChrgEngyWh: number [可选] - 本次放电能量值
        """
        path = f'/api/batteryMock/v3/feign/do18F82480'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryMock_v3_feign_sendMsg(data):
        """
        数据周期发送
        请求参数:
            chrgMode: integer [可选] - 充电模式 1:恒压模式 2:恒流模式
            s_BMSChrgStopErrReason: integer [可选] - 电池箱 BMS 中止充电错误原因
            s_BMSChrgStopFltReason: integer [可选] - 电池箱 BMS 中止充电故障原因
            s_BMSChrgStopReason: integer [可选] - 电池箱 BMS 中止充电原因
            s_BMSLVPowStatus: integer [可选]
            s_CellBalStatus: integer [可选] - 均衡状态0： =关闭， 1： =开启2： =故障，3： =不可用
            s_DCChargeTimesWrite: integer [可选]
            s_DischrgPwrLimContinueKw: number [可选] - 持续放电功率限值 Kw
            s_DischrgPwrLimLongKw: number [可选] - 长时放电功率限值 Kw
            s_DischrgPwrLimShortKw: number [可选] - 瞬时放电功率限值 Kw
            s_FanState: integer [可选] - 电池箱风扇状态0： =关闭，  1： =开启 2： =故障， 3： =不可用
            s_FltLevel: integer [可选] - 报警级别：0： 正常 1： 1级报警 3： 3级报警， 5： 5级报警； 其余为保留
            s_HVCnctrState: integer [可选] - 内部高压继电器状态0： =分开，  1： =预充 2： =闭合， 3： =不可用
            s_HeatRelayExternalVolt: number [可选] - 加热膜继电器外侧对主负内侧
            s_HeatRelayExternalVoltVld: integer [可选] - 加热膜继电器外侧对主负内侧电压有效性
            s_HeatState: integer [可选] - 加热状态0： =关闭 1： =开 2： =故障  3： =不可用
            s_HisStaOutAccumChrgerEngy: number [可选]
            s_HisStaOutReChrgEngy: number [可选]
            s_MainNegCnctrState: integer [可选] - 电池箱内部主负高压继电器状态0：分开，1:闭合
            s_MainPosCnctrState: integer [可选] - 电池箱内部主正高压继电器状态0：分开，1:闭合
            s_OnboardACChrgTimesOnceBatSwap: integer [可选]
            s_PACK_ALLW_MAX_CHRG_CURRENT: number [可选] - 电池箱能承受最大反馈电流值
            s_PACK_ALLW_MAX_DISCHRG_CURRENT: number [可选] - 电池箱能输出的最大电流值
            s_PackExternalVolt: number [可选] - LINk电压
            s_PackExternalVoltVld: integer [可选] - LINk电压有效性
            s_PackInternalVolt: number [可选] - Pack内测电压
            s_PackInternalVoltVld: integer [可选] - Pack内测电压有效性
            s_PackPlaceNum: integer [可选] - 电池箱所在位置编号
            s_PackWorkState: integer [可选] - 电池箱工作模式状态0： =未定义；1： =监控模式；2： =充电模式； 3： =储能模式；4： =换电准备模式；<5～7>： =预留；
            s_PosExternalVolt: number [可选] - 主正外侧对主负内侧电压
            s_PosExternalVoltVld: integer [可选] - 主正外侧对主负内侧电压有效性
            s_SynchroBatteryCurrentA: number [可选] - 与详细电压同步电流
            s_SynchroBatteryToG0Volt: number [可选] - 与详细电压同步电池包内侧电压
            vehiChrgCurrentReq: number [可选] - 车辆充电电流需求
            vehiChrgVoltReq: number [可选] - 车辆充电电压需求
        """
        path = f'/api/batteryMock/v3/feign/sendMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_get0X10E(data):
        """
        get0X10E
        """
        path = f'/api/chargerMock/feign/get0X10E'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_get0X26(data):
        """
        get0X26
        """
        path = f'/api/chargerMock/feign/get0X26'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_getBatteryDetail(data):
        """
        getBatteryDetail
        """
        path = f'/api/chargerMock/feign/getBatteryDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_getCampDetail(data):
        """
        getCampDetail
        请求参数:
        """
        path = f'/api/chargerMock/feign/getCampDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_initBatteryInfo(data):
        """
        initBatteryInfo
        请求参数:
            cellType: integer [可选] - 电芯类型
            ratedCapacity: number [可选] - 电池包额定能量 单位kwh 精度0.1KWh
            sbmuBootVersion: string [可选] - SBMU的BOOT版本
            sbmuCommunicationProtocolVersion: string [可选] - SBMU的通讯协议版本
            sbmuHardwareVersion: string [可选] - SBMU的硬件版本
            sbmuSoftwareVersion: string [可选] - SBMU的软件版本
            serialNum: string [可选] - 电池包SN、24位国标码
            lowerOfRetireSoc: number [可选] - 荣休SOC下限，精度0.001
            upperOfRetireSoc: number [可选] - 荣休SOC上限，精度0.001
            position: integer [可选] - 电池包所在仓位号
            cellStatisticsMockDTOS: array [可选]
                        cellBalRemainTime: number [可选]
                        cellId: integer [可选]
                        cellTotalBalCap: number [可选]
            chargedCapacityThisTime: number [可选] - 电池包本次充电容量 单位Ah，精度0.1
            totalChargedCycle: integer [可选] - 电池包累计充电总Cycle
            totalChargedPower: number [可选] - 电池包累计充电能量 单位kwh，精度0.1
            totalChargedPowerInStation: number [可选] - 电池包累计站内充电能量 单位kwh，精度0.1
            totalDischargedCycle: integer [可选] - 电池包累计放电总Cycle
            totalDischargedPower: number [可选] - 电池包累计放电能量 单位kwh，精度0.1
            totalDischargedPowerInStation: number [可选] - 电池包累计站内放电能量 单位kwh，精度0.1
            tripChargedPowerInStation: number [可选] - 电池包小计站内充电能量 单位kwh，精度0.1
            tripDischargedPowerInStation: number [可选] - 电池包小计站内放电能量 单位kwh，精度0.1
            avgCellVot: integer [可选] - 电池包平均单体电压 单位mV，精度1
            avgModuleTemp: number [可选] - 电池包平均模组温度 单位摄氏度，精度0.5
            cellSummaryVolt: number [可选] - 电池包电芯累加和（实时）
            chargeAllowFlag: integer [可选] - 电池包充电允许标志位 0 "不允许充电" 1 "允许充电"
            chargeDCR: number [可选] - 充电DCR
            chargeState: integer [可选] - 电池包充电状态 0 "默认" 1 "物理连接完成" 2 "低压辅助上电完成" 3 "收到CRM 00" 4 "握手完成" 5 "收到CML" 6 "BMS准备就绪" 7 "参数配置完成" 8 "充电中" 9 "充电完成" 10 "充电故障" 11 "预加热或保温中"
            chrgRemainTime: integer [可选] - 充电剩余时间
            current: number [可选] - 电池包电流(实时) 单位A，精度0.1
            currentSync: number [可选] - 电池包电流(同步)
            disChargeDCR: number [可选] - 放电DCR
            displaySoc: number [可选] - 电池包显示soc 单位%
            faultCodeList: array [可选] - 电池包故障码
            highVoltState: integer [可选] - 电池包高压状态
            hvilState: integer [可选] - 电池包高压互锁状态(实时状态) 0 "OK" 1 "Open"
            innerTotalVolt: number [可选] - 电池包内部总电压 单位V, 精度0.1
            innerTotalVoltSync: number [可选] - 电池包内部总电压（同步）
            labelUnavailableFlag: integer [可选] - 电池包编码不可信标志 2 "No Alarm" 1 "Alarm"
            mainNegativeConcatenateCircleState: integer [可选] - 电池包主负接触器线圈状态 "断开" 1"闭合" 2"粘连故障" 3"开路故障"
            mainPositiveConcatenateCircleState: integer [可选] - 电池包主正接触器线圈状态 0"断开" 1"闭合" 2"粘连故障" 3"开路故障"
            maxCellVolt: integer [可选] - 电池包最高单体电压 单位mV，精度1
            maxCellVoltPosition: integer [可选] - 电池包最高单体电压位置
            maxModuleTemp: number [可选] - 电池包最高模组温度 单位摄氏度，精度0.5
            maxModuleTempPosition: integer [可选] - 电池包最高模组温度位置
            maxRealSoc: number [可选] - 电池包最大真实soc 单位%
            minCellVolt: integer [可选] - 电池包最低单体电压 单位mV，精度1
            minCellVoltPosition: integer [可选] - 电池包最低单体电压位置
            minModuleTemp: number [可选] - 电池包最低模组温度 单位摄氏度，精度0.5
            minModuleTempPosition: integer [可选] - 电池包最低模组温度位置
            minRealSoc: number [可选] - 电池包最小真实soc 单位%
            mostCriticalFaultCode: string [可选] - 电池包最高等级故障码
            mostCriticalFaultLevel: integer [可选] - 电池包最高故障等级
            negativeInsulationValue: integer [可选] - 电池包负极绝缘值 单位kΩ,精度1
            outerTotalVolt: number [可选] - 电池包外部总电压 单位V, 精度0.1
            positiveInsulationValue: integer [可选] - 电池包正极绝缘值 单位kΩ,精度1
            realSoc: number [可选] - 电池包真实soc 单位%
            socAvailableFlag: integer [可选] - 电池包soc可信位标志
            soe: number [可选] - 电池包soe 单位kwh，精度0.0025
            soh: number [可选] - 电池包soh 单位%
        """
        path = f'/api/chargerMock/feign/initBatteryInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_protoMsg0X26Result(data):
        """
        protoMsg0X26Result
        请求参数:
            batteryOut: integer [可选] - 电池出仓结果 1-失败 2-成功
            clearFault: integer [可选] - 故障清除结果 1-失败 2-成功
            clearInStationSubtotal: integer [可选] - 站外小计清除结果 1-失败 2-成功
            clearOutStationSubtotal: integer [可选] - 站外小计清除结果 1-失败 2-成功
            closeHVContactor: integer [可选] - 电池下高压结果 1-失败 2-成功
            position: integer [可选] - 仓位号
        """
        path = f'/api/chargerMock/feign/protoMsg0X26Result'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_update0X26(data):
        """
        updateControlResponse
        请求参数:
            battyOutStaRuquest_Feedback: integer [可选] - 收到电池包出仓请求 0 "未收到" 1 "收到"
            battyOutStaSts: integer [可选] - 反馈电池包出仓请求结果 0 "默认" 1 "Ready"
            fbforBatSwapStat_Reserve1: integer [可选]
            fbforBatSwapStat_Reserve2: integer [可选]
            fltClearingRuquest_Feedback: integer [可选] - 收到故障清除请求 0 "未收到" 1 "收到"
            fltClearingSts: integer [可选] - 故障清除结果 0 "默认" 1 "失败" 2 "成功"
            packhvopenRuquest_Feedback: integer [可选]
            packhvopenSts: integer [可选]
            position: integer [可选] - 仓位号
            subInfoInClrRuquest_Feedback: integer [可选] - 收到站内小计信息清除请求 0 "未收到" 1 "收到"
            subInfoInClrSts: integer [可选] - 站内小计信息清除结果 0 "默认" 1 "失败" 2 "成功"
            subInfoOutClrRuquest_Feedback: integer [可选] - 收到站外小计信息清除请求 0 "未收到" 1 "收到"
            subInfoOutClrSts: integer [可选] - 站外小计信息清除结果 0 "默认" 1 "失败" 2 "成功"
        """
        path = f'/api/chargerMock/feign/update0X26'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_updateBatteryDetail(data):
        """
        updateBatteryDetail
        请求参数:
            cellType: integer [可选] - 电芯类型
            ratedCapacity: number [可选] - 电池包额定能量 单位kwh 精度0.1KWh
            sbmuBootVersion: string [可选] - SBMU的BOOT版本
            sbmuCommunicationProtocolVersion: string [可选] - SBMU的通讯协议版本
            sbmuHardwareVersion: string [可选] - SBMU的硬件版本
            sbmuSoftwareVersion: string [可选] - SBMU的软件版本
            serialNum: string [可选] - 电池包SN、24位国标码
            lowerOfRetireSoc: number [可选] - 荣休SOC下限，精度0.001
            upperOfRetireSoc: number [可选] - 荣休SOC上限，精度0.001
            position: integer [可选] - 电池包所在仓位号
            cellStatisticsMockDTOS: array [可选]
                        cellBalRemainTime: number [可选]
                        cellId: integer [可选]
                        cellTotalBalCap: number [可选]
            chargedCapacityThisTime: number [可选] - 电池包本次充电容量 单位Ah，精度0.1
            totalChargedCycle: integer [可选] - 电池包累计充电总Cycle
            totalChargedPower: number [可选] - 电池包累计充电能量 单位kwh，精度0.1
            totalChargedPowerInStation: number [可选] - 电池包累计站内充电能量 单位kwh，精度0.1
            totalDischargedCycle: integer [可选] - 电池包累计放电总Cycle
            totalDischargedPower: number [可选] - 电池包累计放电能量 单位kwh，精度0.1
            totalDischargedPowerInStation: number [可选] - 电池包累计站内放电能量 单位kwh，精度0.1
            tripChargedPowerInStation: number [可选] - 电池包小计站内充电能量 单位kwh，精度0.1
            tripDischargedPowerInStation: number [可选] - 电池包小计站内放电能量 单位kwh，精度0.1
            avgCellVot: integer [可选] - 电池包平均单体电压 单位mV，精度1
            avgModuleTemp: number [可选] - 电池包平均模组温度 单位摄氏度，精度0.5
            cellSummaryVolt: number [可选] - 电池包电芯累加和（实时）
            chargeAllowFlag: integer [可选] - 电池包充电允许标志位 0 "不允许充电" 1 "允许充电"
            chargeDCR: number [可选] - 充电DCR
            chargeState: integer [可选] - 电池包充电状态 0 "默认" 1 "物理连接完成" 2 "低压辅助上电完成" 3 "收到CRM 00" 4 "握手完成" 5 "收到CML" 6 "BMS准备就绪" 7 "参数配置完成" 8 "充电中" 9 "充电完成" 10 "充电故障" 11 "预加热或保温中"
            chrgRemainTime: integer [可选] - 充电剩余时间
            current: number [可选] - 电池包电流(实时) 单位A，精度0.1
            currentSync: number [可选] - 电池包电流(同步)
            disChargeDCR: number [可选] - 放电DCR
            displaySoc: number [可选] - 电池包显示soc 单位%
            faultCodeList: array [可选] - 电池包故障码
            highVoltState: integer [可选] - 电池包高压状态
            hvilState: integer [可选] - 电池包高压互锁状态(实时状态) 0 "OK" 1 "Open"
            innerTotalVolt: number [可选] - 电池包内部总电压 单位V, 精度0.1
            innerTotalVoltSync: number [可选] - 电池包内部总电压（同步）
            labelUnavailableFlag: integer [可选] - 电池包编码不可信标志 2 "No Alarm" 1 "Alarm"
            mainNegativeConcatenateCircleState: integer [可选] - 电池包主负接触器线圈状态 "断开" 1"闭合" 2"粘连故障" 3"开路故障"
            mainPositiveConcatenateCircleState: integer [可选] - 电池包主正接触器线圈状态 0"断开" 1"闭合" 2"粘连故障" 3"开路故障"
            maxCellVolt: integer [可选] - 电池包最高单体电压 单位mV，精度1
            maxCellVoltPosition: integer [可选] - 电池包最高单体电压位置
            maxModuleTemp: number [可选] - 电池包最高模组温度 单位摄氏度，精度0.5
            maxModuleTempPosition: integer [可选] - 电池包最高模组温度位置
            maxRealSoc: number [可选] - 电池包最大真实soc 单位%
            minCellVolt: integer [可选] - 电池包最低单体电压 单位mV，精度1
            minCellVoltPosition: integer [可选] - 电池包最低单体电压位置
            minModuleTemp: number [可选] - 电池包最低模组温度 单位摄氏度，精度0.5
            minModuleTempPosition: integer [可选] - 电池包最低模组温度位置
            minRealSoc: number [可选] - 电池包最小真实soc 单位%
            mostCriticalFaultCode: string [可选] - 电池包最高等级故障码
            mostCriticalFaultLevel: integer [可选] - 电池包最高故障等级
            negativeInsulationValue: integer [可选] - 电池包负极绝缘值 单位kΩ,精度1
            outerTotalVolt: number [可选] - 电池包外部总电压 单位V, 精度0.1
            positiveInsulationValue: integer [可选] - 电池包正极绝缘值 单位kΩ,精度1
            realSoc: number [可选] - 电池包真实soc 单位%
            socAvailableFlag: integer [可选] - 电池包soc可信位标志
            soe: number [可选] - 电池包soe 单位kwh，精度0.0025
            soh: number [可选] - 电池包soh 单位%
        """
        path = f'/api/chargerMock/feign/updateBatteryDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerMock_feign_updateCampDetail(data):
        """
        updateCampDetail
        请求参数:
            cellType: integer [可选] - 电芯类型
            ratedCapacity: number [可选] - 电池包额定能量 单位kwh 精度0.1KWh
            sbmuBootVersion: string [可选] - SBMU的BOOT版本
            sbmuCommunicationProtocolVersion: string [可选] - SBMU的通讯协议版本
            sbmuHardwareVersion: string [可选] - SBMU的硬件版本
            sbmuSoftwareVersion: string [可选] - SBMU的软件版本
            serialNum: string [可选] - 电池包SN、24位国标码
            lowerOfRetireSoc: number [可选] - 荣休SOC下限，精度0.001
            upperOfRetireSoc: number [可选] - 荣休SOC上限，精度0.001
            position: integer [可选] - 电池包所在仓位号
            cellStatisticsMockDTOS: array [可选]
                        cellBalRemainTime: number [可选]
                        cellId: integer [可选]
                        cellTotalBalCap: number [可选]
            chargedCapacityThisTime: number [可选] - 电池包本次充电容量 单位Ah，精度0.1
            totalChargedCycle: integer [可选] - 电池包累计充电总Cycle
            totalChargedPower: number [可选] - 电池包累计充电能量 单位kwh，精度0.1
            totalChargedPowerInStation: number [可选] - 电池包累计站内充电能量 单位kwh，精度0.1
            totalDischargedCycle: integer [可选] - 电池包累计放电总Cycle
            totalDischargedPower: number [可选] - 电池包累计放电能量 单位kwh，精度0.1
            totalDischargedPowerInStation: number [可选] - 电池包累计站内放电能量 单位kwh，精度0.1
            tripChargedPowerInStation: number [可选] - 电池包小计站内充电能量 单位kwh，精度0.1
            tripDischargedPowerInStation: number [可选] - 电池包小计站内放电能量 单位kwh，精度0.1
            avgCellVot: integer [可选] - 电池包平均单体电压 单位mV，精度1
            avgModuleTemp: number [可选] - 电池包平均模组温度 单位摄氏度，精度0.5
            cellSummaryVolt: number [可选] - 电池包电芯累加和（实时）
            chargeAllowFlag: integer [可选] - 电池包充电允许标志位 0 "不允许充电" 1 "允许充电"
            chargeDCR: number [可选] - 充电DCR
            chargeState: integer [可选] - 电池包充电状态 0 "默认" 1 "物理连接完成" 2 "低压辅助上电完成" 3 "收到CRM 00" 4 "握手完成" 5 "收到CML" 6 "BMS准备就绪" 7 "参数配置完成" 8 "充电中" 9 "充电完成" 10 "充电故障" 11 "预加热或保温中"
            chrgRemainTime: integer [可选] - 充电剩余时间
            current: number [可选] - 电池包电流(实时) 单位A，精度0.1
            currentSync: number [可选] - 电池包电流(同步)
            disChargeDCR: number [可选] - 放电DCR
            displaySoc: number [可选] - 电池包显示soc 单位%
            faultCodeList: array [可选] - 电池包故障码
            highVoltState: integer [可选] - 电池包高压状态
            hvilState: integer [可选] - 电池包高压互锁状态(实时状态) 0 "OK" 1 "Open"
            innerTotalVolt: number [可选] - 电池包内部总电压 单位V, 精度0.1
            innerTotalVoltSync: number [可选] - 电池包内部总电压（同步）
            labelUnavailableFlag: integer [可选] - 电池包编码不可信标志 2 "No Alarm" 1 "Alarm"
            mainNegativeConcatenateCircleState: integer [可选] - 电池包主负接触器线圈状态 "断开" 1"闭合" 2"粘连故障" 3"开路故障"
            mainPositiveConcatenateCircleState: integer [可选] - 电池包主正接触器线圈状态 0"断开" 1"闭合" 2"粘连故障" 3"开路故障"
            maxCellVolt: integer [可选] - 电池包最高单体电压 单位mV，精度1
            maxCellVoltPosition: integer [可选] - 电池包最高单体电压位置
            maxModuleTemp: number [可选] - 电池包最高模组温度 单位摄氏度，精度0.5
            maxModuleTempPosition: integer [可选] - 电池包最高模组温度位置
            maxRealSoc: number [可选] - 电池包最大真实soc 单位%
            minCellVolt: integer [可选] - 电池包最低单体电压 单位mV，精度1
            minCellVoltPosition: integer [可选] - 电池包最低单体电压位置
            minModuleTemp: number [可选] - 电池包最低模组温度 单位摄氏度，精度0.5
            minModuleTempPosition: integer [可选] - 电池包最低模组温度位置
            minRealSoc: number [可选] - 电池包最小真实soc 单位%
            mostCriticalFaultCode: string [可选] - 电池包最高等级故障码
            mostCriticalFaultLevel: integer [可选] - 电池包最高故障等级
            negativeInsulationValue: integer [可选] - 电池包负极绝缘值 单位kΩ,精度1
            outerTotalVolt: number [可选] - 电池包外部总电压 单位V, 精度0.1
            positiveInsulationValue: integer [可选] - 电池包正极绝缘值 单位kΩ,精度1
            realSoc: number [可选] - 电池包真实soc 单位%
            socAvailableFlag: integer [可选] - 电池包soc可信位标志
            soe: number [可选] - 电池包soe 单位kwh，精度0.0025
            soh: number [可选] - 电池包soh 单位%
        """
        path = f'/api/chargerMock/feign/updateCampDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_dcciMock_feign_send4534(data):
        """
        充电设备响应升级请求4534
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            failedReason: integer [可选] - 失败原因
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            result: integer [可选] - 应答结果
        """
        path = f'/api/dcciMock/feign/send4534'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_dcciMock_feign_send4535(data):
        """
        充电设备上送升级状态4535
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            downLoadFailedReason: integer [可选] - 下载失败原因
            fileUrl: string [可选] - 文件URL
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            upgradeStatus: integer [可选] - 升级状态
            upgradeType: integer [可选] - 升级类型
        """
        path = f'/api/dcciMock/feign/send4535'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_dcciMock_feign_send4537(data):
        """
        充电设备上送BMS种子(4537)
        请求参数:
            chargerNo: integer [可选] - 充电机编号
            gunNo: integer [可选] - 充电枪编号（1~12）
            position: integer [可选] - 仓位号
            seed: string [可选] - bms种子
        """
        path = f'/api/dcciMock/feign/send4537'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualBattery._get_path(path), 'POST', data))
