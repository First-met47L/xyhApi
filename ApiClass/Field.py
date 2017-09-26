from ApiException.ApiException import ElemTypeException


class BaseField(object):
    def __new__(cls, *args, **kwargs):
        return super(BaseField, cls).__new__(cls)
    def __init__(self):
        if self.__class__.__name__ == "BaseField":
            raise Exception("BaseField instance could not be initial")
        super(BaseField, self).__init__()


    @property
    def type(self):
        _type = self.__dict__.get("_type",None)
        if _type :
            return _type
        raise ElemTypeException("Object's instance._type can not be None")



class IntegerField(BaseField):
    def __init__(self):
        self._type = int
        super(IntegerField, self).__init__()

class StringField(BaseField):
    def __init__(self):
        self._type = str
        super(StringField,self).__init__()


class FloatField(BaseField):
    def __init__(self):
        self._type = float
        super(FloatField, self).__init__()


class ListField(BaseField):
    def __init__(self):
        self._type = list
        super(ListField, self).__init__()



if __name__ == '__main__':
    IntegerField()
    BaseField()