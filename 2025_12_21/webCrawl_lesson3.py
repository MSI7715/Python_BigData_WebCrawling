import requests  # 套件說明： 用來發送 HTTP 請求，並處理回應。
import json # 套件說明： 用來處理 JSON 格式的資料。

url = "https://graph.facebook.com/v24.0/me/posts?access_token=EAAbmrF1wdnUBQfYcNfdAa2JGoMzZAAyc8VdlYRE0VOgsp4jLVjgVntxpxeX0MsdcLylkYLZBM4m6rqGPhb8ZAaEiTH1X5miJlpAi5SocGNR2SUjFAYvPujHNnB7ldkfzn4D4KtGWEojOxcOK5ao0KqukJt4SE5fpGkNJ6C7pfW6uULYO2LKsVSQee3VvY76OELs8Dd9ZBOZA1hoogyFjsZCRTtg2QZAZCfCjy3Q7TgfegzlZC4SBKLjRWjbXoTZAAIydooRo9oDb0K9VDdLIbnb8hksP1RJ3UKcP1zZBnSOTmxce0cFtk30ZARSoUGA9gIMFtbeZAwQWezIOtfqBs"
res = requests.get( url )

print( res )
print ( res.text )
jd = json.loads( res.text )
print ( jd )

# 抓取第一篇貼文的內容
# 我的解法
first_post_message = jd['data'][0]['message']
print("第一篇貼文內容:", first_post_message)

# 老師解法
print( jd[ "data" ][ 0 ][ "message" ] )
print( jd[ "data" ][ 1 ][ "message" ] )
print( jd[ "data" ][ 2 ][ "message" ] )
print( jd[ "data" ] )

# 抓取第二篇貼文的內容
# 我的解法
second_post_message = jd.get('data')[1].get('message')
print("第二篇貼文內容:", second_post_message)

# 老師解法
print( jd[ "data" ][ 1 ][ "message" ] )

# 抓取所有貼文的內容，用迴圈判斷
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
