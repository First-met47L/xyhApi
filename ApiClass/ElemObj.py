from ApiClass.Field import BaseField
from ApiClass.Field import IntegerField
from ApiException.ApiException import ElemTypeException


class ElemMeta(type):

    def __new__(cls, name, bases, namespace):
        if name == 'BaseElemObj':
            return super(ElemMeta, cls).__new__(cls, name, bases, namespace)
        __mapping__ = dict()
        for key, value in namespace.items():
            if isinstance(value, BaseField):
                __mapping__[key] = value
        for key in __mapping__.keys():
            namespace.pop(key)
        namespace['__mapping__'] = __mapping__
        return super(ElemMeta, cls).__new__(cls, name, bases, namespace)


class BaseElemObj(dict, metaclass=ElemMeta):

    def __init__(self, **kwargs):
        mapping = self.__mapping__
        for k, v in kwargs.items():
            field = mapping.get(k, None)
            if not field:
                continue
            if not isinstance(v, field.type):
                raise ElemTypeException(r"Elem(%s) must be %s,but current type is %s" % (k, field.type, type(v)))
        super(BaseElemObj, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'ElemObj' object has not attribute call (%s)" %item)

    def __setattr__(self, key, value):
        field = self.__mapping__.get(key,None)
        if not field or not isinstance(value,field.type):
            raise ElemTypeException(r"Elem(%s) must be %s,but current type is %s" % (key, field.type, type(value)))
        self[key] = value

    def __setitem__(self, key,value):
        field = self.__mapping__.get(key, None)
        if not field or not isinstance(value, field.type):
            raise ElemTypeException(r"Elem(%s) must be %s,but current type is %s" % (key, field.type, type(value)))
        super(BaseElemObj, self).__setitem__(key, value)





class T(BaseElemObj):
    id = IntegerField()


if __name__ == '__main__':
    T()
