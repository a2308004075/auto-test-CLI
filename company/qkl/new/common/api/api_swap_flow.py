from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiSwapFlow:
    @staticmethod
    def _get_path(path):
        service = '/swap-flow'
        return service + path

    @staticmethod
    def api_cloudMqtt_airControl(data):
        """
        空调控制(云->站)
        请求参数:
            airNo: integer [可选] - 空调编号
            airSwitch: integer [可选] - 空调开关 1-启动 2-停止
            coolTemp: number [可选] - 制冷启动温度
            coolTempDiff: number [可选] - 制冷停止回差值
            dehumidifyDiff: number [可选] - 除湿停止回差值
            dehumidifySwitch: integer [可选] - 除湿使能 1-启动 2-停止
            dehumidifyValue: number [可选] - 除湿开启湿度值
            highTempAlarm: number [可选] - 高温告警温度值
            hotTemp: number [可选] - 制热启动温度
            hotTempDiff: number [可选] - 制热停止回差值
            lowTempAlarm: number [可选] - 低温告警温度值
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/airControl'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_airControllerControl(data):
        """
        【云->站】空调控制器控制
        请求参数:
            controlCommand: integer [可选]
            msgId: integer [可选]
            parameterType: integer [可选]
        """
        path = f'/api/cloudMqtt/airControllerControl'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_authentication(data):
        """
        【站->云】云端登录响应
        请求参数:
            msgId: integer [可选]
            success: boolean [可选]
        """
        path = f'/api/cloudMqtt/authentication'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_blockBattery(data):
        """
        【云->站】电池通缉
        请求参数:
            blockBatteryList: array [可选] - 电池通缉列表
                        batteryNum: integer [可选] - 用户选择换电数
                        bluetoothConnectMode: integer [可选] - 连接方式
                        carNo: string [可选] - 车牌
                        freedomRules: array [可选] - 自由度列表
                                    checkState: integer [可选] - 自由度调整启用状态
                                    code: string [可选] - 自由度调整类型编码
                        mbmuIrk: string [可选] - 车机irk
                        modelCode: string [可选] - 车辆型号（需要统一的数据维护）
                        oob: string [可选] - oob
                        phone: string [可选] - 用户手机号
                        selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
                        supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
                        swapFlowKey: string [可选] - 换电流程编号
                        vbleMac: string [可选] - vbleMac蓝牙mac地址
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/blockBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_carStopped(data):
        """
        【站->云】上报车辆停稳
        请求参数:
            carNo: string [可选] - 车辆牌照
            cloudStatus: integer [可选] - 换电状态 0：道闸开启 1-车辆进站 2-车辆停稳 3-开始换电 4-拆卸电池 5-安装电池 6-换电完成 7-车辆驶离
            msgId: integer [可选]
            orderId: string [可选] - 云下发的换电订单id
            sbmuInfo: array [可选] - 上次换电结束车上电池信息
                        installAddress: integer [可选] - 电池所在位置（1或2）
                        lastLockTurnsCount: array [可选] - 上次加锁圈数
                                    lockNo: integer [可选] - 锁编号
                                    turnsCount: number [可选] - 加锁圈数
                        packSN: string [可选] - 电池SN
                        packType: integer [可选] - 电池包类别 0-未安装电池包 1-C1N-53-264 2-C1N-70-274 3-假包 4-LFP_25_01_L 5-LFP_20_01_L
                        sbmuMac: string [可选] - 电池mac地址
        """
        path = f'/api/cloudMqtt/carStopped'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_carStoppedResp(data):
        """
        【云->站】车辆停稳应答
        请求参数:
            carNo: string [可选] - 车牌号
            msgId: integer [可选]
            orderId: string [可选] - 云下发的换电订单id
            result: integer [可选] - 云端处理结果： 0-云端处理异常 1-成功 2-已上报人工/离线单 3-车上电池不合法
        """
        path = f'/api/cloudMqtt/carStoppedResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_changeDutyMode(data):
        """
        【站->云】换电站值守模式上报
        请求参数:
            changeTime: integer [可选] - 切换时间
            dutyMode: integer [可选] - 值守模式 1-无人值守  2-有人值守
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/changeDutyMode'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_changeDutyModeResp(data):
        """
        【云->站】换电站值守模式上报应答
        请求参数:
            msgId: integer [可选]
            result: integer [可选] - 云端处理结果：0失败 1成功
        """
        path = f'/api/cloudMqtt/changeDutyModeResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_changePowerDone(data):
        """
        【站->云】换电完成
        请求参数:
            blueToothMacAddress: string [可选]
            blueToothSignalStrength: string [可选]
            blueToothSignalStrengthVbleToSble: string [可选]
            carModel: string [可选]
            carNo: string [可选]
            carSwapCount: integer [可选]
            carVin: string [可选]
            clearedSubtotalStatus: integer [可选]
            closeBtStatus: integer [可选]
            cloudCarVin: string [可选]
            cloudOrderId: string [可选]
            cloudUserId: string [可选]
            createEndTime: string [可选]
            createStartTime: string [可选]
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            failReason: string [可选]
            flowCreateType: integer [可选]
            flowNo: string [可选]
            flowStatus: integer [可选]
            flowType: integer [可选]
            id: integer [可选]
            ids: array [可选]
            mbmuHardwareVersion: string [可选]
            mbmuSoftwareVersion: string [可选]
            procInstId: string [可选]
            remark: string [可选]
            requestId: string [可选]
            selectPackageType: integer [可选]
            size: integer [可选]
            swapEndTime: string [可选]
            swapStartTime: string [可选]
            sysSubTotalChargeTimesOutStation: integer [可选]
            sysSubTotalRechargeTimesOutStation: integer [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            uploadFlag: integer [可选]
            uploadTime: string [可选]
            vbleHardwareVersion: string [可选]
            vbleSoftwareVersion: string [可选]
            vehTotalOdometer: string [可选]
        """
        path = f'/api/cloudMqtt/changePowerDone'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_changePowerDoneResp(data):
        """
        【云->站】换电完成应答
        请求参数:
            carNo: string [可选] - 车辆牌照
            msgId: integer [可选]
            orderId: string [可选] - 订单编号
            result: integer [可选] - 云端处理结果：0-失败 1-成功 2-已上报人工/离线单
            retryFlag: integer [可选] - 是否需要重试：（该字段没发默认需要重试）0-不重试 1-重试
        """
        path = f'/api/cloudMqtt/changePowerDoneResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_chargeRestriction(data):
        """
        【云->站】充电控制
        请求参数:
            adjustMode: integer [可选] - 云端下控变更当前充电策略 1：整站调节模式 2：仓位调节模式 3：本地模式 
            channelAdjustList: array [可选] - 云端下发仓位充电命令，下控换电站执行
                        batteryNum: integer [可选] - 用户选择换电数
                        bluetoothConnectMode: integer [可选] - 连接方式
                        carNo: string [可选] - 车牌
                        freedomRules: array [可选] - 自由度列表
                                    checkState: integer [可选] - 自由度调整启用状态
                                    code: string [可选] - 自由度调整类型编码
                        mbmuIrk: string [可选] - 车机irk
                        modelCode: string [可选] - 车辆型号（需要统一的数据维护）
                        oob: string [可选] - oob
                        phone: string [可选] - 用户手机号
                        selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
                        supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
                        swapFlowKey: string [可选] - 换电流程编号
                        vbleMac: string [可选] - vbleMac蓝牙mac地址
            msgId: integer [可选]
            stationAdjustCmd: integer [可选] - 整站充电启停命令 0：默认值1：停止充电2：开启充电
        """
        path = f'/api/cloudMqtt/chargeRestriction'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_chargeRestrictionResp(data):
        """
        【站->云】充电控制命令接收应答
        请求参数:
            failReason: string [可选]
            msgId: integer [可选]
            result: integer [可选]
        """
        path = f'/api/cloudMqtt/chargeRestrictionResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_chargeRestrictionResult(data):
        """
        【站->云】充电控制执行应答
        请求参数:
            allow: integer [可选] - 是否允许换电。1 允许换电，2不允许换电
            carNo: string [可选] - 车牌号
            msgId: integer [可选]
            orderId: string [可选] - 云下发的换电订单id
        """
        path = f'/api/cloudMqtt/chargeRestrictionResult'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_clearBmsFault(data):
        """
        【云->站】清除BMS故障码
        请求参数:
            clear: integer [可选]
            deviceCodeList: array [可选]
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/clearBmsFault'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_cloudConfigAsyncStation(data):
        """
        云配置下发（云到站）
        请求参数:
            configType: string [可选]
            configTypeParams: string [可选]
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/cloudConfigAsyncStation'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_cloudTempPlateSwap(data):
        """
        【云->站】临牌换电
        请求参数:
            cloudTempPlate: string [可选] - 云端生成临牌号
            msgId: integer [可选]
            vin: string [可选] - 车辆vin码
        """
        path = f'/api/cloudMqtt/cloudTempPlateSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_controlAck(data):
        """
        【站->云】下控指令执行应答
        请求参数:
            eventKey: string [可选]
            msg: string [可选]
            msgId: integer [可选]
            result: integer [可选]
        """
        path = f'/api/cloudMqtt/controlAck'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_controlResultAck(data):
        """
        【站->云】下控指令执行结果应答
        请求参数:
            deviceCode: string [可选] - 下控设备编码或仓位
            eventKey: string [可选] - 下控指令eventKey
            failReason: string [可选] - 失败原因
            msgId: integer [可选]
            result: integer [可选] - 下控指令处理结果 1-成功 2-失败
        """
        path = f'/api/cloudMqtt/controlResultAck'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_disconnect(data):
        """
        【控制】断开mqtt
        请求参数:
            id: string [可选]
        """
        path = f'/api/cloudMqtt/disconnect'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_downPowerStationBaseInfo(data):
        """
        【云->站】换电站基本数据设置
        请求参数:
            areaCity: string [可选]
            areaDistrict: string [可选]
            areaLocation: string [可选]
            areaProvince: string [可选]
            belongCompany: string [可选]
            buildEndTime: integer [可选]
            buildStartTime: integer [可选]
            changeReason: string [可选]
            changeReasonCode: integer [可选]
            channelNum: integer [可选]
            commandType: integer [可选]
            developmentType: integer [可选]
            displayStatus: integer [可选]
            executeTime: integer [可选]
            insureEndTime: integer [可选]
            insureStartTime: integer [可选]
            latitude: number [可选]
            launchTime: integer [可选]
            longitude: number [可选]
            maintenanceStatus: integer [可选]
            manager: string [可选]
            msgId: integer [可选]
            operationStatus: integer [可选]
            permitBatterySwap: integer [可选]
            picture: string [可选]
            planStationStatus: integer [可选]
            platformKey: string [可选]
            positionNum: integer [可选]
            providerCode: string [可选]
            realLatitude: number [可选]
            realLongitude: number [可选]
            runEndTime: string [可选]
            runStartTime: string [可选]
            serverNum: integer [可选]
            socialCid: string [可选]
            stationArea: integer [可选]
            stationCode: string [可选]
            stationEnv: integer [可选]
            stationName: string [可选]
            stationNet: string [可选]
            stationStatus: integer [可选]
            stationType: string [可选]
            telNumber: string [可选]
            transformerNum: integer [可选]
            versionId: string [可选]
        """
        path = f'/api/cloudMqtt/downPowerStationBaseInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_fire(data):
        """
        【云->站】消防移仓
        请求参数:
            batteryCompartmentNo: integer [可选]
            moveOrderNo: string [可选]
            msgId: integer [可选]
            triggerType: integer [可选]
        """
        path = f'/api/cloudMqtt/fire'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_getRdbFault(data):
        """
        获取rdb
        请求参数:
            carModel: string [可选]
            vin: string [可选]
        """
        path = f'/api/cloudMqtt/getRdbFault'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_info(data):
        """
        【查看】云站mqtt配置信息
        请求参数:
            id: string [可选]
        """
        path = f'/api/cloudMqtt/info'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_isConnected(data):
        """
        【查看】云站mqtt是否连接
        请求参数:
            id: string [可选]
        """
        path = f'/api/cloudMqtt/isConnected'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_lightControl(data):
        """
        照明灯控制(云->站)
        请求参数:
            leftChargeCityLight: integer [可选] - 左侧充电区市电照明 目前暂未使用 0-默认值不操作1-开启 2-关闭
            leftChargeUpsLight: integer [可选] - 左侧充电区市UPS照明 目前暂未使用 0-默认值不操作1-开启 2-关闭
            logoLight: integer [可选] - 三代 站外LOGO灯 0-默认值不操作 1-开启 2-关闭
            mainControlLight: integer [可选] - 主控室照明 0-默认值不操作1-开启 2-关闭
            msgId: integer [可选]
            rightChargeCityLight: integer [可选] - 右侧充电区市电照明 0-默认值不操作1-开启 2-关闭
            rightChargeUpsLight: integer [可选]
            storageLight: integer [可选] - 三代 储藏室灯带 0-默认值不操作1-开启 2-关闭 pro站没有
            swapCityLight: integer [可选] - 换电区市电照明 0-默认值不操作1-开启 2-关闭
            swapUpsLight: integer [可选] - 换电区UPS照明 0-默认值不操作1-开启 2-关闭
        """
        path = f'/api/cloudMqtt/lightControl'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_manualChangePowerDoneResp(data):
        """
        【云->站】人工换电完成应答
        请求参数:
            carNo: string [可选] - 车辆牌照
            msgId: integer [可选]
            orderId: string [可选] - 订单编号
            result: integer [可选] - 云端处理结果：0-失败 1-成功 2-已上报人工/离线单
            retryFlag: integer [可选] - 是否需要重试：（该字段没发默认需要重试）0-不重试 1-重试
        """
        path = f'/api/cloudMqtt/manualChangePowerDoneResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_offlineChangePowerDoneResp(data):
        """
        【云->站】离线换电完成应答
        请求参数:
            carNo: string [可选] - 车辆牌照
            msgId: integer [可选]
            orderId: string [可选] - 订单编号
            result: integer [可选] - 云端处理结果：0-失败 1-成功 2-已上报人工/离线单
            retryFlag: integer [可选] - 是否需要重试：（该字段没发默认需要重试）0-不重试 1-重试
        """
        path = f'/api/cloudMqtt/offlineChangePowerDoneResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_operationalStrategy(data):
        """
        【云->站】运营策略配置信息
        请求参数:
            chargeStrategyList: array [可选] - 充电策略配置list
                        allowChargeTempLimit: integer [可选] - 允许充电温度上限, 默认值60℃
                        chargeEnoughSoc: integer [可选] - 开始充电SOC（%）, 低于开始充电SOC则开始充电
                        chargeStopSoc: integer [可选] - 停止充电SOC（%）, 高于停止充电SOC则停止充电
                        endTime: string [可选] - 结束时间（HH:mm），结束时间结尾23:59
                        instructionType: integer [可选] - 功率/电流调节指令类型：1：采用BMS充电Map进行功率控制(不做限制) 2：执行最大功率限制 3：执行需求电流比例调节 4：执行最大电流限制。
                        instructionTypeLimitVal: number [可选] - 功率调节指令类型为2时执行
                        positionList: array [可选] - 生效仓位号集合 当策略类型=2时有必填
                        startTime: string [可选] - 开始时间（HH:mm），开始时间结尾00:00
                        strategyNo: integer [可选] - 策略编号 当策略类型=2时有必填
                        strategyType: integer [可选] - 策略类型 1-整站策略 2-仓位策略
            msgId: integer [可选]
            packNumDemandConf: array [可选] - 运营策略配置list
                        batteryNeedNumber: integer [可选] - 电池包需求数
                        electricitySoc: integer [可选] - 允许出仓SOC（%）
                        endTime: string [可选] - 结束时间（HH:mm），结束时间结尾23:59
                        startTime: string [可选] - 开始时间（HH:mm），开始时间结尾00:00
        """
        path = f'/api/cloudMqtt/operationalStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_ota(data):
        """
        OTA升级(云->站)
        请求参数:
            deviceCode: array [可选]
            deviceType: string [可选]
            driveVersion: string [可选]
            driveVersionPack: string [可选]
            firmwareVersion: string [可选]
            firmwareVersionPack: string [可选]
            msgId: integer [可选]
            systemVersionList: array [可选]
            upgradeType: string [可选]
        """
        path = f'/api/cloudMqtt/ota'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_overallStatus(data):
        """
        【站->云】换电站整体状态上报
        请求参数:
            changeReason: string [可选]
            changeReasonCode: integer [可选]
            maintenanceStatus: integer [可选]
            permitBatterySwap: integer [可选]
            sourceForm: integer [可选]
            workStatus: integer [可选]
        """
        path = f'/api/cloudMqtt/overallStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_overallStatusResp(data):
        """
        【云->站】换电站整体状态上报应答
        请求参数:
            msgId: integer [可选]
            result: integer [可选]
        """
        path = f'/api/cloudMqtt/overallStatusResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_plcControl(data):
        """
        【云->站】PLC控制
        请求参数:
            msgId: integer [可选]
            plc: integer [可选] - plc操作
        """
        path = f'/api/cloudMqtt/plcControl'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_powerLimitConfiguration(data):
        """
        功率限制配置信息（云到站）(
        请求参数:
            msgId: integer [可选]
            transformerRelatedList: array [可选]
                        relatedDeviceList: array [可选]
                                    deviceId: integer [可选]
                                    devicePowerLimit: number [可选]
                                    deviceType: integer [可选]
                        transformerId: integer [可选]
                        transformerPowerLimit: number [可选]
        """
        path = f'/api/cloudMqtt/powerLimitConfiguration'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_queryOperationInfo(data):
        """
        运营信息查询
        请求参数:
            msgId: integer [可选]
            operationInfoTypes: array [可选]
        """
        path = f'/api/cloudMqtt/queryOperationInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_queryPackLabel(data):
        """
        【站->云】获取电池标签
        请求参数:
            barcodeList: array [可选]
                        batteryNum: integer [可选] - 用户选择换电数
                        bluetoothConnectMode: integer [可选] - 连接方式
                        carNo: string [可选] - 车牌
                        freedomRules: array [可选] - 自由度列表
                                    checkState: integer [可选] - 自由度调整启用状态
                                    code: string [可选] - 自由度调整类型编码
                        mbmuIrk: string [可选] - 车机irk
                        modelCode: string [可选] - 车辆型号（需要统一的数据维护）
                        oob: string [可选] - oob
                        phone: string [可选] - 用户手机号
                        selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
                        supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
                        swapFlowKey: string [可选] - 换电流程编号
                        vbleMac: string [可选] - vbleMac蓝牙mac地址
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/queryPackLabel'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_queryPackLabelResp(data):
        """
        【云->站】云端返回电池标签
        请求参数:
            msgId: integer [可选]
            packLabelInfoList: array [可选]
                        batteryNum: integer [可选] - 用户选择换电数
                        bluetoothConnectMode: integer [可选] - 连接方式
                        carNo: string [可选] - 车牌
                        freedomRules: array [可选] - 自由度列表
                                    checkState: integer [可选] - 自由度调整启用状态
                                    code: string [可选] - 自由度调整类型编码
                        mbmuIrk: string [可选] - 车机irk
                        modelCode: string [可选] - 车辆型号（需要统一的数据维护）
                        oob: string [可选] - oob
                        phone: string [可选] - 用户手机号
                        selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
                        supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
                        swapFlowKey: string [可选] - 换电流程编号
                        vbleMac: string [可选] - vbleMac蓝牙mac地址
        """
        path = f'/api/cloudMqtt/queryPackLabelResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_queryStationLabel(data):
        """
        【站->云】站控查询换电站标签
        请求参数:
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/queryStationLabel'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_queryStationLabelResp(data):
        """
        【云->站】云端返回换电站标
        请求参数:
            dataDate: integer [可选]
            msgId: integer [可选]
            parameterConf: string [可选] - 车辆参数
            weatherInfos: array [可选] - 天气信息集合
                        batteryNum: integer [可选] - 用户选择换电数
                        bluetoothConnectMode: integer [可选] - 连接方式
                        carNo: string [可选] - 车牌
                        freedomRules: array [可选] - 自由度列表
                                    checkState: integer [可选] - 自由度调整启用状态
                                    code: string [可选] - 自由度调整类型编码
                        mbmuIrk: string [可选] - 车机irk
                        modelCode: string [可选] - 车辆型号（需要统一的数据维护）
                        oob: string [可选] - oob
                        phone: string [可选] - 用户手机号
                        selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
                        supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
                        swapFlowKey: string [可选] - 换电流程编号
                        vbleMac: string [可选] - vbleMac蓝牙mac地址
        """
        path = f'/api/cloudMqtt/queryStationLabelResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_reconnect(data):
        """
        【控制】重连mqtt
        请求参数:
            id: string [可选]
        """
        path = f'/api/cloudMqtt/reconnect'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_reportBmsSeed(data):
        """
        reportBmsSeed
        请求参数:
            bmsSeed: string [可选]
            channelNo: integer [可选]
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/reportBmsSeed'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_reportBmsSeedResp(data):
        """
        reportBmsSeedResp
        请求参数:
            bmsSecretKey: string [可选]
            bmsSecretKeyResult: integer [可选]
            bmsSeed: string [可选]
            channelNo: integer [可选]
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/reportBmsSeedResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_reportCarNo(data):
        """
        【站->云】换电校验
        请求参数:
            carNo: string [可选] - 车辆牌照，近距离通信技术识别出来的码
            msgId: integer [可选]
            swapType: integer [可选] - 换电类型 1：默认 2：云端临牌
            vin: string [可选] - 车辆vin码
        """
        path = f'/api/cloudMqtt/reportCarNo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_reportPlcPrescription(data):
        """
        【站->云】上报PLC配方详细信息
        请求参数:
            msgId: integer [可选]
            plcPrescription: string [可选] - PLC配方类型对应十六进制配方数据
            plcPrescriptionJson: string [可选] - Plc配方解析后的json数据
            plcPrescriptionType: integer [可选] - PLC配方类型 1：电池仓配方详细信息 2：换电通道基础配方详细信息 3：车型配方详细信息 4：站型配置信息 5：站点参数信息 6：车型配方信息
            prescriptionForAsyncPlc: string [可选] - Plc配方原始报文
            prescriptionParams: string [可选] - 配方对应参数
            updateUserId: string [可选] - 更新用户id
            updateUserName: string [可选] - 更新用户名称
        """
        path = f'/api/cloudMqtt/reportPlcPrescription'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_reportPlcPrescriptionResp(data):
        """
        【云->站】云端响应接收PLC配方
        请求参数:
            msgId: integer [可选]
            plcPrescriptionType: integer [可选] - PLC配方类型 1：电池仓配方详细信息 2：换电通道基础配方详细信息 3：车型配方详细信息
            result: integer [可选] - 云端处理结果 0：失败 1：成功
        """
        path = f'/api/cloudMqtt/reportPlcPrescriptionResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_rollingDoorControl(data):
        """
        卷帘门控制(云->站)
        请求参数:
            entryDoor: integer [可选] - 入口卷帘门 1-开启 2-关闭 0-默认值不操作
            exitDoor: integer [可选] - 出口卷帘门 1-开启 2-关闭 0-默认值不操作
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/rollingDoorControl'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendConfigurationSettings(data):
        """
        下发配置信息
        请求参数:
            configurationType: integer [可选] - 配置类型 1-VBLE升级功能开关
            configurationValue: string [可选] - 配置值 配置类型 = 1 升级功能开关1-启用 2-不启用
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/sendConfigurationSettings'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendDictCategories(data):
        """
        下发更新换电站字典值修改(云到站)
        请求参数:
            categoryList: array [可选] - 字典集合
                        batteryNum: integer [可选] - 用户选择换电数
                        bluetoothConnectMode: integer [可选] - 连接方式
                        carNo: string [可选] - 车牌
                        freedomRules: array [可选] - 自由度列表
                                    checkState: integer [可选] - 自由度调整启用状态
                                    code: string [可选] - 自由度调整类型编码
                        mbmuIrk: string [可选] - 车机irk
                        modelCode: string [可选] - 车辆型号（需要统一的数据维护）
                        oob: string [可选] - oob
                        phone: string [可选] - 用户手机号
                        selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
                        supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
                        swapFlowKey: string [可选] - 换电流程编号
                        vbleMac: string [可选] - vbleMac蓝牙mac地址
            msgId: integer [可选]
        """
        path = f'/api/cloudMqtt/sendDictCategories'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendEventKey(data):
        """
        【站->云】发送站端数据
        请求参数:
            eventKey: string [可选]
        """
        path = f'/api/cloudMqtt/sendEventKey'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendPeriodSettings(data):
        """
        【云->站】下发尖峰平谷信息
        请求参数:
            msgId: integer [可选]
            periodList: array [可选]
                        batteryNum: integer [可选] - 用户选择换电数
                        bluetoothConnectMode: integer [可选] - 连接方式
                        carNo: string [可选] - 车牌
                        freedomRules: array [可选] - 自由度列表
                                    checkState: integer [可选] - 自由度调整启用状态
                                    code: string [可选] - 自由度调整类型编码
                        mbmuIrk: string [可选] - 车机irk
                        modelCode: string [可选] - 车辆型号（需要统一的数据维护）
                        oob: string [可选] - oob
                        phone: string [可选] - 用户手机号
                        selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
                        supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
                        swapFlowKey: string [可选] - 换电流程编号
                        vbleMac: string [可选] - vbleMac蓝牙mac地址
        """
        path = f'/api/cloudMqtt/sendPeriodSettings'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendPlcPrescription(data):
        """
        【云->站】下发PLC配方详细信息
        请求参数:
            msgId: integer [可选]
            plcPrescription: string [可选] - PLC配方类型对应十六进制配方数据
            plcPrescriptionType: integer [可选] - PLC配方类型 1：电池仓配方详细信息 2：换电通道基础配方详细信息 3：车型配方详细信息
            prescriptionParams: string [可选] - 配方对应参数
        """
        path = f'/api/cloudMqtt/sendPlcPrescription'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendPlcPrescriptionResp(data):
        """
        【站->云】站端响应接收PLC配方
        请求参数:
            failReason: string [可选] - 失败原因
            msgId: integer [可选]
            plcPrescriptionType: integer [可选] - PLC配方类型 1：电池仓配方详细信息 2：换电通道基础配方详细信息 3：车型配方详细信息
            result: integer [可选] - 云端处理结果 0：失败 1：成功
        """
        path = f'/api/cloudMqtt/sendPlcPrescriptionResp'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendReceiveCloudValid(data):
        """
        【云->站】云端发送检验结果
        请求参数:
            ableToChange: boolean [可选] - 是否抬杆放行
            batteryNum: integer [可选] - 用户选择的换电电池包数量（1或2）预留字段，目前默是2
            bluetoothConnectMode: integer [可选] - 蓝牙连接方式
            afterChangeHabit: integer [可选] - 换电后行为习惯 0：未知 1：换电后持续用车 2：换电后休息 
            carOperationType: integer [可选] - 车辆运营情况 1:优 2:良 3:一般 4:差 0:未知
            city: string [可选] - 城市
            dataDate: integer [可选] - 数据日期
            drivingPeriod: integer [可选] - 习惯用车时段 1:凌晨 2:日间 3:夜间 0:未知
            energyConsumeType: integer [可选] - 车辆能耗类型 1:高 2:中 3:低 0:未知
            energySupplyType: integer [可选] - 补能习惯 1:习惯换电 2:无明显倾向 3:习惯充电  0:未知
            parameterConf: string [可选] - 车辆参数
            tempLifeEqlType: integer [可选] - 等效温度情况 车上电池包等效温度情况 1:高 2:中 3:低 0:未知
            carModel: string [可选] - 车辆型号（需要统一的数据维护）
            carModelName: string [可选] - 车型名称
            carNo: string [可选] - 车牌号
            changeType: integer [可选] - 云换电方式 1-无感 2-有感
            fakePackLocation: integer [可选] - 可安装假包的安装位置 1-1号位 2-2号位
            freedomRules: array [可选] - 自由度调整规则集合 vehicleDoor—车门 gear—挡位 handBrake—手刹 (自动驻车) footBrake—脚刹 steeringTurnAngle—转向角
                        code: string [可选] - 自由度调整类型编码
                        state: boolean [可选] - 自由度调整启用状态
            mbmuIRK: string [可选] - MBMU/VBLE蓝牙IRK
            mbmuMac: string [可选] - Mbmu蓝牙mac地址
            modelBatteryNum: integer [可选] - 车型对应电池数（需要统一的数据维护）
            msg: string [可选] - 不能推送“成功”、“进站”等相关信息
            msgId: integer [可选]
            newFreedomRules: array [可选] - 自由度调整规则集合
                        checkState: integer [可选] - 自由度调整启用状态
                        code: string [可选] - 自由度调整类型编码
            oob: string [可选] - OOB
            orderId: string [可选] - 云下发的换电订单id
            adaptionPrescription: string [可选] - 车型配方信息
            carModelPrescription: string [可选] - 车型配方信息（详细值）
            stationModelConfig: string [可选] - 站型配置信息
            stationParameter: string [可选] - 站点参数信息
            sbmuInfo: array [可选] - 上次换电结束车上电池信息
                        installAddress: integer [可选] - 电池所在位置（1或2）
                        lastLockTurnsCount: array [可选] - 上次加锁圈数
                                    lockNo: integer [可选] - 锁编号
                                    turnsCount: number [可选] - 加锁圈数
                        packSN: string [可选] - 电池SN
                        packType: integer [可选] - 电池包类别 0-未安装电池包 1-C1N-53-264 2-C1N-70-274 3-假包 4-LFP_25_01_L 5-LFP_20_01_L
                        sbmuMac: string [可选] - 电池mac地址
            selectPackType: integer [可选] - 用户租赁的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-LFP_25_01_L 5-LFP_20_01_L
            selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
            specifySelect: boolean [可选] - 是否指定选包 True：指定选包（指定选包信息不能为空） False：不指定选包
            specifySelectResult: array [可选] - 指定选仓信息
                        batteryCompart: integer [可选] - 指定选包电池仓
                        installAddress: integer [可选] - 指定电池包安装位置 1：一号位 2：二号位
            supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-LFP_25_01_L 5-LFP_20_01_L
            swapFlowKey: string [可选] - 换电流程编号
            vin: string [可选] - 车辆vin码
        """
        path = f'/api/cloudMqtt/sendReceiveCloudValid'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendStartSwap(data):
        """
        【云->站】云端发送开始换电
        请求参数:
            allow: integer [可选] - 是否允许换电。1 允许换电，2不允许换电
            carNo: string [可选] - 车牌号
            msgId: integer [可选]
            orderId: string [可选] - 云下发的换电订单id
        """
        path = f'/api/cloudMqtt/sendStartSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_sendStationLogin(data):
        """
        【站->云】站端登录
        """
        path = f'/api/cloudMqtt/sendStationLogin'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_stationHeartBeat(data):
        """
        【站->云】站心跳帧上报
        """
        path = f'/api/cloudMqtt/stationHeartBeat'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_triggerSendPlcPrescription(data):
        """
        【站->云】触发下发PLC配方详细信息
        请求参数:
            msgId: integer [可选]
            plcPrescriptionType: integer [可选] - PLC配方类型 4：站型配置信息 5：站点参数信息 6：车型配方信息
            userId: string [可选] - 用户账号（来源：云、站、PLC）
            userName: string [可选] - 用户名称（来源：云、站、PLC）
        """
        path = f'/api/cloudMqtt/triggerSendPlcPrescription'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_cloudMqtt_voiceControl(data):
        """
        语音播报控制(云->站)
        请求参数:
            msgId: integer [可选]
            voiceNo: integer [可选] - 语音播报内容编号
        """
        path = f'/api/cloudMqtt/voiceControl'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_debug_api_debug_vble_ota(data):
        """
        vble ota
        请求参数:
            irk: string [可选] - irk
            source: string [可选] - 来源
        """
        path = f'/api/debug/api/debug/vble/ota'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_debug_flow_pickPackParams(data):
        """
        查询当前选包所有参数数据
        """
        path = f'/api/debug/flow/pickPackParams'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_debug_flow_skip(data):
        """
        跳过流程
        请求参数:
        """
        path = f'/api/debug/flow/skip'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_debug_flow_skipWithParam(data):
        """
        带参数跳过流程
        请求参数:
            taskId: string [可选]
        """
        path = f'/api/debug/flow/skipWithParam'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_debug_plc_removePLCBMSPackLockStatus(data):
        """
        关闭同步PLC电池锁状态
        """
        path = f'/api/debug/plc/removePLCBMSPackLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_debug_plc_sendPLCBMSPackLockStatus(data):
        """
        下发同步PLC电池锁状态
        请求参数:
            packNum: integer [可选] - 用户选择的换电电池包数量 默认：2
        """
        path = f'/api/debug/plc/sendPLCBMSPackLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_redis_initData(data):
        """
        清除换电缓存数据
        """
        path = f'/api/redis/initData'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapCondition_campExecuteResult(data):
        """
        campExecuteResult
        """
        path = f'/api/swapCondition/campExecuteResult'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapCondition_chargeStatusPacks(data):
        """
        chargeStatusPacks
        """
        path = f'/api/swapCondition/chargeStatusPacks'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapCondition_packStatistics(data):
        """
        packStatistics
        """
        path = f'/api/swapCondition/packStatistics'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapCondition_packSwapMatchInfoList(data):
        """
        packSwapMatchInfoList
        """
        path = f'/api/swapCondition/packSwapMatchInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapCondition_supportPack(data):
        """
        supportPack
        请求参数:
            judgeChargeFlag: boolean [可选]
            socLimit: number [可选]
        """
        path = f'/api/swapCondition/supportPack'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapCondition_supportPackByParam(data):
        """
        supportPackByParam
        请求参数:
            judgeChargeFlag: boolean [可选] - 判断充电标志
            judgePackTempFlag: boolean [可选] - 判断电池温度标志
        """
        path = f'/api/swapCondition/supportPackByParam'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapCondition_swapConditionDetail(data):
        """
        swapConditionDetail
        """
        path = f'/api/swapCondition/swapConditionDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_allowSwapFlow(data):
        """
        允许换电
        """
        path = f'/api/swapFlow/allowSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_clearBbsFault(data):
        """
        清除站控自检故障
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeCode: string [可选] - 故障上报设备类型code
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/swapFlow/clearBbsFault'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_currentFlowIrk(data):
        """
        获取当前订单irk
        """
        path = f'/api/swapFlow/currentFlowIrk'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_currentFlowNo(data):
        """
        获取当前流水号
        """
        path = f'/api/swapFlow/currentFlowNo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_delProcessId():
        """
        删除redis流程id
        """
        path = f'/api/swapFlow/delProcessId'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_delSoftWareTask(data):
        """
        delSoftWareTask
        请求参数:
            softwareCode: integer [可选]
        """
        path = f'/api/swapFlow/delSoftWareTask'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_fireControlStrategy(data):
        """
        消防换电处理策略
        """
        path = f'/api/swapFlow/fireControlStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_forceStopSwapFlow(data):
        """
        强制结束换电流程
        请求参数:
            failType: integer [可选]
            forceEndReason: string [可选]
            pressFlowStatus: integer [可选]
            swapEndTime: string [可选]
        """
        path = f'/api/swapFlow/forceStopSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_getFreedomInfo():
        """
        getFreedomInfo
        """
        path = f'/api/swapFlow/getFreedomInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_getManualSwapData(data):
        """
        获取半自动换电数据
        """
        path = f'/api/swapFlow/getManualSwapData'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_getMbmuInfo():
        """
        getMbmuInfo
        """
        path = f'/api/swapFlow/getMbmuInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_getPackLockInfo():
        """
        getPackLockInfo
        """
        path = f'/api/swapFlow/getPackLockInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_getPlcEquipDynamicStatus():
        """
        getPlcEquipDynamicStatus
        """
        path = f'/api/swapFlow/getPlcEquipDynamicStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_getRpaLinkStatus(data):
        """
        获取RPA连接状态
        请求参数:
        """
        path = f'/api/swapFlow/getRpaLinkStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_getSwapStep():
        """
        getSwapStep
        """
        path = f'/api/swapFlow/getSwapStep'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_getSwapTimingInfo():
        """
        getSwapTimingInfo
        """
        path = f'/api/swapFlow/getSwapTimingInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_getVerifyVehicleInfo():
        """
        getVerifyVehicleInfo
        """
        path = f'/api/swapFlow/getVerifyVehicleInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_getWholeProcessData():
        """
        getWholeProcessData
        """
        path = f'/api/swapFlow/getWholeProcessData'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_getWholeProcessRespDTO():
        """
        getWholeProcessRespDTO
        """
        path = f'/api/swapFlow/getWholeProcessRespDTO'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_hasCarFollow():
        """
        hasCarFollow
        """
        path = f'/api/swapFlow/hasCarFollow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_hasManualSwapFlowTask():
        """
        hasManualSwapFlowTask
        """
        path = f'/api/swapFlow/hasManualSwapFlowTask'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_hasSwapFlowTask():
        """
        hasSwapFlowTask
        """
        path = f'/api/swapFlow/hasSwapFlowTask'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlow_haveWaitSwap(data):
        """
        haveWaitSwap
        """
        path = f'/api/swapFlow/haveWaitSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_judgePressureSwapFlow(data):
        """
        judgePressureSwapFlow
        """
        path = f'/api/swapFlow/judgePressureSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_notAllowSwapFlow(data):
        """
        不允许换电
        """
        path = f'/api/swapFlow/notAllowSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_pickBatteries(data):
        """
        触发自动选包
        请求参数:
            allow: integer [可选] - 是否允许换电。1 允许换电，2不允许换电
            carNo: string [可选] - 车牌号
            msgId: integer [可选]
            orderId: string [可选] - 云下发的换电订单id
        """
        path = f'/api/swapFlow/pickBatteries'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_reExecBeforeTask(data):
        """
        重新执行任务
        请求参数:
            id: string [可选]
        """
        path = f'/api/swapFlow/reExecBeforeTask'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_sendPLCAllowVehicleEnter(data):
        """
        下发PLC允许车辆驶入
        """
        path = f'/api/swapFlow/sendPLCAllowVehicleEnter'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_setSoftWareTask(data):
        """
        setSoftWareTask
        请求参数:
            softwareCode: integer [可选]
        """
        path = f'/api/swapFlow/setSoftWareTask'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_skipCurrentActiviti(data):
        """
        skipCurrentActiviti
        请求参数:
            activitiId: string [可选] - 任务节点来源
        """
        path = f'/api/swapFlow/skipCurrentActiviti'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_startPressureSwapFlow(data):
        """
        startPressureSwapFlow
        """
        path = f'/api/swapFlow/startPressureSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_stopPressureSwapFlow(data):
        """
        stopPressureSwapFlow
        """
        path = f'/api/swapFlow/stopPressureSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_stopSwapFlow(data):
        """
        结束换电流程
        请求参数:
            failType: integer [可选]
            forceEndReason: string [可选]
            pressFlowStatus: integer [可选]
            swapEndTime: string [可选]
        """
        path = f'/api/swapFlow/stopSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_triggerSbleWatchDog(data):
        """
        triggerSbleWatchDog
        """
        path = f'/api/swapFlow/triggerSbleWatchDog'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_unablePressureSwapFlow(data):
        """
        unablePressureSwapFlow
        """
        path = f'/api/swapFlow/unablePressureSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_vbleUpgradeResult(data):
        """
        vbleUpgradeResult
        请求参数:
            createUserId: integer [可选]
            createUserName: string [可选]
            irk: string [可选]
            msg: string [可选]
            result: integer [可选] - 升级结果 2：成功 3：失败
            source: string [可选]
        """
        path = f'/api/swapFlow/vbleUpgradeResult'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_allPacks(data):
        """
        allPacks
        请求参数:
            carModel: string [可选] - 车型代码
            selectPackType: integer [可选] - 换电电池包类型 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
        """
        path = f'/api/swapFlowTask/allPacks'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_autoCardNo(data):
        """
        autoCardNo
        请求参数:
            cameraType: integer [可选] - 抓拍类型 23：自动抓拍 280：手动抓拍
            captureFault: integer [可选] - 是否抓拍机故障 1：是 0：否
            carNo: string [可选] - 车牌
            carVin: string [可选] - 车辆Vin码
            confidence: integer [可选] - 置信度
            createUserId: integer [可选]
            createUserName: string [可选]
            headToward: integer [可选] - 车头朝向 70102:车头，70107:车尾 70101：解析异常
            manualReason: integer [可选] - 手动上传车牌原因 1：临牌 2：车辆不出站换电 3：车辆过户 4：其他
            manualReasonDetail: string [可选] - 原因描述
            msgId: integer [可选] - 云msgId
            picPath: string [可选] - 车牌图片地址
            pressureYn: integer [可选] - 是否压测 1:是
        """
        path = f'/api/swapFlowTask/autoCardNo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_cameraCall(data):
        """
        cameraCall
        请求参数:
            createUserId: integer [可选]
            createUserName: string [可选]
        """
        path = f'/api/swapFlowTask/cameraCall'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_closeHVContactor(data):
        """
        closeHVContactor
        """
        path = f'/api/swapFlowTask/closeHVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_closeLVContactor(data):
        """
        closeLVContactor
        """
        path = f'/api/swapFlowTask/closeLVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_completeTask(data):
        """
        completeTask
        请求参数:
            taskId: string [可选]
        """
        path = f'/api/swapFlowTask/completeTask'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_continueCarStopHandle(data):
        """
        continueCarStopHandle
        """
        path = f'/api/swapFlowTask/continueCarStopHandle'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_continuePressCentering(data):
        """
        continuePressCentering
        """
        path = f'/api/swapFlowTask/continuePressCentering'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getSkipFreedomConfig():
        """
        getSkipFreedomConfig
        """
        path = f'/api/swapFlowTask/getSkipFreedomConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlowTask_installFakePackConfig(data):
        """
        installFakePackConfig
        请求参数:
            realPackNum: integer [可选] - 真包数量
        """
        path = f'/api/swapFlowTask/installFakePackConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manual_manualSave(data):
        """
        manualSave
        请求参数:
            carNo: string [可选]
            createUserId: integer [可选]
            createUserName: string [可选]
            packSn: string [可选]
            realSoc: string [可选]
            manualSwapReason: integer [可选]
            swapEndTime: string [可选]
            swapStartTime: string [可选]
            packSn: string [可选]
            realSoc: string [可选]
            userPhone: string [可选]
            vehTotalOdometer: string [可选]
        """
        path = f'/api/swapFlowTask/manual/manualSave'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manual_reportManualOrder(data):
        """
        reportManualOrder
        请求参数:
            createUserId: integer [可选]
            createUserName: string [可选]
        """
        path = f'/api/swapFlowTask/manual/reportManualOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manual_saveCampBatteryAndDisconnect(data):
        """
        saveCampBatteryAndDisconnect
        请求参数:
            campNo: integer [可选]
            packNo: integer [可选]
        """
        path = f'/api/swapFlowTask/manual/saveCampBatteryAndDisconnect'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manual_saveCarBatteryInfo(data):
        """
        saveCarBatteryInfo
        """
        path = f'/api/swapFlowTask/manual/saveCarBatteryInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manual_saveManualFillInOrder(data):
        """
        saveManualFillInOrder
        请求参数:
            bluetoothConnectMode: integer [可选] - 连接方式
            carModel: string [可选]
            carNo: string [可选]
            endTime: string [可选]
            flowNo: string [可选]
            freedomRules: array [可选] - 自由度列表
                        checkState: integer [可选] - 自由度调整启用状态
                        code: string [可选] - 自由度调整类型编码
            irk: string [可选]
            manualSwapReason: integer [可选]
            oob: string [可选]
            phone: string [可选]
            selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
            startTime: string [可选]
            supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
            userId: string [可选]
            vbleMac: string [可选]
        """
        path = f'/api/swapFlowTask/manual/saveManualFillInOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualAllowReturnVehicle(data):
        """
        manualAllowReturnVehicle
        """
        path = f'/api/swapFlowTask/manualAllowReturnVehicle'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualBreakBatteryBt(data):
        """
        manualBreakBatteryBt
        请求参数:
            batteryMac1: string [可选]
            batteryMac2: string [可选]
        """
        path = f'/api/swapFlowTask/manualBreakBatteryBt'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualConnectBt(data):
        """
        manualConnectBt
        """
        path = f'/api/swapFlowTask/manualConnectBt'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualControlBt(data):
        """
        manualControlBt
        请求参数:
            createUserId: integer [可选]
            createUserName: string [可选]
            disconnectType: integer [可选] - 1:全自动 2：半自动 3：标定 4:压测
            mbmuIrk: string [可选] - irk
            oob: string [可选] - oob
            type: string [可选] - 1:连接； 2：断开
            vbleMac: string [可选] - 蓝牙地址
        """
        path = f'/api/swapFlowTask/manualControlBt'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualControlCarCheckSelf(data):
        """
        manualControlCarCheckSelf
        请求参数:
            batteryMac1: string [可选]
            batteryMac2: string [可选]
            batteryNum: integer [可选]
            batteryStatus1: integer [可选]
            batteryStatus2: integer [可选]
            vbleMac: string [可选]
        """
        path = f'/api/swapFlowTask/manualControlCarCheckSelf'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualHv(data):
        """
        manualHv
        """
        path = f'/api/swapFlowTask/manualHv'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualLv(data):
        """
        manualLv
        """
        path = f'/api/swapFlowTask/manualLv'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualPickPack(data):
        """
        manualPickPack
        请求参数:
            activitiId: string [可选] - 任务节点来源
            preInstallPack1CampNo: integer [可选] - 预安装包1仓位号
            preInstallPack2CampNo: integer [可选] - 预安装包2仓位号
            realPackNum: integer [可选] - 选择真包数量
            selectPackType: integer [可选] - 用户租赁的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
        """
        path = f'/api/swapFlowTask/manualPickPack'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualSendAllowVehicleEnter(data):
        """
        manualSendAllowVehicleEnter
        """
        path = f'/api/swapFlowTask/manualSendAllowVehicleEnter'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualUploadCardNo(data):
        """
        manualUploadCardNo
        请求参数:
            cameraType: integer [可选] - 抓拍类型 23：自动抓拍 280：手动抓拍
            captureFault: integer [可选] - 是否抓拍机故障 1：是 0：否
            carNo: string [可选] - 车牌
            carVin: string [可选] - 车辆Vin码
            confidence: integer [可选] - 置信度
            createUserId: integer [可选]
            createUserName: string [可选]
            headToward: integer [可选] - 车头朝向 70102:车头，70107:车尾 70101：解析异常
            manualReason: integer [可选] - 手动上传车牌原因 1：临牌 2：车辆不出站换电 3：车辆过户 4：其他
            manualReasonDetail: string [可选] - 原因描述
            msgId: integer [可选] - 云msgId
            picPath: string [可选] - 车牌图片地址
            pressureYn: integer [可选] - 是否压测 1:是
        """
        path = f'/api/swapFlowTask/manualUploadCardNo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualVehicleErrorLeave(data):
        """
        manualVehicleErrorLeave
        """
        path = f'/api/swapFlowTask/manualVehicleErrorLeave'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_matchPacks(data):
        """
        matchPacks
        请求参数:
            campNo: integer [可选] - 匹配电池包的仓位号
            selectPackType: integer [可选] - 用户租赁的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
        """
        path = f'/api/swapFlowTask/matchPacks'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_offLineSwapFlow(data):
        """
        offLineSwapFlow
        请求参数:
            batteryNum: integer [必填]
            bluetoothConnectMode: integer [可选] - 连接方式
            fakePackLocation: integer [可选] - 可安装假包的安装位置
            mbmuIrk: string [可选] - 车机irk
            modelBatteryNum: integer [可选] - 车辆电池槽位数
            modelCode: string [可选] - 车辆型号（需要统一的数据维护）
            oob: string [可选] - oob
            phone: string [可选] - 用户手机号
            sbmuInfoData: array [可选] - 上次换电结束车上电池信息
                        installAddress: integer [可选] - 电池所在位置（1或2）
                        lastLockTurnsCount: array [可选] - 上次加锁圈数
                                    lockNo: integer [可选] - 锁编号
                                    turnsCount: number [可选] - 加锁圈数
                        packSN: string [可选] - 电池SN
                        packType: integer [可选] - 电池包类别 0-未安装电池包 1-C1N-53-264 2-C1N-70-274 3-假包 4-LFP_25_01_L 5-LFP_20_01_L
                        sbmuMac: string [可选] - 电池mac地址
            selectPackType: integer [可选] - 用户租赁的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
            selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
            supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
            swapFlowKey: string [可选] - 换电流程编号
            vbleMac: string [可选] - vbleMac蓝牙mac地址
        """
        path = f'/api/swapFlowTask/offLineSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_originPackBack(data):
        """
        originPackBack
        """
        path = f'/api/swapFlowTask/originPackBack'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_pickPackResultStopChargeResult(data):
        """
        pickPackResultStopChargeResult
        请求参数:
            failReason: string [可选]
            result: integer [可选]
        """
        path = f'/api/swapFlowTask/pickPackResultStopChargeResult'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_pressureHv(data):
        """
        pressureHv
        """
        path = f'/api/swapFlowTask/pressureHv'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_pressureLv(data):
        """
        pressureLv
        """
        path = f'/api/swapFlowTask/pressureLv'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_pressureTestProcessInfo(data):
        """
        pressureTestProcessInfo
        """
        path = f'/api/swapFlowTask/pressureTestProcessInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reRequestCloudAuth(data):
        """
        reRequestCloudAuth
        请求参数:
            createUserId: integer [可选]
            createUserName: string [可选]
        """
        path = f'/api/swapFlowTask/reRequestCloudAuth'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendCenteringLift(data):
        """
        reSendCenteringLift
        """
        path = f'/api/swapFlowTask/reSendCenteringLift'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendChannelRecover(data):
        """
        reSendChannelRecover
        """
        path = f'/api/swapFlowTask/reSendChannelRecover'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendEnableHV(data):
        """
        reSendEnableHV
        """
        path = f'/api/swapFlowTask/reSendEnableHV'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendPlcStartSwap(data):
        """
        reSendPlcStartSwap
        """
        path = f'/api/swapFlowTask/reSendPlcStartSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendPreInstallPackInfo(data):
        """
        reSendPreInstallPackInfo
        """
        path = f'/api/swapFlowTask/reSendPreInstallPackInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_receivedVehicleBack(data):
        """
        receivedVehicleBack
        """
        path = f'/api/swapFlowTask/receivedVehicleBack'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_receivedVehicleLeave(data):
        """
        receivedVehicleLeave
        """
        path = f'/api/swapFlowTask/receivedVehicleLeave'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_selfCheck(data):
        """
        selfCheck
        """
        path = f'/api/swapFlowTask/selfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_sendSbleEnableHVContactor(data):
        """
        sendSbleEnableHVContactor
        """
        path = f'/api/swapFlowTask/sendSbleEnableHVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_setPressureTestOrderInfo(data):
        """
        setPressureTestOrderInfo
        请求参数:
            batteryNum: integer [必填]
            bluetoothConnectMode: integer [可选] - 连接方式
            carNo: string [可选] - 车牌
            freedomRules: array [可选] - 自由度列表
                        checkState: integer [可选] - 自由度调整启用状态
                        code: string [可选] - 自由度调整类型编码
            mbmuIrk: string [可选] - 车机irk
            modelCode: string [可选] - 车辆型号（需要统一的数据维护）
            oob: string [可选] - oob
            phone: string [可选] - 用户手机号
            powerDownYn: integer [可选] - 是否下电 1-是 0-否
            selectPackTypes: array [可选] - 用户租赁的电池包类别集合 1-C1N-53-264 2-C1N-70-274 3-假包 4-25#_LFP_01_L 5-20#_LFP_01_L 6-35#_LFP_01_L
            supportPackTypes: array [可选] - 车型可支持的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
            swapFlowKey: string [可选] - 换电流程编号
            totalCount: integer [可选] - 压力测试换电次数
            vbleMac: string [可选] - vbleMac蓝牙mac地址
        """
        path = f'/api/swapFlowTask/setPressureTestOrderInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_setSkipFreedomConfig(data):
        """
        setSkipFreedomConfig
        请求参数:
        """
        path = f'/api/swapFlowTask/setSkipFreedomConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_skipCloudStartSwap(data):
        """
        skipCloudStartSwap
        请求参数:
            batteryNum: integer [必填]
            phone: string [必填]
            selectPackType: integer [可选] - 用户租赁的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
        """
        path = f'/api/swapFlowTask/skipCloudStartSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_supportSwapPacks(data):
        """
        supportSwapPacks
        """
        path = f'/api/swapFlowTask/supportSwapPacks'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_swapStopChargeResult(data):
        """
        swapStopChargeResult
        请求参数:
            failReason: string [可选]
            result: integer [可选]
        """
        path = f'/api/swapFlowTask/swapStopChargeResult'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowVehicleInfo_removeAndSaveByFlowNo(data):
        """
        删除并保存换电车辆信息
        请求参数:
            createTime: string [可选]
            flowNo: string [可选]
            id: integer [可选]
            tirePrsAlarmFl: integer [可选]
            tirePrsAlarmFr: integer [可选]
            tirePrsAlarmRl: integer [可选]
            tirePrsAlarmRr: integer [可选]
            tirePrsFl: integer [可选]
            tirePrsFr: integer [可选]
            tirePrsRl: integer [可选]
            tirePrsRr: integer [可选]
        """
        path = f'/api/swapFlowVehicleInfo/removeAndSaveByFlowNo'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapMark_delMark(data):
        """
        删除标记
        请求参数:
            swapMarkCode: string [可选]
            swapMarkVal: string [可选]
        """
        path = f'/api/swapMark/delMark'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_swapMark_setMark(data):
        """
        添加标记
        请求参数:
            swapMarkCode: string [可选]
            swapMarkVal: string [可选]
        """
        path = f'/api/swapMark/setMark'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))

    @staticmethod
    def api_timeDemandConfig_currentTimeConfig(data):
        """
        获取当前时间区间配置
        """
        path = f'/api/timeDemandConfig/currentTimeConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiSwapFlow._get_path(path), 'POST', data))
