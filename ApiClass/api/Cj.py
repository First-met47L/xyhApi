import requests
from lxml import etree
from urllib import parse
from Tools.Log import Log
from functools import wraps
import requests
import json


def singleton(cls):
    instances = {}
    print(instances)

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Params(object):
    def __init__(self, *args, **kwargs):
        pass

    @property
    def headers(self):
        headers = dict()
        headers[
            'authorization'] = "00c6a112023e1148f40ded1f5a04cac3f0defde77da3edec6abf3b80d3e1f38a6ad25cbdcaf81fb7c6911a478beaea84db4602fa0e0474f225e6138b7e946b6627/16fea09a17db6269b68f03f924e2e06a2b3693ad0ce447615840283adf4695787217a96e60463cd626a9c62128ccf7aabc5254f1c24948577832d7b9144e50c9"
        headers["Host"] = "link-search.api.Cj.com"
        headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        headers["Accept-Language"] = "en-us,en;q=0.5"
        headers["Accept-Encoding"] = "gzip,deflate"
        headers["Accept-Charset"] = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
        headers["Keep-Alive"] = "300"
        headers["Connection"] = "keep-alive"
        headers[
            'Cookie'] = "JSESSIONID=abc91GUZ6k2m1bAEwV26v; lang_r=0; _mkto_trk=id:860-WNA-885&token:_mch-Cj.com-1506304493434-71820; CONTID=4475860; jsContactId=4475860; jsCompanyId=4995472; jsCu=USD; jsDt=d-MMM-yyyy; jsLa=en; cjuMember=0; AuthenticationToken=b1ae5aac-44cf-429f-81d2-fa1bebbc3375; _ga=GA1.2.659817612.1506304420; _gid=GA1.2.1893449106.1506304420"
        return headers

    @property
    def url_format(self):
        return "https://product-search.api.Cj.com/v3/product-search?website-id=8444651&advertiser-ids={0}&records-per-page={1}&low-price={2}&high-price={3}&page-number={4}"

    @property
    def price_list(self):
        return [0,40, 51, 61, 71, 81, 90, 99, 105, 115, 125, 135, 145,
                155, 165, 175, 185, 199, 215, 230, 245, 260, 280, 298, 320, 340, 360, 380, 400, 430,
                460, 490, 520, 550, 580, 610, 655, 700, 750, 800, 870, 930, 999, 1099, 1199, 1299, 1399,
                1499, 1649, 1809, 2009, 2299, 2599, 2899, 3299, 3859, 4400, 5000, 6000, 7500, 10000,
                14500, 20000, 29000, 49000, 79000, 149000, 249000, 500000, 1000000, 101800000]

    @property
    def advertisers(self):
        return [2547997,4859615, 4683856]
        # return [2547997]


class CJ(object):
    logger = Log.getLog("CJ")
    param_obj = Params()
    headers = param_obj.headers
    url_format = param_obj.url_format
    price_list = param_obj.price_list
    advertiser_ids = param_obj.advertisers
    records_per_page = 1000


    @classmethod
    def run(cls):
        for i in CJ.advertiser_ids:
            cls.execute(i)



    @classmethod
    def execute(cls,advertiser_id):
        for i in range(len(cls.price_list)-1):
            low_price = cls.price_list[i]
            high_price = cls.price_list[i+1]
            cls.deep_exec(advertiser_id,low_price,high_price)



    @classmethod
    def deep_exec(cls,advertiser_id,low_price,high_price):
        page_no = 1
        print(low_price,high_price)
        count = 1
        while True:
            url = cls.url_format.format(advertiser_id,cls.records_per_page,low_price,high_price,page_no)
            res = requests.get(url=url,headers=cls.headers)
            result = res.content
            elements = etree.XML(result)
            for elem in elements.xpath('/cj-api/products/product'):
                print(elem.xpath('name/text()')[0])
                print(count)
                count += 1
            total = int(elements.xpath('/cj-api/products/@total-matched')[0])
            if page_no*cls.records_per_page > total:
                break
            page_no += 1



if __name__ == '__main__':
    CJ.run()

    # print(CJ.getheaders())

# print(res.text)
# with open('Interserver.xml','wt') as f:
#     f.write(res.text)
