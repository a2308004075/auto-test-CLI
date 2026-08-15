from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiDccPdu:
    @staticmethod
    def _get_path(path):
        service = '/dcc-pdu'
        return service + path

    @staticmethod
    def dcc_pdu_offline_stop_charge(data):
        """
        监控平台下发掉线停止充电
        请求参数:
            chargeNo: string [可选] - 充电机编号 充电桩
            resultEnableFlag: integer [可选] - 0：不使能 1：使能
        """
        path = f'/dcc/pdu/offline/stop/charge'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))

    @staticmethod
    def dcc_pdu_set_charge_rate(data):
        """
        监控平台下发充电速率设置
        请求参数:
            chargeNo: string [可选]
            chargeRate: number [可选] - 倍率，范围0.1到1
        """
        path = f'/dcc/pdu/set/charge/rate'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))

    @staticmethod
    def dcc_pdu_set_work_power(data):
        """
        监控平台发送功率调节指令
        请求参数:
            chargeNo: string [可选] - 充电机编号 充电桩+枪组合
            expectPower: number [可选] - 期望功率（发送多少，充电机接收就是多少KW）
        """
        path = f'/dcc/pdu/set/work/power'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))

    @staticmethod
    def dcc_pdu_start_charge(data):
        """
        远程启动充电
        请求参数:
            chargeNo: string [可选] - 充电机编号
            chargingPowerPercent: number [可选] - 充电功率百分比 0到100
            controlSource: integer [可选]
            powerParam: number [可选] - 功率调节参数(启用功率百分比后此字段废弃)
            soc: integer [可选]
        """
        path = f'/dcc/pdu/start/charge'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))

    @staticmethod
    def dcc_pdu_stop_charge(data):
        """
        远程停止充电
        请求参数:
            chargeNo: string [可选]
            controlSource: integer [可选]
            stopReason: integer [可选]
        """
        path = f'/dcc/pdu/stop/charge'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))

    @staticmethod
    def dcc_pdu_tftp_charger_chargerTcuUpgrade(data):
        """
        站级监控下发升级请求
        请求参数:
            chargeNo: integer [必填] - 充电机/电桩编号
            filePath: string [必填] - 文件路径
            upgradeId: integer [必填] - 升级记录ID
        """
        path = f'/dcc/pdu/tftp/charger/chargerTcuUpgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))

    @staticmethod
    def dcc_pdu_tftp_charger_queryVersion(data):
        """
        监控平台下发版本号查询
        请求参数:
        """
        path = f'/dcc/pdu/tftp/charger/queryVersion'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))

    @staticmethod
    def dcc_pdu_tftp_charger_status(data):
        """
        监控平台下发版本号查询
        """
        path = f'/dcc/pdu/tftp/charger/status'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))

    @staticmethod
    def dcc_pdu_tftp_charger_upgrade(data):
        """
        站级监控升级请求下发
        请求参数:
            chargeNo: string [必填] - 充电机/电桩编号
            fileName: string [必填] - 文件名
            fileSize: integer [必填] - 文件大小
            maxRepeatCounts: integer [必填] - 最大重传次数
            timeoutInterval: integer [必填] - 超时间隔
            verifyValue: string [必填] - MD5校验值
            version: string [必填] - 版本号
        """
        path = f'/dcc/pdu/tftp/charger/upgrade'
        return HttpRq.req(*HttpMethod.http_info(ApiDccPdu._get_path(path), 'POST', data))
