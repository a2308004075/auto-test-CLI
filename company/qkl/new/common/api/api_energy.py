from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiEnergy:
    @staticmethod
    def _get_path(path):
        service = '/energy'
        return service + path

    @staticmethod
    def api_chargerDcco_startCharge(data):
        """
        startCharge
        请求参数:
            adjustParam: number [可选] - 功率调节参数 功率调节指令为1时，不做限制; 功率调节指令为2时，Factor：0.1 单位：kW； 功率调节指令为3时执行，Factor：1; 单位：%； 功率调节指令为4时执行，Factor：0.1 单位：A；
            adjustType: integer [可选] - 功率调节指令类型 1:采用BMS充电Map进行功率控制 2:执行功率调节，设置充电功率上限值 3:采用充电map比列调节 4:执行最大电流限制
            campNo: integer [可选] - 充电仓位号
            chargeModel: integer [可选] - 充电来源
            chargerNo: integer [可选] - 充电桩号
            cloudFlowNo: string [可选] - 云端流水号
            controlParam: integer [可选] - 控制参数
            controlType: integer [可选] - 控制类型
            direction: integer [可选] - 充电方向 0:充电 1:放电 字典：chargeDirection
            endSoc: number [可选] - 停充SOC
            gunNo: integer [可选] - 充电枪号
        """
        path = f'/api/chargerDcco/startCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_stopCharge(data):
        """
        stopCharge
        请求参数:
            cloudFlowNo: string [可选] - 云端流水号
            flowNo: string [可选] - 充电机交互流水号
            position: integer [可选] - 仓位号
            stopReason: integer [可选] - 1.停止原因 0正常充满停机 1服务器发现桩异常,强制停机 2 账号校验失败 3APP主动停机 4 账号欠费 5无可用模块
        """
        path = f'/api/chargerDcco/stopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_energy_energyJudge(data):
        """
        需求功率判断
        请求参数:
            demandPower: number [可选] - 需求功率
            transformerBoxNo: integer [可选] - 箱变号
        """
        path = f'/api/energy/energyJudge'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_energy_feign_config_getStorageStrategy(data):
        """
        getStorageStrategy
        """
        path = f'/api/energy/feign/config/getStorageStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_energy_feign_config_saveStorageStrategy(data):
        """
        saveStorageStrategy
        请求参数:
            antiBackFlowCurrentPower: number [可选] - 防逆流 实时需求总功率
            antiBackFlowTransformerPower: number [可选] - 防逆流 箱变输出侧实时功率
            chargePower: number [可选] - 储能充电 功率限制
            chargeTm: number [可选] - 储能充电 持续时间
            dischargeSoc: number [可选] - 储能放电 允许放电soc
            dischargeStartPower: number [可选] - 储能放电 放电启动条件 功率限制
            dischargeStopPower: number [可选] - 储能放电 放电停止条件 功率限制
            enable: boolean [可选] - 策略启动状态
            powerDif: number [可选] - 通用配置 本次功率和上次功率差值
        """
        path = f'/api/energy/feign/config/saveStorageStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_energy_feign_config_saveTransformerBox(data):
        """
        saveTransformerBox
        请求参数:
            chargers: array [可选] - 充电机列表
                        no: integer [可选] - 充电机编号
                        powerLimit: number [可选] - 功率限制
            containOther: boolean [可选] - 是否包含其他设备
            emus: array [可选] - EMU列表
                        no: integer [可选] - EMU编号
            id: integer [可选] - id
            powerLimit: number [可选] - 功率限制
        """
        path = f'/api/energy/feign/config/saveTransformerBox'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_chargeRecord(data):
        """
        chargeRecord
        请求参数:
            averageElectricQuantity: number [可选]
            batterySn: string [可选]
            campTotalChargeTime: number [可选]
            cardBalanceAfterCharge: number [可选]
            cardBalanceBeforeCharge: number [可选]
            chargeAmount: number [可选]
            chargeEndTime: string [可选]
            chargePeriodCount: integer [可选]
            chargePower: number [可选]
            chargeStartTime: string [可选]
            chargerNo: integer [可选]
            cloudFlowNo: string [可选]
            controlParam: integer [可选]
            controlType: integer [可选]
            direction: integer [可选]
            electricMeterAfterCharge: number [可选]
            electricMeterBeforeCharge: number [可选]
            factoryStopReason: integer [可选]
            flowNo: string [可选]
            gunNo: integer [可选]
            peakElectricQuantity: number [可选]
            periodList: array [可选]
                        chargePower: number [可选]
                        index: integer [可选]
                        periodIdentity: integer [可选]
                        startTime: string [可选]
            position: integer [可选]
            socAfterCharge: number [可选]
            socBeforeCharge: number [可选]
            startupMethod: integer [可选]
            stopReason: integer [可选]
            stopResult: integer [可选]
            timePeriodChargingAmount: array [可选]
            tipCharge: number [可选]
            totalDeepValleyCharge: number [可选]
            totalFlatCharge: number [可选]
            totalPeakCharge: number [可选]
            totalSharpCharge: number [可选]
            totalValleyCharge: number [可选]
            valleyElectricity: number [可选]
            vin: string [可选]
        """
        path = f'/api/virtualMqtt/chargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_chargeRecordResp(data):
        """
        chargeRecordResp
        请求参数:
            chargeCardNo: string [可选]
            chargeGunNo: integer [可选]
            msgId: integer [可选]
            reserved1: integer [可选]
            reserved2: integer [可选]
        """
        path = f'/api/virtualMqtt/chargeRecordResp'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_del(data):
        """
        pileHeartBeat
        请求参数:
        """
        path = f'/api/virtualMqtt/del'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_mock4200(data):
        """
        mock4200
        请求参数:
            averageElectricQuantity: number [可选]
            batterySn: string [可选]
            campTotalChargeTime: number [可选]
            cardBalanceAfterCharge: number [可选]
            cardBalanceBeforeCharge: number [可选]
            chargeAmount: number [可选]
            chargeEndTime: string [可选]
            chargePeriodCount: integer [可选]
            chargePower: number [可选]
            chargeStartTime: string [可选]
            chargerNo: integer [可选]
            cloudFlowNo: string [可选]
            controlParam: integer [可选]
            controlType: integer [可选]
            direction: integer [可选]
            electricMeterAfterCharge: number [可选]
            electricMeterBeforeCharge: number [可选]
            factoryStopReason: integer [可选]
            flowNo: string [可选]
            gunNo: integer [可选]
            peakElectricQuantity: number [可选]
            periodList: array [可选]
                        chargePower: number [可选]
                        index: integer [可选]
                        periodIdentity: integer [可选]
                        startTime: string [可选]
            position: integer [可选]
            socAfterCharge: number [可选]
            socBeforeCharge: number [可选]
            startupMethod: integer [可选]
            stopReason: integer [可选]
            stopResult: integer [可选]
            timePeriodChargingAmount: array [可选]
            tipCharge: number [可选]
            totalDeepValleyCharge: number [可选]
            totalFlatCharge: number [可选]
            totalPeakCharge: number [可选]
            totalSharpCharge: number [可选]
            totalValleyCharge: number [可选]
            valleyElectricity: number [可选]
            vin: string [可选]
        """
        path = f'/api/virtualMqtt/mock4200'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_mock4501(data):
        """
        mock4501
        请求参数:
        """
        path = f'/api/virtualMqtt/mock4501'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_mock4511(data):
        """
        mock4511
        请求参数:
        """
        path = f'/api/virtualMqtt/mock4511'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_mock4900(data):
        """
        mock4900
        请求参数:
            chargerNo: integer [可选]
            cloudFlowNo: string [可选]
            failedReason: integer [可选]
            failedReasonDetail: string [可选]
            flowNo: string [可选]
            gunNo: integer [可选]
            position: integer [可选]
            result: integer [可选]
        """
        path = f'/api/virtualMqtt/mock4900'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_pileEquipInfo(data):
        """
        pileEquipInfo
        请求参数:
            acurrent: integer [可选]
            airInletTem: integer [可选]
            airOutTem: integer [可选]
            avoltage: number [可选]
            bcurrent: integer [可选]
            bmsChargeMode: integer [可选]
            bmsCurrent: number [可选]
            bmsVoltage: number [可选]
            bookFlag: integer [可选]
            bvoltage: number [可选]
            cardAmount: number [可选]
            ccurrent: integer [可选]
            chargeCapacity: number [可选]
            chargeCase: integer [可选]
            chargeCost: number [可选]
            chargeDuration: integer [可选]
            chargeGunNo: integer [可选]
            chargeGunNum: integer [可选]
            chargeGunType: integer [可选]
            chargeMeterReading: number [可选]
            chargeMode: integer [可选]
            chargeParam: integer [可选]
            chargePower: number [可选]
            chargeStartType: integer [可选]
            connectStatus: integer [可选]
            connectVoltage: number [可选]
            currentMeterReading: number [可选]
            cvoltage: number [可选]
            dcCurrent: number [可选]
            dcVoltage: number [可选]
            dischargeCurrent: number [可选]
            dischargeMeterReading: number [可选]
            moduleMaxTem: integer [可选]
            moduleMinTem: integer [可选]
            moduleNum: integer [可选]
            msgId: integer [可选]
            orderNo: string [可选]
            overTime: integer [可选]
            pileCode: string [可选]
            pileTem: integer [可选]
            portTemDeep: integer [可选]
            portTemPlus: integer [可选]
            remainChargingTime: integer [可选]
            reserved1: integer [可选]
            reserved2: integer [可选]
            reserved3: integer [可选]
            soc: integer [可选]
            startChargeTime: integer [可选]
            warnStatus: integer [可选]
            workStatus: integer [可选]
        """
        path = f'/api/virtualMqtt/pileEquipInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_pileEquipInfoResp(data):
        """
        pileEquipInfoResp
        请求参数:
            amount: number [可选]
            boostChargeStatus: integer [可选]
            chargeCardNo: string [可选]
            chargeGunNo: integer [可选]
            isEnough: integer [可选]
            msgId: integer [可选]
            reserved1: integer [可选]
        """
        path = f'/api/virtualMqtt/pileEquipInfoResp'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_pileEventInfo(data):
        """
        pileEventInfo
        请求参数:
            chargeGunNo: integer [可选]
            eventCode: integer [可选]
            eventParam: string [可选]
            msgId: integer [可选]
            orderNo: string [可选]
            reserved1: integer [可选]
            reserved2: integer [可选]
        """
        path = f'/api/virtualMqtt/pileEventInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_pileEventInfoResp(data):
        """
        pileEventInfoResp
        请求参数:
            chargeGunNo: integer [可选]
            eventName: integer [可选]
            msgId: integer [可选]
            pileCode: string [可选]
            reserved1: integer [可选]
            reserved2: integer [可选]
        """
        path = f'/api/virtualMqtt/pileEventInfoResp'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_pileHeartBeat(data):
        """
        pileHeartBeat
        请求参数:
            heartNum: integer [可选]
            msgId: integer [可选]
            pileCode: string [可选]
            reserved1: integer [可选]
            reserved2: integer [可选]
        """
        path = f'/api/virtualMqtt/pileHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_pileHeartBeatResp(data):
        """
        pileHeartBeatResp
        请求参数:
            heartNum: integer [可选]
            msgId: integer [可选]
            reserved1: integer [可选]
            reserved2: integer [可选]
        """
        path = f'/api/virtualMqtt/pileHeartBeatResp'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_pileSignIn(data):
        """
        pileSignIn
        请求参数:
            bootCount: integer [可选] - 启动次数，终端每次启动计数保存
            ccu2SoftwareVersion: string [可选] - 充电桩CCU2软件版本，0x00010000代表版本0.1.0.0
            ccuSoftwareVersion: string [可选] - 充电桩CCU软件版本，0x00010000代表版本0.1.0.0
            chargeRecordCount: integer [可选] - 充电记录数量
            gunCount: integer [可选] - 充电枪个数
            heartBeatPeriod: integer [可选] - 心跳上报周期，单位：秒
            heartBeatTimeoutCount: integer [可选] - 心跳包检测超时次数
            lastBootTime: integer [可选] - 最近一次启动时间，标准时间
            lastChargeTime: integer [可选] - 最近一次充电时间，标准时间
            macOrImei: string [可选] - 充电桩Mac地址或者IMEI码，ASCII编码，以'\0'结束
            msgId: integer [可选]
            offlineChargeSetting: integer [可选] - 离线/在线允许充电设置，默认值0x01，高位0表示在线允许充电，低位1表示离线禁止充电
            pcuSoftwareVersion: string [可选] - 充电桩PCU软件版本，0x00010000代表版本0.1.0.0
            pileCode: string [可选] - 充电桩编码，ASCII编码
            pileType: integer [可选] - 充电桩类型：0x00-直流，0x01-交流，0x02-混合
            signInInterval: integer [可选] - 签到间隔时间，单位：分钟，默认15分钟
            signInPassword: string [可选] - 签到密码（保留），ASCII编码，以'\0'结束
            softwareVersion: string [可选] - TCU充电桩软件版本原始数值，如65536对应0x00010000，版本0.1.0.0
            systemTime: string [可选] - 当前充电桩系统时间，标准时间
            tcuFlag: integer [可选] - 小桔TCU标识：0-sdk，1-tcu
            totalPower: integer [可选] - 充电桩电源模块总功率大小，单位：kW
            totalPowerModuleCount: integer [可选] - 该充电桩总共电源模块数
            uploadMode: integer [可选] - 数据上传模式（保留）：1-应答模式，2-主动上报模式
        """
        path = f'/api/virtualMqtt/pileSignIn'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_pileSignInResp(data):
        """
        pileSignInResp
        请求参数:
            msgId: integer [可选]
            reserved1: integer [可选] - 预留1
            reserved2: integer [可选] - 预留2
            serverTime: integer [可选] - 标准时钟时间
        """
        path = f'/api/virtualMqtt/pileSignInResp'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_sendMsg(data):
        """
        sendMsg
        请求参数:
            chargeEventKeyCode: integer [可选] - 云协议事件Code
            sendMsgJson: string [可选] - 云协议事件对应json数据
        """
        path = f'/api/virtualMqtt/sendMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_sendMsgWithRetry(data):
        """
        sendMsgWithRetry
        请求参数:
            chargeEventKeyCode: integer [可选] - 云协议事件Code
            sendMsgJson: string [可选] - 云协议事件对应json数据
        """
        path = f'/api/virtualMqtt/sendMsgWithRetry'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_startCharge(data):
        """
        startCharge
        请求参数:
            chargeGunNo: integer [可选]
            msgId: integer [可选]
            orderNo: string [可选]
            pileCode: string [可选]
            reserved1: integer [可选]
            reserved2: integer [可选]
            runResult: string [可选]
        """
        path = f'/api/virtualMqtt/startCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_startChargeResp(data):
        """
        startChargeResp
        请求参数:
            chargeFlag: integer [可选]
            chargeGunNo: integer [可选]
            chargeStrategy: integer [可选]
            chargeStrategyParam: integer [可选]
            chargeType: integer [可选]
            delayFeeFlag: integer [可选]
            delayFeeWaitTime: integer [可选]
            msgId: integer [可选]
            offLineChargePower: number [可选]
            orderNo: string [可选]
            overTime: integer [可选]
            reserved1: integer [可选]
            reserved2: integer [可选]
            scheduleStartTime: integer [可选]
            userPhoneSuffix: integer [可选]
        """
        path = f'/api/virtualMqtt/startChargeResp'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_stopCharge(data):
        """
        stopCharge
        请求参数:
            chargeGunNo: integer [可选]
            msgId: integer [可选]
            orderNo: string [可选]
            pileCode: string [可选]
            result: string [可选]
        """
        path = f'/api/virtualMqtt/stopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))

    @staticmethod
    def api_virtualMqtt_stopChargeResp(data):
        """
        stopChargeResp
        请求参数:
            chargeGunNo: integer [可选]
            msgId: integer [可选]
            orderNo: string [可选]
            pileCode: string [可选]
        """
        path = f'/api/virtualMqtt/stopChargeResp'
        return HttpRq.req(*HttpMethod.http_info(ApiEnergy._get_path(path), 'POST', data))
