from common.http.httpRq import HttpRq
from common.http.httpMethod import HttpMethod


class ApiVideo:
    @staticmethod
    def _get_path(path):
        service = '/video'
        return service + path

    @staticmethod
    def api_video_control_addPlayer(data):
        """
        添加播放语音
        请求参数:
            desc: string [可选] - 描述
            duplicateRemoval: integer [可选] - 是否去重 1：是 0：否
            levelCode: integer [可选] - 语音等级 0~5
            mp3Code: integer [可选] - mp3编码
            vol: integer [可选] - 音量（0~100）
        """
        path = f'/api/video/control/addPlayer'
        return HttpRq.req(*HttpMethod.http_info(ApiVideo._get_path(path), 'POST', data))

    @staticmethod
    def api_video_control_pauseSinglePlayer(data):
        """
        暂停播放（单例）
        请求参数:
            mp3Code: integer [可选] - mp3编码
        """
        path = f'/api/video/control/pauseSinglePlayer'
        return HttpRq.req(*HttpMethod.http_info(ApiVideo._get_path(path), 'POST', data))

    @staticmethod
    def api_video_control_resumeSinglePlayer(data):
        """
        恢复播放（单例）
        请求参数:
            mp3Code: integer [可选] - mp3编码
        """
        path = f'/api/video/control/resumeSinglePlayer'
        return HttpRq.req(*HttpMethod.http_info(ApiVideo._get_path(path), 'POST', data))

    @staticmethod
    def api_video_control_startSinglePlayer(data):
        """
        开启播放（单例）
        请求参数:
            desc: string [可选] - 描述
            duplicateRemoval: integer [可选] - 是否去重 1：是 0：否
            levelCode: integer [可选] - 语音等级 0~5
            mp3Code: integer [可选] - mp3编码
            vol: integer [可选] - 音量（0~100）
        """
        path = f'/api/video/control/startSinglePlayer'
        return HttpRq.req(*HttpMethod.http_info(ApiVideo._get_path(path), 'POST', data))

    @staticmethod
    def api_video_control_stopSinglePlayer(data):
        """
        停止播放（单例）
        请求参数:
            mp3Code: integer [可选] - mp3编码
        """
        path = f'/api/video/control/stopSinglePlayer'
        return HttpRq.req(*HttpMethod.http_info(ApiVideo._get_path(path), 'POST', data))
