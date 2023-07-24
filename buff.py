import requests
import json
import datetime


# 获取时间戳
def get_time():
    # 获取当前时间
    current_time = datetime.datetime.now()
    # 将当前时间转换为时间戳，并乘以1000转换为毫秒级时间戳
    timestamp = current_time.timestamp() * 1000
    return int(timestamp)


# 获取物品名称

def get_goods_name():
    goods_name = input("请输入物品名字：")
    return goods_name
# 输入物品id
def set_goods_id(goods_name):
    try:
        input_file_path = 'buffids_dict.json'
    except IOError:
        print("Error:没有找到buffids_dict.json,id字典文件")
    else:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)

        for goods_id, name in data_dict.items():
            if goods_name in name:
                return goods_id
        return None


def getdata(timestamp, goods_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                      'Safari/537.36 Edg/114.0.1823.82'}

    # cookies = {'Device-Id':'QxOF2mIcdZG7PPAg8dhz','Locale-Supported':'zh-Hans','game':'csgo',
    # 'qr_code_verify_ticket':'524uU82e79ea4b2a26aa9d23ff0916351b09','remember_me ': 'U1090796516 |
    # OKbgo6iOin0jmrfeW4qkEjMrGqrvpEXt','session' : '1-mvYecquC59u_PTsyCZEt-WBGEcJFvZ1yuR77CVYXzOXr2043323580',
    # 'csrf_token' : 'IjA3YzFkYjQ2MzYzMDYyZjMwZDc2OWM4NTQzZWVjMzAyOWJmMjg2NzMi.F5PmMQ.7_s277sVrW9EMCX1ydFonnaDynA'}

    url = 'https://buff.163.com/api/market/goods/sell_order'
    params = {
        "game": "csgo",
        "goods_id": goods_id,
        "page_num": "1",
        "sort_by": "default",
        "mode": "",
        "allow_tradable_cooldown": "1",
        "_": timestamp
    }

    response = requests.get(url, params=params, headers=headers, )
    print(response.url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('请求失败')


# 获得buff最低价格
def get_buff_low_price(data):
    min_Price = data["data"]["items"][0]["price"]
    return float(min_Price)


# 获得steam最低价格（人民币，buffjosn里面有）
def get_steam_low_price(data):
    # 因为goods_infos为物品id所以直接遍历
    for key, value in data["data"]["goods_infos"].items():
        if "steam_price_cny" in value:
            steam_price_cny_value = value["steam_price_cny"]
            return steam_price_cny_value
        break


def get_steam_low_price_us(data):
    for key, value in data["data"]["goods_infos"].items():
        if "steam_price" in value:
            steam_price_value = value["steam_price"]
            return steam_price_value
        break


# 保存Josn文件
def save_josn_data(data):
    file = open("outputbuff.txt", "w")
    json_data = json.dumps(data)
    file.write(json_data)
    file.close()

# goods_name = get_goods_name()
# buffdata = getdata(timestamp=get_time(), goods_id=set_goods_id(goods_name))
# buffLowPrice = get_buff_low_price(buffdata)
# steamLowPrice = get_steam_low_price(buffdata)
# steamLowPrice_US = get_steam_low_price(buffdata)
# print("buff最低价格(人民币）：" + buffLowPrice + "  （美元）" + buffLowPrice / 7.2)
# print("steam最低价格(人民币):" + steamLowPrice)
# print("steam最低价格(美元):" + steamLowPrice_US)
# save_josn_data(buffdata)
