from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.common.ncs.virtual_battery import VirtualBattery


class NcsVirtualBattery:
    """
    nacos操作virtual-battery
    """

    @staticmethod
    @KwDecorator("nacos获取virtual-battery")
    def virtual_battery_get():
        return VirtualBattery.virtual_battery_get()

    @staticmethod
    @KwDecorator("nacos配置virtual-battery：默认配置")
    def virtual_battery_post_1():
        content = """caes:
  swap:
    config:
      heartNormal: true
      ## 多包是否响应
      respMultiPack: true
      ## 多包是否是新协议
      newPro: true
    swagger:
      controllerPackage: com.caes.bss.virtual.battery.server
    redis:
      keyPrefix: virtual_battery
#新增下控自动响应配置
command-result:
  msg026:
    #站内小计信息清除结果  0 "默认" 1 "失败" 2 "成功"
    subInfoInClrSts: 2
    #站外小计信息清除结果  0 "默认" 1 "失败" 2 "成功"
    subInfoOutClrSts: 2
    #反馈电池包出仓请求结果  0 "默认" 1 "Ready"
    battyOutStaSts: 2
    #电池包下高压结果  0 "默认" 1 "失败" 2 "成功"
    pACKHVOpenSts: 2
    #故障清除结果  0 "默认" 1 "失败" 2 "成功"
    fltClearingSts: 2
        """
        return VirtualBattery.virtual_battery_post(content)
