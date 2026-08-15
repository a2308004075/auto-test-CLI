from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiCarStation:
    @staticmethod
    def _get_path(path):
        service = '/car-station'
        return service + path

    @staticmethod
    def api_carStation_feign_carStationInfo_getBlueToothInfo(data):
        """
        共用 获取蓝牙连接信息
        """
        path = f'/api/carStation/feign/carStationInfo/getBlueToothInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_getBluetoothScanInfo(data):
        """
        二代 扫描蓝牙数据
        """
        path = f'/api/carStation/feign/carStationInfo/getBluetoothScanInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_getCarFreedomStatusInfo(data):
        """
        共用 获取车辆自由度信息
        """
        path = f'/api/carStation/feign/carStationInfo/getCarFreedomStatusInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_getCurrentFaultInfo(data):
        """
        getCurrentFaultInfo
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeEnum: string [可选] - 故障上报设备类型
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/carStation/feign/carStationInfo/getCurrentFaultInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_getFastChangeLockStatus(data):
        """
        共用 获取1号电池包和2号电池包的快换锁状态
        """
        path = f'/api/carStation/feign/carStationInfo/getFastChangeLockStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_getLatestBluetoothRpa(data):
        """
        getLatestBluetoothRpa
        """
        path = f'/api/carStation/feign/carStationInfo/getLatestBluetoothRpa'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_getLatestBluetoothScanInfo(data):
        """
        获取最近一次扫描蓝牙数据
        """
        path = f'/api/carStation/feign/carStationInfo/getLatestBluetoothScanInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_getLatestConnectInfo(data):
        """
        getLatestConnectInfo
        """
        path = f'/api/carStation/feign/carStationInfo/getLatestConnectInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_requestForCarInfo(data):
        """
        共用 获取车辆信息
        """
        path = f'/api/carStation/feign/carStationInfo/requestForCarInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_carStationInfo_vehicleSnapshotInfo(data):
        """
        车机快照信息
        """
        path = f'/api/carStation/feign/carStationInfo/vehicleSnapshotInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_cancelCommand(data):
        """
        取消命令
        请求参数:
            cmds: array [可选]
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/cancelCommand'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_clearBbsFault(data):
        """
        清除站控自检故障
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeEnum: string [可选] - 故障上报设备类型
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/carStation/feign/controlCmd/clearBbsFault'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_clearCommand(data):
        """
        清除复位下控
        请求参数:
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/clearCommand'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_clearSubtotalOfBS(data):
        """
        二代 请求清除电池系统小计信息
        """
        path = f'/api/carStation/feign/controlCmd/clearSubtotalOfBS'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_closeAndDisableHVContactor(data):
        """
        共用 请求下高压并禁用上高压
        请求参数:
            commandUniqueKey: string [可选] - 下控唯一码
            controlTimeout: integer [可选] - 下控超时时间(s)
            sendDisableHVContactor: boolean [可选]
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/closeAndDisableHVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_closeLVContactor(data):
        """
        二代 请求下低压
        请求参数:
            commandUniqueKey: string [可选] - 下控唯一码
            controlTimeout: integer [可选] - 下控超时时间(s)
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/closeLVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_connectCarMbmu(data):
        """
        共用 请求蓝牙连接
        请求参数:
            commandUniqueKey: string [可选] - 下控唯一码
            controlTimeout: integer [可选] - 下控超时时间(s)
            irk: string [可选] - irk 默认 FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
            mac: string [可选]
            oob: string [可选]
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/connectCarMbmu'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_disConnectCarMbmu(data):
        """
        共用 请求断开蓝牙连接
        请求参数:
            commandUniqueKey: string [可选] - 下控唯一码
            controlTimeout: integer [可选] - 下控超时时间(s)
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/disConnectCarMbmu'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_mbmuReset(data):
        """
        一代 车机复位
        """
        path = f'/api/carStation/feign/controlCmd/mbmuReset'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_requestOriginPackBack(data):
        """
        一代 下控原包装回
        请求参数:
            originPackList: array [可选] - 待安装pack信息
                        installPackLoc: integer [可选]
                        installPackMAC: string [可选]
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/requestOriginPackBack'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_scanBlueTooth(data):
        """
        二代 请求蓝牙扫描
        请求参数:
            bluetoothScanCommand: integer [可选] - 蓝牙扫描请求信号 未请求蓝牙扫描：0  请求开启蓝牙扫描：1  请求关闭蓝牙扫描：2
            commandUniqueKey: string [可选] - 下控唯一码
            scanKeepTime: integer [可选] - 蓝牙扫描持续时间 单位：秒 1s~254s
            subType: string [可选] - 下控子类型 MANUAL_SCAN_BT(手动蓝牙扫描)
        """
        path = f'/api/carStation/feign/controlCmd/scanBlueTooth'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_selfCheckAndEnableHVContactor(data):
        """
        共用 请求自检且启用上高压
        请求参数:
            commandUniqueKey: string [可选] - 下控唯一码
            controlTimeout: integer [可选] - 下控超时时间(s)
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/selfCheckAndEnableHVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_selfCheckContactor(data):
        """
        二代 请求自检
        请求参数:
            commandUniqueKey: string [可选] - 下控唯一码
            controlTimeout: integer [可选] - 下控超时时间(s)
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/selfCheckContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_sendCarInPlaceStatus(data):
        """
        二代 发送车辆到位状态
        请求参数:
        """
        path = f'/api/carStation/feign/controlCmd/sendCarInPlaceStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_sendHVContactor(data):
        """
        sendHVContactor
        请求参数:
            hvcontactor: integer [可选]
        """
        path = f'/api/carStation/feign/controlCmd/sendHVContactor'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_sendSwapStatus(data):
        """
        二代 发送换电进程
        请求参数:
        """
        path = f'/api/carStation/feign/controlCmd/sendSwapStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_sendToBeInstallBatteryInfo(data):
        """
        一代 发送待安装电池信息
        请求参数:
            changeBatteryRequestDtos: array [可选] - 待安装电池信息
                        changeCmd: integer [可选] - 换电指令 0:未换电；1：开始换电；2：认证失败
                        installAddress: integer [可选] - 安装的位置
                        installNum: integer [可选] - 安装的真包pack个数
                        installPackMac: string [可选] - 安装包mac
            commandUniqueKey: string [可选] - 下控唯一码
            subType: string [可选] - 下控子类型
        """
        path = f'/api/carStation/feign/controlCmd/sendToBeInstallBatteryInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_setPreInstallPackInfo(data):
        """
        二代 设置预安装包信息
        请求参数:
            replacedAmount: integer [可选]
            statusOfPackage1: integer [可选]
            statusOfPackage2: integer [可选]
        """
        path = f'/api/carStation/feign/controlCmd/setPreInstallPackInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_controlCmd_triggerWatchDog(data):
        """
        触发看门狗
        请求参数:
            trigger: integer [可选] - 用于触发软件看门狗功能
        """
        path = f'/api/carStation/feign/controlCmd/triggerWatchDog'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_carStation_feign_v1_carStationInfo_getVehicleSelfCheckInfo(data):
        """
        一代 自检结果查询
        """
        path = f'/api/carStation/feign/v1/carStationInfo/getVehicleSelfCheckInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_sbleStatus(data):
        """
        sbleStatus
        """
        path = f'/api/equipment/sbleStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def config_configIp(data):
        """
        请求设置ip
        请求参数:
            ip: string [可选] - 连接ip
            localIp: string [可选] - 设置SBLE本地IP
            localPort: integer [可选] - 设置SBLE本地端口
            port: integer [可选] - 连接端口
            serverIp: string [可选] - 设置服务器IP
            serverPort: integer [可选] - 设置服务器端口
            subnetMask: string [可选] - 设置子网掩码
        """
        path = f'/config/configIp'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def controlCommand_allAliveTask():
        """
        所有存活的任务
        """
        path = f'/controlCommand/allAliveTask'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'GET', None))

    @staticmethod
    def controlCommand_cancelAll(data):
        """
        取消所有命令任务
        """
        path = f'/controlCommand/cancelAll'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def controlCommand_closeAndDisableHVContactorResult():
        """
        请求下高压执行结果
        """
        path = f'/controlCommand/closeAndDisableHVContactorResult'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'GET', None))

    @staticmethod
    def controlCommand_closeLVContactorResult():
        """
        请求下低压执行结果
        """
        path = f'/controlCommand/closeLVContactorResult'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'GET', None))

    @staticmethod
    def controlCommand_connectCarMbmuResult():
        """
        请求蓝牙连接执行结果
        """
        path = f'/controlCommand/connectCarMbmuResult'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'GET', None))

    @staticmethod
    def controlCommand_disConnectCarMbmuResult():
        """
        请求蓝牙断开执行结果
        """
        path = f'/controlCommand/disConnectCarMbmuResult'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'GET', None))

    @staticmethod
    def controlCommand_selfCheckResult():
        """
        请求自检执行结果
        """
        path = f'/controlCommand/selfCheckResult'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'GET', None))

    @staticmethod
    def nettyChannel_closeChannel():
        """
        关闭通道
        """
        path = f'/nettyChannel/closeChannel'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'GET', None))

    @staticmethod
    def v3_test_tools_configIp(data):
        """
        请求设置ip
        请求参数:
            ip: string [可选] - 连接ip
            localIp: string [可选] - 设置SBLE本地IP
            localPort: integer [可选] - 设置SBLE本地端口
            port: integer [可选] - 连接端口
            sbleGateWay: string [可选] - 设置SBLE网关
            serverIp: string [可选] - 设置服务器IP
            serverPort: integer [可选] - 设置服务器端口
            subnetMask: string [可选] - 设置子网掩码
        """
        path = f'/v3/test/tools/configIp'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))

    @staticmethod
    def v3_test_tools_triggerWatchDog(data):
        """
        触发看门狗
        请求参数:
            trigger: integer [可选] - 用于触发软件看门狗功能
        """
        path = f'/v3/test/tools/triggerWatchDog'
        return HttpRq.req(*HttpMethod.http_info(ApiCarStation._get_path(path), 'POST', data))
