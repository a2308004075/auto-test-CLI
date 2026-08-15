from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiManager:
    @staticmethod
    def _get_path(path):
        service = '/manager'
        return service + path

    @staticmethod
    def api_BluetoothTestBatchData_batchExportBtAnalysisData(data):
        """
        蓝牙压测导出
        请求参数:
            testBatchNo: string [可选]
        """
        path = f'/api/BluetoothTestBatchData/batchExportBtAnalysisData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_BluetoothTestBatchData_btPressureTestProcessInfo(data):
        """
        获取蓝牙压测流程信息
        """
        path = f'/api/BluetoothTestBatchData/btPressureTestProcessInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_BluetoothTestBatchData_page(data):
        """
        page
        请求参数:
            carModel: string [可选]
            carPlace: integer [可选]
            current: integer [可选]
            endTime: string [可选]
            mac: string [可选]
            requestId: string [可选]
            size: integer [可选]
            startTime: string [可选]
            testBatch: string [可选]
            timestamp: integer [可选]
        """
        path = f'/api/BluetoothTestBatchData/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_BluetoothTestBatchData_startPressureBluetooth(data):
        """
        蓝牙压测流程开启
        请求参数:
            carModel: string [可选] - 车型代号
            carNo: string [可选] - 车牌号
            carPlace: integer [可选] - 车辆位置 1：车在站外（指车辆未进站） 2：车在站内（指车辆前轮已驶入 V 槽）
            connectMode: integer [可选] - 连接方式 1：mac 2：irk 3：oob
            irk: string [可选] - irk地址
            linkTime: integer [可选] - 保存连接时长（s）
            mac: string [可选] - 蓝牙地址
            oob: string [可选] - oob地址
            remark: string [可选] - 备注
            totalCount: integer [可选] - 压力测试换电次数
        """
        path = f'/api/BluetoothTestBatchData/startPressureBluetooth'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_BluetoothTestBatchData_stopPressureBluetooth(data):
        """
        蓝牙压测流程结束
        """
        path = f'/api/BluetoothTestBatchData/stopPressureBluetooth'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_SwapFlowTestBatchData_page(data):
        """
        page
        请求参数:
            carModel: string [可选]
            carPlace: integer [可选]
            current: integer [可选]
            endTime: string [可选]
            mac: string [可选]
            requestId: string [可选]
            size: integer [可选]
            startTime: string [可选]
            testBatch: string [可选]
            timestamp: integer [可选]
        """
        path = f'/api/SwapFlowTestBatchData/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_model_create(data):
        """
        创建模型
        请求参数:
            description: string [可选] - 模型描述
            key: string [可选] - 模型标志
            name: string [可选] - 模型名称
        """
        path = f'/api/activiti/model/create'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_model_del(data):
        """
        删除模型
        请求参数:
            id: string [可选]
        """
        path = f'/api/activiti/model/del'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_model_deployByDeployName(data):
        """
        通过流程名称定义发布模型为流程定义
        请求参数:
        """
        path = f'/api/activiti/model/deployByDeployName'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_model_deployment(data):
        """
        发布模型为流程定义
        请求参数:
            id: string [可选]
        """
        path = f'/api/activiti/model/deployment'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_model_exchangeProcessToModel_pdid(pdid):
        """
        根据流程定义ID将流程定义转为模型
        请求参数:
        """
        path = f'/api/activiti/model/exchangeProcessToModel/{pdid}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_activiti_model_export(data):
        """
        模型导出
        请求参数:
            modelId: string [可选]
        """
        path = f'/api/activiti/model/export'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_model_import(data):
        """
        模型导入
        请求参数:
        """
        path = f'/api/activiti/model/import'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_model_page(data):
        """
        获取所有模型
        请求参数:
            current: integer [可选]
            key: string [可选] - 模型标志
            name: string [可选] - 模型名称
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/activiti/model/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_model_unDeployment(data):
        """
        根据部署ID删除流程
        请求参数:
            deploymentId: string [可选]
            forceFlag: string [可选]
        """
        path = f'/api/activiti/model/unDeployment'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_processInstance_batchExportLockData(data):
        """
        快换锁数据导出（同一个包测试）
        请求参数:
            endTime: string [可选]
            startTime: string [可选]
            testBatch: string [可选]
        """
        path = f'/api/activiti/processInstance/batchExportLockData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_processInstance_batchExportPackTemperatureData(data):
        """
        批量导出电池温度数据
        请求参数:
            endTime: string [可选]
            startTime: string [可选]
            testBatch: string [可选]
        """
        path = f'/api/activiti/processInstance/batchExportPackTemperatureData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_processInstance_batchExportSwapFlowData(data):
        """
        快换锁数据导出（全自动换电）
        请求参数:
            endTime: string [可选]
            startTime: string [可选]
            testBatch: string [可选]
        """
        path = f'/api/activiti/processInstance/batchExportSwapFlowData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_processInstance_batchExportSwapFlowTime(data):
        """
        批量导出换电时长
        请求参数:
            endTime: string [可选]
            startTime: string [可选]
            testBatch: string [可选]
        """
        path = f'/api/activiti/processInstance/batchExportSwapFlowTime'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_processInstance_create(data):
        """
        创建流程实例
        请求参数:
            businessKey: string [可选]
            processKey: string [可选]
        """
        path = f'/api/activiti/processInstance/create'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_processInstance_delBatch(data):
        """
        删除批量流程
        请求参数:
        """
        path = f'/api/activiti/processInstance/delBatch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_processInstance_exportImg():
        """
        流程图片导出
        """
        path = f'/api/activiti/processInstance/exportImg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_activiti_processInstance_page(data):
        """
        获取流程实例列表
        请求参数:
            businessKey: string [可选]
            current: integer [可选]
            deploymentId: string [可选]
            processDefinitionKey: string [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/activiti/processInstance/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_task_finishTask(data):
        """
        提交任务
        请求参数:
            activitiId: string [可选]
            processId: string [可选]
            taskId: string [可选]
        """
        path = f'/api/activiti/task/finishTask'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_task_page(data):
        """
        获取任务列表
        请求参数:
            assignee: string [可选]
            current: integer [可选]
            processInstanceId: string [可选]
            processKey: string [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/activiti/task/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_activiti_task_signalTest(data):
        """
        错误任务测试
        请求参数:
            activityId: string [可选]
            catchId: string [可选]
            catchName: string [可选]
            processId: string [可选]
        """
        path = f'/api/activiti/task/signalTest'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_ota_list():
        """
        sbmu升级列表
        """
        path = f'/api/battery/ota/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_battery_ota_upgrade(data):
        """
        sbmu升级
        请求参数:
            driveFileId: integer [可选] - 驱动文件id
            fileId: integer [可选] - app文件id
            msgId: integer [可选]
            positionList: array [可选] - 仓位号
            remark: string [可选] - 备注
            source: integer [可选]
            upgradeType: integer [可选] - 升级类型
        """
        path = f'/api/battery/ota/upgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_packInCamp(data):
        """
        packInCamp
        请求参数:
            packMac: string [可选]
            packSn: string [可选]
        """
        path = f'/api/battery/packInCamp'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_saveRemark(data):
        """
        saveRemark
        请求参数:
            packSn: string [必填] - SN码
            remark: string [必填] - 备注信息
        """
        path = f'/api/battery/saveRemark'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_wanted_batchExport(data):
        """
        批量导出
        请求参数:
            batterySn: string [可选]
            chargeDisableStatus: integer [可选]
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            deleteReason: string [可选]
            executeUser: string [可选]
            id: integer [可选]
            ids: array [可选]
            packMac: string [可选]
            remark: string [可选]
            requestId: string [可选]
            size: integer [可选]
            swapDisableStatus: integer [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            wantedEndTime: string [可选]
            wantedReason: string [可选]
            wantedSource: integer [可选]
            wantedStartTime: string [可选]
            wantedTime: string [可选]
        """
        path = f'/api/battery/wanted/batchExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_wanted_list(data):
        """
        不带分页查询
        请求参数:
            batterySn: string [可选]
            chargeDisableStatus: integer [可选]
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            deleteReason: string [可选]
            executeUser: string [可选]
            id: integer [可选]
            ids: array [可选]
            packMac: string [可选]
            remark: string [可选]
            requestId: string [可选]
            size: integer [可选]
            swapDisableStatus: integer [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            wantedEndTime: string [可选]
            wantedReason: string [可选]
            wantedSource: integer [可选]
            wantedStartTime: string [可选]
            wantedTime: string [可选]
        """
        path = f'/api/battery/wanted/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_battery_wanted_page(data):
        """
        分页查询
        请求参数:
            batterySn: string [可选]
            chargeDisableStatus: integer [可选]
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            deleteReason: string [可选]
            executeUser: string [可选]
            id: integer [可选]
            ids: array [可选]
            packMac: string [可选]
            remark: string [可选]
            requestId: string [可选]
            size: integer [可选]
            swapDisableStatus: integer [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            wantedEndTime: string [可选]
            wantedReason: string [可选]
            wantedSource: integer [可选]
            wantedStartTime: string [可选]
            wantedTime: string [可选]
        """
        path = f'/api/battery/wanted/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_batteryCharge(data):
        """
        电池充电
        请求参数:
            campNoList: array [可选] - 仓位号列表
            chargeLimit: number [可选] - 充电限制值 chargeType=1时不传, chargeType=2时单位kW, chargeType=3时单位%, chargeType=4时单位A
            chargeModelEnum: string [可选]
            chargePowerDiscount: number [可选] - 充电功率折扣系数
            chargeType: integer [可选] - 充电类型 1-不做限制 2-充电功率上限 3-充电电流倍率 4-最大电流限制
            commandSubTypeEnum: string [可选]
            directionEnum: string [可选]
            msgId: string [可选]
            socLimit: integer [可选] - 停止充电soc限制
        """
        path = f'/api/batteryCampManage/batteryCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_batteryChargeAdjust(data):
        """
        电池充电调整
        请求参数:
            campNoList: array [可选] - 仓位号列表
            chargeLimit: number [可选] - 充电限制值 chargeType=1时不传, chargeType=2时单位kW, chargeType=3时单位%, chargeType=4时单位A
            chargeType: integer [可选] - 充电类型 1-不做限制 2-充电功率上限 3-充电电流倍率 4-最大电流限制
            limitPowerSource: integer [可选]
            operationFeedback: integer [可选] - 是否需要操作反馈
        """
        path = f'/api/batteryCampManage/batteryChargeAdjust'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_batteryChargeAdjustCheck(data):
        """
        电池充电调整校验
        请求参数:
            campNo: integer [可选] - 仓位号
        """
        path = f'/api/batteryCampManage/batteryChargeAdjustCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_batteryChargeCheck(data):
        """
        电池充电校验
        请求参数:
            campNoList: array [可选] - 仓位号列表
            chargeDirection: integer [可选] - 充放电类型 0:充电 1：放电
        """
        path = f'/api/batteryCampManage/batteryChargeCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_batteryDisCharge(data):
        """
        电池放电
        请求参数:
            campNoList: array [可选] - 仓位号列表
            chargeLimit: number [可选] - 充电限制值 chargeType=1时不传, chargeType=2时单位kW, chargeType=3时单位%, chargeType=4时单位A
            chargeModelEnum: string [可选]
            chargePowerDiscount: number [可选] - 充电功率折扣系数
            chargeType: integer [可选] - 充电类型 1-不做限制 2-充电功率上限 3-充电电流倍率 4-最大电流限制
            commandSubTypeEnum: string [可选]
            directionEnum: string [可选]
            msgId: string [可选]
            socLimit: integer [可选] - 停止充电soc限制
        """
        path = f'/api/batteryCampManage/batteryDisCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_batteryStopCharge(data):
        """
        电池停止充电
        请求参数:
            campNoList: array [必填] - 仓位号列表
        """
        path = f'/api/batteryCampManage/batteryStopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_batteryStopChargeCheck(data):
        """
        电池停止充电校验
        请求参数:
            campNoList: array [必填] - 仓位号列表
        """
        path = f'/api/batteryCampManage/batteryStopChargeCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_chargerKeyonBatch(data):
        """
        批量电池唤醒源连接/断开
        请求参数:
            campNoList: array [可选] - 仓位号列表
            switchFlag: integer [可选] - 操作类型
        """
        path = f'/api/batteryCampManage/chargerKeyonBatch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_chargerKeyonValid(data):
        """
        电池唤醒源校验
        请求参数:
            campNoList: array [可选] - 仓位号列表
            switchFlag: integer [可选] - 操作类型
        """
        path = f'/api/batteryCampManage/chargerKeyonValid'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_chargerPowerSwitch(data):
        """
        充电机唤醒源开关
        请求参数:
            campNo: integer [可选]
            switchFlag: integer [可选]
        """
        path = f'/api/batteryCampManage/chargerPowerSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_getBatteryDetail_campNo(campNo):
        """
        电池详细信息
        请求参数:
        """
        path = f'/api/batteryCampManage/getBatteryDetail/{campNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_batteryCampManage_getCampDetail_campNo(campNo):
        """
        仓位详细信息
        请求参数:
        """
        path = f'/api/batteryCampManage/getCampDetail/{campNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_batteryCampManage_getCampList(data):
        """
        获取所有仓位列表
        """
        path = f'/api/batteryCampManage/getCampList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_getChargerDetail_campNo(campNo):
        """
        充电机详细信息
        请求参数:
        """
        path = f'/api/batteryCampManage/getChargerDetail/{campNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_batteryCampManage_saveCampRemark(data):
        """
        保存仓位备注
        请求参数:
            campNo: integer [必填] - 仓位号
            remark: string [可选] - 备注信息
        """
        path = f'/api/batteryCampManage/saveCampRemark'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampManage_saveChargerRemark(data):
        """
        保存充电机备注
        请求参数:
            chargerNo: integer [必填] - 充电机编号
            gunNo: integer [必填] - 充电枪编号
            remark: string [可选] - 备注信息
        """
        path = f'/api/batteryCampManage/saveChargerRemark'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampOperationControl_addDisableRecord(data):
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
        path = f'/api/batteryCampOperationControl/addDisableRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampOperationControl_batchExport(data):
        """
        仓位/电池禁用操作日志导出
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
        path = f'/api/batteryCampOperationControl/batchExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampOperationControl_count(data):
        """
        禁用历史数量
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
        path = f'/api/batteryCampOperationControl/count'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_batteryCampOperationControl_deleteDisableRecord(data):
        """
        删除禁用记录
        请求参数:
            id: integer [必填] - 业务主键
            remark: string [必填] - 备注
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作用户名称
        """
        path = f'/api/batteryCampOperationControl/deleteDisableRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'DELETE', data))

    @staticmethod
    def api_batteryCampOperationControl_deleteManualDisableRecord(data):
        """
        删除手动禁用记录
        请求参数:
            id: integer [必填] - 业务主键
            remark: string [必填] - 备注
            userId: integer [可选] - 操作用户
            userName: string [可选] - 操作用户名称
        """
        path = f'/api/batteryCampOperationControl/deleteManualDisableRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'DELETE', data))

    @staticmethod
    def api_batteryCampOperationControl_disableBatteryOpts():
        """
        禁用电池-仓位列表
        """
        path = f'/api/batteryCampOperationControl/disableBatteryOpts'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_batteryCampOperationControl_getDetail(data):
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
        path = f'/api/batteryCampOperationControl/getDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charge_boxTransformer_charges():
        """
        获取箱变充电机列表
        """
        path = f'/api/charge/boxTransformer/charges'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_charge_boxTransformer_getConfigList():
        """
        获取箱变配置列表
        """
        path = f'/api/charge/boxTransformer/getConfigList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_charge_boxTransformer_list():
        """
        获取箱变信息列表
        """
        path = f'/api/charge/boxTransformer/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_charge_boxTransformer_reset(data):
        """
        恢复默认配置
        """
        path = f'/api/charge/boxTransformer/reset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charge_boxTransformer_saveConfigs(data):
        """
        更新箱变配置
        请求参数:
            chargerNos: array [可选]
            containOther: boolean [可选]
            emus: array [可选] - EMU列表
            id: integer [可选] - id
            powerLimit: integer [可选] - 功率限制
        """
        path = f'/api/charge/boxTransformer/saveConfigs'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeRecord_batchExport(data):
        """
        批量导出
        请求参数:
            batteryCampNo: integer [可选]
            batterySn: string [可选]
            campTotalChargeTime: number [可选]
            carVin: string [可选]
            chargeAfterPower: number [可选]
            chargeBeforePower: number [可选]
            chargeEndTime: string [可选]
            chargeGunNo: string [可选]
            chargeModel: integer [可选]
            chargeNo: string [可选]
            chargeParamAdjustType: integer [可选]
            chargePeriodCount: integer [可选]
            chargePeriodDetail: string [可选]
            chargePower: number [可选]
            chargePowerDiscount: number [可选]
            chargePowerLimit: number [可选]
            chargeStartResult: integer [可选]
            chargeStartTime: string [可选]
            chargeStopResult: integer [可选]
            chargeStopTimeBegin: string [可选]
            chargeStopTimeEnd: string [可选]
            chargeType: integer [可选]
            cloudOrderNo: string [可选]
            createTime: string [可选]
            createTimeBegin: string [可选]
            createTimeEnd: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            direction: integer [可选]
            endReason: string [可选]
            endSoc: number [可选]
            endSocBegin: number [可选]
            endSocEnd: number [可选]
            flowNo: string [可选]
            flowStatus: integer [可选]
            id: integer [可选]
            ids: array [可选]
            ratedPower: number [可选]
            remark: string [可选]
            requestId: string [可选]
            size: integer [可选]
            sortNo: integer [可选]
            startSoc: number [可选]
            startSocBegin: number [可选]
            startSocEnd: number [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            uploadFlag: integer [可选]
        """
        path = f'/api/chargeRecord/batchExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeRecord_detailList(data):
        """
        detailList
        请求参数:
            batteryCampNo: integer [可选]
            batterySn: string [可选]
            campTotalChargeTime: number [可选]
            carVin: string [可选]
            chargeAfterPower: number [可选]
            chargeBeforePower: number [可选]
            chargeEndTime: string [可选]
            chargeGunNo: string [可选]
            chargeModel: integer [可选]
            chargeNo: string [可选]
            chargeParamAdjustType: integer [可选]
            chargePeriodCount: integer [可选]
            chargePeriodDetail: string [可选]
            chargePower: number [可选]
            chargePowerDiscount: number [可选]
            chargePowerLimit: number [可选]
            chargeStartResult: integer [可选]
            chargeStartTime: string [可选]
            chargeStopResult: integer [可选]
            chargeStopTimeBegin: string [可选]
            chargeStopTimeEnd: string [可选]
            chargeType: integer [可选]
            cloudOrderNo: string [可选]
            createTime: string [可选]
            createTimeBegin: string [可选]
            createTimeEnd: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            direction: integer [可选]
            endReason: string [可选]
            endSoc: number [可选]
            endSocBegin: number [可选]
            endSocEnd: number [可选]
            flowNo: string [可选]
            flowStatus: integer [可选]
            id: integer [可选]
            ids: array [可选]
            ratedPower: number [可选]
            remark: string [可选]
            requestId: string [可选]
            size: integer [可选]
            sortNo: integer [可选]
            startSoc: number [可选]
            startSocBegin: number [可选]
            startSocEnd: number [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            uploadFlag: integer [可选]
        """
        path = f'/api/chargeRecord/detailList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeRecord_page(data):
        """
        分页查询
        请求参数:
            batteryCampNo: integer [可选]
            batterySn: string [可选]
            campTotalChargeTime: number [可选]
            carVin: string [可选]
            chargeAfterPower: number [可选]
            chargeBeforePower: number [可选]
            chargeEndTime: string [可选]
            chargeGunNo: string [可选]
            chargeModel: integer [可选]
            chargeNo: string [可选]
            chargeParamAdjustType: integer [可选]
            chargePeriodCount: integer [可选]
            chargePeriodDetail: string [可选]
            chargePower: number [可选]
            chargePowerDiscount: number [可选]
            chargePowerLimit: number [可选]
            chargeStartResult: integer [可选]
            chargeStartTime: string [可选]
            chargeStopResult: integer [可选]
            chargeStopTimeBegin: string [可选]
            chargeStopTimeEnd: string [可选]
            chargeType: integer [可选]
            cloudOrderNo: string [可选]
            createTime: string [可选]
            createTimeBegin: string [可选]
            createTimeEnd: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            direction: integer [可选]
            endReason: string [可选]
            endSoc: number [可选]
            endSocBegin: number [可选]
            endSocEnd: number [可选]
            flowNo: string [可选]
            flowStatus: integer [可选]
            id: integer [可选]
            ids: array [可选]
            ratedPower: number [可选]
            remark: string [可选]
            requestId: string [可选]
            size: integer [可选]
            sortNo: integer [可选]
            startSoc: number [可选]
            startSocBegin: number [可选]
            startSocEnd: number [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            uploadFlag: integer [可选]
        """
        path = f'/api/chargeRecord/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeStrategy_cancel(data):
        """
        cancelChargeStrategy
        """
        path = f'/api/chargeStrategy/cancel'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeStrategy_period(data):
        """
        periodChargeStrategy
        请求参数:
            scheduleConf: string [可选]
            taskName: string [可选]
        """
        path = f'/api/chargeStrategy/period'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeStrategy_trigger(data):
        """
        triggerChargeStrategy
        请求参数:
            scheduleConf: string [可选]
            taskName: string [可选]
        """
        path = f'/api/chargeStrategy/trigger'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTestFlow_delChargeTestFlow(data):
        """
        删除充电测试流程
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargeTestFlow/delChargeTestFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTestFlow_getChargeTestFlowDetail(data):
        """
        获取充电测试流程详情
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargeTestFlow/getChargeTestFlowDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTestFlow_getChargeTestFlowList(data):
        """
        获取充电测试流程
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargeTestFlow/getChargeTestFlowList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTestFlow_saveChargeTestFlow(data):
        """
        保存充电测试流程
        请求参数:
            id: integer [可选] - 测试流程id
            itemList: array [可选] - 流程信息
                        childItemList: array [可选] - 子流程信息
                                    controlType: string [可选] - 条件类型 字典：chargeParamAdjustType
                                    fieldVal: string [可选] - 参数值
                                    cutOffConditionConfig: array [可选] - 子截止条件配置
                                                conditionType: string [可选] - 符号类型 字典：conditionType
                                                fieldType: string [可选] - 条件类型 字典：fieldType
                                                fieldVal: string [可选] - 参数值
                                    cutOffConditionConfigOperator: integer [可选] - 运算符号 0-未知 1-或 2-且
                                    fatherItemSort: integer [可选] - 父条目sort
                                    itemControlMode: integer [可选] - 控制方式 1-充电 2-放电 3-静置
                                    itemSort: integer [可选] - 子条目序号
                                    conditionType: string [可选] - 符号类型 字典：conditionType
                                    fieldType: string [可选] - 条件类型 字典：fieldType
                                    fieldVal: string [可选] - 参数值
                        cutOffConditionConfig: array [可选] - 截止条件配置(除去SOC/时间)
                                    conditionType: string [可选] - 符号类型 字典：conditionType
                                    fieldType: string [可选] - 条件类型 字典：fieldType
                                    fieldVal: string [可选] - 参数值
                        cutOffConditionConfigOperator: integer [可选] - 运算符号 0-未知 1-或 2-且
                        cycleTime: integer [可选] - 循环次数
                        itemSort: integer [可选] - 条目序号
            positions: array [可选] - 仓位列表
            testFlowName: string [可选] - 测试流程名称
            testTime: integer [可选] - 测试次数
        """
        path = f'/api/chargeTestFlow/saveChargeTestFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTestFlow_startChargeTestFlow(data):
        """
        开启充电测试流程
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargeTestFlow/startChargeTestFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTestFlow_stopChargeTestFlow(data):
        """
        停止充电测试流程
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargeTestFlow/stopChargeTestFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTestFlowRecord_detail(data):
        """
        详情
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargeTestFlowRecord/detail'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTestFlowRecord_page(data):
        """
        分页查询
        请求参数:
            current: integer [可选]
            endDateBegin: string [可选] - 结束时间-起始
            endDateEnd: string [可选] - 结束时间-结束
            requestId: string [可选]
            size: integer [可选]
            startDateBegin: string [可选] - 开始时间-起始
            startDateEnd: string [可选] - 开始时间-结束
            testFlowRecordStatus: integer [可选] - 流程记录状态 0-未进行 1-进行中 2-已完成 字典：testFlowRecordStatus
            timestamp: integer [可选]
        """
        path = f'/api/chargeTestFlowRecord/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTiling_create(data):
        """
        创建充电窗口
        请求参数:
            id: integer [可选] - id（更新时传入）
            mappingList: array [可选] - Mapping数据列表
                        mappingCoordVal: number [必填] - mapping坐标对应值
                        mappingCoordxVal: number [必填] - mapping坐标x对应值
                        mappingCoordyVal: number [必填] - mapping坐标y对应值
            packRatedCapacity: number [必填] - 包额定容量
            packSoh: number [必填] - 包SOH
            tilingName: string [必填] - 窗口名
            tilingType: integer [必填] - 窗口类型 0-未知 1-温度/时间 Mapping 2-温度/Soc Mapping
        """
        path = f'/api/chargeTiling/create'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTiling_del(data):
        """
        删除充电窗口
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargeTiling/del'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTiling_detail(data):
        """
        查询充电窗口详情
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargeTiling/detail'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTiling_pageQuery(data):
        """
        分页查询充电窗口列表
        请求参数:
            current: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/chargeTiling/pageQuery'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTiling_update(data):
        """
        更新充电窗口
        请求参数:
            id: integer [可选] - id（更新时传入）
            mappingList: array [可选] - Mapping数据列表
                        mappingCoordVal: number [必填] - mapping坐标对应值
                        mappingCoordxVal: number [必填] - mapping坐标x对应值
                        mappingCoordyVal: number [必填] - mapping坐标y对应值
            packRatedCapacity: number [必填] - 包额定容量
            packSoh: number [必填] - 包SOH
            tilingName: string [必填] - 窗口名
            tilingType: integer [必填] - 窗口类型 0-未知 1-温度/时间 Mapping 2-温度/Soc Mapping
        """
        path = f'/api/chargeTiling/update'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTilingMapping_exportExcel(data):
        """
        导出Excel文件
        请求参数:
            tilingId: integer [可选] - 窗口配置id
            tilingType: integer [可选] - 窗口配置类型
        """
        path = f'/api/chargeTilingMapping/exportExcel'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargeTilingMapping_parseExcel(data):
        """
        excel导入
        请求参数:
        """
        path = f'/api/chargeTilingMapping/parseExcel'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_api_chargerControl_feign_startStopHotControl(data):
        """
        startStopHotControl
        请求参数:
            chargerNo: integer [可选]
            gun1: integer [可选]
            gun2: integer [可选]
            gun3: integer [可选]
            gun4: integer [可选]
            startStopControl: integer [可选]
            supportHotNum: integer [可选]
        """
        path = f'/api/charger/api/chargerControl/feign/startStopHotControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_downChargeFault(data):
        """
        导出告警记录
        请求参数:
            no: integer [可选]
        """
        path = f'/api/charger/downChargeFault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_downChargeRecord(data):
        """
        导出充电记录
        请求参数:
            no: integer [可选]
        """
        path = f'/api/charger/downChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_batteryInfo_campNo(campNo):
        """
        获取充电电池信息
        请求参数:
        """
        path = f'/api/charger/equip/batteryInfo/{campNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_charger_equip_chargeDetailInfo_chargeNo(chargeNo):
        """
        获取充电机实时信息
        请求参数:
        """
        path = f'/api/charger/equip/chargeDetailInfo/{chargeNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_charger_equip_chargeEquipInfo_chargeNo(chargeNo):
        """
        获取充电机设备信息
        请求参数:
        """
        path = f'/api/charger/equip/chargeEquipInfo/{chargeNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_charger_equip_chargeSettingInfo_chargeNo(chargeNo):
        """
        获取充电机设置信息
        请求参数:
        """
        path = f'/api/charger/equip/chargeSettingInfo/{chargeNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_charger_equip_faultNum_chargeNo(chargeNo):
        """
        获取充电机实时故障数
        请求参数:
        """
        path = f'/api/charger/equip/faultNum/{chargeNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_charger_equip_gunInfo_campNo(campNo):
        """
        获取充电格口信息
        请求参数:
        """
        path = f'/api/charger/equip/gunInfo/{campNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_charger_equip_historyFault(data):
        """
        获取充电机历史故障信息
        请求参数:
            chargeNo: integer [可选] - 充电机号
            current: integer [可选]
            faultCode: integer [可选]
            gunNo: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            sort: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/charger/equip/historyFault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_historyFaultExport(data):
        """
        充电机历史故障导出
        请求参数:
            chargeNo: integer [可选] - 充电机号
            current: integer [可选]
            faultCode: integer [可选]
            gunNo: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            sort: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/charger/equip/historyFaultExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_historyOrder(data):
        """
        获取充电机历史订单信息
        请求参数:
            chargeNo: integer [可选] - 充电机号
            current: integer [可选]
            flowNo: string [可选]
            gunNo: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            sort: integer [可选]
            stopReason: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/charger/equip/historyOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_historyOrderExport(data):
        """
        充电机历史订单导出
        请求参数:
            chargeNo: integer [可选] - 充电机号
            current: integer [可选]
            flowNo: string [可选]
            gunNo: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            sort: integer [可选]
            stopReason: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/charger/equip/historyOrderExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_list():
        """
        获取主回路列表
        """
        path = f'/api/charger/equip/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_charger_equip_queryConfigPricePeriod(data):
        """
        触发尖峰平谷查询
        """
        path = f'/api/charger/equip/queryConfigPricePeriod'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_queryConfigPricePeriod_chargeNo(chargeNo):
        """
        查询充电机尖峰平谷
        请求参数:
        """
        path = f'/api/charger/equip/queryConfigPricePeriod/{chargeNo}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_charger_equip_queryDeviceParam(data):
        """
        获取充电机历史订单信息
        """
        path = f'/api/charger/equip/queryDeviceParam'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_queryVersion(data):
        """
        触发查询充电机版本信息
        """
        path = f'/api/charger/equip/queryVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_restCharge(data):
        """
        充电机复位
        请求参数:
            chargerNo: integer [可选] - 充电机号
            controlPanelNo: integer [可选] - 控制板编号
            controlPanelType: integer [可选] - 控制板类型
            resetMode: integer [可选] - 复位方式
            subType: string [可选]
        """
        path = f'/api/charger/equip/restCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_equip_settingChargeConfig(data):
        """
        设置充电机充电配置
        请求参数:
            accessControlAlarm: integer [可选] - 门禁报警 0：关闭 1：打开
            chargeEquipOverTemperature: number [可选] - 充电设备过温阈值（ ºC ）
            chargeNo: integer [可选] - 充电机号
            dcMeterBaud: integer [可选] - 直流电表波特率：
0x00：1200bps
0x01：2400bps
0x02：4800bps
0x03：9600bps
0x04：14400bps
0x05：19200bps
0x06：38400bps
0x07：57600bps
0x08：115200bsp
0x09：128000bps
            dcMeterType: integer [可选] - 直流电表类型型号
            electricLossCompensationCoefficient: integer [可选] - 电损补偿系数（%）
            inputOverVoltageValue: number [可选] - 输入过压阈值（V）
            inputUnderVoltageValue: number [可选] - 输入欠压阈值（V）
            offlineChargeTime: integer [可选] - 离线充电时间（min）
            outputOverVoltageValue: number [可选] - 输出过压阈值（V）
            overCurrentFilterTime: number [可选] - 过流滤波时间（ms）
            simulationCharge: integer [可选] - 模拟充电 0：关闭 1：打开
            singleOutputOverCurrentValue: number [可选] - 单路输出过流阈值（A）
            socLimit: integer [可选] - 本地SOC限制（%）
            stationChargeStrategy: integer [可选] - 站内外充放电策略 0:站内优先 1:站外优先 2:优先启动调用（先到先得）
            unEffectiveCurrentAbleCharge: integer [可选] - 无有效电流可持续充电 0：关闭 1：打开
        """
        path = f'/api/charger/equip/settingChargeConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_list():
        """
        充电机列表
        """
        path = f'/api/charger/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_charger_ota_list(data):
        """
        充电机升级列表
        请求参数:
            chargerNos: array [可选] - 充电机号
            upgradeType: integer [可选] - 升级类型 1:蓝牙 2：APP 3:TCU 4：CCU 5:SBLE 6:VBLE 7:PDU
        """
        path = f'/api/charger/ota/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_charger_ota_s2gSwitch():
        """
        S2G手动放电功能开关
        """
        path = f'/api/charger/ota/s2gSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_charger_ota_upgrade(data):
        """
        充电机升级
        请求参数:
            chargerNos: array [可选] - 充电机号
            fileId: integer [可选] - 文件id
            msgId: integer [可选]
            remark: string [可选] - 备注
            source: integer [可选]
            upgradeType: integer [可选] - 升级类型 1:蓝牙 2：APP 3:TCU 4：CCU 5:PDU
        """
        path = f'/api/charger/ota/upgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_downChargeFault(data):
        """
        导出告警记录
        请求参数:
            no: integer [可选]
        """
        path = f'/api/chargerDcco/downChargeFault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_downChargeRecord(data):
        """
        导出充电记录
        请求参数:
            no: integer [可选]
        """
        path = f'/api/chargerDcco/downChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_equipInfo(data):
        """
        设备信息
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/chargerDcco/equipInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_getChargeDetailByNo(data):
        """
        超充桩详情数据
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/chargerDcco/getChargeDetailByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_getGunInfoByPos(data):
        """
        超充枪详情数据
        请求参数:
            campNo: integer [可选]
        """
        path = f'/api/chargerDcco/getGunInfoByPos'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_list(data):
        """
        超充列表
        """
        path = f'/api/chargerDcco/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_startCharge(data):
        """
        开始充电
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
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDcco_stopCharge(data):
        """
        停止充电
        请求参数:
            cloudFlowNo: string [可选] - 云端流水号
            flowNo: string [可选] - 充电机交互流水号
            position: integer [可选] - 仓位号
            stopReason: integer [可选] - 1.停止原因 0正常充满停机 1服务器发现桩异常,强制停机 2 账号校验失败 3APP主动停机 4 账号欠费 5无可用模块
        """
        path = f'/api/chargerDcco/stopCharge'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDccoRecord_detail(data):
        """
        记录详情
        请求参数:
            id: integer [可选]
        """
        path = f'/api/chargerDccoRecord/detail'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDccoRecord_page(data):
        """
        分页列表
        请求参数:
            afterCreateTime: string [可选] - 结束创建时间
            afterStartTime: string [可选] - 结束充电开始时间
            beforeCreateTime: string [可选] - 开始创建时间
            beforeStartTime: string [可选] - 开始充电开始时间
            chargeModel: integer [可选] - 充电类型
            current: integer [可选]
            flowNo: string [可选] - 流水号
            flowStatus: integer [可选] - 充电状态
            gunNo: integer [可选] - 充电枪号
            requestId: string [可选]
            size: integer [可选]
            startResult: integer [可选] - 启动结果
            stopType: integer [可选] - 停止类型
            timestamp: integer [可选]
        """
        path = f'/api/chargerDccoRecord/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerDict_code_import(data):
        """
        字典编码导入
        请求参数:
        """
        path = f'/api/chargerDict/code/import'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_chargerGun_saveRemark(data):
        """
        保存充电枪备注
        请求参数:
            campNo: integer [可选] - 仓位号
            remark: string [可选] - 备注
        """
        path = f'/api/chargerGun/saveRemark'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_config_emu(data):
        """
        emu开关
        """
        path = f'/api/config/emu'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_config_oob(data):
        """
        oob开关
        """
        path = f'/api/config/oob'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_dataCloudMqtt_connect(data):
        """
        连接mqtt
        """
        path = f'/api/dataCloudMqtt/connect'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_dataCloudMqtt_disconnect(data):
        """
        【控制】断开mqtt
        """
        path = f'/api/dataCloudMqtt/disconnect'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_dataCloudMqtt_isConnected(data):
        """
        【查看】mqtt是否连接
        """
        path = f'/api/dataCloudMqtt/isConnected'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_debug_plc_removePLCBMSPackLockStatus(data):
        """
        关闭同步PLC电池锁状态
        """
        path = f'/api/debug/plc/removePLCBMSPackLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_debug_plc_sendPLCBMSPackLockStatus(data):
        """
        下发同步PLC电池锁状态
        请求参数:
            packNum: integer [可选] - 用户选择的换电电池包数量 默认：2
        """
        path = f'/api/debug/plc/sendPLCBMSPackLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_devopsStationStatus(data):
        """
        换电站状态
        """
        path = f'/api/devops/station/devopsStationStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_finishUpgrade(data):
        """
        升级完成
        """
        path = f'/api/devops/station/finishUpgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_importAuth(data):
        """
        导入权限
        请求参数:
        """
        path = f'/api/devops/station/importAuth'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_importFault(data):
        """
        导入故障
        请求参数:
        """
        path = f'/api/devops/station/importFault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_importSwap(data):
        """
        导入换电流程
        请求参数:
        """
        path = f'/api/devops/station/importSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_initStation(data):
        """
        落站初始化
        请求参数:
            pickPackConfig: array [可选]
                        enableFlag: integer [可选]
                        id: integer [可选]
                        limitValue: number [可选]
                        pickPackItem: string [可选]
            stationRegion: integer [可选] - 区域版本类型
        """
        path = f'/api/devops/station/initStation'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_startUpgrade(data):
        """
        开始升级
        """
        path = f'/api/devops/station/startUpgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_stationStatusChange(data):
        """
        站控运营状态切换
        请求参数:
            changeReason: string [可选]
            changeReasonCode: integer [可选]
            changeStationStatus: integer [可选]
            permitBatterySwap: integer [可选]
            sourceForm: integer [可选]
        """
        path = f'/api/devops/station/stationStatusChange'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_devops_station_updateStationVersion(data):
        """
        更新站控版本
        请求参数:
            version: string [可选]
        """
        path = f'/api/devops/station/updateStationVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_dict_addOrUpdate(data):
        """
        addOrUpdate
        请求参数:
            dictType: string [可选]
            dictTypeName: string [可选]
            dictValue: string [可选]
            dictValueName: string [可选]
            id: integer [可选]
            remark: integer [可选]
            sortNo: integer [可选]
        """
        path = f'/api/dict/addOrUpdate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_dict_batchDel(data):
        """
        batchDel
        请求参数:
            dictIds: array [可选]
        """
        path = f'/api/dict/batchDel'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_dict_getByKey_key(key):
        """
        通过key查询字典值
        请求参数:
        """
        path = f'/api/dict/getByKey/{key}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_dict_getByKeys(data):
        """
        通过key数组，查询字典集合
        请求参数:
        """
        path = f'/api/dict/getByKeys'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_dict_page(data):
        """
        page
        请求参数:
            current: integer [可选]
            dictType: string [可选]
            dictTypeName: string [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/dict/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_dict_id(id):
        """
        get
        请求参数:
        """
        path = f'/api/dict/{id}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_disableRecord_disablePackList(data):
        """
        disablePackList
        """
        path = f'/api/disableRecord/disablePackList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_config_getStorageStrategy(data):
        """
        获取储能调度策略配置
        """
        path = f'/api/emu/config/getStorageStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_emu_config_saveStorageStrategy(data):
        """
        保存储能调度策略配置
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
        path = f'/api/emu/config/saveStorageStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_entryCampDebugRecord_page(data):
        """
        分页查询
        请求参数:
            current: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/entryCampDebugRecord/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equip_camera_checkCameraAngle(data):
        """
        checkCameraAngle
        """
        path = f'/api/equip/camera/checkCameraAngle'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_air_faultRest(data):
        """
        faultRest
        请求参数:
            slaveId: integer [可选]
        """
        path = f'/api/equipment/air/faultRest'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_air_getInfos(data):
        """
        getInfos
        """
        path = f'/api/equipment/air/getInfos'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_air_powerSwitch(data):
        """
        powerSwitch
        请求参数:
            on: boolean [可选]
            slaveId: integer [可选]
        """
        path = f'/api/equipment/air/powerSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_air_setParams(data):
        """
        setParams
        请求参数:
            coolTemp: number [可选]
            coolTempDiff: number [可选]
            dehumidifyDiff: number [可选]
            dehumidifySwicth: boolean [可选]
            dehumidifyValue: number [可选]
            highHumidityAlarm: number [可选]
            highTempAlarm: number [可选]
            hotTemp: number [可选]
            hotTempDiff: number [可选]
            internalFanStatus: boolean [可选]
            lowTempAlarm: number [可选]
            slaveId: integer [可选]
        """
        path = f'/api/equipment/air/setParams'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_airConditioningParam(data):
        """
        空调参数设置
        请求参数:
            electricSill: number [可选]
            id: string [必填]
            lowerTemperatureAlarmValueFlag: integer [可选]
            openCloseFlag: integer [可选]
            temperatureLowerLimit: number [可选]
            temperatureUpperLimit: number [可选]
            upperTemperatureLimitAlarmValueFlag: integer [可选]
        """
        path = f'/api/equipment/airConditioning/airConditioningParam'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_autoParam(data):
        """
        空调自动参数获取
        """
        path = f'/api/equipment/airConditioning/autoParam'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_autoParamSet(data):
        """
        空调自动参数设值
        请求参数:
            coolStartTemp: number [可选] - 制冷启动温度
            coolStopTemp: number [可选] - 制冷停止温度
            hotStartTemp: number [可选] - 制热启动温度
            hotStopTemp: number [可选] - 制热停止温度
            on: integer [可选] - 控制模式 1-开；0-关
        """
        path = f'/api/equipment/airConditioning/autoParamSet'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_controlModel(data):
        """
        空调控制模式控制
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
        """
        path = f'/api/equipment/airConditioning/controlModel'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_heat(data):
        """
        空调制热开机发射
        请求参数:
            id: string [必填]
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/airConditioning/heat'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_info(data):
        """
        空调信息
        """
        path = f'/api/equipment/airConditioning/info'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_refrigeration(data):
        """
        空调制冷开机发射
        请求参数:
            id: string [必填]
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/airConditioning/refrigeration'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_shutdown(data):
        """
        空调关机发射
        请求参数:
            id: string [必填]
        """
        path = f'/api/equipment/airConditioning/shutdown'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_airConditioning_temperatureControl(data):
        """
        空调温度控制
        请求参数:
            id: string [必填]
            temperatureLowerLimit: number [可选]
            temperatureUpperLimit: number [可选]
        """
        path = f'/api/equipment/airConditioning/temperatureControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_camera_intrusionStatus(data):
        """
        活物入侵状态
        """
        path = f'/api/equipment/camera/intrusionStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_connectStatus(data):
        """
        设备连接状态
        """
        path = f'/api/equipment/connectStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_connectStatusByCode(data):
        """
        设备连接详情
        请求参数:
            equipmentCode: string [可选]
        """
        path = f'/api/equipment/connectStatusByCode'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_curtain_faultRest(data):
        """
        faultRest
        请求参数:
            slaveId: integer [可选]
        """
        path = f'/api/equipment/curtain/faultRest'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_curtain_forcedHeating(data):
        """
        forcedHeating
        请求参数:
            on: boolean [可选]
            slaveId: integer [可选]
        """
        path = f'/api/equipment/curtain/forcedHeating'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_curtain_getInfos(data):
        """
        getInfos
        """
        path = f'/api/equipment/curtain/getInfos'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_curtain_powerSwitch(data):
        """
        powerSwitch
        请求参数:
            on: boolean [可选]
            slaveId: integer [可选]
        """
        path = f'/api/equipment/curtain/powerSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_curtain_selfCheck(data):
        """
        selfCheck
        请求参数:
            on: boolean [可选]
            slaveId: integer [可选]
        """
        path = f'/api/equipment/curtain/selfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_curtain_setParams(data):
        """
        setParams
        请求参数:
            heaterStartTemp: number [可选]
            heaterStopReturnDiffTemp: number [可选]
            slaveId: integer [可选]
            standbyfanStatus: number [可选]
        """
        path = f'/api/equipment/curtain/setParams'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_electricMeter_list(data):
        """
        电表列表信息
        """
        path = f'/api/equipment/electricMeter/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_enableElectric(data):
        """
        启用电表配置
        请求参数:
            enable: integer [必填]
            equipmentType: integer [必填]
            id: integer [必填]
        """
        path = f'/api/equipment/enableElectric'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fan_alarmReset(data):
        """
        风机告警复位
        请求参数:
            id: string [必填]
        """
        path = f'/api/equipment/fan/alarmReset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fan_controlModelChange(data):
        """
        风机控制模式切换
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            equipActionType: integer [可选] - 设备控制类型 0：默认值 1：开启 2：关闭
            fanCode: string [可选]
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/equipment/fan/controlModelChange'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fan_list(data):
        """
        风机列表信息
        """
        path = f'/api/equipment/fan/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fan_manualSwitchFan(data):
        """
        风机手动开启风扇
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fan/manualSwitchFan'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fan_paramSet(data):
        """
        风机参数设置
        请求参数:
            fanStartSmallBoxTem: number [可选]
            fanStartTem: number [可选]
            fanStopBoxTemDifference: number [可选]
            fanStopTem: number [可选]
            highAlarmTem: number [可选]
            id: string [必填]
            lowAlarmTem: number [可选]
            timerStartHour: integer [可选]
            timerStartMin: integer [可选]
        """
        path = f'/api/equipment/fan/paramSet'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fan_remoteSwitchAirCondition(data):
        """
        风机远程开关空调
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fan/remoteSwitchAirCondition'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_acoustoOpticAlarm(data):
        """
        消防声光报警
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fireControl/acoustoOpticAlarm'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_annihilator(data):
        """
        消防灭火器控制
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fireControl/annihilator'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_auto(data):
        """
        消防自动模式
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fireControl/auto'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_clearAlarm(data):
        """
        消防消报警音
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fireControl/clearAlarm'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_delay(data):
        """
        消防延时设置
        请求参数:
            delaySecond: integer [可选]
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fireControl/delay'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_info(data):
        """
        消防信息
        """
        path = f'/api/equipment/fireControl/info'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_manual(data):
        """
        消防手动模式
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fireControl/manual'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_reSet(data):
        """
        消防复位
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fireControl/reSet'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_fireControl_selfCheck(data):
        """
        消防自检
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/fireControl/selfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_heater_alarmReset(data):
        """
        加热器告警复位
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/heater/alarmReset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_heater_forceHeating(data):
        """
        加热器强制制热
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/heater/forceHeating'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_heater_init(data):
        """
        加热器恢复出厂设置
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/heater/init'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_heater_list(data):
        """
        加热器列表信息
        """
        path = f'/api/equipment/heater/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_heater_paramRet(data):
        """
        加热器参数设置
        请求参数:
            cabinetInsideHighTemperatureLimit: number [可选]
            cabinetInsideLowTemperatureLimit: number [可选]
            heaterStartingTemperature: number [可选]
            heaterStopReturnDifferenceTemperature: number [可选]
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/heater/paramRet'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_heater_remoteSwitch(data):
        """
        加热器远程开关
        请求参数:
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
        """
        path = f'/api/equipment/heater/remoteSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_ipc_rebootNow(data):
        """
        工控机重启
        """
        path = f'/api/equipment/ipc/rebootNow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_ipc_shutdownNow(data):
        """
        工控机关机
        """
        path = f'/api/equipment/ipc/shutdownNow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_plcPeriodicData(data):
        """
        PLC周期数据上报情况
        """
        path = f'/api/equipment/plcPeriodicData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_resetAmmeter(data):
        """
        电表恢复默认配置
        """
        path = f'/api/equipment/resetAmmeter'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_resetEmu(data):
        """
        储能配置恢复默认值
        """
        path = f'/api/equipment/resetEmu'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_selectList(data):
        """
        查询设备列表
        请求参数:
            enableFlag: integer [可选]
            equipmentCodes: array [可选]
            ids: array [可选]
            stationType: integer [可选]
        """
        path = f'/api/equipment/selectList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_temperatureAndHumidity_list(data):
        """
        温湿度列表信息
        """
        path = f'/api/equipment/temperatureAndHumidity/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_temperatureAndHumidity_sensor(data):
        """
        温湿度传感器设置
        请求参数:
            humidityDownAlarm: number [可选]
            humidityDownAlarmEnable: integer [可选]
            humidityUpAlarm: number [可选]
            humidityUpAlarmEnable: integer [可选]
            id: string [必填]
            onOff: integer [可选] - 开关
            temperature: integer [可选] - 温度
            temperatureDownAlarm: number [可选]
            temperatureDownAlarmEnable: integer [可选]
            temperatureUpAlarm: number [可选]
            temperatureUpAlarmEnable: integer [可选]
        """
        path = f'/api/equipment/temperatureAndHumidity/sensor'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_updateEmus(data):
        """
        储能配置
        请求参数:
            enable: integer [可选]
            id: integer [可选]
        """
        path = f'/api/equipment/updateEmus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_ups_info(data):
        """
        ups信息
        """
        path = f'/api/equipment/ups/info'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fan_control(data):
        """
        control
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            equipActionType: integer [可选] - 设备控制类型 0：默认值 1：开启 2：关闭
            fanCode: string [可选]
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/fan/control'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fan_status(data):
        """
        status
        """
        path = f'/api/fan/status'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_clear(data):
        """
        手动清除故障
        请求参数:
            bmsFaultList: array [可选] - bms仓位号故障清除
                        bmsClearType: integer [可选] - BMS故障清除类型 1-清除不存储NVM的故障 2-清除所有故障 (包含存储NVM和不存储NVM) 
                        campNo: integer [可选] - 仓位号：BMS故障清除需传
            clearFaultTargetList: array [必填] - 执行对象
            faultIds: array [可选] - 故障主键列表：本地站控诊断故障清除需传
            userName: string [可选] - 操作人
        """
        path = f'/api/fault/clear'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_current_count(data):
        """
        实时故障-总数
        """
        path = f'/api/fault/current/count'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_current_export(data):
        """
        实时故障-导出
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
        path = f'/api/fault/current/export'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_current_list(data):
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
        path = f'/api/fault/current/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_history_export(data):
        """
        历史故障-导出
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
        path = f'/api/fault/history/export'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_history_gatherPage(data):
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
        path = f'/api/fault/history/gatherPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_history_page(data):
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
        path = f'/api/fault/history/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_faultMatrix_importFile(data):
        """
        导入故障处理矩阵
        请求参数:
        """
        path = f'/api/faultMatrix/importFile'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_faultMatrix_selectPage(data):
        """
        分页列表
        请求参数:
            current: integer [可选]
            deviceCode: string [可选] - 设备简称
            faultCode: string [可选] - 故障码
            faultSource: string [可选] - 故障来源
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/faultMatrix/selectPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_file_down_fileId(fileId):
        """
        下载文件
        请求参数:
        """
        path = f'/api/file/down/{fileId}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_gate_control(data):
        """
        道闸控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            gateControlAction: integer [可选] - 控制道闸动作 0：默认值 1：开启 2：关闭
            gateControlObject: integer [可选] - 控制道闸对象 0：默认值 1：入口道闸 2：出口道闸
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/gate/control'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_gate_status(data):
        """
        获取道闸状态
        """
        path = f'/api/gate/status'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_heatStrategyConfig_getHeatConfig(data):
        """
        getHeatConfig
        """
        path = f'/api/heatStrategyConfig/getHeatConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_heatStrategyConfig_getHeatSwitch(data):
        """
        getHeatSwitch
        """
        path = f'/api/heatStrategyConfig/getHeatSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_heatStrategyConfig_init(data):
        """
        init
        请求参数:
            heatType: integer [可选]
        """
        path = f'/api/heatStrategyConfig/init'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_heatStrategyConfig_update(data):
        """
        update
        请求参数:
            enable: integer [必填]
            id: integer [必填]
            maxEnterTemp: number [必填]
            maxOutTemp: number [必填]
            minEnterTemp: number [必填]
            minOutTemp: number [必填]
        """
        path = f'/api/heatStrategyConfig/update'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_heatStrategyConfig_updateCampExecLimitCurrentNeededCache(data):
        """
        updateCampExecLimitCurrentNeededCache
        请求参数:
            campExecLimit: integer [可选] - 是否存在充电降倍率 1：是 0：否
            position: integer [可选] - 仓位号
            status: integer [可选] - 限制电流类型 0-未知 1-按需充电 2-最佳路径寻优
        """
        path = f'/api/heatStrategyConfig/updateCampExecLimitCurrentNeededCache'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_heatStrategyConfig_updateHotCurrentTypeStrategy(data):
        """
        updateHotCurrentTypeStrategy
        请求参数:
            campExecLimit: integer [可选] - 是否存在充电降倍率 1：是 0：否
            position: integer [可选] - 仓位号
            status: integer [可选] - 限制电流类型 0-未知 1-按需充电 2-最佳路径寻优
        """
        path = f'/api/heatStrategyConfig/updateHotCurrentTypeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_home_chargeStatusPacks(data):
        """
        chargeStatusPacks
        """
        path = f'/api/home/chargeStatusPacks'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_home_equipPingInfo(data):
        """
        equipPingInfo
        """
        path = f'/api/home/equipPingInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_home_packStatistics(data):
        """
        packStatistics
        """
        path = f'/api/home/packStatistics'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_home_packSwapMatchInfoList(data):
        """
        packSwapMatchInfoList
        """
        path = f'/api/home/packSwapMatchInfoList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_home_servicePingInfo(data):
        """
        servicePingInfo
        """
        path = f'/api/home/servicePingInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_home_swapConditionDetail(data):
        """
        swapConditionDetail
        """
        path = f'/api/home/swapConditionDetail'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_code_import(data):
        """
        字典编码导入
        请求参数:
        """
        path = f'/api/hot/code/import'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_getBatteryInfoByPosition(data):
        """
        获取电池信息
        请求参数:
            pos: integer [可选]
        """
        path = f'/api/hot/getBatteryInfoByPosition'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_getDetailByNo(data):
        """
        获取脉冲加热机实时信息
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hot/getDetailByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_getEquipInfoByNo(data):
        """
        获取脉冲加热机设备信息
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hot/getEquipInfoByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_getEquips(data):
        """
        查询脉冲加热设备参数
        """
        path = f'/api/hot/getEquips'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_getFaultNumByNo(data):
        """
        获取加热机实时故障数
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hot/getFaultNumByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_getGunInfoByPos(data):
        """
        获取脉冲加热枪信息
        请求参数:
            pos: integer [可选]
        """
        path = f'/api/hot/getGunInfoByPos'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_getSettingByNo(data):
        """
        获取设备参数
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hot/getSettingByNo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_history_fault(data):
        """
        获取历史故障信息
        请求参数:
            current: integer [可选]
            faultCode: integer [可选]
            gunNo: integer [可选]
            no: integer [必填]
            requestId: string [可选]
            size: integer [可选]
            sort: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/hot/history/fault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_history_faultExport(data):
        """
        历史故障导出
        请求参数:
            current: integer [可选]
            faultCode: integer [可选]
            gunNo: integer [可选]
            no: integer [必填]
            requestId: string [可选]
            size: integer [可选]
            sort: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/hot/history/faultExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_history_order(data):
        """
        获取历史订单信息
        请求参数:
            current: integer [可选]
            flowNo: string [可选]
            gunNo: integer [可选]
            no: integer [必填]
            requestId: string [可选]
            size: integer [可选]
            sort: integer [可选]
            stopReason: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/hot/history/order'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_history_orderExport(data):
        """
        历史订单导出
        请求参数:
            current: integer [可选]
            flowNo: string [可选]
            gunNo: integer [可选]
            no: integer [必填]
            requestId: string [可选]
            size: integer [可选]
            sort: integer [可选]
            stopReason: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/hot/history/orderExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_magnification_exportMagnificationData(data):
        """
        导出边界阈值数据
        """
        path = f'/api/hot/magnification/exportMagnificationData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_magnification_getChargeMagnifications(data):
        """
        获取加热充电倍率配置
        """
        path = f'/api/hot/magnification/getChargeMagnifications'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_magnification_getDischargeMagnifications(data):
        """
        获取加热放电倍率配置
        """
        path = f'/api/hot/magnification/getDischargeMagnifications'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_magnification_importChargeMagnifications(data):
        """
        导入加热充电倍率配置
        请求参数:
        """
        path = f'/api/hot/magnification/importChargeMagnifications'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_magnification_importDischargeMagnifications(data):
        """
        导入加热放倍率配置
        请求参数:
        """
        path = f'/api/hot/magnification/importDischargeMagnifications'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_ota_list(data):
        """
        加热机升级列表
        请求参数:
            hotNos: array [可选] - 充电机号
            upgradeType: integer [可选] - 升级类型 1:蓝牙 2：APP 3:TCU 4：CCU
        """
        path = f'/api/hot/ota/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_ota_upgrade(data):
        """
        加热机升级
        请求参数:
            fileId: integer [可选] - 文件id
            hotNos: array [可选] - 加热机号
            msgId: integer [可选]
            remark: string [可选] - 备注
            source: integer [可选]
            upgradeType: integer [可选] - 升级类型 1:蓝牙 2：APP 3:TCU 4：CCU
        """
        path = f'/api/hot/ota/upgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_queryDeviceParam(data):
        """
        加热机参数配置查询
        """
        path = f'/api/hot/queryDeviceParam'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_queryVersion(data):
        """
        查询版本
        """
        path = f'/api/hot/queryVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_record_detail(data):
        """
        记录详情
        请求参数:
            id: integer [可选]
        """
        path = f'/api/hot/record/detail'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_record_page(data):
        """
        记录分页列表
        请求参数:
            afterCreateTime: string [可选] - 结束创建时间
            afterStartTime: string [可选] - 结束开始时间
            beforeCreateTime: string [可选] - 开始创建时间
            beforeStartTime: string [可选] - 开始开始时间
            current: integer [可选]
            flowNo: string [可选] - 流水号
            position: integer [可选] - 仓位号
            requestId: string [可选]
            size: integer [可选]
            sn: string [可选] - sn
            startResult: integer [可选] - 启动结果
            status: integer [可选] - 状态
            stopType: integer [可选] - 停止类型
            timestamp: integer [可选]
        """
        path = f'/api/hot/record/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_settingChargeConfig(data):
        """
        设置加热机参数配置
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
        path = f'/api/hot/settingChargeConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_startHot(data):
        """
        启动加热
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
        path = f'/api/hot/startHot'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_stopHeatStrategy(data):
        """
        加热膜缓存删除
        请求参数:
            position: integer [可选]
        """
        path = f'/api/hot/stopHeatStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_hot_stoptHot(data):
        """
        停止加热
        请求参数:
            chargerNo: integer [可选]
        """
        path = f'/api/hot/stoptHot'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_light_getConfig(data):
        """
        getConfig
        """
        path = f'/api/light/getConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_light_saveConfig(data):
        """
        saveConfig
        请求参数:
            items: array [可选]
                        control: integer [可选] - 控制类型
                        endTime: string [可选] - 结束时间
                        startTime: string [可选] - 起始时间
            on: boolean [可选]
        """
        path = f'/api/light/saveConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_light_status(data):
        """
        status
        """
        path = f'/api/light/status'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_light_switchControl(data):
        """
        switchControl
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            equipActionType: integer [可选]
            lightCode: string [可选]
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/light/switchControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_login_currentLoginStatus(data):
        """
        当前IP是否存在用户登录
        """
        path = f'/api/login/currentLoginStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_login_currentUser(data):
        """
        获取当前用户
        请求参数:
            accessToken: string [可选]
        """
        path = f'/api/login/currentUser'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_login_getOauth2AppInfo(data):
        """
        获取Oauth2-app信息
        """
        path = f'/api/login/getOauth2AppInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_login_login(data):
        """
        登录
        请求参数:
            account: string [必填] - 手机号
            loginType: string [可选] - accountPwd-账密登录 phoneCaptcha-手机验证码登录 stationLogin-站控登录
            oauthCode: string [可选] - 授权码 oauthCode
            password: string [必填] - 密码
            phoneVerifyCode: string [可选] - 手机验证码
            verifyCode: string [必填] - 验证码
            verifyUniqueCode: string [必填] - 验证码唯一编号，最后一次【获取验证码】获取的verifyUniqueCode值
        """
        path = f'/api/login/login'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_login_logout(data):
        """
        用户登出
        请求参数:
            accessToken: string [可选]
        """
        path = f'/api/login/logout'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_login_removeAllAccessToken(data):
        """
        移除所有登录用户
        """
        path = f'/api/login/removeAllAccessToken'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_login_verifyCode(data):
        """
        获取验证码
        请求参数:
            loginType: string [可选] - accountPwd-账密登录 phoneCaptcha-手机验证码登录 stationLogin-站控登录
            phone: string [可选] - 手机号
        """
        path = f'/api/login/verifyCode'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_menu_add(data):
        """
        添加
        请求参数:
            icon: string [可选] - 菜单图标
            id: integer [可选]
            menuType: integer [必填] - 菜单类型 0-未知 1-菜单 2-按钮
            name: string [必填] - 菜单名字
            parentId: integer [必填] - 父级id
            permCoding: string [必填] - 菜单权限码
            remark: string [可选] - 备注
            routePath: string [可选] - 路由地址
            sortNo: integer [可选] - 排序
        """
        path = f'/api/menu/add'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_menu_del_id(id):
        """
        删除
        请求参数:
        """
        path = f'/api/menu/del/{id}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', None))

    @staticmethod
    def api_menu_edit(data):
        """
        编辑
        请求参数:
            icon: string [可选] - 菜单图标
            id: integer [可选]
            menuType: integer [必填] - 菜单类型 0-未知 1-菜单 2-按钮
            name: string [必填] - 菜单名字
            parentId: integer [必填] - 父级id
            permCoding: string [必填] - 菜单权限码
            remark: string [可选] - 备注
            routePath: string [可选] - 路由地址
            sortNo: integer [可选] - 排序
        """
        path = f'/api/menu/edit'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_menu_importFile(data):
        """
        导入Excel
        请求参数:
        """
        path = f'/api/menu/importFile'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_menu_tree(data):
        """
        分页查询信息
        """
        path = f'/api/menu/tree'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_menu_id(id):
        """
        通过ID查询
        请求参数:
        """
        path = f'/api/menu/{id}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_moduleConfig_controlInvasion(data):
        """
        活物入侵配置
        请求参数:
            invasionYn: string [可选] - 活物入侵开关 1：开启 0：关闭
        """
        path = f'/api/moduleConfig/controlInvasion'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_moduleConfig_getByType(data):
        """
        获取配置项
        请求参数:
            moduleConfigType: string [可选] - 模块配置类型
            moduleType: string [可选] - 模块类型
        """
        path = f'/api/moduleConfig/getByType'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_moduleConfig_getByTypeWithDefault(data):
        """
        获取配置项(带默认值获取)
        请求参数:
            moduleConfigType: string [可选] - 模块配置类型
            moduleType: string [可选] - 模块类型
        """
        path = f'/api/moduleConfig/getByTypeWithDefault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_moduleConfig_getFaultBatteryLowVersionsOn(data):
        """
        获取版本报警配置
        """
        path = f'/api/moduleConfig/getFaultBatteryLowVersionsOn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_moduleConfig_getNeedChargeConfig(data):
        """
        获取充电模型配置
        """
        path = f'/api/moduleConfig/getNeedChargeConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_moduleConfig_initDefault(data):
        """
        恢复默认配置
        请求参数:
            moduleConfigType: string [可选] - 模块配置类型
            moduleType: string [可选] - 模块类型
        """
        path = f'/api/moduleConfig/initDefault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_moduleConfig_saveOrUpdate(data):
        """
        保存或更新配置项
        请求参数:
            id: integer [可选] - id
            moduleConfigType: string [可选] - 模块配置类型
            moduleConfigVal: string [可选] - 模块配置值
            moduleType: string [可选] - 模块类型
            remark: string [可选]
            updateUser: integer [可选] - 更新人
            version: integer [可选] - 模块配置版本
        """
        path = f'/api/moduleConfig/saveOrUpdate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_moduleConfig_updateFaultBatteryLowVersionsOn(data):
        """
        更新版本报警配置
        请求参数:
            on: boolean [可选]
        """
        path = f'/api/moduleConfig/updateFaultBatteryLowVersionsOn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_moduleConfig_updateNeedChargeConfig(data):
        """
        更新充电模型配置
        请求参数:
            busyOrderNum: number [可选] - 全局配置 忙碌订单数阈值
            busySupplyDemand: number [可选] - 全局配置 忙碌时供需差阈值
            enableCampNos: array [可选] - 全局配置 仓位号
            idleSupplyDemand: number [可选] - 全局配置 空闲时供需差阈值
            maxTemp: number [可选] - 按需充电配置 模型边界最低温度
            minLimitChargeNum: number [可选] - 按需充电配置 最小充电时长，小于此值不进行降倍率限制
            minTemp: number [可选] - 按需充电配置 模型边界最低温度
            switchFlag: integer [可选] - 全局配置 开关
            timesOfSwap: number [可选] - 按需充电配置 单次换电时长（排队）
            timesOfSwapNonQueue: number [可选] - 按需充电配置 单次换电时长（非排队）
            vehicleQueueMinNum: integer [可选] - 排队兜底值
        """
        path = f'/api/moduleConfig/updateNeedChargeConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_msgBox_clearMsgBox(data):
        """
        clearMsgBox
        """
        path = f'/api/msgBox/clearMsgBox'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_msgBox_count():
        """
        selectCount
        """
        path = f'/api/msgBox/count'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_msgBox_list():
        """
        selectList
        """
        path = f'/api/msgBox/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_msgBox_page(data):
        """
        page
        请求参数:
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            id: integer [可选]
            ids: array [可选]
            msgCode: string [可选]
            msgContent: string [可选]
            msgFaultCodes: string [可选]
            msgResult: integer [可选]
            msgSource: string [可选]
            msgSourcePosition: integer [可选]
            msgTargetPosition: integer [可选]
            msgTime: string [可选]
            remark: string [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            userId: integer [可选]
        """
        path = f'/api/msgBox/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_msgBox_read(data):
        """
        read
        """
        path = f'/api/msgBox/read'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_newRfid_connect(data):
        """
        连接设备
        """
        path = f'/api/newRfid/connect'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_newRfid_disconnect(data):
        """
        断开设备
        """
        path = f'/api/newRfid/disconnect'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_newRfid_read(data):
        """
        读数据
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            pfk: string [可选] - 下控唯一标志
            readPower: integer [可选]
        """
        path = f'/api/newRfid/read'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_newRfid_write(data):
        """
        写入数据
        请求参数:
            data: string [必填] - 写入数据
            epcId: string [可选] - epc标签
        """
        path = f'/api/newRfid/write'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_optimumChargingMapping_currentMapping(data):
        """
        当前电池SN查询充电Mapping
        请求参数:
            id: string [可选]
        """
        path = f'/api/optimumChargingMapping/currentMapping'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_optimumChargingMapping_queryBySn(data):
        """
        通过电池SN查询充电Mapping
        请求参数:
        """
        path = f'/api/optimumChargingMapping/queryBySn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_ota_file_delete(data):
        """
        delete
        请求参数:
            id: integer [必填]
        """
        path = f'/api/ota/file/delete'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_ota_file_page(data):
        """
        page
        请求参数:
            current: integer [可选]
            fileName: string [可选]
            fileType: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            source: integer [可选]
            target: integer [可选]
            timestamp: integer [可选]
            type: integer [可选]
        """
        path = f'/api/ota/file/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_ota_file_query(data):
        """
        query
        请求参数:
            current: integer [可选]
            fileName: string [可选]
            fileType: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            source: integer [可选]
            target: integer [可选]
            timestamp: integer [可选]
            type: integer [可选]
        """
        path = f'/api/ota/file/query'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_ota_file_save(data):
        """
        save
        请求参数:
        """
        path = f'/api/ota/file/save'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_pickPackConfig_batchSaveOrUpdate(data):
        """
        批量保存
        请求参数:
            enableFlag: integer [可选]
            id: integer [可选]
            limitValue: number [可选]
            pickPackItem: string [可选]
        """
        path = f'/api/pickPackConfig/batchSaveOrUpdate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_pickPackConfig_initDefault(data):
        """
        恢复默认配置
        请求参数:
            pickPackConfType: integer [可选] - 选包配置类型 0-未知 1-初筛 2-海选 3-匹配
        """
        path = f'/api/pickPackConfig/initDefault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_pickPackConfig_list(data):
        """
        列表
        请求参数:
            pickPackConfType: integer [可选] - 选包配置类型 0-未知 1-初筛 2-海选 3-匹配
            pickPackItems: array [可选] - 选包维度条目类型集合
        """
        path = f'/api/pickPackConfig/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_powerModule_currentPower(data):
        """
        currentPower
        请求参数:
            ids: array [可选] - 箱变id
        """
        path = f'/api/powerModule/currentPower'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_powerModule_stopChargeByPower(data):
        """
        stopChargeByPower
        请求参数:
            stopPower: number [可选] - 功率超限值
        """
        path = f'/api/powerModule/stopChargeByPower'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_redis_delKey_key(key):
        """
        delKey
        请求参数:
        """
        path = f'/api/redis/delKey/{key}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'DELETE', None))

    @staticmethod
    def api_redis_getByKey_key(key):
        """
        getByKey
        请求参数:
        """
        path = f'/api/redis/getByKey/{key}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_redis_setKey(data):
        """
        setKey
        请求参数:
            expireTime: integer [可选]
            key: string [可选]
            value: string [可选]
        """
        path = f'/api/redis/setKey'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_role_add(data):
        """
        添加角色数据
        请求参数:
            id: integer [可选]
            menuIds: array [可选] - 角色资源
            name: string [必填] - 角色名
            roleCoding: string [必填] - 角色编码
            roleDesc: string [可选] - 角色描述
            sortNo: integer [可选] - 排序号码
        """
        path = f'/api/role/add'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_role_del_id(id):
        """
        删除角色数据
        请求参数:
        """
        path = f'/api/role/del/{id}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'DELETE', None))

    @staticmethod
    def api_role_edit(data):
        """
        编辑角色数据
        请求参数:
            id: integer [可选]
            menuIds: array [可选] - 角色资源
            name: string [必填] - 角色名
            roleCoding: string [必填] - 角色编码
            roleDesc: string [可选] - 角色描述
            sortNo: integer [可选] - 排序号码
        """
        path = f'/api/role/edit'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_role_list(data):
        """
        获取所有角色列表
        请求参数:
            current: integer [可选]
            name: string [可选] - 角色名字
            requestId: string [可选]
            roleCoding: string [可选] - 角色编码
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/role/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_role_page(data):
        """
        获取角色分页列表
        请求参数:
            current: integer [可选]
            name: string [必填] - 角色名字
            requestId: string [可选]
            roleCoding: string [必填] - 角色编码
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/role/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_role_id(id):
        """
        通过ID查询角色数据
        请求参数:
        """
        path = f'/api/role/{id}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_roleMenu_roleId(roleId):
        """
        获取角色权限树信息
        请求参数:
        """
        path = f'/api/roleMenu/{roleId}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_rollingDoor_control(data):
        """
        道闸控制
        请求参数:
            commandSubType: string [可选] - 下控子类型
            commandTypeVal: string [可选] - 下控类型数据 存储于缓存中
            curtainDoorControlAction: integer [可选] -  控制卷帘门动作 0：默认值 1：开启 2：关闭
            curtainDoorControlObject: integer [可选] -  控制卷帘门对象 0：默认值 1：入口卷帘门 2：出口卷帘门
            pfk: string [可选] - 下控唯一标志
        """
        path = f'/api/rollingDoor/control'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_rollingDoor_status(data):
        """
        获取道闸状态
        """
        path = f'/api/rollingDoor/status'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_rollingStrategy_getConfig(data):
        """
        获取卷帘门自动控制配置
        """
        path = f'/api/rollingStrategy/getConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_rollingStrategy_saveConfig(data):
        """
        保存卷帘门自动控制配置
        请求参数:
            items: array [可选]
                        endTime: string [可选] - 结束时间
                        startTime: string [可选] - 起始时间
                        waitTime: integer [可选] - 配置时间
            on: boolean [可选]
        """
        path = f'/api/rollingStrategy/saveConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_add(data):
        """
        add
        请求参数:
            author: string [可选]
            executorHandler: string [可选]
            remark: string [可选]
            scheduleConf: string [可选]
            scheduleType: integer [可选]
            taskName: string [可选]
        """
        path = f'/api/scheduleTask/add'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_del(data):
        """
        del
        请求参数:
            id: integer [可选]
        """
        path = f'/api/scheduleTask/del'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_exec(data):
        """
        exec
        """
        path = f'/api/scheduleTask/exec'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_executeHandler(data):
        """
        executeHandler
        请求参数:
            current: integer [可选]
            executorHandler: string [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/scheduleTask/executeHandler'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_getByExecutorHandler(data):
        """
        status
        请求参数:
            executorHandler: string [可选]
        """
        path = f'/api/scheduleTask/getByExecutorHandler'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_page(data):
        """
        page
        请求参数:
            author: string [可选]
            current: integer [可选]
            executorHandler: string [可选]
            requestId: string [可选]
            scheduleStatus: integer [可选]
            scheduleType: integer [可选]
            size: integer [可选]
            taskName: string [可选]
            timestamp: integer [可选]
        """
        path = f'/api/scheduleTask/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_update(data):
        """
        update
        请求参数:
            author: string [可选]
            executorHandler: string [可选]
            id: integer [可选]
            remark: string [可选]
            scheduleConf: string [可选]
            scheduleType: integer [可选]
            taskName: string [可选]
        """
        path = f'/api/scheduleTask/update'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_updateStatus(data):
        """
        updateStatus
        请求参数:
            id: integer [可选]
            scheduleStatus: integer [可选]
        """
        path = f'/api/scheduleTask/updateStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_scheduleTask_updateStatusByCode(data):
        """
        updateStatusByCode
        请求参数:
            execHandlerCode: string [可选]
            scheduleStatus: integer [可选]
        """
        path = f'/api/scheduleTask/updateStatusByCode'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_service_editor_stencilset():
        """
        getStencilset
        """
        path = f'/api/service/editor/stencilset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_service_model_modelId_json(modelId):
        """
        getEditorJson
        请求参数:
        """
        path = f'/api/service/model/{modelId}/json'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_service_model_modelId_save(modelId):
        """
        saveModel
        请求参数:
        """
        path = f'/api/service/model/{modelId}/save'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'PUT', None))

    @staticmethod
    def api_service_ping(data):
        """
        ping
        """
        path = f'/api/service/ping'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_snapshotFaultRecord_export(data):
        """
        导出故障快照
        请求参数:
            snapshotPfk: string [可选] - 快照唯一键
            snapshotType: string [可选] - 快照类型
        """
        path = f'/api/snapshotFaultRecord/export'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_statBatteryCamp_list(data):
        """
        仓位列表
        请求参数:
            bmsPackType: integer [可选] - 电池包类别 0-未安装 1-小包 2-打包 3-假包 255-BMS数据有误，字典：bmsPackType
            campDisableStatus: array [可选] - 仓位禁用状态 0-未禁用 1-禁充电 2-禁移仓
            campNo: integer [可选] - 仓位号
            chargeStatus: integer [可选] - 充电状态 1-未充电 2-充电中 字典：batteryChargingStatus
            endSoc: number [可选] - 结束soc
            fakePackFlag: integer [可选] - 假包状态 0-未知 1-真包 2-假包
            faultFlag: integer [可选] - 故障状态（字典：faultStatus）
            packDisableStatus: array [可选] - 电池禁用状态 0-未禁用 1-禁充电 2-禁换电
            packExistFlag: integer [可选] - 电池在位状态 0-默认 1-在位 2-不在位
            packMac: string [可选] - 电池mac
            packSn: string [可选] - 电池sn
            startSoc: number [可选] - 起始soc
        """
        path = f'/api/statBatteryCamp/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_statBatteryCamp_stationCampList(data):
        """
        换电站仓位列表
        """
        path = f'/api/statBatteryCamp/stationCampList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_statBatteryCamp_stationSupportPackTypes(data):
        """
        站型支持的电池包类型查询
        """
        path = f'/api/statBatteryCamp/stationSupportPackTypes'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_statEquipOtaRecord_page(data):
        """
        page
        请求参数:
            current: integer [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
            upgradeObject: integer [可选]
            upgradeType: integer [可选]
        """
        path = f'/api/statEquipOtaRecord/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_statEquipOtaRecordDetail_list(data):
        """
        list
        请求参数:
            recordId: integer [可选]
        """
        path = f'/api/statEquipOtaRecordDetail/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_changeStationGuardFlag(data):
        """
        切换值守状态
        请求参数:
            stationGuardFlag: integer [必填]
        """
        path = f'/api/station/changeStationGuardFlag'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_changeStationLang(data):
        """
        切换站语言类型
        请求参数:
            stationLang: string [可选]
        """
        path = f'/api/station/changeStationLang'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_changeSwapTiming(data):
        """
        切换计时器类型
        请求参数:
            timingConfig: string [可选]
        """
        path = f'/api/station/changeSwapTiming'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_detailList(data):
        """
        detailList
        请求参数:
            address: string [可选]
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            guardFlag: integer [可选]
            id: integer [可选]
            ids: array [可选]
            latitude: string [可选]
            leader: string [可选]
            leaderPhone: string [可选]
            longitude: string [可选]
            name: string [可选]
            optEndTime: string [可选]
            optStartTime: string [可选]
            remark: string [可选]
            requestId: string [可选]
            size: integer [可选]
            stationCoding: string [可选]
            stationEnv: integer [可选]
            stationStatus: integer [可选]
            stationType: string [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            version: string [可选]
        """
        path = f'/api/station/detailList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_info(data):
        """
        基本信息
        """
        path = f'/api/station/info'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_initStation(data):
        """
        落站初始化
        请求参数:
            pickPackConfig: array [可选]
                        enableFlag: integer [可选]
                        id: integer [可选]
                        limitValue: number [可选]
                        pickPackItem: string [可选]
            stationRegion: integer [可选] - 区域版本类型
        """
        path = f'/api/station/initStation'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_stationMaintenanceStatusChange(data):
        """
        站控运维状态切换
        请求参数:
            changeReason: string [可选]
            changeReasonCode: integer [可选]
            displayStatus: integer [可选]
            maintenanceStatus: integer [可选]
            permitBatterySwap: integer [可选]
            planStationStatus: integer [可选]
            sourceForm: integer [可选]
        """
        path = f'/api/station/stationMaintenanceStatusChange'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_stationWorkStatus(data):
        """
        站状态及云环境信息
        """
        path = f'/api/station/stationWorkStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_station_versionInfo(data):
        """
        换电站版本信息
        """
        path = f'/api/station/versionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_storedEnergy_baseInfo(data):
        """
        储能设备基本信息获取
        请求参数:
            deviceId: string [可选] - 根据设备ID获取设备信息  ，优先使用设备ID条件查询
            ip: string [可选] - 根据IP获取设备信息
            type: string [可选] - 查询方式，emu 从EMU本地缓存查询，dev 发送命令给储能设备进行查询
        """
        path = f'/api/storedEnergy/baseInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_batchExport(data):
        """
        batchExport
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
            createEndTime: string [可选]
            createStartTime: string [可选]
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            failReason: string [可选]
            failReasonType: integer [可选]
            failTypes: array [可选]
            flowCreateType: integer [可选]
            flowNo: string [可选]
            flowStatus: integer [可选]
            flowType: integer [可选]
            guardFlag: integer [可选]
            id: integer [可选]
            ids: array [可选]
            manualFlag: integer [可选]
            mbmuHardwareVersion: string [可选]
            mbmuSoftwareVersion: string [可选]
            procInstId: string [可选]
            remark: string [可选]
            requestId: string [可选]
            selectPackageType: integer [可选]
            size: integer [可选]
            swapEndTime: string [可选]
            swapStartTime: string [可选]
            swapStep: integer [可选]
            sysSubTotalChargeTimesOutStation: integer [可选]
            sysSubTotalRechargeTimesOutStation: integer [可选]
            testBatch: string [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            uploadFlag: integer [可选]
            uploadTime: string [可选]
            userPhone: string [可选]
            vbleHardwareVersion: string [可选]
            vbleSoftwareVersion: string [可选]
            vehTotalOdometer: string [可选]
        """
        path = f'/api/swapFlow/batchExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_batchUpload(data):
        """
        batchUpload
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
        path = f'/api/swapFlow/batchUpload'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_detail(data):
        """
        detail
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
            createEndTime: string [可选]
            createStartTime: string [可选]
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            failReason: string [可选]
            failReasonType: integer [可选]
            failTypes: array [可选]
            flowCreateType: integer [可选]
            flowNo: string [可选]
            flowStatus: integer [可选]
            flowType: integer [可选]
            guardFlag: integer [可选]
            id: integer [可选]
            ids: array [可选]
            manualFlag: integer [可选]
            mbmuHardwareVersion: string [可选]
            mbmuSoftwareVersion: string [可选]
            procInstId: string [可选]
            remark: string [可选]
            requestId: string [可选]
            selectPackageType: integer [可选]
            size: integer [可选]
            swapEndTime: string [可选]
            swapStartTime: string [可选]
            swapStep: integer [可选]
            sysSubTotalChargeTimesOutStation: integer [可选]
            sysSubTotalRechargeTimesOutStation: integer [可选]
            testBatch: string [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            uploadFlag: integer [可选]
            uploadTime: string [可选]
            userPhone: string [可选]
            vbleHardwareVersion: string [可选]
            vbleSoftwareVersion: string [可选]
            vehTotalOdometer: string [可选]
        """
        path = f'/api/swapFlow/detail'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_manualSave(data):
        """
        手动创建订单
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
        path = f'/api/swapFlow/manualSave'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_page(data):
        """
        page
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
            createEndTime: string [可选]
            createStartTime: string [可选]
            createTime: string [可选]
            createUser: integer [可选]
            current: integer [可选]
            dataStatus: integer [可选]
            failReason: string [可选]
            failReasonType: integer [可选]
            failTypes: array [可选]
            flowCreateType: integer [可选]
            flowNo: string [可选]
            flowStatus: integer [可选]
            flowType: integer [可选]
            guardFlag: integer [可选]
            id: integer [可选]
            ids: array [可选]
            manualFlag: integer [可选]
            mbmuHardwareVersion: string [可选]
            mbmuSoftwareVersion: string [可选]
            procInstId: string [可选]
            remark: string [可选]
            requestId: string [可选]
            selectPackageType: integer [可选]
            size: integer [可选]
            swapEndTime: string [可选]
            swapStartTime: string [可选]
            swapStep: integer [可选]
            sysSubTotalChargeTimesOutStation: integer [可选]
            sysSubTotalRechargeTimesOutStation: integer [可选]
            testBatch: string [可选]
            timestamp: integer [可选]
            updateTime: string [可选]
            updateUser: integer [可选]
            uploadFlag: integer [可选]
            uploadTime: string [可选]
            userPhone: string [可选]
            vbleHardwareVersion: string [可选]
            vbleSoftwareVersion: string [可选]
            vehTotalOdometer: string [可选]
        """
        path = f'/api/swapFlow/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlow_updateRemark(data):
        """
        updateRemark
        请求参数:
            id: integer [可选] - 换电记录id
            remark: string [可选] - 备注
        """
        path = f'/api/swapFlow/updateRemark'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowConfig_initDefault(data):
        """
        initDefault
        """
        path = f'/api/swapFlowConfig/initDefault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowConfig_save(data):
        """
        save
        请求参数:
            id: integer [可选]
            validPackMacFlag: integer [可选]
            validPackSnFlag: integer [可选]
            validPackTypeFlag: integer [可选]
            validVbleMacFlag: integer [可选]
        """
        path = f'/api/swapFlowConfig/save'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowConfig_validParams(data):
        """
        validParams
        """
        path = f'/api/swapFlowConfig/validParams'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowFailReason_getByOrderId(data):
        """
        getByOrderId
        请求参数:
            flowNo: string [可选]
        """
        path = f'/api/swapFlowFailReason/getByOrderId'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowPackLock_page(data):
        """
        page
        请求参数:
            current: integer [可选]
            flowNo: string [可选]
            requestId: string [可选]
            size: integer [可选]
            timestamp: integer [可选]
        """
        path = f'/api/swapFlowPackLock/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_allPacks(data):
        """
        手动选包 -> 获取所有电池包
        请求参数:
            carModel: string [可选] - 车型代码
            selectPackType: integer [可选] - 换电电池包类型 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
        """
        path = f'/api/swapFlowTask/allPacks'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_cameraSendCarNo(data):
        """
        模拟上报车牌号
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
        path = f'/api/swapFlowTask/cameraSendCarNo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_carSignInfo():
        """
        carSignInfo
        """
        path = f'/api/swapFlowTask/carSignInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlowTask_clipPlayerOpenYn(data):
        """
        背景音乐播放开关
        """
        path = f'/api/swapFlowTask/clipPlayerOpenYn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_closeHVContactor(data):
        """
        触发下高压
        """
        path = f'/api/swapFlowTask/closeHVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_closeLVContactor(data):
        """
        触发下低压
        """
        path = f'/api/swapFlowTask/closeLVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_continueCarStopHandle(data):
        """
        跳过车辆朝向
        """
        path = f'/api/swapFlowTask/continueCarStopHandle'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_continuePressCentering(data):
        """
        跳过车辆压归中
        """
        path = f'/api/swapFlowTask/continuePressCentering'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_forceStopSwapFlow(data):
        """
        强制结束换电流程
        请求参数:
            forceEndReason: string [可选]
        """
        path = f'/api/swapFlowTask/forceStopSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getBtInfo():
        """
        获取蓝牙信息
        """
        path = f'/api/swapFlowTask/getBtInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlowTask_getCloudCarModel(data):
        """
        获取云端车型代号
        请求参数:
            carNo: string [可选]
        """
        path = f'/api/swapFlowTask/getCloudCarModel'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getCloudPhone(data):
        """
        获取云端手机号
        请求参数:
            carNo: string [可选]
        """
        path = f'/api/swapFlowTask/getCloudPhone'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getCloudSwapInfoByCarNo(data):
        """
        通过车牌号获取车辆信息
        请求参数:
            carNo: string [可选]
        """
        path = f'/api/swapFlowTask/getCloudSwapInfoByCarNo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getGateInfo(data):
        """
        获取道闸信息
        """
        path = f'/api/swapFlowTask/getGateInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getLatestBluetoothScanNum(data):
        """
        getLatestBluetoothScanNum
        """
        path = f'/api/swapFlowTask/getLatestBluetoothScanNum'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getLatestConnectInfo(data):
        """
        获取最新蓝牙连接信息
        """
        path = f'/api/swapFlowTask/getLatestConnectInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getManualSwapData(data):
        """
        手动换电数据
        """
        path = f'/api/swapFlowTask/getManualSwapData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_getSkipFreedomConfig():
        """
        getSkipFreedomConfig
        """
        path = f'/api/swapFlowTask/getSkipFreedomConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlowTask_getVerifyVehicleInfo():
        """
        车机必填校验项
        """
        path = f'/api/swapFlowTask/getVerifyVehicleInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlowTask_hasSwapTask():
        """
        是否在换电
        """
        path = f'/api/swapFlowTask/hasSwapTask'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlowTask_installFakePackConfig(data):
        """
        手动选包 -> 获取安装假包配置
        请求参数:
            realPackNum: integer [可选] - 真包数量
        """
        path = f'/api/swapFlowTask/installFakePackConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_judgePressureSwapFlow(data):
        """
        压测流程开启条件判断
        """
        path = f'/api/swapFlowTask/judgePressureSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualAllowReturnVehicle(data):
        """
        手动PLC设备归位
        """
        path = f'/api/swapFlowTask/manualAllowReturnVehicle'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualBreakBatteryBt(data):
        """
        手动断电池蓝牙
        请求参数:
            batteryMac1: string [可选]
            batteryMac2: string [可选]
        """
        path = f'/api/swapFlowTask/manualBreakBatteryBt'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualCapture():
        """
        重新触发抓拍机
        """
        path = f'/api/swapFlowTask/manualCapture'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_swapFlowTask_manualConnectBt(data):
        """
        重新连接蓝牙
        """
        path = f'/api/swapFlowTask/manualConnectBt'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualHv(data):
        """
        手动高压下电
        """
        path = f'/api/swapFlowTask/manualHv'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualLv(data):
        """
        手动低压下电
        """
        path = f'/api/swapFlowTask/manualLv'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualPickPack(data):
        """
        手动选包 -> 确认手动选包
        请求参数:
            activitiId: string [可选] - 任务节点来源
            preInstallPack1CampNo: integer [可选] - 预安装包1仓位号
            preInstallPack2CampNo: integer [可选] - 预安装包2仓位号
            realPackNum: integer [可选] - 选择真包数量
            selectPackType: integer [可选] - 用户选择的换电电池包类型 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
        """
        path = f'/api/swapFlowTask/manualPickPack'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualRoadSwitch(data):
        """
        道闸控制
        请求参数:
            roadStatus: integer [可选] - 道闸状态 0：-；1：开闸；2：闭闸
            roadType: integer [可选] - 道闸类型 1：入口道闸；2：出口道闸
        """
        path = f'/api/swapFlowTask/manualRoadSwitch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualSendAllowVehicleEnter(data):
        """
        重新请求车辆进入换电站
        """
        path = f'/api/swapFlowTask/manualSendAllowVehicleEnter'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualSendBluetoothStatus(data):
        """
        蓝牙控制
        请求参数:
            disconnectType: integer [可选] - 1:全自动 2：半自动 3：标定 4:压测
            mbmuIrk: string [可选] - irk
            oob: string [可选] - oob
            type: string [可选] - 1:连接； 2：断开
            vbleMac: string [可选] - 蓝牙地址
        """
        path = f'/api/swapFlowTask/manualSendBluetoothStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualSendCarInfoAndCheckSelf(data):
        """
        手动换电发送车机信息并自检
        请求参数:
            batteryMac1: string [可选]
            batteryMac2: string [可选]
            batteryNum: integer [可选]
            batteryStatus1: integer [可选]
            batteryStatus2: integer [可选]
            vbleMac: string [可选]
        """
        path = f'/api/swapFlowTask/manualSendCarInfoAndCheckSelf'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_manualVehicleLeave(data):
        """
        手动车辆驶离
        """
        path = f'/api/swapFlowTask/manualVehicleLeave'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_matchPacks(data):
        """
        matchPacks
        请求参数:
            campNo: integer [可选] - 匹配电池包的仓位号
            selectPackType: integer [可选] - 用户租赁的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
        """
        path = f'/api/swapFlowTask/matchPacks'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_offLineSwapFlow(data):
        """
        离线换电
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
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_originPackBack(data):
        """
        原包重连
        """
        path = f'/api/swapFlowTask/originPackBack'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_pickBatteryFailLog(data):
        """
        pickBatteryFailLog
        请求参数:
            flowNo: string [必填]
        """
        path = f'/api/swapFlowTask/pickBatteryFailLog'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_pressureHv(data):
        """
        压测高压下电
        """
        path = f'/api/swapFlowTask/pressureHv'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_pressureLv(data):
        """
        压测低压下电
        """
        path = f'/api/swapFlowTask/pressureLv'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_pressureTestProcessInfo(data):
        """
        获取压测流程信息
        """
        path = f'/api/swapFlowTask/pressureTestProcessInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reRequestCloudAuth(data):
        """
        重新请求认证
        """
        path = f'/api/swapFlowTask/reRequestCloudAuth'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendCenteringLift(data):
        """
        重新下发plc归中举升
        """
        path = f'/api/swapFlowTask/reSendCenteringLift'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendChannelRecover(data):
        """
        重发换电通道设备回位
        """
        path = f'/api/swapFlowTask/reSendChannelRecover'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendEnableHV(data):
        """
        重发允许上高压
        """
        path = f'/api/swapFlowTask/reSendEnableHV'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendPlcStartSwap(data):
        """
        重新下发plc开始换电
        """
        path = f'/api/swapFlowTask/reSendPlcStartSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reSendPreInstallPackInfo(data):
        """
        重发下发拆电池
        """
        path = f'/api/swapFlowTask/reSendPreInstallPackInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_receivedVehicleBack(data):
        """
        触发车辆回位
        """
        path = f'/api/swapFlowTask/receivedVehicleBack'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_receivedVehicleLeave(data):
        """
        触发车辆驶离
        """
        path = f'/api/swapFlowTask/receivedVehicleLeave'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_reportManualOrder(data):
        """
        上报手动订单数据
        """
        path = f'/api/swapFlowTask/reportManualOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_saveCampBatteryAndDisconnect(data):
        """
        保存手动待安装电池数据
        请求参数:
            campNo: integer [可选]
            packNo: integer [可选]
        """
        path = f'/api/swapFlowTask/saveCampBatteryAndDisconnect'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_saveManualFillInOrder(data):
        """
        保存手动填写订单信息
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
        path = f'/api/swapFlowTask/saveManualFillInOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_saveManualInstallBattery(data):
        """
        保存手动待拆卸电池数据
        """
        path = f'/api/swapFlowTask/saveManualInstallBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_scanBtControl(data):
        """
        scanBtControl
        请求参数:
            type: string [可选] - 1:扫描； 2：断开
        """
        path = f'/api/swapFlowTask/scanBtControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_scanBtStatus(data):
        """
        scanBtStatus
        """
        path = f'/api/swapFlowTask/scanBtStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_selfCheck(data):
        """
        触发自检
        """
        path = f'/api/swapFlowTask/selfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_sendSbleEnableHVContactor(data):
        """
        sendSbleEnableHVContactor
        """
        path = f'/api/swapFlowTask/sendSbleEnableHVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_setCarModel(data):
        """
        设置车型代号
        请求参数:
            carModel: string [必填]
            carNo: string [必填]
        """
        path = f'/api/swapFlowTask/setCarModel'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_setPressureTestOrderInfo(data):
        """
        设置压测流程信息
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
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_setSkipFreedomConfig(data):
        """
        setSkipFreedomConfig
        请求参数:
        """
        path = f'/api/swapFlowTask/setSkipFreedomConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_skipCheck(data):
        """
        跳过当前换电步序
        请求参数:
            activitiId: string [可选] - 任务节点来源
        """
        path = f'/api/swapFlowTask/skipCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_skipCloudStartSwap(data):
        """
        跳过云端下发换电指令
        请求参数:
            batteryNum: integer [必填]
            phone: string [必填]
            selectPackType: integer [可选] - 用户租赁的电池包类别 1-C1N-53-264 2-C1N-70-274 3-假包 4-C3F-56-632
        """
        path = f'/api/swapFlowTask/skipCloudStartSwap'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_skipToPickPacks(data):
        """
        手动选包 -> 流程跳转
        """
        path = f'/api/swapFlowTask/skipToPickPacks'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_startPressureSwapFlow(data):
        """
        压测流程开启
        """
        path = f'/api/swapFlowTask/startPressureSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_stopPressureSwapFlow(data):
        """
        压测流程结束
        """
        path = f'/api/swapFlowTask/stopPressureSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowTask_stopSwapFlow(data):
        """
        结束换电流程
        请求参数:
            forceEndReason: string [可选]
        """
        path = f'/api/swapFlowTask/stopSwapFlow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowVehicleInfo_getByFlowNo(data):
        """
        通过流水号获取车辆信息
        请求参数:
            flowNo: string [可选] - 流水号
        """
        path = f'/api/swapFlowVehicleInfo/getByFlowNo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_swapFlowVehicleLabel_getByOrderId(data):
        """
        getByOrderId
        请求参数:
            flowNo: string [可选]
        """
        path = f'/api/swapFlowVehicleLabel/getByOrderId'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_timeDemandConfig_currentConfig(data):
        """
        获取运营配置
        """
        path = f'/api/timeDemandConfig/currentConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_timeDemandConfig_saveConfig(data):
        """
        保存运营配置
        请求参数:
            campChargeConfigList: array [可选] - 仓位充电策略
                        activeCampNos: array [可选] - 生效仓位集合
                        campChargeConfigItems: array [可选] - 充电时间区间策略
                                    endTime: string [可选] - 结束时间
                                    instructionType: integer [可选] - 指令类型 1-自适应 2-功率调节 3-电流比列调节 4-电流调节
                                    instructionTypeLimitVal: number [可选] - 指令类型对应限制值
                                    startChargeSoc: number [可选] - 开始充电soc值
                                    startTime: string [可选] - 起始时间
                                    stopChargeSoc: number [可选] - 停止充电soc值
                                    supportChargeTempLimit: number [可选] - 允许充电温度上限
                        strategyNo: integer [可选] - 策略序号
            socAndPackNumConfigList: array [可选] - SOC与电池个数时间需求配置
                        createTime: string [可选] - 创建时间
                        createUser: integer [可选] - 创建用户id
                        endTime: string [可选] - 结束时间
                        id: integer [可选] - id
                        packDemandCount: integer [可选] - 电池需求数量
                        socLimit: number [可选] - 限制soc值
                        startTime: string [可选] - 起始时间
                        updateTime: string [可选] - 更新时间
                        updateUser: integer [可选] - 更新人
            stationChargeConfigList: array [可选] - 整站充电策略
                        endTime: string [可选] - 结束时间
                        instructionType: integer [可选] - 指令类型 1-自适应 2-功率调节 3-电流比列调节 4-电流调节
                        instructionTypeLimitVal: number [可选] - 指令类型对应限制值
                        startChargeSoc: number [可选] - 开始充电soc值
                        startTime: string [可选] - 起始时间
                        stopChargeSoc: number [可选] - 停止充电soc值
                        supportChargeTempLimit: number [可选] - 允许充电温度上限
        """
        path = f'/api/timeDemandConfig/saveConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_timeDemandFanConfig_batchSave(data):
        """
        batchSave
        请求参数:
            endTime: string [可选]
            startTime: string [可选]
            switchStatus: integer [可选]
        """
        path = f'/api/timeDemandFanConfig/batchSave'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_timeDemandFanConfig_initDefault(data):
        """
        initDefault
        """
        path = f'/api/timeDemandFanConfig/initDefault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_timeDemandFanConfig_list(data):
        """
        list
        """
        path = f'/api/timeDemandFanConfig/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_tools_convertAscFileAndExportNew(data):
        """
        convertAscFileAndExportNew
        请求参数:
        """
        path = f'/api/tools/convertAscFileAndExportNew'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_tools_decode2Json(data):
        """
        decode2Json
        请求参数:
            data: string [可选]
            key: string [可选]
        """
        path = f'/api/tools/decode2Json'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_tools_sbleSoftRestart(data):
        """
        sbleSoftRestart
        """
        path = f'/api/tools/sbleSoftRestart'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_tools_test(data):
        """
        test
        请求参数:
            id: string [可选]
        """
        path = f'/api/tools/test'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_tools_test1(data):
        """
        test1
        请求参数:
            id: string [可选]
        """
        path = f'/api/tools/test1'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_tools_test2(data):
        """
        test2
        请求参数:
            id: string [可选]
        """
        path = f'/api/tools/test2'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_userActionLog_get(data):
        """
        操作记录详情
        请求参数:
            id: integer [可选]
        """
        path = f'/api/userActionLog/get'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_userActionLog_page(data):
        """
        分页列表查询
        请求参数:
            actionEvent: string [可选] - 操作功能
            createUser: string [可选] - 操作人
            current: integer [可选]
            endTime: string [可选] - 结束时间
            requestId: string [可选]
            size: integer [可选]
            startTime: string [可选] - 起始时间
            timestamp: integer [可选]
        """
        path = f'/api/userActionLog/page'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_volumeTimeControlConfig_defaultVolumeTime(data):
        """
        led音量恢复默认
        """
        path = f'/api/volumeTimeControlConfig/defaultVolumeTime'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_volumeTimeControlConfig_list(data):
        """
        音量列表
        """
        path = f'/api/volumeTimeControlConfig/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_volumeTimeControlConfig_listenComputer(data):
        """
        通道试听
        请求参数:
            volume: string [可选] - 音量
        """
        path = f'/api/volumeTimeControlConfig/listenComputer'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_volumeTimeControlConfig_listenLed(data):
        """
        led试听
        请求参数:
            volume: string [可选] - 音量
        """
        path = f'/api/volumeTimeControlConfig/listenLed'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_volumeTimeControlConfig_save(data):
        """
        音量保存
        请求参数:
            endTime: string [可选] - 结束时间
            id: integer [可选] - id
            ledVolume: string [可选] - led音量大小
            startTime: string [可选] - 起始时间
            volume: string [可选] - 音量大小
        """
        path = f'/api/volumeTimeControlConfig/save'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryExchange(data):
        """
        电池交换（二代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/batteryExchange'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryMACConnect(data):
        """
        电池蓝牙连接（一代）
        请求参数:
            mac: string [必填]
            sourcePosition: integer [可选]
        """
        path = f'/api/waveHouse/batteryMACConnect'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryMACDisconnect(data):
        """
        电池蓝牙断开（一代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/batteryMACDisconnect'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryMaintenanceIn(data):
        """
        电池维护转入（一代）
        """
        path = f'/api/waveHouse/batteryMaintenanceIn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryMaintenanceOut(data):
        """
        电池维护转出（一代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/batteryMaintenanceOut'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryOneClickIn(data):
        """
        电池一键入仓rgv转入（一代）
        """
        path = f'/api/waveHouse/batteryOneClickIn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryOneClickInRgvOut(data):
        """
        电池一键入仓转出（一代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/batteryOneClickInRgvOut'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryOneClickOut(data):
        """
        电池一键出仓转出（一代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/batteryOneClickOut'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryOneClickOutRgvIn(data):
        """
        电池一键出仓rgv转入（一代）
        """
        path = f'/api/waveHouse/batteryOneClickOutRgvIn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_batteryTransfer(data):
        """
        库内转移（一代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/batteryTransfer'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_campExecuteReset(data):
        """
        仓位操作复位（一代）
        请求参数:
            packType: integer [可选] - 电池包类型 
            sourcePosition: integer [可选]
            sourceType: string [必填]
        """
        path = f'/api/waveHouse/campExecuteReset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_delSoftWareRedis(data):
        """
        删除软件任务（测试）
        """
        path = f'/api/waveHouse/delSoftWareRedis'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_delWareHouseStatus(data):
        """
        删除消息盒子（测试）
        """
        path = f'/api/waveHouse/delWareHouseStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_fireControlMoving(data):
        """
        消防移仓
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/fireControlMoving'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_fireMoveInWarehouse(data):
        """
        消防机构空载驶入（二代）
        """
        path = f'/api/waveHouse/fireMoveInWarehouse'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_fireOneClickIn(data):
        """
        消防机构一键入仓（二代）
        请求参数:
            packType: integer [可选]
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/fireOneClickIn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_fireOneClickOut(data):
        """
        消防机构一键出仓（二代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/fireOneClickOut'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_fireOutOfWarehouse(data):
        """
        消防机构空载驶出（二代）
        """
        path = f'/api/waveHouse/fireOutOfWarehouse'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_lastFireMovePosition(data):
        """
        获取上次消防移仓仓位号
        """
        path = f'/api/waveHouse/lastFireMovePosition'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_oneClickIn(data):
        """
        一键入仓（二代）
        请求参数:
            packType: integer [可选]
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/oneClickIn'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_oneClickOut(data):
        """
        一键出仓（二代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/oneClickOut'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_plcSelfCheck(data):
        """
        plc设备自检
        """
        path = f'/api/waveHouse/plcSelfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_positionDressing(data):
        """
        仓位筛选列表（二代）
        请求参数:
            packType: integer [可选] - 电池包类型 
            sourcePosition: integer [可选]
            sourceType: string [必填]
        """
        path = f'/api/waveHouse/positionDressing'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_positionList(data):
        """
        仓位筛选列表（一代）
        请求参数:
            packType: integer [可选] - 电池包类型 
            sourcePosition: integer [可选]
            sourceType: string [必填]
        """
        path = f'/api/waveHouse/positionList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_rgvMoveInWarehouse(data):
        """
        rgv驶入（二代）
        """
        path = f'/api/waveHouse/rgvMoveInWarehouse'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_rgvOutOfWarehouse(data):
        """
        rgv驶出（二代）
        """
        path = f'/api/waveHouse/rgvOutOfWarehouse'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_screenReStart(data):
        """
        触摸屏重启
        """
        path = f'/api/waveHouse/screenReStart'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_stopFireMove(data):
        """
        停止消防移仓
        请求参数:
            position: integer [可选]
        """
        path = f'/api/waveHouse/stopFireMove'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_testFireControlMoving(data):
        """
        测试消防移仓
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/testFireControlMoving'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_transferInWarehouse(data):
        """
        库内转移（二代）
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/transferInWarehouse'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_waveHouse_warehouseCheck(data):
        """
        仓位选择校验
        请求参数:
            sourcePosition: integer [可选]
            sourcePositionType: integer [可选]
            sourceType: string [可选]
            targetPosition: integer [可选]
            targetPositionType: integer [可选]
        """
        path = f'/api/waveHouse/warehouseCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_wavyEnergyConfig_getChargeInfo():
        """
        获取充电机尖峰平谷同步结果
        """
        path = f'/api/wavyEnergyConfig/getChargeInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_wavyEnergyConfig_list():
        """
        尖峰平谷列表
        """
        path = f'/api/wavyEnergyConfig/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def api_wavyEnergyConfig_restoreWavyEnergy(data):
        """
        尖峰平谷恢复默认配置
        """
        path = f'/api/wavyEnergyConfig/restoreWavyEnergy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_wavyEnergyConfig_saveWavyEnergy(data):
        """
        尖峰平谷配置保存
        请求参数:
            endTime: string [可选] - 结束时间
            id: integer [可选] - id
            startTime: string [可选] - 起始时间
            wavyType: integer [可选] - 尖峰平谷类型 0-未知 1-尖值 2-峰值 3-平值 4-谷值
        """
        path = f'/api/wavyEnergyConfig/saveWavyEnergy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def api_wavyEnergyConfig_syncWavyEnergy(data):
        """
        单个充电机尖峰平谷同步
        请求参数:
            chargeNo: integer [可选] - chargeNo
        """
        path = f'/api/wavyEnergyConfig/syncWavyEnergy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))
