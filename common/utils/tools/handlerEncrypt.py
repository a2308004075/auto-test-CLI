class HandlerEncrypt:
    @staticmethod
    def md5_encrypt(text: str) -> str:
        """
        MD5加密

        Args:
            text: 待加密文本

        Returns:
            MD5加密后的32位十六进制字符串
        """
        md5_obj = hashlib.md5()
        md5_obj.update(text.encode('utf-8'))
        return md5_obj.hexdigest()
