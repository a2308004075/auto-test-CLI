import pytz
from datetime import datetime


class HandlerTime:
    @staticmethod
    def time_now_timestamp():
        timestamp = int(datetime.now().timestamp())
        return timestamp

    @staticmethod
    def time_now_time():
        current_time = datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S.%f')
        return current_time

    @staticmethod
    def get_now_date() -> str:
        """
        获取当前日期字符串

        Returns:
            格式为 'YYYY-MM-DD' 的日期字符串
        """
        return datetime.now().strftime("%Y-%m-%d")
