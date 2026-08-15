from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.common.ncs.virtual_plc import VirtualPlc


class NcsVirtualPlc:
    """
    nacos配置virtual-plc
    """

    @staticmethod
    @KwDecorator("nacos获取virtual-plc")
    def virtual_plc_get():
        return VirtualPlc.virtual_plc_get()

    @staticmethod
    @KwDecorator("nacos配置virtual-plc：默认配置")
    def virtual_plc_post_1():
        content = """caes:
  swap:
    redis:
      keyPrefix: virtual_plc
      enable: true
    swagger:
      controllerPackage: com.caes.bss.virtual.plc.server
    netty:
      servers:
        - id: virtualPlcServer
          host: 0.0.0.0
          port: 11000
          initType: virtualPlcServerInitType
        - id: plcModbusTcpServer
          host: 0.0.0.0
          port: 503
          initType: plcModbusTcpInitType
        - id: tandhsensor
          host: 0.0.0.0
          port: 515
          initType: plcModbusTcpInitType 
        - id: air
          host: 0.0.0.0
          port: 516
          initType: plcModbusTcpInitType 
        - id: fire
          host: 0.0.0.0
          port: 517
          initType: plcModbusTcpInitType 
        - id: electric
          host: 0.0.0.0
          port: 518
          initType: plcModbusTcpInitType 
        - id: temAndHum
          host: 0.0.0.0
          port: 519
          initType: plcModbusTcpInitType 
        - id: heater
          host: 0.0.0.0
          port: 520
          initType: plcModbusTcpInitType 
        - id: ups
          host: 0.0.0.0
          port: 521
          initType: plcModbusTcpInitType 
        - id: fan
          host: 0.0.0.0
          port: 522
          initType: plcModbusTcpInitType 
        - id: mainControlAir
          host: 0.0.0.0
          port: 523
          initType: plcModbusTcpInitType 
      clients:
        - id: 1
          host: 127.0.0.1
          port: 10002
          reconnectSeconds: 10
          initType: plc_netty_init_type
callback:
    isAutoCallBack: false
    delayTime : 2000
    delayTime001 : 2000
    delayTime002 : 2000
    delayTime003 : 2000
    delayTime004 : 2000
    delayTime005 : 2000
    delayTime006 : 29995
    delayTime0022 : 2000
    delayTime0025 : 2000
    delayTimeForGeneration: 10000
virtualModbus:
    slaveIdConfig: 1
    pointNum: 500
        """
        return VirtualPlc.virtual_plc_post(content)
