from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiBattery:
    @staticmethod
    def _get_path(path):
        service = '/battery'
        return service + path

    @staticmethod
    def api_battery_feign_v1_batteryInfoQuery_getAllBatteryInfoList(data):
        """
        获取所有电池数接口
        请求参数:
        """
        path = f'/api/battery/feign/v1/batteryInfoQuery/getAllBatteryInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_feign_v1_batteryInfoQuery_getAvailableBatteryAmountBySoc(data):
        """
        返回当前可用的电池数量
        请求参数:
            lowerOfSoc: string [可选]
        """
        path = f'/api/battery/feign/v1/batteryInfoQuery/getAvailableBatteryAmountBySoc'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_feign_v1_batteryInfoQuery_getCbmuAndSbmuBlueSts(data):
        """
        获取CBMU和SBMU蓝牙连接情况
        请求参数:
            campNoList: array [可选]
            commandSubType: string [必填] - 下控子类型
        """
        path = f'/api/battery/feign/v1/batteryInfoQuery/getCbmuAndSbmuBlueSts'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_feign_v1_logicMacService_deleteLogicMac(data):
        """
        删除逻辑mac
        请求参数:
            campNoList: array [可选] - 仓位号
        """
        path = f'/api/battery/feign/v1/logicMacService/deleteLogicMac'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_feign_v1_logicMacService_getLogicMac(data):
        """
        查询逻辑mac
        请求参数:
            campNoList: array [可选] - 仓位号
        """
        path = f'/api/battery/feign/v1/logicMacService/getLogicMac'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_feign_v1_logicMacService_getLogicMacList(data):
        """
        获取所有逻辑mac
        """
        path = f'/api/battery/feign/v1/logicMacService/getLogicMacList'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_feign_v1_logicMacService_updateLogicMac(data):
        """
        更新逻辑mac
        请求参数:
            campNo: integer [可选] - 仓位号
            logicMac: string [可选] - 逻辑mac
        """
        path = f'/api/battery/feign/v1/logicMacService/updateLogicMac'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_batteryOut(data):
        """
        请求电池出仓
        请求参数:
            commandSubType: string [必填] - 下控子类型
            positionList: array [必填] - 仓位列表
        """
        path = f'/api/batteryControl/batteryOut'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_chargeControl(data):
        """
        充电控制
        请求参数:
            campNo: integer [可选] - 仓位号
            cmd: integer [可选] - 手动停止充电指令和断蓝牙指令：0：默认值 1：停止充电 2：启动充电 3：断蓝牙+停止充电
        """
        path = f'/api/batteryControl/chargeControl'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_clearBbsFault(data):
        """
        清除站控自检故障
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeEnum: string [可选] - 故障上报设备类型
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/batteryControl/clearBbsFault'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_clearCache(data):
        """
        清除缓存
        请求参数:
            position: integer [必填] - 仓位
        """
        path = f'/api/batteryControl/clearCache'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_clearFault(data):
        """
        请求清除故障
        请求参数:
            commandSubType: string [必填] - 下控子类型
            positionList: array [必填] - 仓位列表
            requestEnum: string [必填] - 清除故障类型
        """
        path = f'/api/batteryControl/clearFault'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_clearInStationSubtotal(data):
        """
        请求清除站内小计
        请求参数:
            commandSubType: string [必填] - 下控子类型
            positionList: array [必填] - 仓位列表
        """
        path = f'/api/batteryControl/clearInStationSubtotal'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_clearOutStationSubtotal(data):
        """
        请求清除站外小计
        请求参数:
            commandSubType: string [必填] - 下控子类型
            positionList: array [必填] - 仓位列表
        """
        path = f'/api/batteryControl/clearOutStationSubtotal'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_closeHVContactor(data):
        """
        电池包下高压控制
        请求参数:
            commandSubType: string [必填] - 下控子类型
            positionList: array [必填] - 仓位列表
        """
        path = f'/api/batteryControl/closeHVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_creatClient(data):
        """
        建立充电连接
        请求参数:
            campNo: integer [可选] - 仓位号
            commandSubType: string [必填] - 下控子类型
            macStr: string [可选] - 请求建立连接pack的蓝牙MAC地址
        """
        path = f'/api/batteryControl/creatClient'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_disconnectBMSConnect(data):
        """
        下控断仓内电池蓝牙
        请求参数:
            campNoList: array [可选]
            commandSubType: string [必填] - 下控子类型
        """
        path = f'/api/batteryControl/disconnectBMSConnect'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_faultClearAll(data):
        """
        清除电池故障
        请求参数:
            campNos: array [可选] - 清除电池所有故障(一二代)
        """
        path = f'/api/batteryControl/faultClearAll'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_hot(data):
        """
        加热控制
        请求参数:
            commandSubType: string [必填] - 下控子类型
            hot: string [必填] - 加热请求类型
            position: integer [必填] - 仓位
            pre: string [必填] - 预加热请求
        """
        path = f'/api/batteryControl/hot'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_hotNotCommond(data):
        """
        加热控制(无命令)
        请求参数:
            commandSubType: string [必填] - 下控子类型
            hot: string [必填] - 加热请求类型
            position: integer [必填] - 仓位
            pre: string [必填] - 预加热请求
        """
        path = f'/api/batteryControl/hotNotCommond'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_sendOutBound(data):
        """
        发送出站命令
        请求参数:
            posList: array [必填] - 仓位
        """
        path = f'/api/batteryControl/sendOutBound'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_setCC2Flg(data):
        """
        设置CC2标志
        请求参数:
            commandSubType: string [必填] - 下控子类型
            positionList: array [必填] - 仓位列表
        """
        path = f'/api/batteryControl/setCC2Flg'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_swapFlowReset(data):
        """
        换电初始化
        请求参数:
            campNos: array [可选] - 仓位号
        """
        path = f'/api/batteryControl/swapFlowReset'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryControl_triggerQuery(data):
        """
        触发查询
        请求参数:
            b2sQueryEnum: string [可选]
            commandSubType: string [必填] - 下控子类型
            position: integer [可选]
        """
        path = f'/api/batteryControl/triggerQuery'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_batchQueryBatteryChargeState(data):
        """
        批量查询电池充电状态
        请求参数:
        """
        path = f'/api/batteryInfoQuery/batchQueryBatteryChargeState'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_getAllBatteryInfoList(data):
        """
        获取所有电池信息列表
        """
        path = f'/api/batteryInfoQuery/getAllBatteryInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_getAllSbmuFaultCodeInfoList(data):
        """
        获取所有SBMU故障码信息
        """
        path = f'/api/batteryInfoQuery/getAllSbmuFaultCodeInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_getAvailableBatteryAmountBySoc(data):
        """
        根据SOC获取可用电池数量
        请求参数:
            lowerOfSoc: string [可选]
        """
        path = f'/api/batteryInfoQuery/getAvailableBatteryAmountBySoc'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_getBatteryStatusDTOInfoList(data):
        """
        获取电池状态信息列表
        """
        path = f'/api/batteryInfoQuery/getBatteryStatusDTOInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_getCbmuAndSbmuBlueSts(data):
        """
        获取CBMU和SBMU蓝牙状态
        请求参数:
            campNoList: array [可选]
            commandSubType: string [必填] - 下控子类型
        """
        path = f'/api/batteryInfoQuery/getCbmuAndSbmuBlueSts'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_getCurrentFaultInfo(data):
        """
        获取当前故障信息
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeEnum: string [可选] - 故障上报设备类型
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/batteryInfoQuery/getCurrentFaultInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_getPackBasicInfo(data):
        """
        获取电池包基本信息
        请求参数:
        """
        path = f'/api/batteryInfoQuery/getPackBasicInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_packInfo(data):
        """
        电池包信息查询
        请求参数:
            snList: array [可选]
        """
        path = f'/api/batteryInfoQuery/packInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_packPortInfo(data):
        """
        电池包端口信息
        """
        path = f'/api/batteryInfoQuery/packPortInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_queryBatteryBasicInfoList(data):
        """
        查询电池基本信息列表
        请求参数:
            pos: array [可选]
            retFields: array [可选]
        """
        path = f'/api/batteryInfoQuery/queryBatteryBasicInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_queryBatteryCheckInfo(data):
        """
        查询电池检测信息
        请求参数:
            pos: array [可选]
        """
        path = f'/api/batteryInfoQuery/queryBatteryCheckInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryInfoQuery_queryBatteryInfoList(data):
        """
        查询电池信息列表
        请求参数:
            positionList: array [可选]
        """
        path = f'/api/batteryInfoQuery/queryBatteryInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryServerStatistics_countSwitch(data):
        """
        计数开关控制
        请求参数:
        """
        path = f'/api/batteryServerStatistics/countSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryServerStatistics_getQpsAll(data):
        """
        获取所有QPS统计
        """
        path = f'/api/batteryServerStatistics/getQpsAll'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_bmsChargerControl_controlChargeUpgrade(data):
        """
        充电机升级请求
        请求参数:
            controlBoardType: integer [可选] - 控制板类型
            fileSize: integer [可选] - 文件大小
            fileSize2: integer [可选] - 文件2大小
            fileUrl: string [可选] - 文件URL
            fileUrl2: string [可选] - 文件2URL
            position: integer [可选] - 仓位号
            subType: string [可选] - 下控子类型
        """
        path = f'/api/bmsChargerControl/controlChargeUpgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_bmsChargerControl_sendBmsSeedSecretKey(data):
        """
        下发充电机解析后秘钥
        请求参数:
            position: integer [可选] - 仓位号
            result: string [可选] - 结果
            secretKey: string [可选] - 秘钥
        """
        path = f'/api/bmsChargerControl/sendBmsSeedSecretKey'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_dataExpireTime_v3DataTimeoutMap(data):
        """
        获取V3数据超时配置
        """
        path = f'/api/dataExpireTime/v3DataTimeoutMap'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_status(data):
        """
        获取电池设备状态
        """
        path = f'/api/equipment/status'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_packInfo_getHighVoltStateMap(data):
        """
        获取电池高压状态Map
        请求参数:
        """
        path = f'/api/packInfo/getHighVoltStateMap'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_packInfo_getPackDynamicData(data):
        """
        获取动态电芯数据
        请求参数:
        """
        path = f'/api/packInfo/getPackDynamicData'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_packInfo_getPackVersionInfo(data):
        """
        获取电池版本信息
        请求参数:
        """
        path = f'/api/packInfo/getPackVersionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_packInfo_getPickPackInfo(data):
        """
        获取选包电池信息
        """
        path = f'/api/packInfo/getPickPackInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))

    @staticmethod
    def api_packInfo_queryRelayState(data):
        """
        查询继电器状态信息
        请求参数:
            pos: array [可选]
        """
        path = f'/api/packInfo/queryRelayState'
        return HttpRq.req(*HttpMethod.http_info(ApiBattery._get_path(path), 'POST', data))
