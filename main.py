import requests

url = f'https://steamcommunity.com/market/itemordershistogram?country=CN&language=schinese&currency=23&item_nameid=176288467&two_factor=0'
cookies = dict(timezoneOffset="28800,0",
               _ga="GA1.2.713889128.1689071050", browserid="2769199545288498865", sessionid="31886805e1246086125301c7",
               steamCountry="JP%7Cf29948361764b68167e9200f4017c1ef",
               steamLoginSecure="76561198274066203%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQwOF8yMkQyOEM0OV9FMTA5MSIsICJzdWIiOiAiNzY1NjExOTgyNzQwNjYyMDMiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY4OTQ5Mjg1MywgIm5iZiI6IDE2ODA3NjQ2NTksICJpYXQiOiAxNjg5NDA0NjU5LCAianRpIjogIjE4NDFfMjJEQjYwM0NfRTNFQzgiLCAib2F0IjogMTY4OTA3MTA5NSwgInJ0X2V4cCI6IDE3MDczOTM5OTcsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIxMzguMTk5LjIxLjE2NSIsICJpcF9jb25maXJtZXIiOiAiMjE4LjI2LjU1LjIyMiIgfQ.3MYVqiBUtzlWZgy2_Q4Rwtf0QYyzzvNHSh7qyHHiKp7flJhbLakNu3tgUmwEX5O2d9Qe6SEp7z3S5rOxG_oHAw",
               webTradeEligibility="%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1689404660%7D")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'}

response = requests.get(url, cookies=cookies, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print('请求失败')
