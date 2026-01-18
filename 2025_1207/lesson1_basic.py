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

# 輸入與轉型
input1 = int( input("請輸入整數: ") )   # input()輸入的資料型態是字串，需要轉型成整數int
input2 = input( "請輸入整數: " )
print( input1, int(input2) )

# 索引 index
print( hello[0] ) # 從0開始，取得字串的第一個字元 (索引從0開始)，中括弧內可以運算也可以是變數
print( hello[1:7] ) # 前含後不含
print( hello[-1] ) # 取得字串的最後一個字元 (負索引從-1開始)，倒數
print( hello[ : -3 ] ) #從頭
print( hello[ 3 : ] ) #到尾
print( hello[ : ] ) #全部
print( hello[ 1:-3:3 ] )   # [開頭(含)：結尾(不含)：項差(預設為1，可為負數)]
#print( hello[20] )

# list 清單 []
list1 = [ 1, 2, 3, '4', 5, [ 6, '7' ] ]
print( list1 + [ '8, 9' ], 10 ) # 清單串接
print( list1 * 3 ) # 清單重複
print( list1[ -1 ] ) # 取得清單的最後一個元素
print( list1[ -1 ][ 1 ] ) # 按照順序選取
print( len( list1 ) )  # 取得清單長度
# 賦值取代
list1[ 0 ] = 0
print( list1 )
print( [ 'a', 'b', 'c', 1, 2, 3 ][ 4 ] )
print( [0][0] )

# Dictionary 字典 { key: value, key: value } key只能是數字或字串
movie = {
    'name': '鋼鐵人3',
    '上映日': { '年': 2013, '月': 5, '日': 3 },
    '演員': [ '小勞勃·道尼', '葛妮絲·派特洛', '唐·奇鐸' ],
    '片長': 130
}
print( movie['name'] )
print( movie['上映日']['年'] )
movie[ '時長' ] = '2小時10分'  # 賦值更新字典內容
print( movie )
movie[ '導演' ] = '沙恩·布萊克'  # 賦值新增字典內容
print( movie )
# 字典如有重複內容會覆蓋
movie = {
    'name': '鋼鐵人3',
    '上映日': { '年': 2013, '月': 5, '日': 3 },
    '演員': [ '小勞勃·道尼', '葛妮絲·派特洛', '唐·奇鐸' ],
    '片長': 130,
    '演員': [ '小勞勃·道尼', '葛妮絲·派特洛', '唐·奇鐸', '陳聲翊' ]
}
print( movie )