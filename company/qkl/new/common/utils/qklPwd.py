from common.utils.tools.handlerEncrypt import HandlerEncrypt
from common.utils.tools.handlerTime import HandlerTime


class QKLPwd:

    @staticmethod
    def get_QKL_linux_pwd(salt: str = '5ncp31') -> str:
        """
        生成Linux密码（MD5加密后取中间16位）

        Args:
            salt: 盐值，默认为'5ncp31'

        Returns:
            16位密码字符串
        """
        now_date = HandlerTime.get_now_date()
        text = f'{salt}:{now_date}'
        return HandlerEncrypt.md5_encrypt(text)[8:24]
