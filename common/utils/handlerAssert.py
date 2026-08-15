class HandlerAssert:
    @staticmethod
    def equal(result, expect):
        assert result == expect

    @staticmethod
    def not_equal(result, expect):
        assert result != expect

    @staticmethod
    def include(result, expect):
        assert result in expect

    @staticmethod
    def not_include(result, expect):
        assert result not in expect

    @staticmethod
    def true(result):
        assert result

    @staticmethod
    def not_true(result):
        assert not result
