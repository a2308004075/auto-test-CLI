from common.http.httpRq import HttpRq
from company.qkl.new.common.utils.qklPwd import QKLPwd


class QKLHttp:
    """
    站控请求
    """

    @staticmethod
    def Req(path=None, method: str = None, data=None):
        # 获取其他授权信息

        # 发起HTTP请求
        return HttpRq.req(other_authorization=QKLPwd.get_QKL_linux_pwd(), path=path, method=method, data=data)
