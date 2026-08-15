from company.qkl.new.common.sh.execSh import ExecSh


class QKLSh:
    @staticmethod
    def current_time():
        """
        获取当前时间
        """
        cmd_id = 1
        return ExecSh.api_test_shell(cmd_id)

    @staticmethod
    def get_log(start_time: str, end_time: str, log_file: str):
        """
        获取指定时间日志
        start_time：2025-04-29 10:00:00
        end_time：2025-04-29 10:06:00
        log_file：/logs/svc-swap-flow/all/all-svc-swap-flow.log
        """
        cmd_id = 2
        params = {
            "start_time": start_time,
            "end_time": end_time,
            "log_file": log_file
        }
        return ExecSh.api_test_shell(cmd_id, params)
