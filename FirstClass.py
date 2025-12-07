# 數字運算
print( 3 + 4 )      # 加法
print( 3 - 4 )      # 減法
print( 3 * 4 )      # 乘法
print( 3 / 4 )      # 除法
print( 3 ** 4 )     # 次方
print( 3 // 4 )     # 整除
print( 3 % 4 )      # 取餘數

# = 賦值
x = 3   # x是變數(箱子)，被賦值(放入)3
print( x )
化妝品 = "玩具"
化妝品 = "化妝品" # 重複賦值會覆蓋舊值(變數可以重新賦值)


# 變數命名
help("keywords")  # 查看Python保留字(不能用來當變數名稱)
# 變數命名規則: 只能包含字母、數字、底線，且不能以數字開頭，區分大小寫，不能使用保留字，而且只能使用_符號
# 3c = 5
# hi! = 7


# 變數運算      程式碼運行順序：由上至下，由左至右，由內至外，右側運算完才賦值至左側變數
a = 0
a = a + 1
print( a )
a += 1  # 簡寫
print( a )
a *= 2  # 簡寫
print( a )

a1, b1 = 1, 2  # 多重賦值
a1, b1 = b1, a1  # 交換變數值
print( a1, b1 )
print( type( 4 * 1 ) ) # 整數 int integer
print( type( 4 / 1 ) ) # 浮點數 float
print( type( "4 / 1" ) ) # 字串 str string

# 字串運算
hello = 'hello world'
print( hello  + "!" ) # 字串串接
print( "100" + "1" ) # 字串串接
# print( hello * "2" ) # 字串重複
print( hello * 2 )  # 字串重複

#
input1 = int( input("請輸入整數: ") )   # input()輸入的資料型態是字串，需要轉型成整數int
input2 = input( "請輸入整數: " )
print( input1, int(input2) )