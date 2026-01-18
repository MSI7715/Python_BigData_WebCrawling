import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res = requests.get( 'https://www.1111.com.tw/search/job?page=1&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify = False )
soup = BeautifulSoup( res.text )
print( soup.prettify() )
'''
print( soup.find_all( "div", class_= "job-card" )[2]("h2")[0].text )
print( soup.find_all( "div", class_= "job-card" )[2]("h2")[1].text )
print( soup.find_all( "div", class_= "job-card" )[2]("a")[2].text )
print( soup.find_all( "div", class_= "job-card" )[2]("h4")[0].text )
print( "https://www.1111.com.tw" + soup.find_all( "div", class_= "job-card" )[2]("a")[0]["href"] )

# 練習1：職缺清單(for迴圈)
for jobs in soup.find_all( "div", class_= "job-card" ):
    print( jobs("h2")[0].text )
    print( jobs("h2")[1].text )
    print( jobs("a")[2].text )
    print( jobs("h4")[0].text )
    print( "https://www.1111.com.tw" + jobs("a")[0]["href"] )
print( "=" * 50 + ">" )

# 練習2：搜尋下一頁職缺(for迴圈)
res1 = requests.get( 'https://www.1111.com.tw/search/job?page=2&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify = False )
soup1 = BeautifulSoup( res1.text )
for jobs in soup.find_all( "div", class_= "job-card" ):
    print( jobs("h2")[0].text )
    print( jobs("h2")[1].text )
    print( jobs("a")[2].text )
    print( jobs("h4")[0].text )
    print( "https://www.1111.com.tw" + jobs("a")[0]["href"] )
print( "=" * 50 + ">" )
'''
# 練習3：印出每一頁的職缺清單直到soup.find為空值(while迴圈)
page = 1
while True:
    print(f"正在搜尋第 {page} 頁的職缺資料...")
    res2 = requests.get(f'https://www.1111.com.tw/search/job?page={page}&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify=False)
    soup2 = BeautifulSoup(res2.text)

    job_titles = soup2.find_all( "div", class_= "job-card" )
    if not job_titles:
        print("已無更多職缺資料，結束搜尋。")
        break

    for jobs in job_titles:
        print( jobs("h2")[0].text )
        print( jobs("h2")[1].text )
        print( jobs("a")[2].text )
        print( jobs("h4")[0].text )
        print( "https://www.1111.com.tw" + jobs("a")[0]["href"] )
    print( f"--- 第 {page} 頁搜尋完畢 ---\n" )
    page += 1

