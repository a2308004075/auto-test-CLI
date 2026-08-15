class KwDecorator:
    """
    一个装饰器类，用于为函数添加关键字描述属性。

    属性:
        description (str): 要添加的关键字描述。
    """

    def __init__(self, description):
        """
        使用特定的关键字描述初始化装饰器。

        参数:
            description (str): 要添加的关键字描述。
        """
        if not isinstance(description, str):
            raise ValueError("description 必须是字符串")
        self.description = description

    def __call__(self, func):
        """
        当装饰器被调用时，它将关键字描述作为属性添加到函数并返回该函数。

        参数:
            func (function): 要装饰的函数。

        返回:
            function: 带有添加的关键字描述属性的装饰函数。
        """
        if not self.description:
            raise ValueError("description 不能为空字符串")
        func.keyword_description = self.description
        return func
