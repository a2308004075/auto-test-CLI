import sys
import os
from loguru import logger
from common.utils.tools.handlerTime import HandlerTime
from common.utils.getProject import GetProject

# 提取日志格式到常量
CONSOLE_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <level>| {level} |{message}</level>"
LOG_FORMAT = "<green>{time: YYYY-MM-DD HH:mm:ss.SSS}</green> <level>| {level} |{message}</level>"

try:
    project_path = GetProject.get_project_path()
    directory = os.path.join(project_path, 'logs')
    logfile = os.path.join(directory, f'{HandlerTime.get_now_date()}.log')

    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
except Exception as e:
    print(f"Error initializing log directory: {e}")
    sys.exit(1)


class LogConfig:
    def __init__(self, level: str = 'TRACE', colorlog: bool = True):
        self.logger = logger
        self._colorlog = colorlog
        self._console_format = CONSOLE_FORMAT
        self._log_format = LOG_FORMAT
        self._level = level
        self.logfile = logfile
        self.set_level(self._colorlog, self._console_format, self._level)

    def set_level(self, colorlog: bool = True, log_format: str = None, level: str = "TRACE"):
        """
        设置level
        :param colorlog:
        :param log_format:
        :param level:
        :return:
        """
        if log_format is None:
            log_format = self._console_format
        # 移除所有处理器
        self.logger.remove()
        self._level = level
        # 添加日志处理器，输出到标准错误
        # colorize支持自定义颜色
        self.logger.add(sys.stderr, level=level, colorize=colorlog, format=log_format)
        # 添加日志处理器，输出到日志文件
        self.logger.add(self.logfile, level=level, colorize=False, format=self._log_format, encoding="utf-8", rotation="1 day")


log_cfg = LogConfig(level="TRACE")

log = logger
