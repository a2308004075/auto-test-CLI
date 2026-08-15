from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiEmu:
    @staticmethod
    def _get_path(path):
        service = '/emu'
        return service + path

    @staticmethod
    def api_device_getAllDevice(data):
        """
        获取所有设备列表
        """
        path = f'/api/device/getAllDevice'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_device_getEmuConfig(data):
        """
        获取EMU配置
        """
        path = f'/api/device/getEmuConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_device_getStationConfig(data):
        """
        获取电站配置配置
        """
        path = f'/api/device/getStationConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_clearCmdCache(data):
        """
        清除设备命令缓存记录
        """
        path = f'/api/emu/clearCmdCache'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_chargeCmd(data):
        """
        充放电命令下发
        请求参数:
            adjustType: integer [可选] - 1：采用设备内部电池需求功率进行充电； 默认值  2：设置充/放电功率上限值
            cmdScene: integer [可选] - 触发场景,原因,参考协议文档定义
            cmdSource: integer [可选] - 触发来源 1.云端  2.站控   3.储能柜/设备本地  4.EMU
            cmdType: integer [可选] - 命令类型  0:停止充电 1:停止放电   2:充电开启    3:放电开启   4:充电功率调控  5:放电功率调控 
            deviceId: string [可选] - 指定设备ID
            endSoc: number [可选] - 停止soc  0--1
            endTime: integer [可选] -  停止时间
            maxPower: number [可选] - 指定功率， adjustType=2 必须设置 ,大于1 kw
        """
        path = f'/api/emu/ess/chargeCmd'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_getAllDevRealData(data):
        """
        获取所有设备实时状态数据
        """
        path = f'/api/emu/ess/getAllDevRealData'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_getDevInfo(data):
        """
        获取储能设备基本信息
        请求参数:
            deviceId: string [可选] - 根据设备ID获取设备信息  ，优先使用设备ID条件查询
            ip: string [可选] - 根据IP获取设备信息
            type: string [可选] - 查询方式，emu 从EMU本地缓存查询，dev 发送命令给储能设备进行查询
        """
        path = f'/api/emu/ess/getDevInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_getDevParamConfig(data):
        """
        获取设备参数配置
        请求参数:
            deviceId: string [可选] - 根据设备ID获取设备信息  ，优先使用设备ID条件查询
            ip: string [可选] - 根据IP获取设备信息
            type: string [可选] - 查询方式，emu 从EMU本地缓存查询，dev 发送命令给储能设备进行查询
        """
        path = f'/api/emu/ess/getDevParamConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_getDevRealData(data):
        """
        获取指定设备实时状态数据
        请求参数:
            deviceId: string [可选] - 根据设备ID获取设备信息  ，优先使用设备ID条件查询
            ip: string [可选] - 根据IP获取设备信息
            type: string [可选] - 查询方式，emu 从EMU本地缓存查询，dev 发送命令给储能设备进行查询
        """
        path = f'/api/emu/ess/getDevRealData'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_getEssCacheData(data):
        """
        储能设备最后一帧遥测缓存数据
        请求参数:
            deviceId: string [可选] - 根据设备ID获取设备信息  ，优先使用设备ID条件查询
            ip: string [可选] - 根据IP获取设备信息
            type: string [可选] - 查询方式，emu 从EMU本地缓存查询，dev 发送命令给储能设备进行查询
        """
        path = f'/api/emu/ess/getEssCacheData'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_history_getDevAlarmEvent(data):
        """
        设备故障记录
        请求参数:
            current: integer [可选]
            deviceId: string [可选] - 根据设备ID获取设备信息 ,优先使用设备ID条件查询
            endTime: string [可选]
            ip: string [可选] - 根据IP获取设备信息
            level: integer [可选]
            module: string [可选]
            moduleSn: integer [可选]
            msgId: string [可选] - 云端/站控发起请求消息唯一ID
            reason: integer [可选] - 操作原因 
            size: integer [可选]
            source: integer [可选] - 命令来源 1云端 2 站控
            startTime: string [可选]
        """
        path = f'/api/emu/ess/history/getDevAlarmEvent'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_history_getDevChargeOrder(data):
        """
        获取订单记录
        请求参数:
            current: integer [可选]
            deviceId: string [可选] - 根据设备ID获取设备信息 ,优先使用设备ID条件查询
            endTime: string [可选]
            ip: string [可选] - 根据IP获取设备信息
            level: integer [可选]
            module: string [可选]
            moduleSn: integer [可选]
            msgId: string [可选] - 云端/站控发起请求消息唯一ID
            reason: integer [可选] - 操作原因 
            size: integer [可选]
            source: integer [可选] - 命令来源 1云端 2 站控
            startTime: string [可选]
        """
        path = f'/api/emu/ess/history/getDevChargeOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_history_getDevOperateLog(data):
        """
        获取命令操作记录
        请求参数:
            current: integer [可选]
            deviceId: string [可选] - 根据设备ID获取设备信息 ,优先使用设备ID条件查询
            endTime: string [可选]
            ip: string [可选] - 根据IP获取设备信息
            level: integer [可选]
            module: string [可选]
            moduleSn: integer [可选]
            msgId: string [可选] - 云端/站控发起请求消息唯一ID
            reason: integer [可选] - 操作原因 
            size: integer [可选]
            source: integer [可选] - 命令来源 1云端 2 站控
            startTime: string [可选]
        """
        path = f'/api/emu/ess/history/getDevOperateLog'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_history_getDevSysEvent(data):
        """
        设备系统事件记录
        请求参数:
            current: integer [可选]
            deviceId: string [可选] - 根据设备ID获取设备信息 ,优先使用设备ID条件查询
            endTime: string [可选]
            ip: string [可选] - 根据IP获取设备信息
            level: integer [可选]
            module: string [可选]
            moduleSn: integer [可选]
            msgId: string [可选] - 云端/站控发起请求消息唯一ID
            reason: integer [可选] - 操作原因 
            size: integer [可选]
            source: integer [可选] - 命令来源 1云端 2 站控
            startTime: string [可选]
        """
        path = f'/api/emu/ess/history/getDevSysEvent'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_ipConfig(data):
        """
        储能设备IP配置
        请求参数:
            deviceNum: integer [可选] - 设备序号 1--5
            ip: string [可选] - ip地址
            status: integer [可选] - 0 未配置   1 配置
        """
        path = f'/api/emu/ess/ipConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_safetyAlert(data):
        """
        设备安全预警通知
        请求参数:
            deviceId: string [可选]
            eventCode: integer [可选]
            eventId: string [可选]
            eventName: string [可选]
            ip: string [可选] - 根据IP获取设备信息
            level: integer [可选]
            msgId: string [可选] - 云端/站控发起请求消息唯一ID
            packNum: integer [可选]
            packSn: string [可选]
            reason: integer [可选] - 操作原因 
            remark: string [可选]
            source: integer [可选] - 命令来源 1云端 2 站控
            time: integer [可选]
        """
        path = f'/api/emu/ess/safetyAlert'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_syncTime(data):
        """
        同步设备时间
        请求参数:
            deviceId: string [可选] - 根据设备ID获取设备信息  ，优先使用设备ID条件查询
            ip: string [可选] - 根据IP获取设备信息
            type: string [可选] - 查询方式，emu 从EMU本地缓存查询，dev 发送命令给储能设备进行查询
        """
        path = f'/api/emu/ess/syncTime'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_ess_updateParamConfig(data):
        """
        修改设备参数配置
        请求参数:
            antiRefluxEnable: integer [可选] - 0 关闭防逆流  1 开启防逆流，默认开启
            gridPower: number [可选] - 防逆流市电功率监控限值，大于0
            updateDate: integer [可选] - 修改时间
            maxChargePower: number [可选] - 最大充电功率
            maxDischargePower: number [可选] - 最大放电功率
            powerControlEnable: integer [可选] - 0 关闭  1 开启
            updateDate: integer [可选] - 修改时间
            dataReportEnable: integer [可选] - 是否主动上报遥测数据   0 关闭  1 开启    默认开启
            essDataCollect: integer [可选] - 全量数据采集频率 单位 ms
            gridMeterCollect: integer [可选] - 箱变电表采集频率  单位 ms
            packDataCollect: integer [可选] - 充电过程电池包采集频率 单位 ms
            updateDate: integer [可选] - 修改时间
            demandEnable: integer [可选] - 需量控制开启  0 关闭需量控制  1 开启需量控制，默认开启
            demandVaule: number [可选] - 需量值  kw
            updateDate: integer [可选] - 修改时间
            deviceId: string [可选] - 根据设备ID获取设备信息 ,优先使用设备ID条件查询
            ip: string [可选] - 根据IP获取设备信息
            msgId: string [可选] - 云端/站控发起请求消息唯一ID
            reason: integer [可选] - 操作原因 
            source: integer [可选] - 命令来源 1云端 2 站控
            type: integer [可选] - 1 充放电控制、防逆流参数、需量控制参数修改  2 数据采集配置修改  3 需量控制参数修改
        """
        path = f'/api/emu/ess/updateParamConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_getCmdCache(data):
        """
        获取设备命令缓存记录
        """
        path = f'/api/emu/getCmdCache'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_getDeviceSession(data):
        """
        获取设备链接信息
        """
        path = f'/api/emu/getDeviceSession'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_test_cloud_reportChargePackData(data):
        """
        pack遥测数据上报
        请求参数:
            bmu: array [可选]
                        alarmCode: array [可选]
                        alarmStatus: integer [可选]
                        commStatus: integer [可选]
                        deviceNum: integer [可选]
                        deviceSn: string [可选]
                        fltLevel: integer [可选]
                        heatStatus: integer [可选]
                        insulationEnable: integer [可选]
                        mainNegCnctrStatus: integer [可选]
                        mainPosCnctrStatus: integer [可选]
                        negativeInsulation: number [可选]
                        positiveInsulation: number [可选]
                        soc: number [可选]
                        soh: number [可选]
                        totalCharge: number [可选]
                        totalDisCharge: number [可选]
                        waterCoolingStatus: integer [可选]
                        workStatus: integer [可选]
                        avgTemp: number [可选]
                        avgVoltage: number [可选]
                        maxTemp: number [可选]
                        maxTempNum: integer [可选]
                        maxVoltage: number [可选]
                        maxVoltageCellNum: integer [可选]
                        minTemp: number [可选]
                        minTempNum: integer [可选]
                        minVoltage: number [可选]
                        minVoltageCellNum: integer [可选]
                        tempDiff: number [可选]
                        voltageDiff: number [可选]
                        cellVoltageList: array [可选]
                        current: number [可选]
                        tempList: array [可选]
                        voltage: number [可选]
            dataId: string [可选]
            devTime: integer [可选]
        """
        path = f'/api/test/cloud/reportChargePackData'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_test_cloud_reportDevAlarmEvent(data):
        """
        模拟设备告警、系统事件上报
        请求参数:
            deviceId: string [可选]
            deviceSn: string [可选]
            deviceType: integer [可选]
            endTime: integer [可选] - 故障恢复时间
            eventCode: integer [可选] - 故障/事件代码
            eventId: string [可选] - 故障唯一标识UUID
            eventName: string [可选] - 故障/事件名称
            level: integer [可选] - 故障等级  1级   2级  3级别
            module: string [可选] - 模块代码
            moduleNum: integer [可选] - 模块序号
            moduleSn: string [可选] - 模块编号/sn
            remark: string [可选] - 备注
            startTime: integer [可选] - 故障/事件开始时间
        """
        path = f'/api/test/cloud/reportDevAlarmEvent'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_test_cloud_reportDevData(data):
        """
        储能柜全量遥测数据上报
        请求参数:
            aCurrent: number [可选]
            aVoltage: number [可选]
            abVoltage: number [可选]
            acBreakerStatus: integer [可选]
            acVoltage: number [可选]
            activePower: number [可选]
            alarmStatus: integer [可选]
            apparentPower: number [可选]
            bCurrent: number [可选]
            bVoltage: number [可选]
            bcVoltage: number [可选]
            cCurrent: number [可选]
            cVoltage: number [可选]
            chargeLeftTime: number [可选]
            dischargeLeftTime: number [可选]
            gridStatus: integer [可选]
            powerFactor: number [可选]
            reactivePower: number [可选]
            soc: number [可选]
            soe: number [可选]
            soh: number [可选]
            sysCurrent: number [可选]
            sysVoltage: number [可选]
            totalCharge: number [可选]
            totalDisCharge: number [可选]
            totalUseEnergy: number [可选]
            workStatus: integer [可选]
            bmu: array [可选]
                        alarmCode: array [可选]
                        alarmStatus: integer [可选]
                        commStatus: integer [可选]
                        deviceNum: integer [可选]
                        deviceSn: string [可选]
                        fltLevel: integer [可选]
                        heatStatus: integer [可选]
                        insulationEnable: integer [可选]
                        mainNegCnctrStatus: integer [可选]
                        mainPosCnctrStatus: integer [可选]
                        negativeInsulation: number [可选]
                        positiveInsulation: number [可选]
                        soc: number [可选]
                        soh: number [可选]
                        totalCharge: number [可选]
                        totalDisCharge: number [可选]
                        waterCoolingStatus: integer [可选]
                        workStatus: integer [可选]
                        avgTemp: number [可选]
                        avgVoltage: number [可选]
                        maxTemp: number [可选]
                        maxTempNum: integer [可选]
                        maxVoltage: number [可选]
                        maxVoltageCellNum: integer [可选]
                        minTemp: number [可选]
                        minTempNum: integer [可选]
                        minVoltage: number [可选]
                        minVoltageCellNum: integer [可选]
                        tempDiff: number [可选]
                        voltageDiff: number [可选]
                        cellVoltageList: array [可选]
                        current: number [可选]
                        tempList: array [可选]
                        voltage: number [可选]
            avgTemp: number [可选]
            avgVoltage: number [可选]
            maxTemp: number [可选]
            maxTempNum: integer [可选]
            maxTempPackNum: integer [可选]
            maxTempPackSn: string [可选]
            maxVoltage: number [可选]
            maxVoltageCellNum: integer [可选]
            maxVoltagePackNum: integer [可选]
            maxVoltagePackSn: string [可选]
            minTemp: number [可选]
            minTempNum: integer [可选]
            minTempPackNum: integer [可选]
            minTempPackSn: string [可选]
            minVoltage: number [可选]
            minVoltageCellNum: integer [可选]
            minVoltagePackNum: integer [可选]
            minVoltagePackSN: string [可选]
            tempDiff: number [可选]
            voltageDiff: number [可选]
            dataId: string [可选]
            alarmCode: array [可选]
            alarmStatus: integer [可选]
            commStatus: integer [可选]
            humidity: number [可选]
            temp: number [可选]
            workStatus: integer [可选]
            devTime: integer [可选]
            aerosolStatus: array [可选]
            alarmCode: array [可选]
            alarmStatus: integer [可选]
            commStatus: integer [可选]
            fireFightingStatus: integer [可选]
            smokeStatus: array [可选]
            tempStatus: array [可选]
            workStatus: integer [可选]
            commStatus: integer [可选]
            gridPower: number [可选]
            alarmCode: array [可选]
            alarmStatus: integer [可选]
            commStatus: integer [可选]
            controlMode: integer [可选]
            pressure: array [可选]
            temp: array [可选]
            workStatus: integer [可选]
            dcdcList: array [可选]
            doorStatus: integer [可选]
            fanList: array [可选]
            humidityList: array [可选]
            pcsList: array [可选]
            tempList: array [可选]
            upsStatus: integer [可选]
            waterStatus: integer [可选]
            avgSoc: number [可选]
            avgTemp: number [可选]
            avgVoltage: number [可选]
            maxSoc: number [可选]
            maxSocPackNum: integer [可选]
            maxSocPackSn: string [可选]
            maxTemp: number [可选]
            maxTempNum: integer [可选]
            maxTempPackNum: integer [可选]
            maxTempPackSn: string [可选]
            maxVoltage: number [可选]
            maxVoltagePackNum: integer [可选]
            maxVoltagePackSn: string [可选]
            minInsulation: number [可选]
            minInsulationPackNum: integer [可选]
            minInsulationPackSn: string [可选]
            minSoc: number [可选]
            minSocPackNum: integer [可选]
            minSocPackSn: string [可选]
            minTemp: number [可选]
            minTempNum: integer [可选]
            minTempPackNum: integer [可选]
            minTempPackSn: string [可选]
            minVoltage: number [可选]
            minVoltagePackNum: integer [可选]
            minVoltagePackSn: string [可选]
            socDiff: number [可选]
            tempDiff: number [可选]
            voltageDiff: number [可选]
        """
        path = f'/api/test/cloud/reportDevData'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))

    @staticmethod
    def api_test_cloud_reportOnlineMsg(data):
        """
        设备上下线通知
        """
        path = f'/api/test/cloud/reportOnlineMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiEmu._get_path(path), 'POST', data))
