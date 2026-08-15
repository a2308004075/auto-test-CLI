from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiCamera:
    @staticmethod
    def _get_path(path):
        service = '/camera'
        return service + path

    @staticmethod
    def api_algorithm_optimumChargingMapping(data):
        """
        最优充电映射
        请求参数:
            campTemp: number [可选] - 仓内温度
            maxModuleTemp: number [可选] - 最大模组温度
            maxRealSoc: number [可选] - 最大真实soc
            minModuleTemp: number [可选] - 最小模组温度
            minRealSoc: number [可选] - 最小真实soc
            packLabel: string [可选] - 电池标签
            packSn: string [可选] - 电池barcode
            packType: integer [可选] - 电池类型
            soh: number [可选] - 电池SOH
            stationBusyFlag: integer [可选] - 换电站闲忙标志 0-闲 1-忙
            targetChargeTime: integer [可选] - 目标充电时间
            targetSoc: number [可选] - 目标soc
        """
        path = f'/api/algorithm/optimumChargingMapping'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_algorithm_queryChargeLimitMin(data):
        """
        查询充电限制最小值
        请求参数:
            envTemp: number [可选] - 环境温度
            maxModuleTemp: number [可选] - 最大模组温度
            minModuleTemp: number [可选] - 最小模组温度
            soc: number [可选] - 当前soc
        """
        path = f'/api/algorithm/queryChargeLimitMin'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_algorithm_queryChargeLimitMins(data):
        """
        查询多个充电限制最小值
        请求参数:
            params: array [可选] - 参数
                        campNo: integer [可选] - 仓位号
                        envTemp: number [可选] - 仓内温度
                        maxModuleTemp: number [可选] - 最大模组温度
                        minModuleTemp: number [可选] - 最小模组温度
                        soc: number [可选] - 当前soc
        """
        path = f'/api/algorithm/queryChargeLimitMins'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_algorithm_uninstallPackLocation(data):
        """
        拆卸电池包位置变化
        请求参数:
            flowNo: string [可选] - 订单号
            packSn: string [可选] - 电池sn
            uninstallPackLocation: integer [可选] - 拆卸电池位置
        """
        path = f'/api/algorithm/uninstallPackLocation'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_camera_initAndLogin(data):
        """
        初始化登录抓拍机
        """
        path = f'/api/camera/initAndLogin'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_camera_isYiboCamera():
        """
        是否为艺博相机
        """
        path = f'/api/camera/isYiboCamera'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'GET', None))

    @staticmethod
    def api_camera_logoutAndCleanup(data):
        """
        登出抓拍机
        """
        path = f'/api/camera/logoutAndCleanup'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_camera_ocrPicture(data):
        """
        OCR识别图片
        请求参数:
            filepath: string [可选] - 文件路径
        """
        path = f'/api/camera/ocrPicture'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_camera_reTakePicture(data):
        """
        重新拍照
        请求参数:
            cameraSubTypeEnum: string [可选] - 下控子类型
        """
        path = f'/api/camera/reTakePicture'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_camera_sendBrodAreaLed(data):
        """
        发送区域广播LED
        请求参数:
            ledAreaContent1: string [可选] - LED显示屏区域1显示内容
            ledAreaContent2: string [可选] - LED显示屏区域2显示内容
            ledAreaContent3: string [可选] - LED显示屏区域3显示内容
            ledAreaContent4: string [可选] - LED显示屏区域4显示内容
            ledVoiceContent: string [可选] - LED播报语音内容
        """
        path = f'/api/camera/sendBrodAreaLed'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_camera_sendBrodLed(data):
        """
        发送广播LED
        请求参数:
            ledDisplayContent: string [可选] - LED显示屏显示内容
            ledVoiceContent: string [可选] - LED播报语音内容
        """
        path = f'/api/camera/sendBrodLed'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_camera_sendBrodLedList(data):
        """
        发送广播LED列表
        请求参数:
            displayList: array [可选] - LED显示语音内容
                        area: integer [可选] - 区域1~4
                        context: string [可选] - 文本
                        nheight: string [可选]
                        nwidth: string [可选]
                        nx: string [可选]
                        ny: string [可选]
                        textColor: integer [可选] - 文本颜色
                        textStyle: integer [可选] - 文本动作方式 0x01：精致显示 0x0c：滚动 0x20:连续滚动
            ledVoiceContent: string [可选] - LED播报语音内容
        """
        path = f'/api/camera/sendBrodLedList'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_camera_settingOnOff(data):
        """
        设置LED开关
        请求参数:
            onOff: integer [可选] - LED显示屏开关
        """
        path = f'/api/camera/settingOnOff'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_eparking_camera_disConnect(data):
        """
        登出易泊抓拍机
        请求参数:
            pcameraIP: string [可选]
        """
        path = f'/api/eparking/camera/disConnect'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_eparking_camera_initEparkingCamera(data):
        """
        初始化连接易泊抓拍机
        """
        path = f'/api/eparking/camera/initEparkingCamera'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_getCurrentFaultInfo(data):
        """
        获取当前故障信息
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeEnum: string [可选] - 故障上报设备类型
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/equipment/getCurrentFaultInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_intrusionStatus(data):
        """
        获取入侵状态
        """
        path = f'/api/equipment/intrusionStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_equipment_status(data):
        """
        获取设备状态
        """
        path = f'/api/equipment/status'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_fault_clearFault(data):
        """
        清除故障
        请求参数:
            deviceNo: integer [可选] - 设备ID
            faultCode: string [可选] - 故障编码
            faultTypeEnum: string [可选] - 故障上报设备类型
            originFaultCode: string [可选] - 原始故障编码
        """
        path = f'/api/fault/clearFault'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_video_analyzeAngle(data):
        """
        分析角度
        请求参数:
            cameraSubTypeEnum: string [可选] - 下控子类型
            msgId: string [可选]
        """
        path = f'/api/video/analyzeAngle'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_video_analyzeBrightness(data):
        """
        环境亮度分析
        请求参数:
            cameraSubTypeEnum: string [可选] - 下控子类型
            msgId: string [可选]
        """
        path = f'/api/video/analyzeBrightness'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_video_analyzeCentering(data):
        """
        分析对中
        请求参数:
            cameraSubTypeEnum: string [可选] - 下控子类型
            msgId: string [可选]
        """
        path = f'/api/video/analyzeCentering'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_video_analyzeVehicleDirection(data):
        """
        分析车辆方向
        """
        path = f'/api/video/analyzeVehicleDirection'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))

    @staticmethod
    def api_video_takePic(data):
        """
        拍照
        请求参数:
            commandSubType: string [可选]
            commandType: string [可选]
            fileName: string [可选]
            videoNos: array [可选]
        """
        path = f'/api/video/takePic'
        return HttpRq.req(*HttpMethod.http_info(ApiCamera._get_path(path), 'POST', data))
