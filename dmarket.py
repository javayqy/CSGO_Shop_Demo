from urllib.parse import quote
import requests
import json


# 将物品名转换为URL格式
def turn_name_url(goods_name):
    url_encoded_item_name = quote(goods_name)
    print(url_encoded_item_name)
    return url_encoded_item_name


def getdata(goods_name):
    # 自己的代理地址
    proxy_address = "http://127.0.0.1:4568"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 ''Safari/537.36 Edg/114.0.1823.82'}
    url = 'https://api.dmarket.com/exchange/v1/market/items'

    # cookies = {
    #     "incap_ses_894_2319161": "XfbbPoK9CA3x+j9JJSFoDICavGQAAAAA/aJ5Rxv+VQvpi347Mkg+OQ==",
    #     "visid_incap_2319161": "Yl/b88l7RMinxAWidz3wTYCavGQAAAAAQUIPAAAAAACVCXxQn3yQLdlMGLwin+tJ"
    # }
    params = {
        "side": "market",
        "orderBy": "price",
        "orderDir": "asc",
        "title": "",
        "priceFrom": 0,
        "priceTo": 0,
        "treeFilters": "",
        "gameId": "a8db",
        "types": "dmarket",
        "cursor": "",
        "limit": 10,
        "currency": "USD",
        "platform": "browser",
        "isLoggedIn": True
    }
    response = requests.get(url, params=params, proxies={"http": proxy_address, "https": proxy_address})
    print(response.url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('请求失败')


def save_josn_data(data):
    file = open("output_dmarkt.txt", "w")
    json_data = json.dumps(data)
    file.write(json_data)
    file.close()


# sellname = "AUG | Condemned (Field-Tested)"
dmdata = getdata()
print(dmdata)
save_josn_data(dmdata)
