import requests

headers = dict()
# headers['authorization'] = "0094b1c2429a0f51c65804ab5352e54200d44f9a48ca4d27759cd6d0bf4abb915219815b0b9f2b55af4a74248258b054fafbca0cc94fa2a1dc6abf9e81c0a09a3f/2903a31eb5d9f5e76ccdd4e805dc80c933c6c53ac0ba6960f2a2fa2f5990c53360a5a884837bd85fb867ed4f69c4cd0ac73f6160afbe3abdfde6e6fa6ff17569"
headers['authorization'] = "00c6a112023e1148f40ded1f5a04cac3f0defde77da3edec6abf3b80d3e1f38a6ad25cbdcaf81fb7c6911a478beaea84db4602fa0e0474f225e6138b7e946b6627/16fea09a17db6269b68f03f924e2e06a2b3693ad0ce447615840283adf4695787217a96e60463cd626a9c62128ccf7aabc5254f1c24948577832d7b9144e50c9"
headers["Host"]= "link-search.api.cj.com"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
headers["Accept-Language"] = "en-us,en;q=0.5"
headers["Accept-Encoding"] = "gzip,deflate"
headers["Accept-Charset"] = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
headers["Keep-Alive"] = "300"
headers["Connection"] = "keep-alive"
headers['Cookie'] = "JSESSIONID=abc91GUZ6k2m1bAEwV26v; lang_r=0; _mkto_trk=id:860-WNA-885&token:_mch-cj.com-1506304493434-71820; CONTID=4475860; jsContactId=4475860; jsCompanyId=4995472; jsCu=USD; jsDt=d-MMM-yyyy; jsLa=en; cjuMember=0; AuthenticationToken=b1ae5aac-44cf-429f-81d2-fa1bebbc3375; _ga=GA1.2.659817612.1506304420; _gid=GA1.2.1893449106.1506304420"

# res = requests.get("https://product-search.api.cj.com/v3/product-search?website-id=7665447&advertiser-ids=2547997&records-per-page=1000&keywords=&high-price=40&page-number=1",headers=headers)
# res = requests.get("https://product-search.api.cj.com/v3/product-search?website-id=8444651&advertiser-ids=2547997&records-per-page=1000&keywords=&high-price=40&page-number=2",headers=headers)
res = requests.get("https://product-search.api.cj.com/v3/product-search?website-id=8444651&advertiser-ids=4683856&records-per-page=1000&keywords=&high-price=40&page-number=1",headers=headers)

# with open('Interserver.xml','wt') as f:
#     f.write(res.text)
