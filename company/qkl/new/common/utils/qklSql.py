from company.qkl.new.common.sh.execSh import ExecSh


class QKLSQL:
    @staticmethod
    def get_timeout(station_type):
        """
        获取超时时间
        """
        cmd_id = 1
        data = [station_type]
        return ExecSh.api_test_sql(cmd_id, data)
