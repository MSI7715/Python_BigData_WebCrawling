# 輸入數字，判斷是奇數或偶數
num = int(input("請輸入一個整數: "))
if num % 2 == 0:
    print( num, "是偶數" )
else:
    print( num, "是奇數" )

# 輸入月份數字，判斷是哪個季節(冬天12-2，春天3-5，夏天6-8，秋天9-11)
month = int(input("請輸入月份數字(1-12): "))
if month == 12 or month == 1 or month == 2:
    print( month, "月是冬天。" )
elif month >= 3 and month <= 5:
    print( month, "月是春天。" )
elif month >= 6 and month <= 8:
    print( month, "月是夏天。" )
elif month >= 9 and month <= 11:
    print( month, "月是秋天。" )
else:
    print( "輸入錯誤，請輸入1-12的數字。" )

# 輸入年份，判斷是平年或閏年(4年1閏，100年為平，400年再閏，千年又閏)
year = int(input("請輸入年份: "))
if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
    print( year, "年是閏年。" )
else:
    print( year, "年是平年。" )