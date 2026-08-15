from common.handlerKw.kwDecorator import KwDecorator
from company.qkl.new.common.ncs.virtual_dcci import VirtualDcci


class NcsVirtualDcci:
    """
    nacos操作virtual-dcci
    """

    @staticmethod
    @KwDecorator("nacos获取virtual-dcci")
    def virtual_dcci_get():
        return VirtualDcci.virtual_dcci_get()

    @staticmethod
    @KwDecorator("nacos配置virtual-dcci：默认配置")
    def virtual_dcci_post_1():
        content = """caes:
  swap:
    redis:
      keyPrefix: virtual_dcci
      enable: true
    swagger:
      controllerPackage: com.caes.bss.virtual.dcci.server
callback:
    isAutoCallBack: true
    delayTime : 3000
virtual:
  authAutoFail: false
        """
        return VirtualDcci.virtual_dcci_post(content)
