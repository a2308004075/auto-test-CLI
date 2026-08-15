from common.http.httpMethod import HttpMethod
from common.http.httpRq import HttpRq


class ExecSh:
    @staticmethod
    def _get_path(path):
        service = "/autotest"
        return service + path

    @staticmethod
    def api_test_shell(cmd_id, params: dict = None):
        """
        执行shell
        """
        path = "/api/test/shell"
        if params:
            data = {
                "id": cmd_id,
                "params": params
            }
        else:
            data = {
                "id": cmd_id
            }

        return HttpRq.req(HttpMethod.http_info(ExecSh._get_path(path), 'POST', data))

    @staticmethod
    def api_test_sql(cmd_id, params: list = None):
        """
        执行sql
        """
        path = "/api/test/sql"
        if params:
            data = {
                "id": cmd_id,
                "params": params
            }
        else:
            data = {
                "id": cmd_id
            }
        return HttpRq.req(HttpMethod.http_info(ExecSh._get_path(path), 'POST', data))
