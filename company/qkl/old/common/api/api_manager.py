from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiManager:
    @staticmethod
    def _get_path(path):
        service = '/manager'
        return service + path

    @staticmethod
    def ad_file_id(id):
        """
        删除广告文件
        请求参数:
        """
        path = f'/ad/file/{id}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'DELETE', None))

    @staticmethod
    def ad_getAllAdFiles():
        """
        获取所有广告文件
        """
        path = f'/ad/getAllAdFiles'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def ad_getConfig():
        """
        获取广告配置
        """
        path = f'/ad/getConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def ad_saveConfig(data):
        """
        保存广告配置
        请求参数:
            open: boolean [可选]
        """
        path = f'/ad/saveConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def ad_saveFile(data):
        """
        保存广告文件配置
        请求参数:
        """
        path = f'/ad/saveFile'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def airParamData_airOperationSendCloud():
        """
        空调信息上报（测试）
        请求参数:
            address: integer [可选]
            command: integer [可选]
            executeTime: string [可选]
            humidity: number [可选]
            isRemote: integer [可选]
            switchFlag: boolean [可选]
            temperature: number [可选]
        """
        path = f'/airParamData/airOperationSendCloud'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def airParamData_controlInternalFanStatus():
        """
        内风机开启策略（定时任务）
        """
        path = f'/airParamData/controlInternalFanStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def airParamData_getAirParamData():
        """
        获取空调传感器数据信息
        """
        path = f'/airParamData/getAirParamData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def airParamData_getAlarmDataInfo():
        """
        获取空调报警数据
        请求参数:
        """
        path = f'/airParamData/getAlarmDataInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def airParamData_getSensorDataInfo():
        """
        获取传感器数据
        请求参数:
        """
        path = f'/airParamData/getSensorDataInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def airParamData_getStatusDataCloud():
        """
        获取空调状态信息
        """
        path = f'/airParamData/getStatusDataCloud'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def airParamData_getStatusDataInfo():
        """
        获取空调状态数据
        请求参数:
        """
        path = f'/airParamData/getStatusDataInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def airParamData_getSystemDataInfo():
        """
        获取空调系统数据
        """
        path = f'/airParamData/getSystemDataInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def airParamData_setAir(data):
        """
        设置空调数据
        请求参数:
            address: integer [可选]
            command: integer [可选]
            executeTime: string [可选]
            humidity: number [可选]
            isRemote: integer [可选]
            switchFlag: boolean [可选]
            temperature: number [可选]
        """
        path = f'/airParamData/setAir'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def airParamData_setHeatingTemperature(data):
        """
        设置空调数据（测试）
        请求参数:
            address: integer [可选]
            command: integer [可选]
            executeTime: string [可选]
            humidity: number [可选]
            isRemote: integer [可选]
            switchFlag: boolean [可选]
            temperature: number [可选]
        """
        path = f'/airParamData/setHeatingTemperature'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def auth_login(data):
        """
        用户登录
        请求参数:
            code: string [可选]
            kid: string [可选]
            password: string [必填] - 用户密码
            username: string [必填] - 用户名
        """
        path = f'/auth/login'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def auth_logout(data):
        """
        用户登出
        请求参数:
        """
        path = f'/auth/logout'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def auth_test(data):
        """
        test
        请求参数:
            cnName: string [可选]
            createTime: string [可选]
            id: integer [可选]
            oldPassword: string [可选]
            password: string [可选]
            password2: string [可选]
            passwordValidityPeriod: integer [可选]
            promptTime: integer [可选]
            roleId: integer [可选]
            roleName: string [可选]
            roles: array [可选]
                        createTime: string [可选]
                        id: integer [可选]
                        permissionIds: string [可选]
                        permissions: array [可选]
                                    allowModify: integer [可选]
                                    createTime: string [可选]
                                    id: integer [可选]
                                    permission: string [可选]
                                    permissionCode: string [可选]
                                    permissionName: string [可选]
                                    updateTime: string [可选]
                        roleDescribe: string [可选]
                        roleName: string [可选]
                        updateTime: string [可选]
            salt: string [可选]
            telphoneNum: string [可选]
            updateTime: string [可选]
            userStatus: integer [可选]
            username: string [可选]
        """
        path = f'/auth/test'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def autoControlRollingShutterDoor_getConfig():
        """
        获取卷帘门自动控制配置
        """
        path = f'/autoControlRollingShutterDoor/getConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def autoControlRollingShutterDoor_saveConfig(data):
        """
        保存卷帘门自动控制配置
        请求参数:
            data: array [可选]
                        endTime: string [可选] - 结束时间
                        id: integer [可选] - id
                        startTime: string [可选] - 起始时间
                        waitTime: integer [可选] - 配置时间
            open: boolean [可选]
        """
        path = f'/autoControlRollingShutterDoor/saveConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryManager_batteryCabinet():
        """
        电池标定出柜
        请求参数:
        """
        path = f'/batteryManager/batteryCabinet'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_batteryCalibration():
        """
        电池标定连接
        请求参数:
        """
        path = f'/batteryManager/batteryCalibration'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_batteryFaultClear():
        """
        清除故障
        请求参数:
        """
        path = f'/batteryManager/batteryFaultClear'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_carAuthentication():
        """
        换电前验证电池信息
        """
        path = f'/batteryManager/carAuthentication'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getBattery1List():
        """
        获取装车电池信息1
        """
        path = f'/batteryManager/getBattery1List'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getBattery2List(data):
        """
        获取装车电池信息2
        请求参数:
            batteryConnectStatus: string [可选]
            batteryFaultStatus: boolean [可选]
            batteryVolt: number [可选]
            dccNo: string [可选]
            dccStatus: string [可选]
            disableCause: array [可选]
            flag: integer [可选]
            isAvailable: integer [可选]
            mac: string [可选]
            noticeColor: string [可选]
            plcNo: string [可选]
            position: string [可选]
            signalColor: string [可选]
            signalStrength: integer [可选]
            sn: string [可选]
            soc: number [可选]
            systemNo: string [可选]
        """
        path = f'/batteryManager/getBattery2List'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryManager_getBatteryExtInfo():
        """
        获取电池包相关拓展信息
        """
        path = f'/batteryManager/getBatteryExtInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getBatteryFaultInfo():
        """
        获取电池是否存在故障
        请求参数:
        """
        path = f'/batteryManager/getBatteryFaultInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getBatteryGroupList():
        """
        获取电池分组列表
        """
        path = f'/batteryManager/getBatteryGroupList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getBatteryInfo():
        """
        查询电池参数数据
        请求参数:
        """
        path = f'/batteryManager/getBatteryInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getBatteryOutList():
        """
        获取出柜仓位下拉列表
        """
        path = f'/batteryManager/getBatteryOutList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getBlueToothStatus():
        """
        获取仓位蓝牙连接状态
        请求参数:
        """
        path = f'/batteryManager/getBlueToothStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getEquNumList():
        """
        获取仓位下拉列表
        """
        path = f'/batteryManager/getEquNumList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getEquNumListIncludeNoAvailable():
        """
        获取包含禁用仓位下拉列表
        """
        path = f'/batteryManager/getEquNumListIncludeNoAvailable'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getFaultClearResult():
        """
        获取故障清除结果
        请求参数:
        """
        path = f'/batteryManager/getFaultClearResult'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getOptionBatteryInfo():
        """
        获取操作电池数据
        请求参数:
        """
        path = f'/batteryManager/getOptionBatteryInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_getSelectBatteryInfo():
        """
        获取入仓电池仓位信息
        请求参数:
        """
        path = f'/batteryManager/getSelectBatteryInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryManager_operationSendCloud():
        """
        换电站运营信息上报云端
        """
        path = f'/batteryManager/operationSendCloud'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryOperateLog_addBatteryOperateLog(data):
        """
        新增电池操作信息
        请求参数:
            avgTemp: number [可选]
            batteryMac: string [可选]
            createTime: string [可选]
            currentNo: string [可选]
            displaySoc: number [可选]
            faultCode: integer [可选]
            id: integer [可选]
            maxTemp: number [可选]
            minTemp: number [可选]
            operateResult: integer [可选]
            operateResultInfo: string [可选]
            operateTime: string [可选]
            operateType: integer [可选]
            operateTypeInfo: string [可选]
            realSoc: number [可选]
            soh: number [可选]
            targetNo: string [可选]
        """
        path = f'/batteryOperateLog/addBatteryOperateLog'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryOperateLog_batteryOperate():
        """
        导出电池操作信息
        请求参数:
        """
        path = f'/batteryOperateLog/batteryOperate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def batteryOperateLog_findBatteryOperateInfo(data):
        """
        查询电池操作信息
        请求参数:
            avgTemp: number [可选]
            batteryMac: string [可选]
            createTime: string [可选]
            currentNo: string [可选]
            displaySoc: number [可选]
            faultCode: integer [可选]
            id: integer [可选]
            maxTemp: number [可选]
            minTemp: number [可选]
            operateResult: integer [可选]
            operateResultInfo: string [可选]
            operateTime: string [可选]
            operateTimes: array [可选]
            operateType: integer [可选]
            operateTypeInfo: string [可选]
            operateTypes: array [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            position: string [可选]
            realSoc: number [可选]
            soh: number [可选]
            targetNo: string [可选]
        """
        path = f'/batteryOperateLog/findBatteryOperateInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryStatusTask_accumulatedMileage(data):
        """
        累计里程和外接充电能量信息
        请求参数:
        """
        path = f'/batteryStatusTask/accumulatedMileage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryStatusTask_alarmThreshold(data):
        """
        电池报警阀值信息
        请求参数:
        """
        path = f'/batteryStatusTask/alarmThreshold'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryStatusTask_basicInfo(data):
        """
        电池基本属性信息
        请求参数:
        """
        path = f'/batteryStatusTask/basicInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryStatusTask_basicStatus(data):
        """
        电池基本状态信息
        请求参数:
        """
        path = f'/batteryStatusTask/basicStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryStatusTask_energyStatus(data):
        """
        电池能量状态信息
        请求参数:
        """
        path = f'/batteryStatusTask/energyStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryStatusTask_historyData(data):
        """
        清理历史数据
        请求参数:
        """
        path = f'/batteryStatusTask/historyData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def batteryStatusTask_measurement(data):
        """
        电池测量值信息
        请求参数:
        """
        path = f'/batteryStatusTask/measurement'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def blockBatteryInfo_batchExport():
        """
        batchExport
        请求参数:
        """
        path = f'/blockBatteryInfo/batchExport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def blockBatteryInfo_batchImport(data):
        """
        batchImport
        请求参数:
        """
        path = f'/blockBatteryInfo/batchImport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def blockBatteryInfo_deleteById():
        """
        deleteById
        请求参数:
        """
        path = f'/blockBatteryInfo/deleteById'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def blockBatteryInfo_deleteByIds():
        """
        deleteByIds
        请求参数:
        """
        path = f'/blockBatteryInfo/deleteByIds'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def blockBatteryInfo_importTemplate():
        """
        importTemplate
        """
        path = f'/blockBatteryInfo/importTemplate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def blockBatteryInfo_listPage(data):
        """
        listPage
        请求参数:
            barcode: string [可选]
            blockOperator: string [可选]
            blockReason: string [可选]
            createTime: string [可选]
            dataType: string [可选]
            id: integer [可选]
            ids: array [可选]
            mac: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            updateTime: string [可选]
        """
        path = f'/blockBatteryInfo/listPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def busEquipment_addEquipment(data):
        """
        新增设备列表
        请求参数:
            createTime: string [可选]
            equCode: string [可选]
            equId: string [可选]
            equLocation: string [可选]
            equModel: string [可选]
            equName: string [可选]
            equNum: string [可选]
            equProducer: string [可选]
            equSoftwareVersion: string [可选]
            equType: string [可选]
            equTypeNumber: string [可选]
            equVersion: string [可选]
            id: integer [可选]
            installTime: string [可选]
            stationCode: string [可选]
            updateTime: string [可选]
        """
        path = f'/busEquipment/addEquipment'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def busEquipment_deleteEquipment(data):
        """
        删除设备列表
        请求参数:
        """
        path = f'/busEquipment/deleteEquipment'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def busEquipment_findAll(data):
        """
        分页查询设备列表
        请求参数:
            createTime: string [可选]
            endTime: string [可选]
            equCode: string [可选]
            equId: string [可选]
            equLocation: string [可选]
            equModel: string [可选]
            equName: string [可选]
            equNum: string [可选]
            equProducer: string [可选]
            equSoftwareVersion: string [可选]
            equType: string [可选]
            equTypeNumber: string [可选]
            equVersion: string [可选]
            id: integer [可选]
            installTime: string [可选]
            keyword: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
            stationCode: string [可选]
            updateTime: string [可选]
        """
        path = f'/busEquipment/findAll'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def busEquipment_findDeviceTypeNumber():
        """
        查询设备类型编号
        """
        path = f'/busEquipment/findDeviceTypeNumber'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def busEquipment_updateEquipment(data):
        """
        更新设备列表
        请求参数:
            createTime: string [可选]
            equCode: string [可选]
            equId: string [可选]
            equLocation: string [可选]
            equModel: string [可选]
            equName: string [可选]
            equNum: string [可选]
            equProducer: string [可选]
            equSoftwareVersion: string [可选]
            equType: string [可选]
            equTypeNumber: string [可选]
            equVersion: string [可选]
            id: integer [可选]
            installTime: string [可选]
            stationCode: string [可选]
            updateTime: string [可选]
        """
        path = f'/busEquipment/updateEquipment'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def cabinTransfer_batteryMaintenance(data):
        """
        电池维护
        请求参数:
            accessSpace: string [可选]
            dataType: integer [可选]
            selectSpace: string [可选]
        """
        path = f'/cabinTransfer/batteryMaintenance'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def cabinTransfer_clickCabinTransferFrom(data):
        """
        一键入仓
        请求参数:
            accessSpace: string [可选]
            dataType: integer [可选]
            selectSpace: string [可选]
        """
        path = f'/cabinTransfer/clickCabinTransferFrom'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def cabinTransfer_clickCabinTransferTo(data):
        """
        一键出仓
        请求参数:
            accessSpace: string [可选]
            dataType: integer [可选]
            selectSpace: string [可选]
        """
        path = f'/cabinTransfer/clickCabinTransferTo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def cabinTransfer_confirmOneHundredAndTwo(data):
        """
        一键出入库及电池维护 '确认操作'
        请求参数:
            confirmType: integer [可选]
        """
        path = f'/cabinTransfer/confirmOneHundredAndTwo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def cabinTransfer_fireTransferTo(data):
        """
        消防移仓
        请求参数:
            accessSpace: string [可选]
            dataType: integer [可选]
            selectSpace: string [可选]
        """
        path = f'/cabinTransfer/fireTransferTo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def cabinTransfer_transferReset(data):
        """
        仓位操作复位
        """
        path = f'/cabinTransfer/transferReset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def cabinTransfer_warehouseCabinTransfer(data):
        """
        库内仓位转移
        请求参数:
            accessSpace: string [可选]
            dataType: integer [可选]
            selectSpace: string [可选]
        """
        path = f'/cabinTransfer/warehouseCabinTransfer'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def carManage_addCarManage(data):
        """
        新增车辆管理
        请求参数:
            brand: string [可选]
            carNo: string [可选]
            carType: integer [可选]
            createBy: string [可选]
            createTime: string [可选]
            id: integer [可选]
            mbmu: string [可选]
            temporaryFlag: integer [可选]
            updateBy: string [可选]
            updateTime: string [可选]
            vin: string [可选]
        """
        path = f'/carManage/addCarManage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def carManage_bluetoothConnectionResult():
        """
        获取自动蓝牙标定结果
        """
        path = f'/carManage/bluetoothConnectionResult'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_carBluetoothConnection(data):
        """
        自动蓝牙标定
        请求参数:
            packMac: string [可选]
            pcakLoc: integer [可选]
        """
        path = f'/carManage/carBluetoothConnection'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def carManage_carMachineReset():
        """
        车机复位
        """
        path = f'/carManage/carMachineReset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_carStatusShow():
        """
        车辆数据展示
        """
        path = f'/carManage/carStatusShow'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_connectMbmuByMac():
        """
        车辆mbmu建立连接
        请求参数:
        """
        path = f'/carManage/connectMbmuByMac'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_deleteCarManage(data):
        """
        删除车辆管理
        请求参数:
        """
        path = f'/carManage/deleteCarManage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def carManage_findAirCarStatus():
        """
        获取车辆云端状态
        """
        path = f'/carManage/findAirCarStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_findAll(data):
        """
        分页查询车辆管理
        请求参数:
            brand: string [可选]
            carNo: string [可选]
            carType: integer [可选]
            createBy: string [可选]
            createTime: string [可选]
            endTime: string [可选]
            id: integer [可选]
            keyword: string [可选]
            mbmu: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
            temporaryFlag: integer [可选]
            updateBy: string [可选]
            updateTime: string [可选]
            vin: string [可选]
        """
        path = f'/carManage/findAll'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def carManage_sendAMessageToDisconnectBluetooth():
        """
        下发断开蓝牙
        请求参数:
        """
        path = f'/carManage/sendAMessageToDisconnectBluetooth'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_sendChangeInfo():
        """
        下发换电信息
        请求参数:
        """
        path = f'/carManage/sendChangeInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_sendPackInstallResult():
        """
        包安装完成
        请求参数:
        """
        path = f'/carManage/sendPackInstallResult'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_sendResult():
        """
        发送结果
        """
        path = f'/carManage/sendResult'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_sendSwapCommandToGateway():
        """
        恢复换电
        """
        path = f'/carManage/sendSwapCommandToGateway'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_stopSendInfoToTcbmu():
        """
        下发清空
        """
        path = f'/carManage/stopSendInfoToTcbmu'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_swapChangeBattery():
        """
        云端离线车辆换电
        请求参数:
        """
        path = f'/carManage/swapChangeBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def carManage_updateCarManage(data):
        """
        更新车辆管理
        请求参数:
            brand: string [可选]
            carNo: string [可选]
            carType: integer [可选]
            createBy: string [可选]
            createTime: string [可选]
            id: integer [可选]
            mbmu: string [可选]
            temporaryFlag: integer [可选]
            updateBy: string [可选]
            updateTime: string [可选]
            vin: string [可选]
        """
        path = f'/carManage/updateCarManage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def carStatusMonitor_currentFault(data):
        """
        实时故障状态
        """
        path = f'/carStatusMonitor/currentFault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def chargeEquManager_chargeInfoSendCloud():
        """
        充电机数据上报云端（测试）
        """
        path = f'/chargeEquManager/chargeInfoSendCloud'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeEquManager_controlStartCharging(data):
        """
        开始充电
        请求参数:
            chargeNo: string [可选] - 充电机编号
            chargingPowerPercent: number [可选] - 充电功率百分比 0到100
            controlSource: integer [可选]
            powerParam: number [可选] - 功率调节参数(启用功率百分比后此字段废弃)
            soc: integer [可选]
        """
        path = f'/chargeEquManager/controlStartCharging'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def chargeEquManager_controlStopCharging(data):
        """
        停止充电
        请求参数:
            chargeNo: string [可选]
            controlSource: integer [可选]
            stopReason: integer [可选]
        """
        path = f'/chargeEquManager/controlStopCharging'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def chargeEquManager_findBatteryConnectStatus():
        """
        电池连接状态列表
        """
        path = f'/chargeEquManager/findBatteryConnectStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeEquManager_getChargeEquExtInfo():
        """
        获取充电机相关拓展信息
        """
        path = f'/chargeEquManager/getChargeEquExtInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeEquManager_getChargeEquInfo():
        """
        查询充电机固有属性信息
        请求参数:
        """
        path = f'/chargeEquManager/getChargeEquInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeEquManager_switchCabinStatus():
        """
        仓位启用，禁用
        请求参数:
        """
        path = f'/chargeEquManager/switchCabinStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeEquManager_updateAutocharge(data):
        """
        修改自动充电状态
        请求参数:
            autoCharge: integer [可选]
            createTime: string [可选]
            dccNo: string [可选]
            disableCause: string [可选]
            id: integer [可选]
            isAvailable: integer [可选]
            plcNo: string [可选]
            position: string [可选]
            systemNo: string [可选]
            updateTime: string [可选]
        """
        path = f'/chargeEquManager/updateAutocharge'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def chargeStrategy_addChargeStrategy(data):
        """
        新增充电策略
        请求参数:
            baseStrategy: integer [可选]
            cloudUpdateTime: integer [可选]
            cloudUpdateUser: string [可选]
            createTime: string [可选]
            id: integer [可选]
            maxStopSoc: integer [可选]
            minSwapSoc: integer [可选]
            needBatteryCount: integer [可选]
            restrictMode: integer [可选]
            startPosition: integer [可选]
            stopPosition: integer [可选]
            updateTime: string [可选]
        """
        path = f'/chargeStrategy/addChargeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def chargeStrategy_addChargeStrategyTime(data):
        """
        新增充电策略分时信息
        请求参数:
            chargingPowerPercent: number [可选]
            cloudUpdateTime: integer [可选]
            cloudUpdateUser: string [可选]
            createTime: string [可选]
            endTime: string [可选]
            id: integer [可选]
            startTime: string [可选]
            updateTime: string [可选]
        """
        path = f'/chargeStrategy/addChargeStrategyTime'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def chargeStrategy_delChargeStrategy():
        """
        删除充电策略
        请求参数:
        """
        path = f'/chargeStrategy/delChargeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeStrategy_delChargeStrategyTime():
        """
        删除充电策略分时信息
        请求参数:
        """
        path = f'/chargeStrategy/delChargeStrategyTime'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeStrategy_findChargeStrategy():
        """
        获取充电策略
        """
        path = f'/chargeStrategy/findChargeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeStrategy_getGlobalChargeStrategy():
        """
        获取全局充电策略
        """
        path = f'/chargeStrategy/getGlobalChargeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def chargeStrategy_updateChargeStrategy(data):
        """
        编辑充电策略
        请求参数:
            baseStrategy: integer [可选]
            cloudUpdateTime: integer [可选]
            cloudUpdateUser: string [可选]
            createTime: string [可选]
            id: integer [可选]
            maxStopSoc: integer [可选]
            minSwapSoc: integer [可选]
            needBatteryCount: integer [可选]
            restrictMode: integer [可选]
            startPosition: integer [可选]
            stopPosition: integer [可选]
            updateTime: string [可选]
        """
        path = f'/chargeStrategy/updateChargeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def chargeStrategy_updateGlobalChargeStrategy(data):
        """
        更新全局充电策略
        请求参数:
            cloudUpdateTime: integer [可选]
            cloudUpdateUser: string [可选]
            maxChargeNum: integer [可选]
        """
        path = f'/chargeStrategy/updateGlobalChargeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def commonDic_amcType():
        """
        电表类型
        """
        path = f'/commonDic/amcType'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def commonDic_failStage():
        """
        换电失败阶段
        """
        path = f'/commonDic/failStage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def commonDic_failType():
        """
        换电失败类型
        """
        path = f'/commonDic/failType'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainAlarmRest():
        """
        控制热风帘告警复位
        请求参数:
        """
        path = f'/curtainHeater/curtainAlarmRest'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainFanStateInStandbyMode():
        """
        待机模式风机状态控制
        请求参数:
        """
        path = f'/curtainHeater/curtainFanStateInStandbyMode'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainForceHeating():
        """
        热风帘强制制热
        请求参数:
        """
        path = f'/curtainHeater/curtainForceHeating'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainRemoteControl():
        """
        热风帘机组运行状态控制
        请求参数:
        """
        path = f'/curtainHeater/curtainRemoteControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainRestoreDefault():
        """
        热风帘恢复出厂参数
        请求参数:
        """
        path = f'/curtainHeater/curtainRestoreDefault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainSelfCheck():
        """
        热风帘自检
        请求参数:
        """
        path = f'/curtainHeater/curtainSelfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainStatusAlarmSensorMsg():
        """
        查询热风帘状态、告警及传感器信息
        请求参数:
        """
        path = f'/curtainHeater/curtainStatusAlarmSensorMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainStatusMsg():
        """
        热风帘状态数据列表
        """
        path = f'/curtainHeater/curtainStatusMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainSystemParamsMsg():
        """
        查询热风帘系统参数
        请求参数:
        """
        path = f'/curtainHeater/curtainSystemParamsMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_curtainTemperatureSetting(data):
        """
        热风帘相关温度参数设置
        请求参数:
            slaveId: integer [可选]
            temp: integer [可选]
            type: integer [可选]
        """
        path = f'/curtainHeater/curtainTemperatureSetting'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def curtainHeater_heaterAlarmRest():
        """
        控制加热器告警复位
        请求参数:
        """
        path = f'/curtainHeater/heaterAlarmRest'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_heaterForceHeating():
        """
        加热器强制制热
        请求参数:
        """
        path = f'/curtainHeater/heaterForceHeating'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_heaterRemoteControl():
        """
        加热器机组运行状态控制
        请求参数:
        """
        path = f'/curtainHeater/heaterRemoteControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_heaterRestoreDefault():
        """
        加热器恢复出厂参数
        请求参数:
        """
        path = f'/curtainHeater/heaterRestoreDefault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_heaterStatusAlarmSensorMsg():
        """
        查询加热器状态、告警及传感器信息
        请求参数:
        """
        path = f'/curtainHeater/heaterStatusAlarmSensorMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_heaterStatusMsg():
        """
        加热器状态数据列表
        """
        path = f'/curtainHeater/heaterStatusMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_heaterSystemParamsMsg():
        """
        查询加热器系统参数
        请求参数:
        """
        path = f'/curtainHeater/heaterSystemParamsMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def curtainHeater_heaterTemperatureSetting(data):
        """
        加热器相关温度参数设置
        请求参数:
            slaveId: integer [可选]
            temp: integer [可选]
            type: integer [可选]
        """
        path = f'/curtainHeater/heaterTemperatureSetting'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def document_addDocument(data):
        """
        新增文档数据
        请求参数:
            businessId: string [可选]
            createTime: string [可选]
            docNo: string [可选]
            fileName: string [可选]
            id: integer [可选]
            title: string [可选]
            type: string [可选]
            updateTime: string [可选]
        """
        path = f'/document/addDocument'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def document_addDocumentType(data):
        """
        新增文档分类
        请求参数:
            createTime: string [可选]
            id: integer [可选]
            type: string [可选]
            updateTime: string [可选]
        """
        path = f'/document/addDocumentType'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def document_deleteDocument():
        """
        删除文档数据
        请求参数:
        """
        path = f'/document/deleteDocument'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def document_deleteDocumentType(data):
        """
        删除文档分类
        请求参数:
            createTime: string [可选]
            id: integer [可选]
            type: string [可选]
            updateTime: string [可选]
        """
        path = f'/document/deleteDocumentType'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def document_findDocumentByPage(data):
        """
        分页查询文档数据
        请求参数:
            endTime: string [可选]
            keyword: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
        """
        path = f'/document/findDocumentByPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def document_findDocumentTypeByPage(data):
        """
        分页查询文档分类数据
        请求参数:
            pageNum: integer [可选]
            pageSize: integer [可选]
            type: string [可选]
        """
        path = f'/document/findDocumentTypeByPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def document_updateDocument(data):
        """
        更新文档数据
        请求参数:
            businessId: string [可选]
            createTime: string [可选]
            docNo: string [可选]
            fileName: string [可选]
            id: integer [可选]
            title: string [可选]
            type: string [可选]
            updateTime: string [可选]
        """
        path = f'/document/updateDocument'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def document_updateDocumentType(data):
        """
        更新文档分类
        请求参数:
            createTime: string [可选]
            id: integer [可选]
            type: string [可选]
            updateTime: string [可选]
        """
        path = f'/document/updateDocumentType'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_airSwitchControl():
        """
        控制空调开关
        请求参数:
        """
        path = f'/equipment/airSwitchControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_amcConfig():
        """
        查询电表配置
        """
        path = f'/equipment/amcConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_amcConfig_post(data):
        """
        更新电表配置
        请求参数:
            slaveList: array [可选] - 电表配置列表
                        no: integer [可选] - 电表编号
                        type: string [可选] - 电表类型
        """
        path = f'/equipment/amcConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_amcList():
        """
        电表列表
        """
        path = f'/equipment/amcList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_chargeAreaLightingControl(data):
        """
        充电区灯光控制
        请求参数:
            address: integer [可选]
            command: integer [可选]
            isRemote: integer [可选]
        """
        path = f'/equipment/chargeAreaLightingControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_controlCurtainedDoor(data):
        """
        卷帘门控制
        请求参数:
            doorFlag: integer [可选]
            isRemote: integer [可选]
            opeResult: integer [可选]
            opeType: integer [可选]
        """
        path = f'/equipment/controlCurtainedDoor'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_enableSoundLightAlarm():
        """
        声光报警控制
        请求参数:
        """
        path = f'/equipment/enableSoundLightAlarm'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_fan_alarmReset(data):
        """
        风机告警复位
        请求参数:
            id: string [可选]
            onOff: integer [可选]
        """
        path = f'/equipment/fan/alarmReset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_fan_init(data):
        """
        风机恢复出厂设置
        请求参数:
            id: string [可选]
            onOff: integer [可选]
        """
        path = f'/equipment/fan/init'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_fan_list():
        """
        风机列表信息
        """
        path = f'/equipment/fan/list'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_fan_manualSwitchFan(data):
        """
        风机手动开启风扇
        请求参数:
            id: string [可选]
            onOff: integer [可选]
        """
        path = f'/equipment/fan/manualSwitchFan'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_fan_paramSet(data):
        """
        风机参数设置
        请求参数:
            fanStartSmallBoxTem: number [可选]
            fanStartTem: number [可选]
            fanStopBoxTemDifference: number [可选]
            fanStopTem: number [可选]
            highAlarmTem: number [可选]
            id: string [可选]
            lowAlarmTem: number [可选]
            onOff: integer [可选]
            timerStartHour: integer [可选]
            timerStartMin: integer [可选]
        """
        path = f'/equipment/fan/paramSet'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_fan_remoteSwitchAirCondition(data):
        """
        风机远程开关空调
        请求参数:
            id: string [可选]
            onOff: integer [可选]
        """
        path = f'/equipment/fan/remoteSwitchAirCondition'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_fanControl():
        """
        风扇控制
        请求参数:
        """
        path = f'/equipment/fanControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_findEquModeByType():
        """
        获取设备控制模式
        请求参数:
        """
        path = f'/equipment/findEquModeByType'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_findSensorTandhDeviceInfo():
        """
        获取温湿度传感器数据
        """
        path = f'/equipment/findSensorTandhDeviceInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_fireExtinguisherStates():
        """
        获取消防灭火器状态数据
        """
        path = f'/equipment/fireExtinguisherStates'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_fireSensorMsg():
        """
        获取消防传感器(复合型探测器)数据
        """
        path = f'/equipment/fireSensorMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_fireSystemStates():
        """
        获取消防系统状态数据
        """
        path = f'/equipment/fireSystemStates'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_getEquStatus():
        """
        获取设备状态
        请求参数:
        """
        path = f'/equipment/getEquStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_getSensorTandhDeviceData():
        """
        保存传感器温湿度数据到云端
        """
        path = f'/equipment/getSensorTandhDeviceData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_partitionMsg():
        """
        消防分区信息
        """
        path = f'/equipment/partitionMsg'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_rbcAreaLightingControl(data):
        """
        换电区灯光控制
        请求参数:
            address: integer [可选]
            command: integer [可选]
            isRemote: integer [可选]
        """
        path = f'/equipment/rbcAreaLightingControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_reset():
        """
        消防复位
        """
        path = f'/equipment/reset'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_roadGateControl(data):
        """
        道闸控制
        请求参数:
            doorFlag: integer [可选]
            isRemote: integer [可选]
            opeResult: integer [可选]
            opeType: integer [可选]
        """
        path = f'/equipment/roadGateControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_selfCheck():
        """
        消防自检
        """
        path = f'/equipment/selfCheck'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_stationStatusControl(data):
        """
        站点运营状态控制
        请求参数:
            areaCity: string [可选] - 市
            areaDistrict: string [可选] - 区
            areaLocation: string [可选] - 具体地理位置（换电站地点）
            areaProvince: string [可选] - 省
            belongCompany: string [可选] - 换电站运营公司
            channelNum: integer [可选] - 通道类型(1.左单通道；2.右单通道；3.双通道)
            createTime: string [可选]
            developmentType: integer [可选] - 版本类型： 1.试验站 2.批量站
            id: integer [可选]
            isRemote: integer [可选]
            latitude: number [可选] - 纬度
            longitude: number [可选] - 经度
            maintainCompany: string [可选] - 换电站维保公司
            maintainPhone: string [可选] - 换电站维保联系方式
            manager: string [可选] - 换电站负责人
            manufactureCompany: string [可选] - 换电站制造公司
            manufacturePhone: string [可选] - 换电站运营联系方式
            msgId: integer [可选]
            parameterConfig: string [可选] - 换电站参数
            path: string [可选] - 云端地址
            picture: string [可选] - 图片名称
            platformKey: string [可选] - 平台标识码
            providerCode: string [可选] - 供应商代码
            remark: string [可选] - 备注
            retryCount: integer [可选]
            runEndTime: string [可选] - 运营结束时间
            runStartTime: string [可选] - 运营开始时间
            secret: string [可选] - 云端密钥
            serverNum: integer [可选] - 站控服务数
            socialCid: string [可选] - 社会信用代码
            stationCode: string [可选] - 换电站编号
            stationEnv: integer [可选] - 站控环境(1:预发环境；2:正式环境)
            stationName: string [可选] - 换电站名称
            stationStatus: integer [可选] - 运营状态 0:正常1:歇业2:维修
            stationType: string [可选] - 站类型
            swapMethod: boolean [可选] - 换电模式,0:在线换电、1:离线换电
            telNumber: string [可选] - 换电站负责人联系方式
            updateTime: string [可选]
            versionId: string [可选] - 站控主机版本号
            versionPublicStr: string [可选] - 版本公共匹配串
        """
        path = f'/equipment/stationStatusControl'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_stopAlarm():
        """
        消报警音
        """
        path = f'/equipment/stopAlarm'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_switchMode():
        """
        消防切换控制模式
        请求参数:
        """
        path = f'/equipment/switchMode'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipment_temperatureAndHumiditySetting(data):
        """
        温湿度报警阀值设置(温湿度传感器数据)
        请求参数:
            deviceNo: integer [可选]
            type: integer [可选]
            valueData: number [可选]
        """
        path = f'/equipment/temperatureAndHumiditySetting'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_updateEquMode(data):
        """
        更新设备控制模式
        请求参数:
            equMode: integer [可选]
            equType: string [可选]
            equTypeNumber: string [可选]
        """
        path = f'/equipment/updateEquMode'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipment_updateSensorTandhName():
        """
        更新传感器温湿度位置
        请求参数:
        """
        path = f'/equipment/updateSensorTandhName'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def equipmentInfo_addEquipmentInfo(data):
        """
        充电机信息维护新增
        请求参数:
            connectorInfoVOList: array [可选]
                        current: number [可选]
                        equipmentId: string [可选]
                        power: number [可选]
                        voltageLowerLimits: number [可选]
                        voltageUpperLimits: number [可选]
            createTime: string [可选]
            equipmentId: string [可选]
            equipmentName: string [可选]
            equipmentType: integer [可选]
            id: integer [可选]
            power: number [可选]
            updateTime: string [可选]
        """
        path = f'/equipmentInfo/addEquipmentInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipmentInfo_findEquipmentInfo(data):
        """
        查询充电机维护信息
        请求参数:
            connectorInfoVOList: array [可选]
                        current: number [可选]
                        equipmentId: string [可选]
                        power: number [可选]
                        voltageLowerLimits: number [可选]
                        voltageUpperLimits: number [可选]
            createTime: string [可选]
            equipmentId: string [可选]
            equipmentName: string [可选]
            equipmentType: integer [可选]
            id: integer [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            power: number [可选]
            updateTime: string [可选]
        """
        path = f'/equipmentInfo/findEquipmentInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def equipmentInfo_findEquipmentProducer(data):
        """
        查询充电机生产商信息
        """
        path = f'/equipmentInfo/findEquipmentProducer'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def eventLogs_findEventLogs(data):
        """
        分页查询事件日志
        请求参数:
            createTime: string [可选]
            endTime: string [可选]
            equName: string [可选]
            equNum: string [可选]
            eventName: string [可选]
            eventStatus: string [可选]
            id: integer [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
            updateTime: string [可选]
        """
        path = f'/eventLogs/findEventLogs'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def faultDict_addFaultDict(data):
        """
        新增设备故障类别
        请求参数:
            createTime: string [可选]
            dealMethod: string [可选]
            equCode: string [可选]
            equNumber: string [可选]
            equTypeName: string [可选]
            equTypeNumber: string [可选]
            faultCode: string [可选]
            faultContent: string [可选]
            faultNumber: string [可选]
            id: integer [可选]
            level: integer [可选]
            prodCondition: string [可选]
            remark: string [可选]
            updateTime: string [可选]
        """
        path = f'/faultDict/addFaultDict'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def faultDict_deleteFaultDict(data):
        """
        删除故障类别
        请求参数:
        """
        path = f'/faultDict/deleteFaultDict'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def faultDict_findAll(data):
        """
        分页查询设备故障类别
        请求参数:
            createTime: string [可选]
            dealMethod: string [可选]
            endTime: string [可选]
            equCode: string [可选]
            equNumber: string [可选]
            equTypeName: string [可选]
            equTypeNumber: string [可选]
            faultCode: string [可选]
            faultContent: string [可选]
            faultNumber: string [可选]
            id: integer [可选]
            keyword: string [可选]
            level: integer [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            prodCondition: string [可选]
            remark: string [可选]
            startTime: string [可选]
            updateTime: string [可选]
        """
        path = f'/faultDict/findAll'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def faultDict_updateFaultDict(data):
        """
        更新设备故障类别
        请求参数:
            createTime: string [可选]
            dealMethod: string [可选]
            equCode: string [可选]
            equNumber: string [可选]
            equTypeName: string [可选]
            equTypeNumber: string [可选]
            faultCode: string [可选]
            faultContent: string [可选]
            faultNumber: string [可选]
            id: integer [可选]
            level: integer [可选]
            prodCondition: string [可选]
            remark: string [可选]
            updateTime: string [可选]
        """
        path = f'/faultDict/updateFaultDict'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def faultMaintainManage_add(data):
        """
        新增维护记录
        请求参数:
            belongSystem: string [可选]
            createTime: string [可选]
            id: integer [可选]
            maintainContent: string [可选]
            maintainPerson: string [可选]
            maintainProject: string [可选]
            maintainResult: string [可选]
            maintainStatus: integer [可选]
            picture: string [可选]
            remark: string [可选]
            telNumber: string [可选]
            updateTime: string [可选]
        """
        path = f'/faultMaintainManage/add'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def faultMaintainManage_delete():
        """
        根据主键id删除
        请求参数:
        """
        path = f'/faultMaintainManage/delete'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def faultMaintainManage_findByPage(data):
        """
        分页查询维护记录列表
        请求参数:
            endTime: string [可选]
            keyword: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
        """
        path = f'/faultMaintainManage/findByPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def faultMaintainManage_update(data):
        """
        修改维护记录
        请求参数:
            belongSystem: string [可选]
            createTime: string [可选]
            id: integer [可选]
            maintainContent: string [可选]
            maintainPerson: string [可选]
            maintainProject: string [可选]
            maintainResult: string [可选]
            maintainStatus: integer [可选]
            picture: string [可选]
            remark: string [可选]
            telNumber: string [可选]
            updateTime: string [可选]
        """
        path = f'/faultMaintainManage/update'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def file_deleteFile():
        """
        删除文件
        请求参数:
        """
        path = f'/file/deleteFile'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def file_getFileByPath():
        """
        根据路径获取文件
        请求参数:
        """
        path = f'/file/getFileByPath'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def file_getFileSource():
        """
        根据业务id获取文件资源
        请求参数:
        """
        path = f'/file/getFileSource'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def file_getStationPic():
        """
        获取换电站图片
        """
        path = f'/file/getStationPic'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def file_upload(data):
        """
        上传文件并保存文件数据
        请求参数:
        """
        path = f'/file/upload'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def fire_getProcess():
        """
        获取消防进度
        """
        path = f'/fire/getProcess'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def menu_addNewMenu(data):
        """
        新增菜单
        请求参数:
        """
        path = f'/menu/addNewMenu'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def menu_delMenuById(data):
        """
        根据id删除菜单，可批量删除
        请求参数:
        """
        path = f'/menu/delMenuById'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def menu_findAllMenus(data):
        """
        查询菜单列表
        """
        path = f'/menu/findAllMenus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def menu_findAllPermission():
        """
        查询所有的权限和其code
        """
        path = f'/menu/findAllPermission'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def menu_findMenuIdsByRoleId():
        """
        查询某角色下分配的所有菜单id
        请求参数:
        """
        path = f'/menu/findMenuIdsByRoleId'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def menu_findMenuPermission():
        """
        查询某角色单个菜单下分配的权限
        请求参数:
        """
        path = f'/menu/findMenuPermission'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def menu_findMenuTree(data):
        """
        查询菜单树
        """
        path = f'/menu/findMenuTree'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def menu_findMenusByPage(data):
        """
        分页查询菜单列表
        请求参数:
        """
        path = f'/menu/findMenusByPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def menu_nav(data):
        """
        导航菜单
        """
        path = f'/menu/nav'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def menu_updateMenu(data):
        """
        修改菜单
        请求参数:
        """
        path = f'/menu/updateMenu'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def menu_updateMenuPermission(data):
        """
        修改某角色单个菜单下分配的权限
        请求参数:
        """
        path = f'/menu/updateMenuPermission'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def monitor_electricityStatistics(data):
        """
        电量统计
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/monitor/electricityStatistics'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def monitor_fireMonitor(data):
        """
        火警监控
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/monitor/fireMonitor'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def monitor_stationStatus(data):
        """
        换电站状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/monitor/stationStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def offline_swapEnd(data):
        """
        离线模式下结束换电
        """
        path = f'/offline/swapEnd'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def offline_swapStart(data):
        """
        离线模式下启动换电
        """
        path = f'/offline/swapStart'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def offline_switch(data):
        """
        离线换电开关
        请求参数:
            flag: boolean [可选]
        """
        path = f'/offline/switch'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def offline_vehicleConnectResult():
        """
        车站连接结果
        请求参数:
        """
        path = f'/offline/vehicleConnectResult'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def offline_vehicleStationBluetoothConnect(data):
        """
        离线换电发起车站蓝牙连接
        请求参数:
            mac: string [可选]
            phoneNumber: string [可选]
            vehicleType: string [可选]
        """
        path = f'/offline/vehicleStationBluetoothConnect'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def order_chargeRecordSent(data):
        """
        充电订单数据上报市政平台
        请求参数:
            batteryNo: string [可选]
            chargeAfterEnergy: number [可选]
            chargeEndTime: string [可选]
            chargeFrontEnergy: number [可选]
            chargeStartTime: string [可选]
            chargeTime: integer [可选]
            createTime: string [可选]
            dcChargerNo: string [可选]
            failCause: integer [可选]
            failCauseDesc: string [可选]
            id: integer [可选]
            isCloud: integer [可选]
            isCloudInfo: string [可选]
            orderId: string [可选]
            outputPower: number [可选]
            outputPower1: number [可选]
            outputPower1End: number [可选]
            outputPower1Start: number [可选]
            outputPower2: number [可选]
            outputPower2End: number [可选]
            outputPower2Start: number [可选]
            outputPower3: number [可选]
            outputPower3End: number [可选]
            outputPower3Start: number [可选]
            outputPower4: number [可选]
            outputPower4End: number [可选]
            outputPower4Start: number [可选]
            plcNo: string [可选]
            startSoc: number [可选]
            stopSoc: number [可选]
            updateTime: string [可选]
        """
        path = f'/order/chargeRecordSent'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def order_chargingOrderReport():
        """
        充电订单数据上报云端（测试）
        """
        path = f'/order/chargingOrderReport'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def order_findChargeRecord(data):
        """
        分页查询充电订单
        请求参数:
            batteryNo: string [可选]
            chargeTimes: array [可选]
            dcChargerNo: string [可选]
            orderId: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
        """
        path = f'/order/findChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def order_findExchangeBattery():
        """
        根据订单编号查询换电详情信息
        请求参数:
        """
        path = f'/order/findExchangeBattery'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def order_findExchangeOrder(data):
        """
        分页查询换电订单
        请求参数:
            carNo: string [可选]
            changeResult: integer [可选] - 换电结果：1-成功，2-失败
            endTime: string [可选] - 结束时间
            failStage: string [可选] - 换电失败阶段
            failType: string [可选] - 换电失败失败类型
            orderId: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选] - 开始时间
            swapTotalTime: integer [可选]
        """
        path = f'/order/findExchangeOrder'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def order_recordOperate():
        """
        充电记录导出
        请求参数:
        """
        path = f'/order/recordOperate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def order_recordSwappingOperate():
        """
        换电记录导出
        请求参数:
        """
        path = f'/order/recordSwappingOperate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def order_recordSwappingPush():
        """
        换电记录推送云端
        请求参数:
        """
        path = f'/order/recordSwappingPush'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def otaUpgrade_getOtaUpgradePackageList(data):
        """
        获取ota升级包信息
        请求参数:
            appFileId: integer [可选]
            appFileName: string [可选]
            batchNumber: string [可选]
            bluetoothFileId: integer [可选]
            bluetoothFileName: string [可选]
            cloudMsgId: integer [可选]
            detailStatus: integer [可选]
            downProgress: integer [可选]
            driveFileId: integer [可选]
            driveFileName: string [可选]
            failCause: string [可选]
            flag: boolean [可选]
            id: integer [可选]
            otaNo: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            remark: string [可选]
            respCloud: integer [可选]
            source: integer [可选]
            status: integer [可选]
            upgradeCount: integer [可选]
            upgradeEndTime: string [可选]
            upgradeFileId: integer [可选]
            upgradeInfo: string [可选]
            upgradeStartTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
            upgradeUser: string [可选]
        """
        path = f'/otaUpgrade/getOtaUpgradePackageList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgrade_getotaUpgradeDetails(data):
        """
        ota升级详情
        请求参数:
            appFileId: integer [可选]
            appFileName: string [可选]
            batchNumber: string [可选]
            bluetoothFileId: integer [可选]
            bluetoothFileName: string [可选]
            cloudMsgId: integer [可选]
            detailStatus: integer [可选]
            downProgress: integer [可选]
            driveFileId: integer [可选]
            driveFileName: string [可选]
            failCause: string [可选]
            flag: boolean [可选]
            id: integer [可选]
            otaNo: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            remark: string [可选]
            respCloud: integer [可选]
            source: integer [可选]
            status: integer [可选]
            upgradeCount: integer [可选]
            upgradeEndTime: string [可选]
            upgradeFileId: integer [可选]
            upgradeInfo: string [可选]
            upgradeStartTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
            upgradeUser: string [可选]
        """
        path = f'/otaUpgrade/getotaUpgradeDetails'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgrade_otaUpgradeCount(data):
        """
        ota升级记录
        请求参数:
            appFileId: integer [可选]
            appFileName: string [可选]
            batchNumber: string [可选]
            bluetoothFileId: integer [可选]
            bluetoothFileName: string [可选]
            cloudMsgId: integer [可选]
            detailStatus: integer [可选]
            downProgress: integer [可选]
            driveFileId: integer [可选]
            driveFileName: string [可选]
            failCause: string [可选]
            flag: boolean [可选]
            id: integer [可选]
            otaNo: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            remark: string [可选]
            respCloud: integer [可选]
            source: integer [可选]
            status: integer [可选]
            upgradeCount: integer [可选]
            upgradeEndTime: string [可选]
            upgradeFileId: integer [可选]
            upgradeInfo: string [可选]
            upgradeStartTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
            upgradeUser: string [可选]
        """
        path = f'/otaUpgrade/otaUpgradeCount'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgrade_otaUpgradeCountInfo(data):
        """
        ota升级记录详情
        请求参数:
            appFileId: integer [可选]
            appFileName: string [可选]
            batchNumber: string [可选]
            bluetoothFileId: integer [可选]
            bluetoothFileName: string [可选]
            cloudMsgId: integer [可选]
            detailStatus: integer [可选]
            downProgress: integer [可选]
            driveFileId: integer [可选]
            driveFileName: string [可选]
            failCause: string [可选]
            flag: boolean [可选]
            id: integer [可选]
            otaNo: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            remark: string [可选]
            respCloud: integer [可选]
            source: integer [可选]
            status: integer [可选]
            upgradeCount: integer [可选]
            upgradeEndTime: string [可选]
            upgradeFileId: integer [可选]
            upgradeInfo: string [可选]
            upgradeStartTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
            upgradeUser: string [可选]
        """
        path = f'/otaUpgrade/otaUpgradeCountInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgrade_otaUpgradeEquipment(data):
        """
        开始ota升级文件
        请求参数:
            appFileId: integer [可选]
            appFileName: string [可选]
            batchNumber: string [可选]
            bluetoothFileId: integer [可选]
            bluetoothFileName: string [可选]
            cloudMsgId: integer [可选]
            detailStatus: integer [可选]
            downProgress: integer [可选]
            driveFileId: integer [可选]
            driveFileName: string [可选]
            failCause: string [可选]
            flag: boolean [可选]
            id: integer [可选]
            otaNo: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            remark: string [可选]
            respCloud: integer [可选]
            source: integer [可选]
            status: integer [可选]
            upgradeCount: integer [可选]
            upgradeEndTime: string [可选]
            upgradeFileId: integer [可选]
            upgradeInfo: string [可选]
            upgradeStartTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
            upgradeUser: string [可选]
        """
        path = f'/otaUpgrade/otaUpgradeEquipment'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgrade_otaUpgradePdu(data):
        """
        开始ota升级pdu文件
        请求参数:
            appFileId: integer [可选]
            appFileName: string [可选]
            batchNumber: string [可选]
            bluetoothFileId: integer [可选]
            bluetoothFileName: string [可选]
            cloudMsgId: integer [可选]
            detailStatus: integer [可选]
            downProgress: integer [可选]
            driveFileId: integer [可选]
            driveFileName: string [可选]
            failCause: string [可选]
            flag: boolean [可选]
            id: integer [可选]
            otaNo: string [可选]
            remark: string [可选]
            respCloud: integer [可选]
            source: integer [可选]
            status: integer [可选]
            upgradeCount: integer [可选]
            upgradeEndTime: string [可选]
            upgradeFileId: integer [可选]
            upgradeInfo: string [可选]
            upgradeStartTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
            upgradeUser: string [可选]
        """
        path = f'/otaUpgrade/otaUpgradePdu'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgrade_otaUpgradeUpdate(data):
        """
        ota更新
        请求参数:
            appFileId: integer [可选]
            appFileName: string [可选]
            batchNumber: string [可选]
            bluetoothFileId: integer [可选]
            bluetoothFileName: string [可选]
            cloudMsgId: integer [可选]
            detailStatus: integer [可选]
            downProgress: integer [可选]
            driveFileId: integer [可选]
            driveFileName: string [可选]
            failCause: string [可选]
            flag: boolean [可选]
            id: integer [可选]
            otaNo: string [可选]
            remark: string [可选]
            respCloud: integer [可选]
            source: integer [可选]
            status: integer [可选]
            upgradeCount: integer [可选]
            upgradeEndTime: string [可选]
            upgradeFileId: integer [可选]
            upgradeInfo: string [可选]
            upgradeStartTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
            upgradeUser: string [可选]
        """
        path = f'/otaUpgrade/otaUpgradeUpdate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgrade_otaUploadList():
        """
        ota升级列表
        请求参数:
        """
        path = f'/otaUpgrade/otaUploadList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def otaUpgradePackageManage_addUpgradePackage(data):
        """
        新增ota升级包
        请求参数:
            createTime: string [可选]
            fileType: integer [可选]
            id: integer [可选]
            newFileName: string [可选]
            originalFileName: string [可选]
            remark: string [可选]
            source: integer [可选]
            updateTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
        """
        path = f'/otaUpgradePackageManage/addUpgradePackage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgradePackageManage_deleteUpgradePackage():
        """
        删除ota升级包
        请求参数:
        """
        path = f'/otaUpgradePackageManage/deleteUpgradePackage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def otaUpgradePackageManage_findAll(data):
        """
        查询ota升级包
        请求参数:
            createTime: string [可选]
            fileType: integer [可选]
            id: integer [可选]
            newFileName: string [可选]
            originalFileName: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            remark: string [可选]
            source: integer [可选]
            updateTime: string [可选]
            upgradeTarget: string [可选]
            upgradeType: string [可选]
        """
        path = f'/otaUpgradePackageManage/findAll'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def otaUpgradePackageManage_uploadUpgradePackage(data):
        """
        上传ota升级文件
        请求参数:
        """
        path = f'/otaUpgradePackageManage/uploadUpgradePackage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def permission_addPermission(data):
        """
        新增权限
        请求参数:
        """
        path = f'/permission/addPermission'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def permission_delPermissionById(data):
        """
        根据id删除权限
        请求参数:
        """
        path = f'/permission/delPermissionById'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def permission_findPermissionsByPage(data):
        """
        分页查询权限列表
        请求参数:
        """
        path = f'/permission/findPermissionsByPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def permission_findUserPermissions():
        """
        查询当前用户拥有的权限
        """
        path = f'/permission/findUserPermissions'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def permission_updatePermission(data):
        """
        修改权限
        请求参数:
        """
        path = f'/permission/updatePermission'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def picturesAndVideos_addPicturesAndVideos(data):
        """
        新增轮播图
        请求参数:
            addresspath: string [可选] - 存放地址
            businessid: string [可选] - 编码
            createTime: string [可选]
            exhibition: integer [可选] - 展示或不展示(1 展示 , 0 不展示)
            id: integer [可选]
            sname: string [可选] - 名称
            spare: string [可选] - 备用
            textSource: integer [可选] - 文本来源(1:本地；2:云端)
            type: integer [可选] - 分类 1: 待机轮播图, 2: 换电轮播图 3、视频广告
            updateTime: string [可选]
        """
        path = f'/picturesAndVideos/addPicturesAndVideos'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def picturesAndVideos_delPicturesAndVideos(data):
        """
        删除轮播图
        请求参数:
        """
        path = f'/picturesAndVideos/delPicturesAndVideos'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def picturesAndVideos_findPicturesAndVideos(data):
        """
        查询分类信息
        请求参数:
            addresspath: string [可选] - 存放地址
            businessid: string [可选] - 编码
            createTime: string [可选]
            exhibition: integer [可选] - 展示或不展示(1 展示 , 0 不展示)
            id: integer [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            sname: string [可选] - 名称
            spare: string [可选] - 备用
            textSource: integer [可选] - 文本来源(1:本地；2:云端)
            type: integer [可选] - 分类 1: 待机轮播图, 2: 换电轮播图 3、视频广告
            updateTime: string [可选]
        """
        path = f'/picturesAndVideos/findPicturesAndVideos'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def picturesAndVideos_updateExhibition(data):
        """
        修改 视频的可见性
        请求参数:
            addresspath: string [可选] - 存放地址
            businessid: string [可选] - 编码
            createTime: string [可选]
            exhibition: integer [可选] - 展示或不展示(1 展示 , 0 不展示)
            id: integer [可选]
            sname: string [可选] - 名称
            spare: string [可选] - 备用
            textSource: integer [可选] - 文本来源(1:本地；2:云端)
            type: integer [可选] - 分类 1: 待机轮播图, 2: 换电轮播图 3、视频广告
            updateTime: string [可选]
        """
        path = f'/picturesAndVideos/updateExhibition'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def positionConfig_UpdatePositionConfig(data):
        """
        修改系统仓位配置
        请求参数:
            autoCharge: integer [可选]
            createTime: string [可选]
            dccNo: string [可选]
            disableCause: string [可选]
            id: integer [可选]
            isAvailable: integer [可选]
            plcNo: string [可选]
            position: string [可选]
            systemNo: string [可选]
            updateTime: string [可选]
        """
        path = f'/positionConfig/UpdatePositionConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def positionConfig_addPositionConfig(data):
        """
        新增系统仓位配置
        请求参数:
            autoCharge: integer [可选]
            createTime: string [可选]
            dccNo: string [可选]
            disableCause: string [可选]
            id: integer [可选]
            isAvailable: integer [可选]
            plcNo: string [可选]
            position: string [可选]
            systemNo: string [可选]
            updateTime: string [可选]
        """
        path = f'/positionConfig/addPositionConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def positionConfig_delPositionConfig():
        """
        删除系统仓位配置
        请求参数:
        """
        path = f'/positionConfig/delPositionConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def positionConfig_getPositionConfigList(data):
        """
        分页查询系统仓位配置
        请求参数:
            dccNo: string [可选]
            id: integer [可选]
            isAvailable: integer [可选]
            noticeColor: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            plcNo: string [可选]
            position: string [可选]
            systemNo: string [可选]
        """
        path = f'/positionConfig/getPositionConfigList'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def powerChangeDemo_addPowerChangeDemo(data):
        """
        新增换电动画
        请求参数:
            addresspath: string [可选] - 存放地址
            businessType: integer [可选] - 业务种类
            businessid: string [可选] - 编码
            createTime: string [可选]
            id: integer [可选]
            type: integer [可选] - 分类
            updateTime: string [可选]
        """
        path = f'/powerChangeDemo/addPowerChangeDemo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def powerChangeDemo_delPowerChangeDemo_id(id):
        """
        删除换电动画
        请求参数:
        """
        path = f'/powerChangeDemo/delPowerChangeDemo/{id}'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def powerChangeDemo_findAll():
        """
        查询所有换电动画列表
        """
        path = f'/powerChangeDemo/findAll'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def powerChangeDemo_updataPowerChangeDemo(data):
        """
        更新换电动画
        请求参数:
            addresspath: string [可选] - 存放地址
            businessType: integer [可选] - 业务种类
            businessid: string [可选] - 编码
            createTime: string [可选]
            id: integer [可选]
            type: integer [可选] - 分类
            updateTime: string [可选]
        """
        path = f'/powerChangeDemo/updataPowerChangeDemo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def putFaultInfo_downloadExcelTemplate():
        """
        下载excel模板---故障字典
        """
        path = f'/putFaultInfo/downloadExcelTemplate'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def putFaultInfo_findHistoryFaultByPage(data):
        """
        分页查询历史故障
        请求参数:
            endTime: string [可选]
            keyword: string [可选]
            level: integer [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
        """
        path = f'/putFaultInfo/findHistoryFaultByPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def putFaultInfo_findRealtimeFaultByPage(data):
        """
        分页查询实时故障
        请求参数:
            endTime: string [可选]
            keyword: string [可选]
            level: integer [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
        """
        path = f'/putFaultInfo/findRealtimeFaultByPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def putFaultInfo_parsingExcelForFaultDict(data):
        """
        上传excel批量导入故障字典
        请求参数:
        """
        path = f'/putFaultInfo/parsingExcelForFaultDict'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def putFaultInfo_removeThermorunawayFault(data):
        """
        BMS热失控故障消除
        请求参数:
            batteryNo: string [可选]
            createTime: string [可选]
            dccNo: string [可选]
            equCode: string [可选]
            equName: string [可选]
            equNumber: string [可选]
            equTypeCode: string [可选]
            equTypeNumber: string [可选]
            faultCode: string [可选]
            faultNumber: string [可选]
            faultVersion: integer [可选]
            normalSignal: boolean [可选]
            updateTime: string [可选]
        """
        path = f'/putFaultInfo/removeThermorunawayFault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def putFaultInfo_socketTimedPushStationFault():
        """
        socket推送信息（测试）
        """
        path = f'/putFaultInfo/socketTimedPushStationFault'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def putFaultInfo_thermorunawayFaultHandle():
        """
        BMS热失控故障处理
        请求参数:
        """
        path = f'/putFaultInfo/thermorunawayFaultHandle'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def putFaultInfo_unifyFaultHandle(data):
        """
        统一故障处理
        请求参数:
            batteryNo: string [可选]
            createTime: string [可选]
            dccNo: string [可选]
            equCode: string [可选]
            equName: string [可选]
            equNumber: string [可选]
            equTypeCode: string [可选]
            equTypeNumber: string [可选]
            faultCode: string [可选]
            faultNumber: string [可选]
            faultVersion: integer [可选]
            normalSignal: boolean [可选]
            updateTime: string [可选]
        """
        path = f'/putFaultInfo/unifyFaultHandle'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def rechargeElectricity_getConfig():
        """
        获取防过放补电策略
        """
        path = f'/rechargeElectricity/getConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def rechargeElectricity_saveConfig(data):
        """
        保存防过放补电策略
        请求参数:
            stopSoc: number [可选]
        """
        path = f'/rechargeElectricity/saveConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def remoteDownLog_findByPage(data):
        """
        分页查询远程下控操作日志
        请求参数:
            endTime: string [可选]
            keyword: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
        """
        path = f'/remoteDownLog/findByPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def report_signalingAndTelemeryData(data):
        """
        遥信及遥测数据上报
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/report/signalingAndTelemeryData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def role_addRole(data):
        """
        新增角色
        请求参数:
        """
        path = f'/role/addRole'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def role_delRoleByIds(data):
        """
        角色删除/适用于批量删除
        请求参数:
        """
        path = f'/role/delRoleByIds'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def role_findAllRoles():
        """
        查询所有角色
        """
        path = f'/role/findAllRoles'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def role_findRoleMenuId(data):
        """
        角色菜单ID查询
        请求参数:
        """
        path = f'/role/findRoleMenuId'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def role_findRolePermission(data):
        """
        查询角色权限
        """
        path = f'/role/findRolePermission'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def role_findRoles(data):
        """
        角色查询
        请求参数:
        """
        path = f'/role/findRoles'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def role_updateRole(data):
        """
        更新角色
        请求参数:
        """
        path = f'/role/updateRole'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def role_updateRoleMenu(data):
        """
        角色分配菜单
        请求参数:
        """
        path = f'/role/updateRoleMenu'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def role_updateRolePermission(data):
        """
        角色分配权限
        请求参数:
        """
        path = f'/role/updateRolePermission'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def serviceMonitor_RBCserviceRestart():
        """
        站控主机重启
        请求参数:
        """
        path = f'/serviceMonitor/RBCserviceRestart'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def serviceMonitor_serviceRestart():
        """
        服务重启
        """
        path = f'/serviceMonitor/serviceRestart'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def stationInfo_findCities():
        """
        查询所有市级信息
        请求参数:
        """
        path = f'/stationInfo/findCities'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def stationInfo_findDistricts():
        """
        查询所有区级信息
        请求参数:
        """
        path = f'/stationInfo/findDistricts'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def stationInfo_findProvinces():
        """
        查询所有省级信息
        """
        path = f'/stationInfo/findProvinces'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def stationInfo_findSwapData():
        """
        查询换电数据及状态
        """
        path = f'/stationInfo/findSwapData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def stationInfo_getStationConfig():
        """
        getStationConfig
        """
        path = f'/stationInfo/getStationConfig'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def stationInfo_getStationInfo():
        """
        查询换电站基本信息
        """
        path = f'/stationInfo/getStationInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def stationInfo_updateStationInfo(data):
        """
        更新换电站基本信息
        请求参数:
            areaCity: string [可选] - 市
            areaDistrict: string [可选] - 区
            areaLocation: string [可选] - 具体地理位置（换电站地点）
            areaProvince: string [可选] - 省
            belongCompany: string [可选] - 换电站运营公司
            channelNum: integer [可选] - 通道类型(1.左单通道；2.右单通道；3.双通道)
            createTime: string [可选]
            developmentType: integer [可选] - 版本类型： 1.试验站 2.批量站
            id: integer [可选]
            isRemote: integer [可选]
            latitude: number [可选] - 纬度
            longitude: number [可选] - 经度
            maintainCompany: string [可选] - 换电站维保公司
            maintainPhone: string [可选] - 换电站维保联系方式
            manager: string [可选] - 换电站负责人
            manufactureCompany: string [可选] - 换电站制造公司
            manufacturePhone: string [可选] - 换电站运营联系方式
            msgId: integer [可选]
            parameterConfig: string [可选] - 换电站参数
            path: string [可选] - 云端地址
            picture: string [可选] - 图片名称
            platformKey: string [可选] - 平台标识码
            providerCode: string [可选] - 供应商代码
            remark: string [可选] - 备注
            retryCount: integer [可选]
            runEndTime: string [可选] - 运营结束时间
            runStartTime: string [可选] - 运营开始时间
            secret: string [可选] - 云端密钥
            serverNum: integer [可选] - 站控服务数
            socialCid: string [可选] - 社会信用代码
            stationCode: string [可选] - 换电站编号
            stationEnv: integer [可选] - 站控环境(1:预发环境；2:正式环境)
            stationName: string [可选] - 换电站名称
            stationStatus: integer [可选] - 运营状态 0:正常1:歇业2:维修
            stationType: string [可选] - 站类型
            swapMethod: boolean [可选] - 换电模式,0:在线换电、1:离线换电
            telNumber: string [可选] - 换电站负责人联系方式
            updateTime: string [可选]
            versionId: string [可选] - 站控主机版本号
            versionPublicStr: string [可选] - 版本公共匹配串
        """
        path = f'/stationInfo/updateStationInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def stationInfo_uploadPicture(data):
        """
        上传图片
        请求参数:
        """
        path = f'/stationInfo/uploadPicture'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def statisticalCalculation_chargeOrderCount():
        """
        充电订单数量统计
        请求参数:
        """
        path = f'/statisticalCalculation/chargeOrderCount'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def statisticalCalculation_chargeOrderInfoCount():
        """
        充电订单详情统计
        """
        path = f'/statisticalCalculation/chargeOrderInfoCount'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def statisticalCalculation_faultManageCount():
        """
        故障数量统计
        请求参数:
        """
        path = f'/statisticalCalculation/faultManageCount'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def statisticalCalculation_orderManagerCount():
        """
        换电订单数量统计
        请求参数:
        """
        path = f'/statisticalCalculation/orderManagerCount'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def strategyManage_addChargeStrategy(data):
        """
        添加/更新充电策略
        请求参数:
            createTime: string [可选]
            id: integer [可选]
            name: string [可选] - 策略名称
            parentId: integer [可选] - 父级ID
            platformKey: string [可选] - 电站唯一Key
            maxChargeSoc: integer [可选]
            minSwapSoc: integer [可选]
            needSwapCount: integer [可选]
            timeQuantum: array [可选]
                        chargingPowerPercent: number [可选]
                        endLowTime: string [可选]
                        startLowTime: string [可选]
            strategyJson: string [可选] - 策略内容
            strategyType: string [可选] - 策略类型
            updateTime: string [可选]
        """
        path = f'/strategyManage/addChargeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_addTakStrategy(data):
        """
        添加/更新取电策略
        请求参数:
            createTime: string [可选]
            id: integer [可选]
            name: string [可选] - 策略名称
            parentId: integer [可选] - 父级ID
            platformKey: string [可选] - 电站唯一Key
            batteryNumber: integer [可选] - 取电池组数
            minSoc: integer [可选] - 最低soc
            strategyJson: string [可选] - 策略内容
            strategyType: string [可选] - 策略类型
            updateTime: string [可选]
        """
        path = f'/strategyManage/addTakStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_findAirConditioner(data):
        """
        获取空调启停温度
        """
        path = f'/strategyManage/findAirConditioner'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_findAlarmThreshold(data):
        """
        获取温湿度告警阀值
        请求参数:
            pageNum: integer [可选]
            pageSize: integer [可选]
            type: string [可选]
        """
        path = f'/strategyManage/findAlarmThreshold'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_findFanSite(data):
        """
        获取风扇开启关闭时间
        """
        path = f'/strategyManage/findFanSite'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_getAirStrategy():
        """
        获取空调偏差策略
        请求参数:
        """
        path = f'/strategyManage/getAirStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def strategyManage_getStrategy():
        """
        获取取电/充电策略
        请求参数:
        """
        path = f'/strategyManage/getStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def strategyManage_obtainHydrogenRemovalStrategy():
        """
        获取排氢策略
        """
        path = f'/strategyManage/obtainHydrogenRemovalStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def strategyManage_updateAirConditioner(data):
        """
        修改空调启停温度
        请求参数:
            createTime: string [可选]
            id: integer [可选]
            name: string [可选] - 策略名称
            parentId: integer [可选] - 父级ID
            platformKey: string [可选] - 电站唯一Key
            endTemperature: string [可选] - 停止温度
            startTemperature: string [可选] - 启动温度
            strategyJson: string [可选] - 策略内容
            strategyType: string [可选] - 策略类型
            updateTime: string [可选]
        """
        path = f'/strategyManage/updateAirConditioner'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_updateAirDeviation(data):
        """
        修改空调偏差值
        请求参数:
            createTime: string [可选]
            id: integer [可选]
            name: string [可选] - 策略名称
            parentId: integer [可选] - 父级ID
            platformKey: string [可选] - 电站唯一Key
            deviation: integer [可选]
            strategyJson: string [可选] - 策略内容
            strategyType: string [可选] - 策略类型
            updateTime: string [可选]
        """
        path = f'/strategyManage/updateAirDeviation'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_updateAlarmThreshold(data):
        """
        修改温湿度告警阀值
        请求参数:
            createTime: string [可选]
            highOver: string [可选]
            humidityHigh: string [可选]
            humidityOver: string [可选]
            id: integer [可选]
            lowOver: string [可选]
            scode: string [可选]
            sname: string [可选]
            temperatureHigh: string [可选]
            temperatureLow: string [可选]
            updateTime: string [可选]
        """
        path = f'/strategyManage/updateAlarmThreshold'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_updateFanSite(data):
        """
        修改风扇开启关闭时间
        请求参数:
            createTime: string [可选]
            id: integer [可选]
            name: string [可选] - 策略名称
            parentId: integer [可选] - 父级ID
            platformKey: string [可选] - 电站唯一Key
            fanStatus: integer [可选]
            timeQuantum: array [可选]
                        endTime: string [可选]
                        startTime: string [可选]
            strategyJson: string [可选] - 策略内容
            strategyType: string [可选] - 策略类型
            updateTime: string [可选]
        """
        path = f'/strategyManage/updateFanSite'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def strategyManage_updateHydrogenRemovalStrategy():
        """
        更新排氢策略
        请求参数:
        """
        path = f'/strategyManage/updateHydrogenRemovalStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def sysKaptcha_getKaptcha():
        """
        生成验证码
        请求参数:
        """
        path = f'/sysKaptcha/getKaptcha'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def sysVisitorLogs_findSysVisitorLogs(data):
        """
        分页查询操作记录
        请求参数:
            content: string [可选]
            createTime: string [可选]
            description: string [可选]
            endTime: string [可选]
            id: integer [可选]
            module: string [可选]
            operateType: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            startTime: string [可选]
            updateTime: string [可选]
            username: string [可选]
        """
        path = f'/sysVisitorLogs/findSysVisitorLogs'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def systemConfig_getCurrentTime():
        """
        获取当前系统时间
        """
        path = f'/systemConfig/getCurrentTime'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def systemConfig_setServerTime(data):
        """
        设置服务器时间
        请求参数:
            time: string [可选]
        """
        path = f'/systemConfig/setServerTime'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def systemConfig_stopServer(data):
        """
        关闭服务
        """
        path = f'/systemConfig/stopServer'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_batteryStatusTask(data):
        """
        电池状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/batteryStatusTask'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_chargeStrategy(data):
        """
        充电策略定时任务控制
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/chargeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_checkBatteryStatusTask(data):
        """
        电池体检
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/checkBatteryStatusTask'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_lightPeriodStrategy(data):
        """
        灯光分时模式策略
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/lightPeriodStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_outSideLightingStrategy(data):
        """
        站外装饰灯光冬令时夏令时控制策略
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/outSideLightingStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodChangeEquErrorInfo(data):
        """
        供电设备状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodChangeEquErrorInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodChangeEquInfo(data):
        """
        充电设备编号
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodChangeEquInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodDCMeterInfo(data):
        """
        直流电表状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodDCMeterInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodDistributionInfo(data):
        """
        配电设备状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodDistributionInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodFireControlEquInfo(data):
        """
        消防状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodFireControlEquInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodHvacEquInfo(data):
        """
        暖通设备
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodHvacEquInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodPowerStationBatteryErrorInfo(data):
        """
        充电设备故障
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodPowerStationBatteryErrorInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodPowerStationInfo(data):
        """
        运营状态数据
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodPowerStationInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodPowerSupplyInfo(data):
        """
        电池报警故障
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodPowerSupplyInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodRobotEquInfo(data):
        """
        电池更换设备状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodRobotEquInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodRobotStackFireControlEquInfo(data):
        """
        电池更换设备+池转运设备+消防设备
        请求参数:
        """
        path = f'/task/periodRobotStackFireControlEquInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodStackEquInfo(data):
        """
        电池转运设备状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodStackEquInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_periodUPSInfo(data):
        """
        UPS设备状态
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/periodUPSInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def task_thermometerStrategy(data):
        """
        温度控制风扇定时任务
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/task/thermometerStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def temperatureHumidity_exportTemperatureHumidity():
        """
        导出温湿度
        请求参数:
        """
        path = f'/temperatureHumidity/exportTemperatureHumidity'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def temperatureHumidity_findTemperatureHumidity():
        """
        查询温湿度
        """
        path = f'/temperatureHumidity/findTemperatureHumidity'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_addChargeRecord(data):
        """
        充电记录新增
        请求参数:
            batteryNo: string [可选]
            chargeAfterEnergy: number [可选]
            chargeEndTime: string [可选]
            chargeFrontEnergy: number [可选]
            chargeStartTime: string [可选]
            chargeTime: integer [可选]
            createTime: string [可选]
            dcChargerNo: string [可选]
            failCause: integer [可选]
            failCauseDesc: string [可选]
            id: integer [可选]
            isCloud: integer [可选]
            isCloudInfo: string [可选]
            orderId: string [可选]
            outputPower: number [可选]
            outputPower1: number [可选]
            outputPower1End: number [可选]
            outputPower1Start: number [可选]
            outputPower2: number [可选]
            outputPower2End: number [可选]
            outputPower2Start: number [可选]
            outputPower3: number [可选]
            outputPower3End: number [可选]
            outputPower3Start: number [可选]
            outputPower4: number [可选]
            outputPower4End: number [可选]
            outputPower4Start: number [可选]
            plcNo: string [可选]
            startSoc: number [可选]
            stopSoc: number [可选]
            updateTime: string [可选]
        """
        path = f'/test/addChargeRecord'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def test_airConditionerSiteHandler():
        """
        自动开启关闭空调(测试)
        """
        path = f'/test/airConditionerSiteHandler'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_delete(data):
        """
        delete
        请求参数:
        """
        path = f'/test/delete'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'DELETE', data))

    @staticmethod
    def test_downFile():
        """
        downFile
        请求参数:
        """
        path = f'/test/downFile'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_getNewBatteryExchangeStrategy():
        """
        新取电策略接口（2真换2真）
        请求参数:
        """
        path = f'/test/getNewBatteryExchangeStrategy'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_p():
        """
        p
        请求参数:
        """
        path = f'/test/p'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_receiveCarMachineFeedback():
        """
        车机断蓝牙（测试）
        请求参数:
        """
        path = f'/test/receiveCarMachineFeedback'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_resetBatteryFlag():
        """
        重置取电进入标识
        """
        path = f'/test/resetBatteryFlag'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_save(data):
        """
        save
        请求参数:
        """
        path = f'/test/save'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def test_save2(data):
        """
        save2
        请求参数:
        """
        path = f'/test/save2'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def test_select():
        """
        select
        请求参数:
        """
        path = f'/test/select'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_svip():
        """
        svip
        请求参数:
        """
        path = f'/test/svip'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_tastScheduled():
        """
        延迟线程测试
        """
        path = f'/test/tastScheduled'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_testSwitchCabinStatus():
        """
        TestSwitchCabinStatus
        """
        path = f'/test/testSwitchCabinStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def test_update(data):
        """
        update
        请求参数:
        """
        path = f'/test/update'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'PUT', data))

    @staticmethod
    def test_vip():
        """
        vip
        请求参数:
        """
        path = f'/test/vip'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def timeReportData_timeReportData(data):
        """
        定时类数据上报
        请求参数:
            cron: string [可选]
            name: string [可选]
            status: string [可选]
        """
        path = f'/timeReportData/timeReportData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def timeTariff_findPage(data):
        """
        查询分时电价
        请求参数:
            pageNum: integer [可选]
            pageSize: integer [可选]
        """
        path = f'/timeTariff/findPage'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def timeTariff_saveData(data):
        """
        保存分时电价
        请求参数:
            createTime: string [可选]
            delFlag: string [可选]
            endTime: string [可选]
            id: integer [可选]
            price: number [可选]
            startTime: string [可选]
            updateTime: string [可选]
        """
        path = f'/timeTariff/saveData'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def upgrade_getUpgradeDetails(data):
        """
        获取详情
        请求参数:
            batteryNo: string [可选]
            beforeVersionNo: string [可选]
            dccNo: string [可选]
            equNo: string [可选]
            fileName: string [可选]
            id: integer [可选]
            maxRepeatCounts: integer [可选]
            originalFileName: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            remark: string [可选]
            status: integer [可选]
            timeoutInterval: integer [可选]
            type: integer [可选]
            upgradeStartTime: string [可选]
            upgradeStatus: string [可选]
            upgradeUser: string [可选]
            versionNo: string [可选]
        """
        path = f'/upgrade/getUpgradeDetails'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def upgrade_updateResult(data):
        """
        设备升级结果回调
        请求参数:
            equNo: string [可选] - 升级设备编号
            type: integer [可选] - 升级设备类型(1:充电机，2:BMS)
            upgradeResult: integer [可选] - 升级状态(1:升级中，2:升级成功，3:升级失败)
        """
        path = f'/upgrade/updateResult'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def upgrade_upgradeEquipment(data):
        """
        开始升级文件
        请求参数:
            batteryNo: string [可选]
            beforeVersionNo: string [可选]
            dccNo: string [可选]
            equNo: string [可选]
            fileName: string [可选]
            id: integer [可选]
            maxRepeatCounts: integer [可选]
            originalFileName: string [可选]
            pageNum: integer [可选]
            pageSize: integer [可选]
            remark: string [可选]
            status: integer [可选]
            timeoutInterval: integer [可选]
            type: integer [可选]
            upgradeStartTime: string [可选]
            upgradeStatus: string [可选]
            upgradeUser: string [可选]
            versionNo: string [可选]
        """
        path = f'/upgrade/upgradeEquipment'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def upgrade_uploadFile(data):
        """
        升级文件上传
        请求参数:
        """
        path = f'/upgrade/uploadFile'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def upsParamData_getUpsParamDataInfo():
        """
        查询UPS设备信息
        """
        path = f'/upsParamData/getUpsParamDataInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def upsParamData_getUpsParamDataInfoV2():
        """
        查询UPS设备信息V2
        """
        path = f'/upsParamData/getUpsParamDataInfoV2'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'GET', None))

    @staticmethod
    def user_addUser(data):
        """
        新增用户
        请求参数:
        """
        path = f'/user/addUser'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def user_delUserByIds(data):
        """
        用户删除/适用于批量删除
        请求参数:
        """
        path = f'/user/delUserByIds'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def user_findUserInfoByPermission(data):
        """
        查询用户信息和用户权限
        """
        path = f'/user/findUserInfoByPermission'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def user_findUserinfoById(data):
        """
        根据用户id查询
        请求参数:
        """
        path = f'/user/findUserinfoById'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def user_findUsers(data):
        """
        用户查询
        请求参数:
        """
        path = f'/user/findUsers'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def user_passwordValidityPeriod(data):
        """
        设置密码有效期
        请求参数:
            passwordValidityPeriod: integer [可选]
            promptTime: integer [可选]
        """
        path = f'/user/passwordValidityPeriod'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def user_updatePassword(data):
        """
        修改密码
        请求参数:
            cnName: string [可选]
            createTime: string [可选]
            id: integer [可选]
            oldPassword: string [可选]
            password: string [可选]
            password2: string [可选]
            passwordValidityPeriod: integer [可选]
            promptTime: integer [可选]
            roleId: integer [可选]
            roleName: string [可选]
            roles: array [可选]
                        createTime: string [可选]
                        id: integer [可选]
                        permissionIds: string [可选]
                        permissions: array [可选]
                                    allowModify: integer [可选]
                                    createTime: string [可选]
                                    id: integer [可选]
                                    permission: string [可选]
                                    permissionCode: string [可选]
                                    permissionName: string [可选]
                                    updateTime: string [可选]
                        roleDescribe: string [可选]
                        roleName: string [可选]
                        updateTime: string [可选]
            salt: string [可选]
            telphoneNum: string [可选]
            updateTime: string [可选]
            userStatus: integer [可选]
            username: string [可选]
        """
        path = f'/user/updatePassword'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def user_updateUser(data):
        """
        更新用户
        请求参数:
        """
        path = f'/user/updateUser'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))

    @staticmethod
    def user_updateUserRole(data):
        """
        用户分配角色
        请求参数:
        """
        path = f'/user/updateUserRole'
        return HttpRq.req(*HttpMethod.http_info(ApiManager._get_path(path), 'POST', data))
