from common.utils.logConfig import log


class RunKw:
    @staticmethod
    def __run(action_list, keyword, *args):
        """
        执行关键字
        """
        if keyword in action_list:
            return action_list[keyword](*args)
        else:
            log.error(f"Unknown keyword: {keyword}")

    @staticmethod
    def ts_run(action_list, keyword, *args):
        log.info(keyword)
        return RunKw.__run(action_list, keyword, *args)

    @staticmethod
    def act_run(action_list, keyword, *args):
        log.info(f'\raction：{keyword}')
        return RunKw.__run(action_list, keyword, *args)

    @staticmethod
    def api_run(action_list, keyword, *args):
        log.info(f'api：{keyword}')
        return RunKw.__run(action_list, keyword, *args)

    @staticmethod
    def tools_run(action_list, keyword, *args):
        return RunKw.__run(action_list, keyword, *args)
