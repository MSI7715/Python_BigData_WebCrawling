import requests

url = 'https://www.tpex.org.tw/www/zh-tw/afterTrading/tradingStock'
payload = { 'code': '3630', 'date': '2026/02/01', 'id':'', 'response': 'json'}
res = requests.post( url, data = payload, verify=False )
print( res.text )