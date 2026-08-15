from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiVirtualModbus:
    @staticmethod
    def _get_path(path):
        service = '/virtual-modbus'
        return service + path

    @staticmethod
    def modbusVirtual_getCoinsData(data):
        """
        查询线圈数据
        请求参数:
            slaveId: integer [可选] - 从机id
        """
        path = f'/modbusVirtual/getCoinsData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_getHoldingRegistersData(data):
        """
        查询保持寄存器值数据
        请求参数:
            slaveId: integer [可选] - 从机id
        """
        path = f'/modbusVirtual/getHoldingRegistersData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_getInputRegistersData(data):
        """
        查询输入寄存器值数据
        请求参数:
            slaveId: integer [可选] - 从机id
        """
        path = f'/modbusVirtual/getInputRegistersData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_getReadDiscreteInputsData(data):
        """
        查询离散量值数据
        请求参数:
            slaveId: integer [可选] - 从机id
        """
        path = f'/modbusVirtual/getReadDiscreteInputsData'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_initReadHoldingRegisters(data):
        """
        初始化保持寄存器值(PLC)
        """
        path = f'/modbusVirtual/initReadHoldingRegisters'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_updateReadCoils(data):
        """
        更新线圈值
        请求参数:
            id: integer [可选] - 地址
            slaveId: integer [可选] - 从机id
            value: integer [可选] - 值
        """
        path = f'/modbusVirtual/updateReadCoils'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_updateReadDiscreteInputs(data):
        """
        更新离散量值
        请求参数:
            id: integer [可选] - 地址
            slaveId: integer [可选] - 从机id
            value: integer [可选] - 值
        """
        path = f'/modbusVirtual/updateReadDiscreteInputs'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_updateReadHoldingRegisters(data):
        """
        更新保持寄存器值
        请求参数:
            id: integer [可选] - 地址
            slaveId: integer [可选] - 从机id
            value: integer [可选] - 值
        """
        path = f'/modbusVirtual/updateReadHoldingRegisters'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))

    @staticmethod
    def modbusVirtual_updateReadInputRegisters(data):
        """
        更新输入寄存器值
        请求参数:
            id: integer [可选] - 地址
            slaveId: integer [可选] - 从机id
            value: integer [可选] - 值
        """
        path = f'/modbusVirtual/updateReadInputRegisters'
        return HttpRq.req(*HttpMethod.http_info(ApiVirtualModbus._get_path(path), 'POST', data))
