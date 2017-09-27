import requests
import json
import time
from ApiException import ApiException
from ApiClass.Field import *
from ApiClass.ElemObj import BaseElemObj
from ApiClass.StandardOutput import *
from Tools.Mongo import MongoDb
from Tools.Log import Log


class RediBase(object):
    logger = Log.getLog("Redi")
    token = "cf7feb99-71fe-4113-ad11-5a527d9d0a79"
    mongo = MongoDb()
    mongo.db = 'xyh_api'
    mongo.collection = 'redi'

    @classmethod
    def get_products(cls, conditionObj=None):

        if conditionObj != None and not isinstance(conditionObj, SearchCondition):
            raise ApiException.ElemException()
        headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
        url = "https://www.redigroup.it/Api/getItems/1.0/%s/" % cls.token
        params = conditionObj
        res = requests.get(url=url, params=params,headers=headers)
        return json.loads(res.text)

    @classmethod
    def get_stocks(cls, conditionObj=None):
        if conditionObj == None or not conditionObj.get('item_id', None):
            raise ApiException.ElemException("item_id chould not be None")
        url = "https://www.redigroup.it/api/stocks/1.0/%s/" % cls.token
        params = dict(item_id=conditionObj.item_id)
        res = requests.get(url=url, params=params)
        return json.loads(res.text)

    @classmethod
    def get_prices(cls, conditionObj=None):
        if conditionObj == None or not conditionObj.get('item_id', None):
            raise ApiException.ElemException("item_id chould not be None")
        url = "https://www.redigroup.it/api/prices/1.0/%s/​" % cls.token
        params = dict(item_id=conditionObj.item_id)
        res = requests.get(url=url, params=params)
        return json.loads(res.text)

    @classmethod
    def get_images(cls, conditionObj=None):
        if conditionObj == None or not conditionObj.get('item_id', None):
            raise ApiException.ElemException("item_id chould not be None")
        url = "https://www.redigroup.it/api/images/1.0/%s/​" % cls.token
        params = dict(item_id=conditionObj.item_id)
        res = requests.get(url=url, params=params)
        return json.loads(res.text)

        # def __new__(cls):
        #     self = super(Redi, cls).__new__(cls)
        #     self.token = "cf7feb99-71fe-4113-ad11-5a527d9d0a79"
        #     return self
        #


class SearchCondition(BaseElemObj):
    item_id = IntegerField()
    item_brand = StringField()
    item_gender = StringField()
    item_category = StringField()


class Redi(RediBase):
    @staticmethod
    def trans2standard(dictObj):
        product = Product()
        product.source = 'redi'
        product.sn = dictObj.get('item_id')
        product.title = dictObj.get('item_name')
        product.brand = dictObj.get('item_gender')
        product.description = dictObj.get('item_description')
        product.currency = 'EUR'
        product.price = float(dictObj.get('item_supply_price')) if dictObj.get('item_supply_price') else None
        product.original_price = float(dictObj.get('item_retail_price')) if dictObj.get('item_supply_price') else None
        product.images = dictObj.get('item_images')
        product.face_image = product.images[0] if product.images else None
        product.buy_url = ""
        product.update_at = (lambda  time_str :int(time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S"))))(dictObj.get('item_update'))


        item_sizes = dictObj.get('item_sizes')
        sizes = []
        for i in item_sizes:
            size = Size()
            size.description = i.get('item_size')
            size.stock = int(i.get('item_stock')) if i.get('item_stock') else 0
            sizes.append(size)
        product.sizes = sizes
        product.in_stock = False
        for i in sizes:
            if i.stock > 0:
                product.in_stock = True
                break
        return product

    @classmethod
    def run(cls):
        try:

            condition = SearchCondition()
            count = 1
            for i in cls.get_products(conditionObj=condition):
                try:
                    proudct = Redi.trans2standard(i)
                except Exception as e :
                    cls.logger.exception(e)
                    continue

                cls.logger.info("redi has been insert ,no.%s id is %s"%(count,cls.mongo.insert(doc=proudct)))
                count += 1

            cls.logger.info("end")
        except Exception as e:
            cls.logger.exception(e)






if __name__ == '__main__':
    Redi.run()

