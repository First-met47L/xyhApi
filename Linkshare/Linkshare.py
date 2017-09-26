from lxml import etree
from urllib import parse
from Tools.Log import Log
import requests
import json


class LinkShare(object):
    logger = Log.getLog("LinkShare")

    @property
    def token(self):
        headers = {}
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Authorization"] = "Basic V0tvRWIwVm9SNTExODJfTlZ1cWliSk5CendvYTpwaG1paFBLZmVxdlYwQmFPNVJuSWM2UUsxRDhh"

        url = "https://api.rakutenmarketing.com/token"
        data = dict(grant_type="password", username=self._username, password=self._password, scope=self._scope)
        try:
            res = requests.post(url=url, data=data, headers=headers)
            result = res.text
            return json.loads(result, encoding="utf-8")['access_token']

        except Exception as e:
            self.logger.exception(e)
            return

    @property
    def ls_headers(self):
        headers = dict()
        token = None
        count = 0
        while not token:
            if count > 10:
                self.logger.exception("linkshare can not get the tooken(had tried 10 times) ")
                raise Exception("linkshare can not get the tooken(had tried 10 times)")
            token = self.token
            count += 1

        headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Accept-Language"] = "zh-CN,zh;q=0.8"
        headers["authorization"] = "Bearer " + token
        headers["Connection"] = "keep-alive"
        headers["Host"] = "api.rakutenmarketing.com"
        headers["Origin"] = "https://developers.rakutenmarketing.com"
        headers[
            "Referer"] = "https://developers.rakutenmarketing.com/subscribe/apis/info?name=ProductSearch&version=1.0&provider=LinkShare&"
        headers[
            "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

        return headers

    def __init__(self, username="kingmaxyang", password="Jackson99", scope="3217198"):
        '''
        initial instance
        :param username:
        :param password:
        :param scope:
        '''
        self._username = username
        self._password = password
        self._scope = scope

    def run(self):
        mids = [41970, 39288, 39133, 38729, 36666, 39435, 37978, 39265, 37385, 40315, 41846, 38292, 38707, 42352, 40490,
                37119, 41892, 40506, 24285, 456946, 438426, 240197]
        headers = self.ls_headers
        for mid in mids:
            # self.execute_script(mid)
            self.execute(mid)
            break
        self.logger.info("end")

    def execute(self, mid):
        '''

        :param mid:
        :return:
        '''
        ls_headers = self.ls_headers
        per_max = 100
        page_number = 1
        url = "https://api.rakutenmarketing.com/productsearch/1.0?mid={0}&max={1}&pagenumber={2}"

        while True:
            res = requests.get(url.format(mid, per_max, page_number), headers=ls_headers)
            result = res.text

            # update ls_header
            if "<ams:code>900902</ams:code>" in result or "<ams:code>900904</ams:code>" in result:
                ls_headers = self.ls_headers
                continue

            elements = etree.XML(result)
            total_pages = int(elements.xpath('/result/TotalPages/text()')[0])
            page_number = int(elements.xpath('/result/PageNumber/text()')[0])
            print(total_pages)
            items = []

            for i in elements.xpath('/result/item'):
                item = dict()
                item['advertiser'] = i.xpath('merchantname/text()')[0].split(':')[0]
                item['create_at'] = i.xpath('createdon/text()')[0]
                item['productname'] = i.xpath('productname/text()')[0]
                item['price'] =  i.xpath('price/text()')[0] + i.xpath('price/@currency')[0]
                item['saleprice'] = i.xpath('saleprice/text()')[0] + i.xpath('saleprice/@currency')[0]
                item['description'] = i.xpath('description/long/text()')[0]
                item['url'] = parse.unquote(i.xpath('linkurl/text()')[0])
                item['image'] = i.xpath('imageurl/text()')[0]
                items.append(item)
                print(item)
            print(items)
            if page_number == total_pages:
                self.logger.info("page number({0}) is equal to totalpages({1}".format(page_number, total_pages))
                return
            page_number += 1
            break

    def execute_script(self, mid):
        '''

        :param mid:
        :return:
        '''
        ls_headers = self.ls_headers
        per_max = 3
        page_number = 1
        url = "https://api.rakutenmarketing.com/productsearch/1.0?mid={0}&max={1}&pagenumber={2}"

        while True:
            res = requests.get(url.format(mid, per_max, page_number), headers=ls_headers)
            result = res.text

            # update ls_header
            if "<ams:code>900902</ams:code>" in result or "<ams:code>900904</ams:code>" in result:
                ls_headers = self.ls_headers
                continue

            elements = etree.XML(result)
            total = int(elements.xpath('/result/TotalMatches/text()')[0])
            if total == 0:
                break

            advertiser = elements.xpath('/result/item[1]/merchantname/text()')[0]

            dict1 = dict()
            dict1[advertiser] = total
            self.logger.info(json.dumps(dict1))
            break

if __name__ == '__main__':
    LinkShare().run()


    #
    # headers = dict()
    # headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
    # headers["Accept-Encoding"] = "gzip, deflate, br"
    # headers["Accept-Language"] = "zh-CN,zh;q=0.8"
    # headers["authorization"] = "Bearer " + "3b18833db0404d959455e386bf0be82"
    # headers["Connection"] = "keep-alive"
    # headers["Host"] = "api.rakutenmarketing.com"
    # headers["Origin"] = "https://developers.rakutenmarketing.com"
    # headers[
    #     "Referer"] = "https://developers.rakutenmarketing.com/subscribe/apis/info?name=ProductSearch&version=1.0&provider=LinkShare&"
    # headers[
    #     "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    #
    # res = requests.get("https://api.rakutenmarketing.com/productsearch/1.0" + "?mid=37938&max=3&pagenumber=1&keyword=red" , headers=headers)
    # print(res.text)
    # selector = etree.XML(res.text)
    # item = dict()
    # item['totalMatch'] = selector.xpath('/result/TotalMatches/text()')
    # item['TotalPages'] = selector.xpath('/result/TotalPages/text()')
    # item['PageNumber'] = selector.xpath('/result/PageNumber/text()')
    # for i in selector.xpath('/result/item'):
    #
    #     print(etree.tostring(i))
    # print(parse.unquote(i.xpath('linkurl/text()')[0]))


    # res = requests.get(
    #     "https://api.rakutenmarketing.com/productsearch/1.0" + "?keyword=beverage&sort=retailprice&sorttype=asc&sort=productname&sorttype=asc",
    #     headers=headers)

    # with open("Linkshare.xml", "wt") as f:
    #     f.write(res.text)

    # headers = {}
    # headers["Content-Type"] = "application/x-www-form-urlencoded"
    # headers["Authorization"]="Basic V0tvRWIwVm9SNTExODJfTlZ1cWliSk5CendvYTpwaG1paFBLZmVxdlYwQmFPNVJuSWM2UUsxRDhh"
    #
    # url = "https://api.rakutenmarketing.com/token"
    # data = dict(grant_type = "password",username = "kingmaxyang",password="Jackson99",scope="3217198")
    #
    # res = requests.post(url=url,data=data,headers=headers)
    # print(res.text)


    # headers = dict()
    # headers["Cookie"] = "JSESSIONID=1114020779F5F6B0A2417CE8288A6D93; AWSELB=61D9E5B06BE1990FCF7932EE85C8DA3A673CF2C5D3AAECE385CD57B1B4E873692F2A22CFBC814D5BE2619AFD25D8BABC3B6E5731FDA33B61FA0D20D5DD5D734B528DF1A0; i18next=en"
    # headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
    # headers["Accept-Encoding"] = "gzip, deflate, br"
    # headers["Accept-Language"] = "zh-CN,zh;q=0.8"
    # headers["Origin"] =  "https://developers.rakutenmarketing.com"
    # headers["Referer"] = "https://developers.rakutenmarketing.com/subscribe/apis/info?name=ProductSearch&version=1.0&provider=LinkShare&"
    # headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
    # res = requests.get("http://click.linksynergy.com/fs-bin/click?id=YDPKR7dygqg&offerid=274712&type=15&storeid=9881",headers=headers)
    # res = requests.get("http://click.linksynergy.com/fs-bin/click",headers=headers)
    # print(res.text)
