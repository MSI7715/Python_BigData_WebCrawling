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
import openpyxl
import os
from bs4 import BeautifulSoup
'''
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
print( "=" * 50 + ">" )

# 1111網頁爬蟲 - 搜尋每一頁職缺內容
page = 1
res1 = requests.get('https://www.1111.com.tw/search/job?page=1&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify=False)
soup1 = BeautifulSoup(res1.text)
while soup( "div", class_ = "job-card" ) != [] and page < 15:
    for jobs in soup.find_all( "div", class_= "job-card" ):
        print( jobs("h2")[0].text )
        print( jobs("h2")[1].text )
        print( jobs("a")[2].text )
        print( jobs("h4")[0].text )
        print( "https://www.1111.com.tw" + jobs("a")[0]["href"] )
        print( "=" * 50 )

    print( "page", page )
    page += 1
    print()
    res1 = requests.get(f'https://www.1111.com.tw/search/job?page={page}&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify=False)
    soup1 = BeautifulSoup(res1.text)

# 資料清洗
# isdigit() / .find() 函式說明，判斷字串是否全為數字
print( "3.14159".isdigit(), "abcd".isdigit(), "314159".isdigit() ) # 判斷字串能不能轉成數字
print( "3.14159".find("."), "abcd".find("e"), "314159".find("15") ) # 找到參數在目標中的位置
'''

page = 1
res1 = requests.get('https://www.1111.com.tw/search/job?page=1&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify=False)
soup1 = BeautifulSoup(res1.text)
while soup1( "div", class_ = "job-card" ) != [] and page < 15:
    for jobs in soup1.find_all( "div", class_ = "job-card" ): # 職缺清單
        print( "職缺名稱：", jobs( "h2" )[0].text )
        print( "公司名稱：", jobs( "h2" )[1].text )
        print( "職缺連結：", "https://www.1111.com.tw" + jobs( "a" )[0]["href"] )
        print( "工作地區：", jobs( "a" )[2].text )
        print( "縣市：", jobs( "a" )[2].text[:3] )
        print( "鄉鎮市區：", jobs( "a" )[2].text[3:] )
        print( "薪資待遇：", jobs( "h4" )[0].text )
        print( "給薪方式：", jobs( "h4" )[0].text[:2] )
        pay_type = jobs( "h4" )[0].text[:2]
        salary = ""
        for st in jobs( "h4" )[0].text:
            if st.isdigit() or st == "~":
                salary += st
        print( "薪資範圍：", salary )
        # 如果~存在薪資範圍
        if "~" in salary:
            salary_min = int( salary[ :salary.find("~")] )
            salary_max = int( salary[ salary.find("~") + 1:] )
            salary_avg = ( salary_min + salary_max ) // 2
        else:
            salary_min = salary_max = salary_avg = int( salary )
        if pay_type == "面議":
            salary_min = salary_max = salary_avg = 40000
        elif pay_type == "月薪":
            pass
        elif pay_type ==  "年薪":
            salary_min /= 12
            salary_max /= 12
            salary_avg /= 12
        elif pay_type == "時薪":
            salary_min *= 21 * 8
            salary_max *= 21 * 8
            salary_avg *= 21 * 8
        else:
            print( pay_type )
        print( "薪資下限(月薪)：", salary_min )
        print( "薪資上限(月薪)：", salary_max )
        print( "平均薪資(月薪)：", salary_avg )
    print("page", page)
    page += 1
    print()
    res1 = requests.get(f'https://www.1111.com.tw/search/job?page={page}&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify=False)
    soup1 = BeautifulSoup(res1.text)

# Excel活頁簿寫入
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join( current_dir, "1111_job.xlsx" )

wb = openpyxl.Workbook()
ws = wb.active
ws[ "A1" ] = '職缺名稱'
wb.save( file_path )