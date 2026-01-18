import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res = requests.get( 'https://www.1111.com.tw/search/job?page=1&col=ab&sort=desc&ks=%E5%A4%A7%E6%95%B8%E6%93%9A', verify = False )
soup = BeautifulSoup( res.text )
print( soup.prettify() )

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
print( "*" * 50 )

# 練習4：資料整理
'''
"職缺名稱"
"公司名稱"
"職缺連結"
"工作地區"
"縣市"
"鄉鎮市區"
"薪資待遇"
"給新方式"
"薪資上限(月薪)" # 使用函式： .isdigit(), .find()
"薪資下限(月薪)" # 面試：都是4萬，月薪：直接使用資料，年薪：除以12，時薪：概算為月薪-8hr*21工作天
"薪資平均(月薪)"
'''
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
        jd_title = jobs("h2")[0].text
        jd_company = jobs("h2")[1].text
        jd_link = "https://www.1111.com.tw" + jobs("a")[0]["href"]
        jd_location = jobs("a")[2].text
        jd_salary = jobs("h4")[0].text

        city_info = jd_location[ :3 ]
        city_district = jd_location[ 3: ]

        salary_type = "月薪"
        salary_min = 0
        salary_max = 0

        if jd_salary.find( "面議" ) != -1:
            salary_min = 40000
            salary_max = 40000
            salary_type = "面議"
        else:
            if jd_salary.find( "年薪" ) != -1:
                salary_type = "年薪"
            elif jd_salary.find( "時薪" ) != -1:
                salary_type = "時薪"

            temp_num_str = ""
            for char in jd_salary:
                if char.isdigit():
                    temp_num_str += char
                else:
                    temp_num_str += " "
                salary_numbers = temp_num_str.split()
                raw_min = 0
                raw_max = 0
            if len( salary_numbers ) >= 2:
                raw_min = int( salary_numbers[0] )
                raw_max = int( salary_numbers[1] )
            elif len( salary_numbers ) == 1:
                raw_min = int( salary_numbers[0] )
                raw_max = int( salary_numbers[0] )

            if salary_type == "年薪":
                salary_min = int( raw_min / 12 )
                salary_max = int( raw_max / 12 )
            elif salary_type == "時薪":
                salary_min = int( raw_min * 8 * 21 )
                salary_max = int( raw_max * 8 * 21 )
            else:
                salary_min = raw_min
                salary_max = raw_max
        salary_avg = int( ( salary_min + salary_max ) / 2 )

        print( f"職缺名稱： {jd_title}" )
        print( f"公司名稱： {jd_company}" )
        print( f"職缺連結： {jd_link}" )
        print( f"工作地區： {jd_location}" )
        print( f"縣市： {city_info}" )
        print( f"鄉鎮市區： {city_district}" )
        print( f"薪資待遇： {jd_salary}" )
        print( f"給薪方式： {salary_type}" )
        print( f"薪資下限(月薪)： {salary_min}" )
        print( f"薪資上限(月薪)： {salary_max}" )
        print( f"薪資平均(月薪)： {salary_avg}" )
        print( "-" * 30 )

    print( f"--- 第 {page} 頁搜尋完畢 ---\n" )
    page += 1