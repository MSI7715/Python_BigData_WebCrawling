import requests  # 套件說明： 用來發送 HTTP 請求，並處理回應。
import json # 套件說明： 用來處理 JSON 格式的資料。
import time # 套件說明： 用來處理時間相關的操作。

url = 'https://graph.facebook.com/v24.0/me/posts?access_token='
token = 'EAAbmrF1wdnUBQTtgDxIKJkKjZCYwHV0F6Tlw7umsDqfc11xCp0AH2Y0mZBHF9ee3qApaARdV0yczw2o09HgKqBWZAfpi3wtjumwp9EW2NFtrfUkTfb8qJ2SWUCPZAV183yGRiTsVUyONbggXXrPHSobLAqm0lKJPHUTYAW6Pn3MUAuiTsyB3Nkqsi3VflQLLSQ4Sg9UBZCrAANTuQAa6ltoOe6ozzXWK7DRkQod2ZAXd4VsbbZAIZBbeFhI6N873IherZA3QBTBS3QxZAEOR3e74ZANDnnC5f9ISQIw9VZAQjxtKlsOZAfxWBk3oSf1MrcasbzCzZBvXQZD'
params = {'access_token': token}
res = requests.get( url, params=params, timeout = 5 )

print( res )
print ( res.text )
jd = json.loads( res.text )
print ( jd )

# ==抓取第一篇貼文的內容==
# 我的解法
first_post_message = jd['data'][0]['message']
print("第一篇貼文內容:", first_post_message)

# 老師解法
print( jd[ "data" ][ 0 ][ "message" ] )
# print( jd[ "data" ][ 1 ][ "message" ] )
# print( jd[ "data" ][ 2 ][ "message" ] )
print( jd[ "data" ] )

# ==抓取第二篇貼文的內容==
# 我的解法
second_post_message = jd.get('data')[1].get('message')
print("第二篇貼文內容:", second_post_message)

# 老師解法
# print( jd[ "data" ][ 1 ][ "message" ] )

#== 抓取所有貼文的內容，用迴圈判斷==
# 我的解法
if 'data' in jd:
    for post in jd['data']:
        if 'message' in post:
            print("貼文內容:", post['message'])
        else:
            print("此篇貼文沒有內容")
else:
    print("沒有貼文資料")

# 老師解法
for post in jd['data']:
    if 'message' in post:
        print( post[ "message" ] )

#== 抓取下一頁貼文內容==
# 我的解法
if 'paging' in jd and 'next' in jd['paging']:
    next_page_url = jd['paging']['next']
    res_next = requests.get(next_page_url)
    jd_next = json.loads(res_next.text)
    for post in jd_next['data']:
        if 'message' in post:
            print("下一頁貼文內容:", post['message'])
        else:
            print("此篇貼文沒有內容")
else:
    print("沒有下一頁貼文資料")

# 老師解法
for post in jd['data']:
    if 'message' in post:
        print( "第一頁貼文內容： ", post[ "message" ] )
time.sleep(3)   # 暫停3秒鐘，避免請求過於頻繁
res_next = requests.get( jd["paging"]["next"] )
jd1 = json.loads( res_next.text )
# 抓取下一頁的貼文內容
for post in jd1['data']:
    if 'message' in post:
        print( "第二頁貼文內容： ", post[ "message" ] )
print( jd["paging"]["next"] )
print("*" * 20 )

#==用while迴圈抓取每一頁的貼文內容==
# 我的解法
jd = res.json()
page = 0
max_page = 20
while jd and page < max_page:
    page += 1
    print( f'Page: {page}' )
    for post in jd.get('data', []):
        msg = post.get( 'message' )
        if msg:
            print( f'貼文內容: {msg}' )
        else:
            print( '此篇貼文沒有內容' )
    next_page_url = jd.get('paging', {}).get('next')
    if not next_page_url:
        print( '沒有下一頁貼文資料' )
        break
    time.sleep( 3 )  # 暫停3秒鐘，避免請求過於頻繁
    res = requests.get( next_page_url )
    jd = json.loads( res.text )
print( "資料抓取結束，共抓取頁數： ", page )
print( "-" * 20 )

# 老師解法
jd = json.loads( res.text )
for post in jd['data']:
    if 'message' in post:
        print( post[ "message" ] )

page = 0
while page < 5:
    page += 1
    print( f'Page{page}' )
    time.sleep(3)
    res = requests.get( jd["paging"]["next"] )
    jd = json.loads( res.text )
    for post in jd['data']:
        if 'message' in post:
            print( post[ "message" ] )
