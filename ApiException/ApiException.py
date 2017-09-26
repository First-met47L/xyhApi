class ElemException(Exception):
    @staticmethod
    def __new__(*args, **kwargs):
        return Exception.__new__(*args, **kwargs)

    def __init__(self, msg="Parameter is illegal"):
        super(ElemException, self).__init__(msg)


class ElemTypeException(ElemException):
    @staticmethod
    def __new__(*args, **kwargs):
        return Exception.__new__(*args, **kwargs)

    def __init__(self, msg="Elem's type illegal"):
        super(ElemTypeException, self).__init__(msg=msg)


