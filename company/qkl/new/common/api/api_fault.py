from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiFault:
    @staticmethod
    def _get_path(path):
        service = '/fault'
        return service + path

    @staticmethod
    def api_disableRecord_add(data):
        """
        add
        请求参数:
            disableReason: string [必填] - 禁用原因
            disableSource: string [必填] - 操作来源
            disableTarget: string [必填] - 操作目标
            disableType: string [必填] - 操作类型
            targetNos: array [必填] - 操作编号：仓位号或电池SN
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作用户名称
        """
        path = f'/api/disableRecord/add'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_disableRecord_batchAdd(data):
        """
        batchAdd
        请求参数:
            busCode: string [可选] - 关联业务唯一编号
            disableReason: string [必填] - 禁用原因
            disableSource: string [必填] - 操作来源
            disableTarget: string [必填] - 操作目标
            disableType: string [必填] - 操作类型
            targetNo: string [必填] - 操作编号：仓位号或电池SN
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作用户名称
        """
        path = f'/api/disableRecord/batchAdd'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_disableRecord_del(data):
        """
        del
        请求参数:
            busCode: string [可选] - 关联业务唯一编号
            disableReason: string [必填] - 禁用原因
            disableSource: string [必填] - 操作来源
            disableTarget: string [必填] - 操作目标
            disableType: string [必填] - 操作类型
            targetNos: array [必填] - 操作编号：仓位号或电池SN
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作用户名称
        """
        path = f'/api/disableRecord/del'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_disableRecord_list(data):
        """
        list
        请求参数:
            disableSource: string [必填] - 操作来源
            disableTarget: string [必填] - 操作目标
            disableTypes: array [必填] - 操作类型
            targetNos: array [必填] - 操作编号：仓位号或电池SN
        """
        path = f'/api/disableRecord/list'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_disableRecordLog_cleanup(data):
        """
        cleanup
        请求参数:
            cleanupDayOffset: integer [可选]
        """
        path = f'/api/disableRecordLog/cleanup'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_batteryCampOperation_addDisableRecord(data):
        """
        新增禁用记录
        请求参数:
            disableReason: string [必填] - 禁用原因
            disableSource: string [必填] - 操作来源
            disableTarget: string [必填] - 操作目标
            disableType: string [必填] - 操作类型
            targetNo: string [必填] - 操作编号：仓位号或电池SN，多个用英文,拼接
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作用户名称
        """
        path = f'/api/fault/feign/batteryCampOperation/addDisableRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_batteryCampOperation_addDisableRecordWithBusCode(data):
        """
        新增禁用记录-带业务唯一编号
        请求参数:
            busCode: string [必填] - 关联业务唯一编号
            disableReason: string [必填] - 禁用原因
            disableSource: string [必填] - 操作来源
            disableTarget: string [必填] - 操作目标
            disableType: string [必填] - 操作类型
            targetNo: string [必填] - 操作编号：仓位号或电池SN，多个用英文,拼接
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作人
        """
        path = f'/api/fault/feign/batteryCampOperation/addDisableRecordWithBusCode'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_batteryCampOperation_batchAddDisableRecord(data):
        """
        批量新增禁用记录
        请求参数:
            disableReason: string [必填] - 禁用原因
            disableSource: string [必填] - 操作来源
            disableTarget: string [必填] - 操作目标
            disableType: string [必填] - 操作类型
            targetNo: string [必填] - 操作编号：仓位号或电池SN，多个用英文,拼接
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作用户名称
        """
        path = f'/api/fault/feign/batteryCampOperation/batchAddDisableRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_batteryCampOperation_batteryOpts():
        """
        仓位电池筛选列表
        """
        path = f'/api/fault/feign/batteryCampOperation/batteryOpts'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'GET', None))

    @staticmethod
    def api_fault_feign_batteryCampOperation_count(data):
        """
        禁用历史记录数量
        请求参数:
            busCode: string [可选] - 操作编号: 关联业务唯一编号(自动充电使用)
            current: integer [可选]
            disableSources: array [可选] - 禁用来源
            disableTarget: string [必填] - 操作目标
            endTime: string [可选] - 过滤结束时间
            requestId: string [可选]
            size: integer [可选]
            startTime: string [可选] - 过滤开始时间
            targetNos: array [必填] - 操作编号：仓位号或电池SN
            timestamp: integer [可选]
        """
        path = f'/api/fault/feign/batteryCampOperation/count'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_batteryCampOperation_deleteDisableRecord(data):
        """
        删除禁用记录
        请求参数:
            id: integer [必填] - 业务主键
            remark: string [必填] - 备注
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作用户名称
        """
        path = f'/api/fault/feign/batteryCampOperation/deleteDisableRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'DELETE', data))

    @staticmethod
    def api_fault_feign_batteryCampOperation_deleteDisableRecordWithBusCode(data):
        """
        删除禁用记录-带业务唯一编号
        请求参数:
            busCode: string [必填] - 关联业务唯一编号
            disableSource: string [必填] - 禁用业务
            remark: string [必填] - 备注
            userName: string [可选] - 操作人
        """
        path = f'/api/fault/feign/batteryCampOperation/deleteDisableRecordWithBusCode'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'DELETE', data))

    @staticmethod
    def api_fault_feign_batteryCampOperation_disableBatteryOpts():
        """
        禁用电池-仓位列表
        """
        path = f'/api/fault/feign/batteryCampOperation/disableBatteryOpts'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'GET', None))

    @staticmethod
    def api_fault_feign_batteryCampOperation_getDetail(data):
        """
        详情
        请求参数:
            busCode: string [可选] - 操作编号: 关联业务唯一编号(自动充电使用)
            current: integer [可选]
            disableSources: array [可选] - 禁用来源
            disableTarget: string [必填] - 操作目标
            endTime: string [可选] - 过滤结束时间
            requestId: string [可选]
            size: integer [可选]
            startTime: string [可选] - 过滤开始时间
            targetNos: array [必填] - 操作编号：仓位号或电池SN
            timestamp: integer [可选]
        """
        path = f'/api/fault/feign/batteryCampOperation/getDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_excelOperation_faultCode_export(data):
        """
        故障编码导出
        """
        path = f'/api/fault/feign/excelOperation/faultCode/export'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_excelOperation_faultCode_import(data):
        """
        故障编码导入
        请求参数:
            createTime: string [可选]
            fileBlob: string [可选]
            faultCodeList: array [可选] - 故障编码列表
                        accidentFanControlStrategy: string [可选]
                        airControlStrategy: string [可选]
                        alarmOrPromptStrategy: string [可选]
                        batteryChargeStrategy: string [可选]
                        batterySwapStrategy: string [可选]
                        chargerSafetyStatusStrategy: string [可选]
                        deviceCode: string [可选]
                        deviceCodeNew: string [可选]
                        deviceFaultCodeV1: string [可选]
                        deviceFaultCodeV2: string [可选]
                        deviceFaultCodeV3: string [可选]
                        deviceNo: string [可选]
                        fanControlStrategy: string [可选]
                        faultCause: string [可选]
                        faultCode: string [可选]
                        faultDesc: string [可选]
                        faultDiagnosticsConditionV1: string [可选]
                        faultDiagnosticsConditionV2: string [可选]
                        faultDiagnosticsConditionV3: string [可选]
                        faultDiagnosticsConfirmTimeV1: string [可选]
                        faultDiagnosticsConfirmTimeV2: string [可选]
                        faultDiagnosticsConfirmTimeV3: string [可选]
                        faultExistV1: string [可选]
                        faultExistV2: string [可选]
                        faultExistV3: string [可选]
                        faultInfluence: string [可选]
                        faultLevel: string [可选]
                        faultName: string [可选]
                        faultNameEn: string [可选]
                        faultNameTw: string [可选]
                        faultRecoverConditionV1: string [可选]
                        faultRecoverConditionV2: string [可选]
                        faultRecoverConditionV3: string [可选]
                        faultRecoverConfirmTimeV1: string [可选]
                        faultRecoverConfirmTimeV2: string [可选]
                        faultRecoverConfirmTimeV3: string [可选]
                        faultRepair: string [可选]
                        faultSource: string [可选]
                        fireHandleStrategy: string [可选]
                        gateStrategy: string [可选]
                        reportCloudStrategy: string [可选]
                        rollingDoorStrategy: string [可选]
                        singleCampChargeStrategy: string [可选]
                        singleCampDischargeStrategy: string [可选]
                        singleCampSwapStrategy: string [可选]
                        specialHandleStrategy: string [可选]
                        stationChangeStatusStrategy: string [可选]
                        stationChargeStrategy: string [可选]
                        swapChannelVoiceStrategy: string [可选]
                        swapFunctionStrategy: string [可选]
        """
        path = f'/api/fault/feign/excelOperation/faultCode/import'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_handle_cleanup(data):
        """
        定时删除历史故障记录
        请求参数:
            cleanupDayOffset: integer [可选]
        """
        path = f'/api/fault/feign/handle/cleanup'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_handle_clear(data):
        """
        手动清除故障
        请求参数:
            bmsClearType: integer [可选] - BMS故障清除类型 1-清除不存储NVM的故障 2-清除所有故障 (包含存储NVM和不存储NVM) 
            campNo: integer [可选] - 仓位号：BMS故障清除需传
            clearFaultTarget: string [必填] - 执行对象
            faultIds: array [可选] - 故障主键列表：本地站控诊断故障清除需传
            userName: string [可选] - 操作人
        """
        path = f'/api/fault/feign/handle/clear'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_handle_recover(data):
        """
        故障恢复
        请求参数:
            campNo: integer [可选] - 仓位号
            deviceCode: string [必填] - 设备编码（设备简称）
            deviceNo: integer [必填] - 设备编号
            faultCode: string [必填] - 故障码
            oriFaultCode: string [可选]
            serialNum: string [可选] - 电池包SN
            userName: string [可选] - 操作人
        """
        path = f'/api/fault/feign/handle/recover'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_handle_report(data):
        """
        故障上报
        请求参数:
            campNo: integer [可选] - 仓位号
            desc: string [可选] - 描述
            deviceCode: string [必填] - 设备编码（设备简称）
            deviceNo: integer [必填] - 设备编号
            faultCode: string [必填] - 故障码
            oriFaultCode: string [可选]
            serialNum: string [可选] - 电池包SN
        """
        path = f'/api/fault/feign/handle/report'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_info_code_page(data):
        """
        故障编码-分页
        请求参数:
            current: integer [可选]
            deviceCode: string [可选] - 设备简称（数据字典：deviceCode）
            faultCode: string [可选] - 故障码
            faultSource: string [可选] - 故障来源（数据字典：faultSource）
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/fault/feign/info/code/page'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_info_current_count(data):
        """
        实时故障-总数
        """
        path = f'/api/fault/feign/info/current/count'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_info_current_haveStationFaultBlackList(data):
        """
        是否存在整站故障黑名单
        """
        path = f'/api/fault/feign/info/current/haveStationFaultBlackList'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_info_current_list(data):
        """
        实时故障-列表
        请求参数:
            batteryCampNo: integer [可选] - 电池仓位号
            campFaultCode: string [可选] - 仓位相关故障编码
            campNo: integer [可选] - 仓位号
            combinedFaultCode: string [可选] - 故障编码
            createTimeEnd: string [可选] - 故障发生时间-结束
            createTimeStart: string [可选] - 故障发生时间-开始
            deviceCodes: array [可选]
            faultName: string [可选] - 故障名称
            faultSource: string [可选] - 故障来源（数据字典：faultSource）
            faultSources: array [可选] - 故障来源（数据字典：faultSource）
            idList: array [可选] - id列表，用于批量导出
            localCombinedFaultCode: string [可选] - 本地故障编码
            resultLimit: integer [可选] - 返回结果条数限制
            serialNum: string [可选] - sn
        """
        path = f'/api/fault/feign/info/current/list'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_info_history_gatherPageQuery(data):
        """
        历史故障-汇总分页
        请求参数:
            campNo: integer [可选] - 仓位号
            combinedFaultCode: string [可选] - 故障编码
            createTimeEnd: string [可选] - 故障发生时间-结束
            createTimeStart: string [可选] - 故障发生时间-开始
            current: integer [可选]
            deviceCodes: array [可选]
            faultCode: string [可选]
            faultName: string [可选] - 故障名称
            faultSource: string [可选] - 故障来源（数据字典：faultSource）
            idList: array [可选] - id列表，用于批量导出
            localCombinedFaultCode: string [可选] - 本地故障编码
            oriFaultCode: string [可选]
            recoverTimeEnd: string [可选] - 故障恢复时间-结束
            recoverTimeStart: string [可选] - 故障恢复时间-开始
            requestId: string [可选]
            serialNum: string [可选] - sn
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/fault/feign/info/history/gatherPageQuery'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_info_history_list(data):
        """
        历史故障-列表
        请求参数:
            campNo: integer [可选] - 仓位号
            combinedFaultCode: string [可选] - 故障编码
            createTimeEnd: string [可选] - 故障发生时间-结束
            createTimeStart: string [可选] - 故障发生时间-开始
            current: integer [可选]
            deviceCodes: array [可选]
            faultCode: string [可选]
            faultName: string [可选] - 故障名称
            faultSource: string [可选] - 故障来源（数据字典：faultSource）
            idList: array [可选] - id列表，用于批量导出
            localCombinedFaultCode: string [可选] - 本地故障编码
            oriFaultCode: string [可选]
            recoverTimeEnd: string [可选] - 故障恢复时间-结束
            recoverTimeStart: string [可选] - 故障恢复时间-开始
            requestId: string [可选]
            serialNum: string [可选] - sn
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/fault/feign/info/history/list'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_feign_info_history_page(data):
        """
        历史故障-分页
        请求参数:
            campNo: integer [可选] - 仓位号
            combinedFaultCode: string [可选] - 故障编码
            createTimeEnd: string [可选] - 故障发生时间-结束
            createTimeStart: string [可选] - 故障发生时间-开始
            current: integer [可选]
            deviceCodes: array [可选]
            faultCode: string [可选]
            faultName: string [可选] - 故障名称
            faultSource: string [可选] - 故障来源（数据字典：faultSource）
            idList: array [可选] - id列表，用于批量导出
            localCombinedFaultCode: string [可选] - 本地故障编码
            oriFaultCode: string [可选]
            recoverTimeEnd: string [可选] - 故障恢复时间-结束
            recoverTimeStart: string [可选] - 故障恢复时间-开始
            requestId: string [可选]
            serialNum: string [可选] - sn
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/fault/feign/info/history/page'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_faultMatrix_handle(data):
        """
        handle
        请求参数:
            campNos: array [可选] - 仓位号集合
            deviceCode: string [可选] - 设备简称
            deviceFaultCode: string [可选] - 设备原始故障码
            deviceNo: integer [可选] - 设备编号
            faultCode: string [可选] - 故障码
            faultId: integer [可选]
            packMac: string [可选] - 电池包Mac
            packSn: string [可选] - 电池包SN
        """
        path = f'/api/faultMatrix/handle'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))

    @staticmethod
    def api_snapshotFaultRecord_triggerSave(data):
        """
        triggerSave
        请求参数:
            faultTime: string [可选] - 故障时间
            faultTimeEnd: string [可选] - 故障结束时间
            faultTimeStart: string [可选] - 故障前置时间
            snapshotPfk: string [可选] - 快照唯一键
            snapshotType: string [可选] - 故障快照类型
        """
        path = f'/api/snapshotFaultRecord/triggerSave'
        return HttpRq.req(*HttpMethod.http_info(ApiFault._get_path(path), 'POST', data))
