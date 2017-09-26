import requests
import json
from ApiException import ApiException
from ApiClass.Field import *
from ApiClass.ElemObj import BaseElemObj


class Redi(object):
    token = "cf7feb99-71fe-4113-ad11-5a527d9d0a79"


    @classmethod
    def getProducts(cls,conditionObj=None):

        if conditionObj != None and not isinstance(conditionObj, SearchCondition):
            raise ApiException.ElemException()
        url = "https://www.redigroup.it/Api/getItems/1.0/%s/" % cls.token
        params = conditionObj
        print(params)
        res = requests.get(url=url,params=params)
        return json.loads(res.text)

    @classmethod
    def getStocks(cls,conditionObj=None):
        if conditionObj == None or not conditionObj.get('item_id',None):
            raise ApiException.ElemException("item_id chould not be None")
        url = "https://www.redigroup.it/api/stocks/1.0/%s/"%cls.token
        params = dict(item_id = conditionObj.item_id)
        print(params)
        res = requests.get(url=url,params=params)
        return json.loads(res.text)

    @classmethod
    def getPrices(cls,conditionObj=None):
        if conditionObj == None or not conditionObj.get('item_id',None):
            raise ApiException.ElemException("item_id chould not be None")
        url = "https://www.redigroup.it/api/prices/1.0/%s/​"%cls.token
        params = dict(item_id = conditionObj.item_id)
        print(params)
        res = requests.get(url=url,params=params)
        return json.loads(res.text)

    @classmethod
    def getImages(cls,conditionObj=None):
        if conditionObj == None or not conditionObj.get('item_id',None):
            raise ApiException.ElemException("item_id chould not be None")
        url = "https://www.redigroup.it/api/images/1.0/%s/​"%cls.token
        params = dict(item_id = conditionObj.item_id)
        print(params)
        res = requests.get(url=url,params=params)
        return json.loads(res.text)

    # def __new__(cls):
    #     self = super(Redi, cls).__new__(cls)
    #     self.token = "cf7feb99-71fe-4113-ad11-5a527d9d0a79"
    #     return self
    #
    # def __init__(self):
    #     self.url =  "https://www.redigroup.it/Api/getItems/1.0/%s/" % self.token
    #     super(Redi, self).__init__()
    #
    # def getProducts(self, conditionObj=None):
    #     if conditionObj != None and not isinstance(conditionObj, SearchCondition):
    #         raise ApiException.ParamException()
    #
    #     params = conditionObj
    #     print(params)
    #     res = requests.get(url=self.url,params=params)
    #     return json.loads(res.text)





class SearchCondition(BaseElemObj):
    item_id = IntegerField()
    item_brand = StringField()
    item_gender = StringField()
    item_category = StringField()


if __name__ == '__main__':
    # for i in Redi().getProducts():
    #     print(i)
    #     break
    # print(SearchCondition.__dict__)
    # print(SearchCondition().identification)
    # print(SearchCondition().__dict__)
    #item_brand='DONDUP'
    condition = SearchCondition()
    print(type(condition))
    print(len(Redi().getProducts(conditionObj=condition)))
    # with open('redi.json','wt') as f:
    #     f.write(json.dumps())
    # print(Redi.getStocks(conditionObj=condition))
    # print(Redi.getPrices(conditionObj=condition))
    # print(Redi.getImages(conditionObj=condition))
