from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiCloud:
    @staticmethod
    def _get_path(path):
        service = '/cloud'
        return service + path

    @staticmethod
    def batteryPhotographyUpload(data):
        """
        电池底部拍照上传
        请求参数:
            batteryInfoList: array [可选]
                        batteryLocation: integer [可选]
                        packMac: string [可选]
                        packSn: string [可选]
                        photoUrls: string [可选]
            carNo: string [可选]
            orderId: string [可选]
            vin: string [可选]
        """
        path = f'/batteryPhotographyUpload'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))

    @staticmethod
    def getOssToken(data):
        """
        请求获取电池拍照ossToken
        请求参数:
            upType: integer [可选]
        """
        path = f'/getOssToken'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))

    @staticmethod
    def reportStationBaseInfo(data):
        """
        上报站控基本信息
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
        path = f'/reportStationBaseInfo'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))

    @staticmethod
    def test_batteryLabelRequest(data):
        """
        batteryLabelRequest
        请求参数:
        """
        path = f'/test/batteryLabelRequest'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))

    @staticmethod
    def test_handleClearBmsFault(data):
        """
        handleClearBmsFault
        请求参数:
            clear: integer [可选]
            deviceCodes: array [可选]
            msgId: integer [可选]
        """
        path = f'/test/handleClearBmsFault'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))

    @staticmethod
    def test_handleOtaControl(data):
        """
        handleOtaControl
        请求参数:
            deviceCodes: array [可选]
            deviceType: string [可选]
            driveVersion: string [可选]
            driveVersionPack: string [可选]
            firmwareVersion: string [可选]
            firmwareVersionPack: string [可选]
            msgId: integer [可选]
            systemVersions: array [可选]
            upgradeType: string [可选]
        """
        path = f'/test/handleOtaControl'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))

    @staticmethod
    def test_handlerStationLabelResp(data):
        """
        handlerStationLabelResp
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
        path = f'/test/handlerStationLabelResp'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))

    @staticmethod
    def test_queryStationLable(data):
        """
        queryStationLable
        """
        path = f'/test/queryStationLable'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))

    @staticmethod
    def test_swapAuthentication(data):
        """
        swapAuthentication
        请求参数:
            plateNo: string [可选] - 车牌号
        """
        path = f'/test/swapAuthentication'
        return HttpRq.req(*HttpMethod.http_info(ApiCloud._get_path(path), 'POST', data))
