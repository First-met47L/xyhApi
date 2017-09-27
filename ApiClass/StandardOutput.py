from ApiClass.Field import *
from ApiClass.ElemObj import BaseElemObj


class Product(BaseElemObj):
    _id = ObjectIdField()
    source = StringField()
    sn = StringField()
    title = StringField()
    brand = StringField()
    description = StringField()
    currency = StringField()
    price = FloatField()
    original_price = FloatField()
    face_image = StringField()
    buy_url = StringField()
    images = ListField()
    in_stock = BoolField()
    update_at = IntegerField()
    sizes = ListField()


class Size(BaseElemObj):
    description = StringField()
    stock = IntegerField()