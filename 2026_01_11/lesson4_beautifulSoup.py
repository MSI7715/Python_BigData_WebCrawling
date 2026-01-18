# HTML
# <tag_name attribute_name = attribute_value> text </tag_name>
web = """
<body>
<h1 class = 'abc' href = 123> abc </h1>
<a> 第四行 </a>
<a> 第五行 </a>
<h1 class = 'job'> 職缺：<h2>大數據工程師</h2> </h1>
</body>
"""

import requests
from bs4 import BeautifulSoup
# 基本觀念
soup = BeautifulSoup( web ) # 把html的str變成beautifulSoup格式，才能以html規則處理
print( soup.prettify() ) # 使html碼更容易閱讀，查找位置，但會變回str
print( soup.body.text )  # 直接選取從上到下第一個符合的標籤名稱
print( soup.find( "h1", class_ = "job" ) )
print( soup.find_all( "h1", href = "123" ) ) # 選取多筆資料, 從上到下排序, 形成清單
print( soup( "a" ) ) # 省略.find_all
print( soup( "h1" )[0]["href"] )
print( soup.select('h1[class="job"]') )
# 取得  五
print( soup("a")[1].text[2] )
print( "=" * 50 + ">" )

# 1111網頁爬蟲
res = requests.get( 'https://www.1111.com.tw/search/job?page=1&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify = False )
soup = BeautifulSoup( res.text )
print( soup.prettify() )
# 職缺名稱
print( soup.find( "h2", class_ = "text-[18px] leading-[1.5] font-medium whitespace-wrap break-all" ).text )
# 公司名稱
print( soup.find( "h2", class_ = "inline" ).text )
# 工作區域
print( soup.find( "a", class_ = "job-card-condition__text cursor-pointer hover:underline underline-offset-2" ).text )
# 薪資待遇
print( soup.find( "h4", class_ = "job-card-condition__text" ).text )
# 職缺網址
print( "https://www.1111.com.tw" + soup.find( "a", class_ = "text-[#212529] mb-1 line-clamp-1 lg:line-clamp-2 hover:underline" )["href"] )
print( "=" * 50 + ">" )

print( soup.find_all( "div", class_= "job-card" )[2]("h2")[0].text )
print( soup.find_all( "div", class_= "job-card" )[2]("h2")[1].text )
print( soup.find_all( "div", class_= "job-card" )[2]("a")[2].text )
print( soup.find_all( "div", class_= "job-card" )[2]("h4")[0].text )
print( "https://www.1111.com.tw" + soup.find_all( "div", class_= "job-card" )[2]("a")[0]["href"] )