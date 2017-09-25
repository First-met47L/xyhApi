import requests
from lxml import etree
from urllib import parse
mids = [41970,39288,39133,38729,36666,39435,37978,39265,37385,40315,41846,38292,38707,42352,40490,37119,41892,40506,24285,456946,438426,240197]
headers = dict()
headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Accept-Language"] = "zh-CN,zh;q=0.8"
headers["authorization"] = "Bearer " + "3b18833db0404d959455e386bf0be82"
headers["Connection"] = "keep-alive"
headers["Host"] = "api.rakutenmarketing.com"
headers["Origin"] = "https://developers.rakutenmarketing.com"
headers[
    "Referer"] = "https://developers.rakutenmarketing.com/subscribe/apis/info?name=ProductSearch&version=1.0&provider=LinkShare&"
headers[
    "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

res = requests.get("https://api.rakutenmarketing.com/productsearch/1.0" + "?mid=37938&max=3&pagenumber=1&keyword=red" , headers=headers)
# print(res.text)
selector = etree.XML(res.text)
item = dict()
item['totalMatch'] = selector.xpath('/result/TotalMatches/text()')
item['TotalPages'] = selector.xpath('/result/TotalPages/text()')
item['PageNumber'] = selector.xpath('/result/PageNumber/text()')
for i in selector.xpath('/result/item'):

    print(parse.unquote(i.xpath('linkurl/text()')[0]))


# res = requests.get(
#     "https://api.rakutenmarketing.com/productsearch/1.0" + "?keyword=beverage&sort=retailprice&sorttype=asc&sort=productname&sorttype=asc",
#     headers=headers)

# with open("linkshare.xml", "wt") as f:
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