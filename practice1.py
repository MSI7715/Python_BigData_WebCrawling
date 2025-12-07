# 第一個練習 - 變數計算
# 晚爨1000元(未稅5%)，服務費1成，請問總共多少錢?
price_dinner = 1000
tax_rate = 0.05
service_rate = 0.1
service_dinner = price_dinner * ( 1 + service_rate )
total_dinner = service_dinner * ( 1 + tax_rate )
print("總共需要支付:", total_dinner, "元")

# 第二個練習 - input輸入
# 輸入出生國曆年份，輸出自己預計西元幾年退休(65歲)，輸出格式：“您的退休年份為”***"
birth_year = int( input("請輸入您的出生國曆年份: ") )
retiredAge = 65
retiredYear = birth_year + retiredAge
print("您的退休年份為", retiredYear)

# 第三個練習 -
