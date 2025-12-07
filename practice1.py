# 第一個練習
# 晚爨1000元(未稅5%)，服務費1成，請問總共多少錢?
price_dinner = 1000
tax_rate = 0.05
service_rate = 0.1
tax_dinner = price_dinner * tax_rate
service_dinner = price_dinner * service_rate
total_dinner = price_dinner + tax_dinner + service_dinner
print("總共需要支付:", total_dinner, "元")