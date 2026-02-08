'''
-----Pandas模組的Series介紹-----
'''
import pandas as pd
import numpy as np

data1 = pd.Series( [ 'ant', 'bug', 'cat', 'dog' ] ) # 製作串列，預設目錄為0, 1, 2,...
print( data1 )
data1 = pd.Series( [ 'ant', 'bug', 'cat', 'dog' ], index = [ 'A', 'B', 'C', 'D' ] ) # 製作串列
print( data1 )
print( "-" * 10 )
# data1 = pd.Series( {'A': 'ant', 'B': 'bug', 'C': 'cat', 'D': 'dog'} )
nu = pd.Series( { 'A': 25, 'B': 100 } )
print( data1.iloc[1] )  # 依順序
print( data1["C"] ) # 依index
print( data1[ [ "A", "C" ] ] )  # 依index取多項
print( data1[ 1:4 ] )
print( data1.index )
print( data1.values )
print( data1 + data1 )   # 文字 > 串接，數字 > 加總
print( np.mean(nu) )   # 平均值
print( data1.str.replace( "bug", "bee" ) )
data1[ 0 ] = 'ape'
print( data1 )
print( data1.str.contains( "at" ) ) # 是否包含at(True/False顯示)
print( data1.str.upper() )   # 全部轉大寫
print( data1.str.lower() )   # 全部轉小寫
print( pd.concat( [ data1, pd.Series( { "E": "eagle", "F": "fox" } ), nu ] ) )
print( pd.concat( [ data1, pd.Series( { "E": "eagle", "F": "fox" } ), nu ], ignore_index = True ) )

'''
-----Pandas模組的Series統計函數介紹-----
'''
num = pd.Series( [ 36, 8, 45, 90, 1 ] )
print( num.max() )   # 最大值
print( num.min() )   # 最小值
print( num.sum() )   # 加總
print( num.mean() )  # 平均值
print( num.nlargest( 2 ) )   # 前兩大
print( num.nsmallest( 2 ) )  # 前兩小

'''
-----Pandas模組的DataFrame介紹-----
'''
grades = pd.DataFrame( { 'Name': [ 'Amy', 'Tom', 'Jay', 'May' ], 'Math': [ 70, 55, 36, 81 ], 'English': [ '80', '65', '44', '25' ] } )
print( grades )
print( pd.DataFrame( grades, columns = [ 'Name', 'English', 'Math' ] ) )  # 指定行序
print( grades.head( 2 ) )  # 前兩列
print( grades.tail( 2 ) )  # 後兩列
print( grades[ "Name" ] )
print( grades[ [ "Math", "Name" ] ] )
print( grades[ 1:3 ] )
print( grades.at[ 2, "Math" ] )   # 指定某一個位置的資料
print( grades.iat[ 1, 0 ] )
print( grades.loc[[ 3, 2 ], [ "English", "Name" ]] )
print( grades.iloc[[ 0,3 ], [ 2, 1 ]] )
print( grades.drop( [ "Math" ], axis = 1 ) )  # 刪除Math欄位，axis=1表示刪除欄位，axis=0表示刪除列
print( grades.drop( 1, axis = 0 ) )