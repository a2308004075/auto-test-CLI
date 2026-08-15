from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.common.ncs.virtual_car_station import VirtualCarStation


class NcsVirtualCarStation:
    """
    nacos操作virtual-car-station
    """

    @staticmethod
    @KwDecorator("nacos获取virtual-car-station")
    def virtual_car_station_get():
        return VirtualCarStation.virtual_car_station_get()

    @staticmethod
    @KwDecorator("nacos配置virtual-car-station：默认配置")
    def virtual_car_station_post_1():
        content = """caes:
  swap:
    config:
    # MBMU心跳：true 心跳会变化 false不会变化
      heartNormal112: true
      heartNormal105: true
      heartNormal12D: true
      heartNormal12F: true
    netty:
      #一代配置
      servers:
        - host: 0.0.0.0
          port: 4001
          initType: v3NettyServerInitializer
          id: 1
        - host: 0.0.0.0
          port: 4001
          initType: v1NettyServerInitializer
          id: 1
      #二代配置
      clients:
        - nettyClientId: 1
          enable: true
          host: 0.0.0.0
          port: 10003
          reconnectSeconds: 10
          initType: virtual_car_station
###下控命令执行结果         
commandResult:
  ##请求蓝牙连接
  msg0205:
    # 执行失败：1，执行成功：2
    resultCode: 2
    #无故障/无法识别故障：0 故障码：1~254
    errorCode: 0
    #是否模拟响应超时：false-正常响应，true-超时响应
    mockTimeout: false
    #模拟响应开关：true：开启自动响应 false：不自动响应
    autoCallBack: true
  ##请求下高压
  msg0216:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求下低压
  msg0218:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求自检
  msg021A:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求清除电池系统小计信息
  msg021E:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求蓝牙断开
  msg0220:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求蓝牙扫描
  msg0224:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
"""
        return VirtualCarStation.virtual_car_station_post(content)

    @staticmethod
    @KwDecorator("nacos配置virtual-car-station：修改heartNormal12F")
    def virtual_car_station_post_2():
        content = """caes:
  swap:
    config:
    # MBMU心跳：true 心跳会变化 false不会变化
      heartNormal112: true
      heartNormal105: true
      heartNormal12D: true
      heartNormal12F: false
    netty:
      #一代配置
      servers:
        - host: 0.0.0.0
          port: 4001
          initType: v3NettyServerInitializer
          id: 1
        - host: 0.0.0.0
          port: 4001
          initType: v1NettyServerInitializer
          id: 1
      #二代配置
      clients:
        - nettyClientId: 1
          enable: true
          host: 0.0.0.0
          port: 10003
          reconnectSeconds: 10
          initType: virtual_car_station
###下控命令执行结果         
commandResult:
  ##请求蓝牙连接
  msg0205:
    # 执行失败：1，执行成功：2
    resultCode: 2
    #无故障/无法识别故障：0 故障码：1~254
    errorCode: 0
    #是否模拟响应超时：false-正常响应，true-超时响应
    mockTimeout: false
    #模拟响应开关：true：开启自动响应 false：不自动响应
    autoCallBack: true
  ##请求下高压
  msg0216:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求下低压
  msg0218:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求自检
  msg021A:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求清除电池系统小计信息
  msg021E:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求蓝牙断开
  msg0220:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
  ##请求蓝牙扫描
  msg0224:
    resultCode: 2
    errorCode: 0
    mockTimeout: false
    autoCallBack: true
"""
        return VirtualCarStation.virtual_car_station_post(content)
