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

# ==============================
# 我的解法
# 1~9的拉霸機，呈現每次拉霸結果，出現3個7就停止
import random
# 初始化計數器
count = 0
while True:
    # 每次拉霸，計數器加1
    count = count + 1

    # 產生3個1~10的隨機數字
    num1 = random.randint( 1, 10 )
    num2 = random.randint( 1, 10 )
    num3 = random.randint( 1, 10 )

    # 印出當前拉霸結果
    print( f"第 {count} 次：({num1}, {num2}, {num3})" )

    # 判斷是否出現3個7
    if num1 == 7 and num2 == 7 and num3 == 7:
        print( "恭喜中獎！拉霸機出現3個7，遊戲結束！" )
        print( f"總共拉了 {count} 次。" )
        break
# ==============================
# 進階拉霸機：
# 呈現每次拉霸結果，出現3個7就停止
# 事先設定本局要拉幾次，中獎或次數用完後，輸入Y繼續，N結束
import random

while True:
    max_times = int( input( "請輸入本局要拉幾次: " ) )

    # 初始化計數器
    count = 0
    is_win = False # 是否中獎

    # 條件：只要「目前次數」小於「限制次數」，就繼續跑
    while count < max_times:
        # 每次拉霸，計數器加1
        count = count + 1
        # 產生3個1~10的隨機數字
        num1 = random.randint( 1, 10 )
        num2 = random.randint( 1, 10 )
        num3 = random.randint( 1, 10 )

        # 印出當前拉霸結果
        print( f"第 {count} 次：({num1}, {num2}, {num3})" )

        # 判斷是否出現3個7
        if num1 == 7 and num2 == 7 and num3 == 7:
            print( "恭喜中獎！拉霸機出現3個7，遊戲結束！" )
            print( f"總共拉了 {count} 次。" )
            is_win = True # 標記為中獎
            break
    if is_win == False:
        print( f"本局次數用完，共拉了 {count} 次，未中獎。" )
    play_again = input( "是否要繼續遊戲？(Y/N): " )
    if play_again != 'Y' and play_again != 'y':
        print( "遊戲結束！" )
        break

# ==============================
# 老師的解法
import random
n = 0
result = '000'
while result != '777':
    n += 1
    print( n, "次" )
    result = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
    print( "拉霸結果：", result )

import random
while True:
    t = int(input('Times:'))
    n = 0
    result = '000'
    while result != '777':
        t -= 1
        n += 1
        print( n, "次" )
        result = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
        print( "拉霸結果：", result )
    play = input('Continue? Y/N: ')
    if play != 'y' and play != 'Y':
        break

# ==============================
# 1~1000所有偶數加總
# 我的解法
total = 0
for i in range( 1, 1001 ):
    if i % 2 == 0:
        total += i
print( "1~1000所有偶數加總為:", total )
# 老師的解法
a = 0
for ev in range(2, 1001, 2):
    a += ev
    print(a)
# 輸入一個數字，產生對應長度的費氏數列
# 1 1 2 3 5 8 13 21 ...
# a + b = c
#   a + b = c
#     a + b = c
# 我的解法
num = int( input( "請輸入一個正整數: " ) )


# 老師的解法
a = 1
b = 0
for f in range( int( input('數列長度'))):
    c = a + b
    a = b
    b = c
    print( c )
    x, y = y, x + y
    print( y, end = " " )
