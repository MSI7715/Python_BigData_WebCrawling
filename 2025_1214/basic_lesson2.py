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