class ParamException(Exception):
    @staticmethod
    def __new__(*args, **kwargs):
        return Exception.__new__(*args, **kwargs)

    def __init__(self, msg="Parameter is illegal"):
        super(ParamException, self).__init__(msg)


class ParamTypeException(ParamException):
    @staticmethod
    def __new__(*args, **kwargs):
        return Exception.__new__(*args, **kwargs)

    def __init__(self, msg="Parameter's type illegal"):
        super(ParamTypeException, self).__init__(msg=msg)


