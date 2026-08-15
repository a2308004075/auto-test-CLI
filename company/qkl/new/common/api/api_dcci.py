from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiDcci:
    @staticmethod
    def _get_path(path):
        service = '/dcci'
        return service + path

    @staticmethod
    def api_chargerControl_feign_clearBbsFault(data):
        """
        清除BBS故障
        请求参数:
            chargeFaultTypeEnum: string [可选] - 故障上报设备类型
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
        """
        path = f'/api/chargerControl/feign/clearBbsFault'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_configPricePeriod(data):
        """
        配置电价时段
        请求参数:
            chargerNo: integer [可选] - 充电设备编号
            items: array [可选] - 时段配置列表
                        index: integer [可选]
                        periodType: integer [可选]
                        startTime: string [可选]
            periodCount: integer [可选] - 时段数量
        """
        path = f'/api/chargerControl/feign/configPricePeriod'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_controlChargeRate(data):
        """
        控制充电速率
        请求参数:
            chargeRateModel: number [可选] - 倍率，范围0.1到1
            position: integer [可选] - 仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/controlChargeRate'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_controlChargeUpgrade(data):
        """
        控制充电升级
        请求参数:
            bytesPerPacket: integer [可选] - 每包字节数
            chargerNo: integer [可选] - 充电机号
            controlBoardType: integer [可选] - 控制板类型
            fileSize: integer [可选] - 文件大小
            fileUrl: string [可选] - 文件URL
            subType: string [可选] - 下控子类型
            totalPacket: integer [可选] - 总包数
        """
        path = f'/api/chargerControl/feign/controlChargeUpgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_controlOfflineStopCharge(data):
        """
        控制离线停止充电
        请求参数:
            position: integer [可选] - 仓位号
            result: integer [可选] - 0：不使能 1：使能
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/controlOfflineStopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_curCommandCache():
        """
        获取当前指令缓存
        """
        path = f'/api/chargerControl/feign/curCommandCache'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'GET', None))

    @staticmethod
    def api_chargerControl_feign_keyonControl(data):
        """
        钥匙开关控制
        请求参数:
            keyonControl: integer [可选] - 1：KEYON电源导通 0：KEYON电源断开
            position: integer [可选] - 仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/keyonControl'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_keyonControls(data):
        """
        批量钥匙开关控制
        请求参数:
            keyonControl: integer [可选] - 1：KEYON电源导通 0：KEYON电源断开
            position: integer [可选] - 仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/keyonControls'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_queryConfigPricePeriod(data):
        """
        查询配置价格时段
        """
        path = f'/api/chargerControl/feign/queryConfigPricePeriod'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_restCharge(data):
        """
        重置充电
        请求参数:
            chargerNo: integer [可选] - 充电机号
            controlPanelNo: integer [可选] - 控制板编号
            controlPanelType: integer [可选] - 控制板类型
            resetMode: integer [可选] - 复位方式 1:软复位 2：硬复位
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/restCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_sendChargeAdjustParam(data):
        """
        发送充电调整参数
        请求参数:
            electricityAdjustParam: number [可选] - 电流调节参数 Factor：0.1 单位：A
            flowNo: string [可选] - 流水号
            position: integer [可选] - 仓位号
            powerAdjustParam: number [可选] - 功率调节参数 Factor：0.1 单位：kW
            powerAdjustType: integer [可选] - 功率调节指令类型 1：采用BMS充电Map进行功率控制 2：执行功率调节，设置充电功率上限值 3：采用充电map比列调节 4：执行最大电流限制
            powerPercentage: integer [可选] - 功率百分比 功率调节指令为3时执行，分辨率为1，其他功率调节指令时值为0
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/sendChargeAdjustParam'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_sendModuleSerialNumber(data):
        """
        下发充电模块序列号
        请求参数:
        """
        path = f'/api/chargerControl/feign/sendModuleSerialNumber'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_setDeviceParam(data):
        """
        设置设备参数
        请求参数:
            chargeDeviceOverTemperatureThreshold: number [可选] - 充电设备过温阈值
            chargerNo: integer [可选] - 充电机号
            dcMeterBaudRate: integer [可选] - 直流电表波特率
            dcMeterModel: integer [可选] - 直流电表型号
            doorQuote: integer [可选] - 门禁报警
            inputOverVoltageThreshold: number [可选] - 输入过压阈值
            inputUnderVoltageThreshold: number [可选] - 输入欠压阈值
            limitSoc: integer [可选] - 本地SOC限制
            noEffectiveCurrentContinuouslyCharged: integer [可选] - 无有效电流可持续充电
            offlineChargeTs: integer [可选] - 离线充电时间
            outOvervoltageThreshold: number [可选] - 输出过压阈值
            overcurrentFilterTs: number [可选] - 过流滤波时间
            powerLossCompensationCoefficient: integer [可选] - 电损补偿系数
            simulatedCharged: integer [可选] - 模拟充电
            singleOutputOvercurrentThreshold: number [可选] - 单路输出过流阈值
            stationChargeStrategy: integer [可选] - 站内外充放电策略 0:站内优先 1:站外优先 2:优先启动调用（先到先得）
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/setDeviceParam'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_setStationStatus(data):
        """
        设置站点状态
        请求参数:
            chargerNo: integer [可选] - 充电机号，空代表全部
            reason: integer [可选] - 故障原因
            status: integer [可选] - 换电站安全状态
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/setStationStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_startCharge(data):
        """
        开始充电
        请求参数:
            direction: integer [可选] - 充放电方向
            electricityAdjustParam: number [可选] - 电流调节参数 功率调节指令为4时，Factor：0.1 单位：A；其他功率调节指令时值为0
            flowNo: string [可选] - 充电机交互流水号
            msgId: string [可选] - 下控唯一标志
            position: integer [可选] - 仓位号
            powerAdjustParam: number [可选] - 功率调节参数 功率调节指令为2时，Factor：0.1 单位：kW；其他功率调节指令时值为0
            powerAdjustType: integer [可选] - 功率调节指令类型 1:采用BMS充电Map进行功率控制 2:执行功率调节，设置充电功率上限值 3:采用充电map比列调节 4:执行最大电流限制
            powerPercentage: number [可选] - 功率百分比 功率调节指令为3时执行，分辨率为1，其他功率调节指令时值为0
            socLimit: integer [可选] - soc限制 百分比
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/startCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_startStopHotControl(data):
        """
        启动/停止热管理控制
        请求参数:
            chargerNo: integer [可选]
            gun1: integer [可选]
            gun2: integer [可选]
            gun3: integer [可选]
            gun4: integer [可选]
            startStopControl: integer [可选]
            supportHotNum: integer [可选]
        """
        path = f'/api/chargerControl/feign/startStopHotControl'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerControl_feign_stopCharge(data):
        """
        停止充电
        请求参数:
            flowNo: string [可选] - 充电机交互流水号
            msgId: string [可选] - 下控唯一标志
            position: integer [可选] - 仓位号
            stopReason: integer [可选] - 1.停止原因 0正常充满停机 1服务器发现桩异常,强制停机 2 账号校验失败 3APP主动停机 4 账号欠费 5无可用模块
            subType: string [可选] - 下控子类型
        """
        path = f'/api/chargerControl/feign/stopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getBatteryInfoByPosition(data):
        """
        根据位置获取电池信息
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getBatteryInfoByPosition'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargeDetailInfoByChargerNo(data):
        """
        根据充电桩编号获取充电详情信息
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getChargeDetailInfoByChargerNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargeEquipInfoByChargerNo(data):
        """
        根据充电桩编号获取充电设备信息
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getChargeEquipInfoByChargerNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargeEquipList(data):
        """
        获取充电设备列表
        """
        path = f'/api/chargerQuery/feign/getChargeEquipList'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargeFaultNumByChargerNo(data):
        """
        根据充电桩编号获取故障数量
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getChargeFaultNumByChargerNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargeSettingInfoByChargerNo(data):
        """
        根据充电桩编号获取充电设置信息
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getChargeSettingInfoByChargerNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargerBaseInfo(data):
        """
        获取充电桩基本信息
        """
        path = f'/api/chargerQuery/feign/getChargerBaseInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargerCacheInfo(data):
        """
        获取充电桩缓存信息
        """
        path = f'/api/chargerQuery/feign/getChargerCacheInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargerNoAndGunNo(data):
        """
        获取充电桩编号和充电枪编号
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getChargerNoAndGunNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getChargerNoByPosition(data):
        """
        根据位置获取充电桩编号
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getChargerNoByPosition'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getCloseCampList(data):
        """
        获取关闭营位列表
        """
        path = f'/api/chargerQuery/feign/getCloseCampList'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getCurrentFaultInfo(data):
        """
        获取当前故障信息
        请求参数:
            chargeFaultTypeEnum: string [可选] - 故障上报设备类型
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
        """
        path = f'/api/chargerQuery/feign/getCurrentFaultInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getEquipmentProducer(data):
        """
        获取设备生产商
        """
        path = f'/api/chargerQuery/feign/getEquipmentProducer'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getGunInfo(data):
        """
        获取充电枪信息
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getGunInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getGunInfoByPosition(data):
        """
        根据位置获取充电枪信息
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getGunInfoByPosition'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getGunRsInfo(data):
        """
        获取充电枪信息列表
        请求参数:
            chargerNoList: array [可选] - 充电机编号列表
            positionList: array [可选] - 仓位编号列表
        """
        path = f'/api/chargerQuery/feign/getGunRsInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getPduChargeNoList(data):
        """
        获取pdu充电机号列表
        """
        path = f'/api/chargerQuery/feign/getPduChargeNoList'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_getPositionByChargerNo(data):
        """
        根据充电桩编号获取位置
        请求参数:
        """
        path = f'/api/chargerQuery/feign/getPositionByChargerNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_queryChargerInfoList(data):
        """
        查询充电桩信息列表
        请求参数:
            chargerNoList: array [可选] - 充电机编号列表
            positionList: array [可选] - 仓位编号列表
        """
        path = f'/api/chargerQuery/feign/queryChargerInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_queryConfigPricePeriod(data):
        """
        查询配置价格时段
        请求参数:
        """
        path = f'/api/chargerQuery/feign/queryConfigPricePeriod'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_queryDeviceParam(data):
        """
        查询设备参数
        """
        path = f'/api/chargerQuery/feign/queryDeviceParam'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerQuery_feign_queryVersion(data):
        """
        查询版本信息
        """
        path = f'/api/chargerQuery/feign/queryVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dcci_local_cleanDcciCmd(data):
        """
        cleanDcciCmd
        请求参数:
            dcciCommandTypeEnum: string [可选]
            position: integer [可选]
        """
        path = f'/api/dcci/local/cleanDcciCmd'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dcci_local_configPricePeriod(data):
        """
        发送尖峰平谷配置
        请求参数:
            chargerNo: integer [可选] - 充电设备编号
            items: array [可选] - 时段配置列表
                        index: integer [可选]
                        periodType: integer [可选]
                        startTime: string [可选]
            periodCount: integer [可选] - 时段数量
        """
        path = f'/api/dcci/local/configPricePeriod'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dcci_local_curCommandCache(data):
        """
        查询当前缓存中的下控命令
        """
        path = f'/api/dcci/local/curCommandCache'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dcci_local_keyonControl(data):
        """
        发送keyon下控
        请求参数:
            keyonControl: integer [可选] - 1：KEYON电源导通 0：KEYON电源断开
            position: integer [可选] - 仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/dcci/local/keyonControl'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dcci_local_keyonControls(data):
        """
        发送批量keyon下控
        请求参数:
            keyonControl: integer [可选] - 1：KEYON电源导通 0：KEYON电源断开
            position: integer [可选] - 仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/dcci/local/keyonControls'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dcci_local_sendChargeAdjustParam(data):
        """
        发送充电中充电参数调节指令
        请求参数:
            electricityAdjustParam: number [可选] - 电流调节参数 Factor：0.1 单位：A
            flowNo: string [可选] - 流水号
            position: integer [可选] - 仓位号
            powerAdjustParam: number [可选] - 功率调节参数 Factor：0.1 单位：kW
            powerAdjustType: integer [可选] - 功率调节指令类型 1：采用BMS充电Map进行功率控制 2：执行功率调节，设置充电功率上限值 3：采用充电map比列调节 4：执行最大电流限制
            powerPercentage: integer [可选] - 功率百分比 功率调节指令为3时执行，分辨率为1，其他功率调节指令时值为0
            subType: string [可选] - 下控子类型
        """
        path = f'/api/dcci/local/sendChargeAdjustParam'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dcci_local_startCharge(data):
        """
        发送启动充电
        请求参数:
            direction: integer [可选] - 充放电方向
            electricityAdjustParam: number [可选] - 电流调节参数 功率调节指令为4时，Factor：0.1 单位：A；其他功率调节指令时值为0
            flowNo: string [可选] - 充电机交互流水号
            msgId: string [可选] - 下控唯一标志
            position: integer [可选] - 仓位号
            powerAdjustParam: number [可选] - 功率调节参数 功率调节指令为2时，Factor：0.1 单位：kW；其他功率调节指令时值为0
            powerAdjustType: integer [可选] - 功率调节指令类型 1:采用BMS充电Map进行功率控制 2:执行功率调节，设置充电功率上限值 3:采用充电map比列调节 4:执行最大电流限制
            powerPercentage: number [可选] - 功率百分比 功率调节指令为3时执行，分辨率为1，其他功率调节指令时值为0
            socLimit: integer [可选] - soc限制 百分比
            subType: string [可选] - 下控子类型
        """
        path = f'/api/dcci/local/startCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dcci_local_stopCharge(data):
        """
        发送停止充电
        请求参数:
            flowNo: string [可选] - 充电机交互流水号
            msgId: string [可选] - 下控唯一标志
            position: integer [可选] - 仓位号
            stopReason: integer [可选] - 1.停止原因 0正常充满停机 1服务器发现桩异常,强制停机 2 账号校验失败 3APP主动停机 4 账号欠费 5无可用模块
            subType: string [可选] - 下控子类型
        """
        path = f'/api/dcci/local/stopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerControl_feign_startCharge(data):
        """
        DCCO开始充电
        请求参数:
            cloudFlowNo: string [可选] - 云端流水号
            controlParam: integer [可选] - 控制参数
            controlType: integer [可选] - 控制类型
            direction: integer [可选] - 充放电方向
            flowNo: string [可选] - 充电机交互流水号
            msgId: string [可选] - 下控唯一标志
            param: number [可选] - 参数
            position: integer [可选] - 仓位号
            powerAdjustType: integer [可选] - 功率调节指令类型 1:采用BMS充电Map进行功率控制 2:执行功率调节，设置充电功率上限值 3:采用充电map比列调节 4:执行最大电流限制
            socLimit: integer [可选] - soc限制 百分比
            subType: string [可选] - 下控子类型
        """
        path = f'/api/dccoChargerControl/feign/startCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerControl_feign_stopCharge(data):
        """
        DCCO停止充电
        请求参数:
            cloudFlowNo: string [可选] - 云端流水号
            flowNo: string [可选] - 充电机交互流水号
            msgId: string [可选] - 下控唯一标志
            position: integer [可选] - 仓位号
            stopReason: integer [可选] - 1.停止原因 0正常充满停机 1服务器发现桩异常,强制停机 2 账号校验失败 3APP主动停机 4 账号欠费 5无可用模块
            subType: string [可选] - 下控子类型
        """
        path = f'/api/dccoChargerControl/feign/stopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerQuery_feign_equipStatus(data):
        """
        获取DCCO设备状态
        """
        path = f'/api/dccoChargerQuery/feign/equipStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerQuery_feign_getChargeDetailByNo(data):
        """
        根据编号获取DCCO充电详情
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/dccoChargerQuery/feign/getChargeDetailByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerQuery_feign_getChargeEquipInfoByCNo(data):
        """
        根据充电桩编号获取DCCO充电设备信息
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/dccoChargerQuery/feign/getChargeEquipInfoByCNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerQuery_feign_getChargeEquips(data):
        """
        获取DCCO充电设备列表
        """
        path = f'/api/dccoChargerQuery/feign/getChargeEquips'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerQuery_feign_getGunInfoByPos(data):
        """
        根据位置获取DCCO充电枪信息
        请求参数:
            campNo: integer [可选]
        """
        path = f'/api/dccoChargerQuery/feign/getGunInfoByPos'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerQuery_feign_getGunInfoByPosList(data):
        """
        根据仓位列表获取DCCO充电枪信息
        请求参数:
        """
        path = f'/api/dccoChargerQuery/feign/getGunInfoByPosList'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_dccoChargerQuery_feign_supportSuperCharger(data):
        """
        supportSuperCharger
        """
        path = f'/api/dccoChargerQuery/feign/supportSuperCharger'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_getChargeDeviceInfo(data):
        """
        获取充电设备信息
        """
        path = f'/api/equipment/getChargeDeviceInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_status(data):
        """
        获取充电设备状态列表
        """
        path = f'/api/equipment/status'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_adjustParam(data):
        """
        调整热管理参数
        请求参数:
            chargeElectricit: number [可选] - 充电电流
            chargerNo: integer [可选] - 加热机号
            dischargeElectricit: number [可选] - 放电电流
            flowNo: string [可选] - 订单号
            gunNo: integer [可选] - 加热机枪号
            msgId: string [可选] - 下控唯一标志
            subType: string [可选] - 下控子类型
        """
        path = f'/api/hotControl/feign/adjustParam'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_controlChargeUpgrade(data):
        """
        控制充电升级
        请求参数:
            bytesPerPacket: integer [可选] - 每包字节数
            chargerNo: integer [可选] - 充电机号
            controlBoardType: integer [可选] - 控制板类型
            fileSize: integer [可选] - 文件大小
            fileUrl: string [可选] - 文件URL
            subType: string [可选] - 下控子类型
            totalPacket: integer [可选] - 总包数
        """
        path = f'/api/hotControl/feign/controlChargeUpgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_queryDeviceParam(data):
        """
        查询热管理设备参数
        """
        path = f'/api/hotControl/feign/queryDeviceParam'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_queryVersion(data):
        """
        查询热管理版本
        """
        path = f'/api/hotControl/feign/queryVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_sendFaultThreshold(data):
        """
        发送故障阈值
        请求参数:
            chargeMagnification: number [可选] - 充电倍率
            chargerNo: integer [可选] - 加热机号
            dischargeMagnification: number [可选] - 放电倍率
            gunNo: integer [可选] - 加热机枪号
            hotNum: integer [可选] - 加热数
            msgId: string [可选] - 下控唯一标志
            position: integer [可选] - 仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/hotControl/feign/sendFaultThreshold'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_setDeviceParam(data):
        """
        设置热管理设备参数
        请求参数:
            chargeDeviceOverTemperatureThreshold: number [可选] - 充电设备过温阈值
            doorQuote: integer [可选] - 门禁报警
            hotTimeOutTs: integer [可选] - 加热超时时间 min
            inputOverVoltageThreshold: number [可选] - 输入过压阈值
            inputUnderVoltageThreshold: number [可选] - 输入欠压阈值
            insulationSelfTestEfficientTs: integer [可选] - 绝缘自检有效 min
            no: integer [可选] - 加热机号
            offlineChargeTs: integer [可选] - 离线充电时间
            outOverVoltageThreshold: number [可选] - 输出过压阈值
            overcurrentFilterTs: number [可选] - 过流滤波时间
            singleOutputOvercurrentThreshold: number [可选] - 单路输出过流阈值
            subType: string [可选] - 下控子类型
        """
        path = f'/api/hotControl/feign/setDeviceParam'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_start(data):
        """
        启动热管理
        请求参数:
            flowNo: string [可选] - 流水号
            model: integer [可选] - 充放电方向
            msgId: string [可选] - 下控唯一标志
            no: integer [可选] - 加热机号
            postions: array [可选] - 仓位
                        chargeMagnification: number [可选] - 充电倍率
                        dischargeMagnification: number [可选] - 放电倍率
                        pos: integer [可选] - 仓位号
                        type: integer [可选] - 加热模式
            subType: string [可选] - 下控子类型
        """
        path = f'/api/hotControl/feign/start'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_stationSafetyStatus(data):
        """
        获取站点安全状态
        请求参数:
            chargerNo: integer [可选] - 充电机号
            msgId: string [可选] - 下控唯一标志
            reason: integer [可选] - 故障原因 0:无 1:消防移仓故障 2:火灾报警 255:其它故障
            status: integer [可选] - 换电站安全状态 0:正常 1:故障
            subType: string [可选] - 下控子类型
        """
        path = f'/api/hotControl/feign/stationSafetyStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotControl_feign_stop(data):
        """
        停止热管理
        请求参数:
            flowNo: string [可选] - 交互流水号
            msgId: string [可选] - 下控唯一标志
            no: integer [可选] - 加热机号
            stopReason: integer [可选] - 停止原因
            subType: string [可选] - 下控子类型
        """
        path = f'/api/hotControl/feign/stop'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_equipStatus(data):
        """
        获取热管理设备状态
        """
        path = f'/api/hotQuery/feign/equipStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_getBatteryInfoByPosition(data):
        """
        根据位置获取电池信息
        请求参数:
            pos: integer [可选]
        """
        path = f'/api/hotQuery/feign/getBatteryInfoByPosition'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_getDetailByNo(data):
        """
        根据编号获取热管理详情
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hotQuery/feign/getDetailByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_getEquipInfoByNo(data):
        """
        根据编号获取热管理设备信息
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hotQuery/feign/getEquipInfoByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_getEquipmentProducer(data):
        """
        获取热管理设备生产商
        """
        path = f'/api/hotQuery/feign/getEquipmentProducer'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_getEquips(data):
        """
        获取热管理设备列表
        """
        path = f'/api/hotQuery/feign/getEquips'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_getFaultNumByNo(data):
        """
        根据编号获取故障数量
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hotQuery/feign/getFaultNumByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_getGunInfoByPos(data):
        """
        根据位置获取热管理充电枪信息
        请求参数:
            pos: integer [可选]
        """
        path = f'/api/hotQuery/feign/getGunInfoByPos'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_hotQuery_feign_getSettingByNo(data):
        """
        根据编号获取热管理设置
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hotQuery/feign/getSettingByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))

    @staticmethod
    def api_schedule_getDcciScheduleList(data):
        """
        获取DCCI调度列表
        请求参数:
            jobName: string [可选] - 任务名称
            scheduleBelongs: string [可选] - 任务所属
        """
        path = f'/api/schedule/getDcciScheduleList'
        return HttpRq.req(*HttpMethod.http_info(ApiDcci._get_path(path), 'POST', data))
