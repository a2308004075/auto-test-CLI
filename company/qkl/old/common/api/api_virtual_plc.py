from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiVirtualPlc:
    @staticmethod
    def _get_path(path):
        service = '/virtual-plc'
        return service + path

    @staticmethod
    def plcMock_changeStatus(data):
        """
        plc模式和状态修改
        请求参数:
            autoMode: integer [可选] - 40001PLC自动模式
            carHasLeft: integer [可选] - 40004车已完全离开
            carInVGroove: integer [可选] - 40004车停好在V槽
            localMode: integer [可选] - 40001PLC本地模式
            manualMode: integer [可选] - 40001PLC手动模式
            remoteMode: integer [可选] - 40001PLC远程模式
            swapDeviceStatus: integer [可选] - 40011点位换电设备运行状态
            swapProcessStatus: integer [可选] - 40006点位（换电流程状态）
            taskStatus: integer [可选] - 40002点位任务状态
        """
        path = f'/plcMock/changeStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def plcMock_getRegisters(data):
        """
        获取寄存器值
        """
        path = f'/plcMock/getRegisters'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def plcMock_updateBarrierGateStatus(data):
        """
        修改道闸开启状态
        请求参数:
            backGateCloseStatus: integer [可选] - 出口道闸关闭状态
            backGateOpenStatus: integer [可选] - 出口道闸开启状态
            frontGateCloseStatus: integer [可选] - 入口道闸关闭状态
            frontGateOpenStatus: integer [可选] - 入口道闸开启状态
        """
        path = f'/plcMock/updateBarrierGateStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def plcMock_updateCampInStatus(data):
        """
        修改仓位状态
        请求参数:
            itemDTOList: array [可选] - 仓位在位状态列表 40020-40022（R1-48仓电池在位）
                        inPlace: integer [可选] - 在位状态
                        position: integer [可选] - 仓位
        """
        path = f'/plcMock/updateCampInStatus'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))

    @staticmethod
    def plcMock_updateRegisters(data):
        """
        更新寄存器值
        请求参数:
            id: integer [可选] - 地址
            value: integer [可选] - 值
        """
        path = f'/plcMock/updateRegisters'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualPlc._get_path(path), 'POST', data))
