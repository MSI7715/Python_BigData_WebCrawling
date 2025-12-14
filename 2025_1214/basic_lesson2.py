# 布林值 True False
print( type(True) )
print( 1 + 1 == "2" ) # 是否相同
print( 3 < 5 )
print( 2 * 5 >= 3 ** 2 )
print( "al" in "apple" ) # 是否包含值
line1 = 2 in [1, 2, 3]
print( line1 )

# 邏輯運算 AND OR NOT
nu = int(input('Integer: '))
print( nu > 3 and nu > 10 ) # 和
print( nu > 3 or nu > 10 ) # 或
print( not ( nu != 5 ) ) # 非
'''
& | T | F
T | T | F
F | F | F
==========
| | T | F
T | T | T
F | T | F
'''

# 條件判斷 if elif else 條件越嚴苛越前面，每個子程式縮排4格
temp = int(input('溫度： '))
if temp < 30:              # 母程式
    print( "Hot" )         # 子程式
elif temp < 20:
    print( "Cool" )
elif temp < 40:
    print( "Cold" )
else:
    print( "Crazy" )

# 迴圈 while
n = 0
while 1 + 1 == 2 and n < 10:   # 條件為True時執行
    n = n + 1  # 記得更新條件，避免無限迴圈 n += 1
    print( "fire" )
print( "end" )

i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        if i == 2:
            print( "二" )
            pass            # 無實質功能，作為子程式讓結構正確
            print( "pass" )
        elif i == 4:
            print( "四" )
            continue       # 繼續開始下一圈迴圈
            print( "continue" )
        elif i == 8:
            print( "八" )
            break           # 跳出迴圈
            print( "break" )
        print( i )
    print( "end" )

# import 導入
import random
print( random.randint(1, 10) )  # 產生1-10隨機整數

# for 迴圈 (遍歷)
class_ = [ '小黃', '小花', '大黑', '阿材' ]
for student in class_:      # for 統稱(自訂變數) in 集合
    print( student )

字串 = 'ㄅㄆㄇㄈ'
for 字元 in 字串:
    字串 += '@'
    print( 字串, 字元 )
清單 = [ '刷牙', '洗臉', '收書包', '睡覺' ]
for 代辦 in 清單:
    print( 代辦 + " checked! " )
菜單 = { '滷肉飯':50, '貢丸湯':60, '燙青菜':70 }
for 餐點 in 菜單:
    print( 餐點, 菜單[餐點] )

# range() 產生數字序列
print( range(1, 10) )
print( list(range(1, 10)) )
print( list(range(1, 10, 2)) )
for n in range(5):
    print( "hi" )