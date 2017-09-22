from ApiClass.Field import BaseField
from ApiClass.Field import IntegerField
from ApiException.ApiException import ParamTypeException


class ParamMeta(type):

    def __new__(cls, name, bases, namespace):
        if name == 'BaseParamObj':
            return super(ParamMeta, cls).__new__(cls, name, bases, namespace)
        __mapping__ = dict()
        for key, value in namespace.items():
            if isinstance(value, BaseField):
                __mapping__[key] = value
        for key in __mapping__.keys():
            namespace.pop(key)
        namespace['__mapping__'] = __mapping__
        return super(ParamMeta, cls).__new__(cls, name, bases, namespace)


class BaseParamObj(dict, metaclass=ParamMeta):

    def __init__(self, **kwargs):
        mapping = self.__mapping__
        for k, v in kwargs.items():
            field = mapping.get(k, None)
            if not field:
                continue
            if not isinstance(v, field.type):
                raise ParamTypeException(r"param(%s) must be %s,but current type is %s"%(k,field.type,type(v)))
        super(BaseParamObj, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'ParamObj' object has not attribute call (%s)" %item)

    def __setattr__(self, key, value):
        field = self.__mapping__.get(key,None)
        if not field or not isinstance(value,field.type):
            raise ParamTypeException(r"param(%s) must be %s,but current type is %s" % (key, field.type, type(value)))
        self[key] = value

    def __setitem__(self, key,value):
        field = self.__mapping__.get(key, None)
        if not field or not isinstance(value, field.type):
            raise ParamTypeException(r"param(%s) must be %s,but current type is %s" % (key, field.type, type(value)))
        super(BaseParamObj, self).__setitem__(key,value)





class T(BaseParamObj):
    id = IntegerField()


if __name__ == '__main__':
    T()
