from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiRbc:
    @staticmethod
    def _get_path(path):
        service = '/rbc'
        return service + path

    @staticmethod
    def rbc_api_supportTest_pullBatteryLabels():
        """
        拉取电池标签
        请求参数:
        """
        path = f'/rbc/api/supportTest/pullBatteryLabels'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_api_supportTest_sendBrodLED2(data):
        """
        sendBrodLED2
        请求参数:
        """
        path = f'/rbc/api/supportTest/sendBrodLED2'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_api_supportTest_sendBrodLED3(data):
        """
        sendBrodLED3
        请求参数:
            ledAreaContent1: string [可选] - LED显示屏区域1显示内容
            ledAreaContent2: string [可选] - LED显示屏区域2显示内容
            ledAreaContent3: string [可选] - LED显示屏区域3显示内容
            ledAreaContent4: string [可选] - LED显示屏区域4显示内容
            ledVoiceContent: string [可选] - LED播报语音内容
        """
        path = f'/rbc/api/supportTest/sendBrodLED3'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_batteryTakePhoto(data):
        """
        电池底部拍照测试
        请求参数:
            savePath: string [可选]
        """
        path = f'/rbc/batteryexchange/batteryTakePhoto'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_conncbmucommand(data):
        """
        车机换电信号确认
        请求参数:
            command: integer [可选]
        """
        path = f'/rbc/batteryexchange/conncbmucommand'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_requestForOssTokenTest(data):
        """
        电池底部拍照测试获取token
        请求参数:
            upType: integer [可选]
        """
        path = f'/rbc/batteryexchange/requestForOssTokenTest'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_sendgetewaycommand(data):
        """
        PLC向站控传递信号
        请求参数:
            command: integer [可选]
        """
        path = f'/rbc/batteryexchange/sendgetewaycommand'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_setsbmumac(data):
        """
        RFID模拟信号
        请求参数:
            command: integer [可选]
            mac: string [可选]
        """
        path = f'/rbc/batteryexchange/setsbmumac'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_swapallow(data):
        """
        有感换电确认信号
        请求参数:
            batteryNum: integer [可选]
            msgId: integer [可选]
            swapAllow: boolean [可选]
        """
        path = f'/rbc/batteryexchange/swapallow'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_swapallownofeel(data):
        """
        无感换电确认信号
        请求参数:
            batteryNum: integer [可选]
            msgId: integer [可选]
            swapAllow: boolean [可选]
        """
        path = f'/rbc/batteryexchange/swapallownofeel'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_swapoffline(data):
        """
        离线一键换电
        请求参数:
            ableToChange: boolean [必填] - 是否可换电
            batteryNum: integer [必填] - 真包数量
            afterChangeHabit: integer [可选] - 换电后行为习惯：1-换电后持续用车，2-换电后休息
            city: string [可选] - 车辆所属城市
            dataDate: integer [可选] - 数据日期
            drivingPeriod: integer [可选] - 习惯用车时段：1-凌晨，2-日间，3-夜间
            energyConsumeType: integer [可选] - 车辆能耗类型：1-高，2-中，3-低
            energySupplyType: integer [可选] - 补能习惯：1-习惯换电，2-无明显倾向，3-习惯充电
            operationType: integer [可选] - 车辆运营情况：1-优，2-良，3-一般，4-差
            parameterConf: string [可选] - 参数列表
            tempLifeEqlType: integer [可选] - 车上电池包等效温度情况：1-高，2-中，3-低
            carModel: string [必填] - 站端车型编码(与系统内编码一一对应)
            carNo: string [必填] - 车牌
            changeType: integer [必填] - 换电方式: 2-有感（默认）, 1-无感
            cloudDownVin: string [必填] - 车辆vin码
            mbmuMac: string [必填] - Mbmu蓝牙mac地址
            msg: string [必填] - 校验结果消息
            offline: boolean [可选]
            sbmuInfo: array [必填] - 上次拆卸电池数据
                        installAddress: integer [可选]
                        packSN: string [可选]
                        packType: integer [可选]
                        sbmuMac: string [可选]
        """
        path = f'/rbc/batteryexchange/swapoffline'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_testSwapallow(data):
        """
        启动换电测试
        """
        path = f'/rbc/batteryexchange/testSwapallow'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_testswap(data):
        """
        测试
        请求参数:
            plateNo: string [可选]
        """
        path = f'/rbc/batteryexchange/testswap'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_batteryexchange_testswap2(data):
        """
        测试2
        请求参数:
            command: integer [可选]
        """
        path = f'/rbc/batteryexchange/testswap2'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_certification_carchangepowertypecmd(data):
        """
        换电方式
        请求参数:
            changePowerType: integer [可选]
            orderId: string [可选]
            vin: string [可选]
        """
        path = f'/rbc/certification/carchangepowertypecmd'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_certification_inpasscarinfo(data):
        """
        车牌校验
        请求参数:
            plateNo: string [可选] - 车牌号
        """
        path = f'/rbc/certification/inpasscarinfo'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_certification_notifyVinCmdOffline(data):
        """
        离线换电车辆vin码校验
        请求参数:
            ableToChange: boolean [必填] - 是否可换电
            batteryNum: integer [必填] - 真包数量
            afterChangeHabit: integer [可选] - 换电后行为习惯：1-换电后持续用车，2-换电后休息
            city: string [可选] - 车辆所属城市
            dataDate: integer [可选] - 数据日期
            drivingPeriod: integer [可选] - 习惯用车时段：1-凌晨，2-日间，3-夜间
            energyConsumeType: integer [可选] - 车辆能耗类型：1-高，2-中，3-低
            energySupplyType: integer [可选] - 补能习惯：1-习惯换电，2-无明显倾向，3-习惯充电
            operationType: integer [可选] - 车辆运营情况：1-优，2-良，3-一般，4-差
            parameterConf: string [可选] - 参数列表
            tempLifeEqlType: integer [可选] - 车上电池包等效温度情况：1-高，2-中，3-低
            carModel: string [必填] - 站端车型编码(与系统内编码一一对应)
            carNo: string [必填] - 车牌
            changeType: integer [必填] - 换电方式: 2-有感（默认）, 1-无感
            cloudDownVin: string [必填] - 车辆vin码
            mbmuMac: string [必填] - Mbmu蓝牙mac地址
            msg: string [必填] - 校验结果消息
            offline: boolean [可选]
            sbmuInfo: array [必填] - 上次拆卸电池数据
                        installAddress: integer [可选]
                        packSN: string [可选]
                        packType: integer [可选]
                        sbmuMac: string [可选]
        """
        path = f'/rbc/certification/notifyVinCmdOffline'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_certification_notifyvincmd(data):
        """
        云端换电结果下发
        请求参数:
            ableToChange: boolean [必填] - 是否可换电
            batteryNum: integer [必填] - 真包数量
            afterChangeHabit: integer [可选] - 换电后行为习惯：1-换电后持续用车，2-换电后休息
            city: string [可选] - 车辆所属城市
            dataDate: integer [可选] - 数据日期
            drivingPeriod: integer [可选] - 习惯用车时段：1-凌晨，2-日间，3-夜间
            energyConsumeType: integer [可选] - 车辆能耗类型：1-高，2-中，3-低
            energySupplyType: integer [可选] - 补能习惯：1-习惯换电，2-无明显倾向，3-习惯充电
            operationType: integer [可选] - 车辆运营情况：1-优，2-良，3-一般，4-差
            parameterConf: string [可选] - 参数列表
            tempLifeEqlType: integer [可选] - 车上电池包等效温度情况：1-高，2-中，3-低
            carModel: string [必填] - 站端车型编码(与系统内编码一一对应)
            carNo: string [必填] - 车牌
            changeType: integer [必填] - 换电方式: 2-有感（默认）, 1-无感
            cloudDownVin: string [必填] - 车辆vin码
            mbmuMac: string [必填] - Mbmu蓝牙mac地址
            msg: string [必填] - 校验结果消息
            offline: boolean [可选]
            sbmuInfo: array [必填] - 上次拆卸电池数据
                        installAddress: integer [可选]
                        packSN: string [可选]
                        packType: integer [可选]
                        sbmuMac: string [可选]
        """
        path = f'/rbc/certification/notifyvincmd'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_preparation_acceptcabin(data):
        """
        电池仓位信息
        请求参数:
            AccessSpace: string [可选]
            SelectSpace: string [可选]
            accessChargeNo: string [可选]
            batteryNo: string [可选]
            chargeNo: string [可选]
            soc: number [可选]
            batteryMileage: number [可选]
            batteryPower: number [可选]
            chargeNo: string [可选]
            cumulativeTotalCharge: number [可选]
            cumulativeTotalDischargePower: number [可选]
            cutStatus: boolean [可选]
            displaySoc: number [可选]
            displaySoh: number [可选]
            isReally: boolean [可选]
            notCredibleFlag: integer [可选]
            sbmuRealSoc: number [可选]
            selectSpaceMac: string [可选]
            snCode: string [可选]
        """
        path = f'/rbc/preparation/acceptcabin'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_preparation_batterydetect(data):
        """
        电池在役信息
        请求参数:
            batteryVerifyResult: boolean [可选]
            msg: string [可选]
            orderId: string [可选]
        """
        path = f'/rbc/preparation/batterydetect'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_preparation_checkcarnobyvehicle(data):
        """
        车辆信息获取
        请求参数:
            batteries: array [可选]
                        batteryMileage: number [可选]
                        batteryNo: string [可选]
                        batteryPower: number [可选]
                        cumulativeTotalCharge: number [可选]
                        cumulativeTotalDischargePower: number [可选]
                        displaySoc: number [可选]
                        displaySoh: number [可选]
                        fluteType: integer [可选]
                        mostSeriouFaultCode: integer [可选]
                        notCredibleFlag: integer [可选]
                        packPollId: string [可选]
                        singleOutputEnergy: number [可选]
                        snCode: string [可选]
                        soe: number [可选]
                        subChaEnergyOutside: number [可选]
                        subOffDischargeEnergy: number [可选]
                        subReEnergyOutside: number [可选]
                        subtotalMileage: number [可选]
                        tripOutChargeEnergy: number [可选]
                        useableSoc: number [可选]
            batteryCapacityTotalOutput: number [可选]
            batterySwapFailReason: string [可选]
            batterySwapSelfCheckFailReason: string [可选]
            bmsBatteryCapacityTotalInput: number [可选]
            bmsFlagBit: string [可选]
            bmsOffStationChargingCapacity: number [可选]
            carNo: string [可选]
            carUploadVin: string [可选]
            cloudDownVin: string [可选]
            hisAccumChrgTimes: integer [可选]
            mbmuMac: string [可选]
            packNo1: string [可选]
            packNo2: string [可选]
            sbmu1Code: integer [可选]
            sbmu2Code: integer [可选]
            subTotalChargeTimeOutStation: integer [可选]
            tbmuMbmuCommSignalStrength: string [可选]
            tripMilKm: number [可选]
            vehicleMileage: number [可选]
        """
        path = f'/rbc/preparation/checkcarnobyvehicle'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_preparation_isvehicleplace(data):
        """
        车身自由度状态
        请求参数:
            autoHold: integer [可选]
            bmcp: number [可选]
            bmcpMax: number [可选]
            bmcpMin: number [可选]
            doorSts: integer [可选]
            epbStatus: integer [可选]
            gear: integer [可选]
            pgearLock: integer [可选]
            saav: number [可选]
            saavMax: number [可选]
            saavMin: number [可选]
            shutDown: integer [可选]
            vehHVState: integer [可选]
        """
        path = f'/rbc/preparation/isvehicleplace'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_preparation_putvehicleinplace(data):
        """
        车辆到位信号
        请求参数:
            inPlace: boolean [可选]
            inPlaceCount: integer [可选]
        """
        path = f'/rbc/preparation/putvehicleinplace'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_preparation_putvgrooveinplace(data):
        """
        V槽到位信号
        请求参数:
            cloudDownPack1Type: integer [可选]
            inPlace: boolean [可选]
            inPlaceCount: integer [可选]
            mbmuMac: string [可选]
        """
        path = f'/rbc/preparation/putvgrooveinplace'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_preparation_sendstationstatus(data):
        """
        车机交互
        请求参数:
            command: integer [可选]
        """
        path = f'/rbc/preparation/sendstationstatus'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_preparation_updateBatteryByVehicle(data):
        """
        更新车辆电池信息
        请求参数:
            batteries: array [可选]
                        batteryMileage: number [可选]
                        batteryNo: string [可选]
                        batteryPower: number [可选]
                        cumulativeTotalCharge: number [可选]
                        cumulativeTotalDischargePower: number [可选]
                        displaySoc: number [可选]
                        displaySoh: number [可选]
                        fluteType: integer [可选]
                        mostSeriouFaultCode: integer [可选]
                        notCredibleFlag: integer [可选]
                        packPollId: string [可选]
                        singleOutputEnergy: number [可选]
                        snCode: string [可选]
                        soe: number [可选]
                        subChaEnergyOutside: number [可选]
                        subOffDischargeEnergy: number [可选]
                        subReEnergyOutside: number [可选]
                        subtotalMileage: number [可选]
                        tripOutChargeEnergy: number [可选]
                        useableSoc: number [可选]
            batteryCapacityTotalOutput: number [可选]
            batterySwapFailReason: string [可选]
            batterySwapSelfCheckFailReason: string [可选]
            bmsBatteryCapacityTotalInput: number [可选]
            bmsFlagBit: string [可选]
            bmsOffStationChargingCapacity: number [可选]
            carNo: string [可选]
            carUploadVin: string [可选]
            cloudDownVin: string [可选]
            hisAccumChrgTimes: integer [可选]
            mbmuMac: string [可选]
            packNo1: string [可选]
            packNo2: string [可选]
            sbmu1Code: integer [可选]
            sbmu2Code: integer [可选]
            subTotalChargeTimeOutStation: integer [可选]
            tbmuMbmuCommSignalStrength: string [可选]
            tripMilKm: number [可选]
            vehicleMileage: number [可选]
        """
        path = f'/rbc/preparation/updateBatteryByVehicle'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_specialSwapMode():
        """
        获取特殊值守模式
        """
        path = f'/rbc/specialSwapMode'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_specialSwapMode_failProcessPath():
        """
        获取异常处理的接口路径
        """
        path = f'/rbc/specialSwapMode/failProcessPath'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_specialSwapMode_passVehicleFreeTask():
        """
        跳过自由度检测任务
        """
        path = f'/rbc/specialSwapMode/passVehicleFreeTask'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_specialSwapMode_reconnectMbmu():
        """
        重连mbmu
        请求参数:
        """
        path = f'/rbc/specialSwapMode/reconnectMbmu'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_specialSwapMode_restartCarMachineTask():
        """
        车辆下高压重试
        """
        path = f'/rbc/specialSwapMode/restartCarMachineTask'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_specialSwapMode_restartCheckBmsSwapTask():
        """
        BMS换电准备重试
        """
        path = f'/rbc/specialSwapMode/restartCheckBmsSwapTask'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_specialSwapMode_restartSelfCheckTask():
        """
        重新开启BMS自检任务
        """
        path = f'/rbc/specialSwapMode/restartSelfCheckTask'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_specialSwapMode_mode(mode):
        """
        特殊值守模式切换
        请求参数:
        """
        path = f'/rbc/specialSwapMode/{mode}'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', None))

    @staticmethod
    def rbc_stationcontrol_batteryTakeStrategy():
        """
        查询取电策略（车包匹配取电策略）
        """
        path = f'/rbc/stationcontrol/batteryTakeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_stationcontrol_batteryTakeStrategy_post(data):
        """
        更新取电策略（车包匹配取电策略）
        请求参数:
            allowCirculationRate: number [可选] - 配对条件 允许环流倍率
            batteryMaxSocDiff: number [可选] - 海选条件 电池内SOC最大差值（%）
            batteryMaxTemp: integer [可选] - 海选条件 电池最高温度（℃）
            batteryMinChargeCompletedTime: integer [可选] - 海选条件 电池最低充电完成时间（min)
            cloudUpdateTime: integer [可选]
            cloudUpdateUser: string [可选]
            enableCarAndPackMatch: boolean [可选] - 是否开启车包匹配
            matchCycleDod: integer [可选] - 配对条件 累计Cycle数
            matchMaxSocDiff: number [可选] - 配对条件 最大soc差值（%）
            matchMaxSohDiff: number [可选] - 配对条件 最大soh差值（%）
            matchMaxVoltageDiff: integer [可选] - 配对条件 最大电压差值 (V)
            matchTempDiff: integer [可选] - 配对条件 最大温差 (℃)
            minSoc: number [可选] - 电池最低soc（开启和不开启车包匹配共用字段）
        """
        path = f'/rbc/stationcontrol/batteryTakeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_stationcontrol_faulthandling(data):
        """
        故障处理
        请求参数:
        """
        path = f'/rbc/stationcontrol/faulthandling'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_stationcontrol_getstationinfobystatus():
        """
        站点服务
        """
        path = f'/rbc/stationcontrol/getstationinfobystatus'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_stationcontrol_getswaptimeout():
        """
        获取线程超时信息
        """
        path = f'/rbc/stationcontrol/getswaptimeout'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_stationcontrol_getunloadbattery():
        """
        获取卸载电池信息
        请求参数:
        """
        path = f'/rbc/stationcontrol/getunloadbattery'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_stationcontrol_openSwapStation(data):
        """
        歇业/营业站点
        请求参数:
        """
        path = f'/rbc/stationcontrol/openSwapStation'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_stationcontrol_repOrder():
        """
        手动上报订单
        请求参数:
        """
        path = f'/rbc/stationcontrol/repOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_stationcontrol_selectPackDetailLockTimer():
        """
        查询机械锁状态上报周期
        """
        path = f'/rbc/stationcontrol/selectPackDetailLockTimer'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_stationcontrol_selectstationdevice():
        """
        查询站点设备信息
        """
        path = f'/rbc/stationcontrol/selectstationdevice'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'GET', None))

    @staticmethod
    def rbc_stationcontrol_setPackDetailLockTimer(data):
        """
        设置机械锁状态上报周期
        请求参数:
            exportTime: integer [可选] - 机械锁状态上报周期 ms
        """
        path = f'/rbc/stationcontrol/setPackDetailLockTimer'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_stationcontrol_setstationdevice(data):
        """
        设置站点设备信息
        请求参数:
            deviceBaseDtoList: array [可选]
                        deviceId: string [可选]
                        deviceName: string [可选]
                        existFlag: string [可选]
                        stationProcessWayDtoList: array [可选]
                                    businessDetail: string [可选]
                                    businessDetailNo: string [可选]
                                    deviceId: string [可选]
                                    existTriggerFlag: string [可选]
                                    timeOut: string [可选]
                                    triggerFlag: string [可选]
            stationId: string [可选]
            stationType: string [可选]
        """
        path = f'/rbc/stationcontrol/setstationdevice'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_stationcontrol_setswaptimeout(data):
        """
        配置线程超时信息
        请求参数:
            autoModelSelect: integer [可选]
            autoModelSelectVoice: integer [可选]
            bluetoothBreak: integer [可选]
            carMachSignal: integer [可选]
            checkCarMach: integer [可选]
            checkCarNoVehicle: integer [可选]
            cloudCanLetCarEnter: integer [可选]
            connCarMachine: integer [可选]
            createTime: string [可选]
            id: integer [可选]
            macAddrCheck: integer [可选]
            manageBatteryModel: integer [可选]
            plcSignal: integer [可选]
            putVehicleInPlace: integer [可选]
            putVehicleInPlaceVoice: integer [可选]
            rbcModelSelect: integer [可选]
            swapCarMachine: integer [可选]
            swapPauseCloseDoor: integer [可选]
            updateTime: string [可选]
            userSwapAllowRequest: integer [可选]
            userSwapAllowRequestVoice: integer [可选]
            vehicleFreeStatus: integer [可选]
            vehicleFreeStatusVoice: integer [可选]
            vgrooveInPlace: integer [可选]
        """
        path = f'/rbc/stationcontrol/setswaptimeout'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_stationcontrol_swapreset(data):
        """
        换电系统复位
        请求参数:
            swapReset: boolean [可选]
        """
        path = f'/rbc/stationcontrol/swapreset'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))

    @staticmethod
    def rbc_wsMessage_swapProgress(data):
        """
        发送换电进程消息
        请求参数:
            command: integer [可选]
            bmcp: boolean [可选]
            doorSts: boolean [可选]
            epbStatus: boolean [可选]
            gear: boolean [可选]
            saav: boolean [可选]
            shutDown: boolean [可选]
            vehHVState: boolean [可选]
            inPlace: boolean [可选]
            qrCodeMsg: string [可选]
            read: integer [可选]
            stop: boolean [可选]
            timeOut: string [可选]
            tips: string [可选]
            tipsText: string [可选]
            voiceCode: string [可选]
            voicePath: string [可选]
        """
        path = f'/rbc/wsMessage/swapProgress'
        return HttpRq.req(*HttpMethod.http_info(ApiRbc._get_path(path), 'POST', data))
