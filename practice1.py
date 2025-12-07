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
retiredYear = birth_year + retiredAge + 1911
print("您的退休年份為", retiredYear)

# 第三個練習 - 字串選取
alp = 'abcdefghijklmnopqrstuvwxyz'
# 輸出結果為：'cfilo'
alp_pick = alp[ 2 : 15 : 3 ]
print( alp_pick )
# 輸出結果為：'z~a'
alp_reverse = alp[ ::-1 ]
print( alp_reverse )
# 輸出結果為：'xsni'
alp_pick_reverse = alp[ -3 : 7 : -5 ]
print( alp_pick_reverse )
# 補充 - 連續選取
print( alp[::-1][5:20][:10][9] )

# 第四個練習 - list清單操作
list_m = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ]
list_d = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# 輸出結果為： 'x月有 y days.'
month_index = int( input("請輸入月份數字(1-12): ") ) - 1
print( list_m[ month_index ] + " has", list_d[ month_index ], "days." )

# 第五個練習 - 字典索引
dict=[ "a","b,c","d","e",{ "f":[ "g","h" ],"i":"j","k,l":{ "m":[ "n","o","p" ] },"q":"r" },"s",[ "t,u","v","w" ],"x","y,z" ]
# 索引出'python'
dict_result = dict[4]["k,l"]["m"][2] + dict[4]["k,l"]["m"][0] + dict[4]["k,l"]["m"][1] + dict[6][0][2] + dict[6][1][0] + dict[6][2][1]
print( dict_result )