# /=====補充說明 Python 中的模組導入方式=====\
import datetime

print( datetime.datetime.now() )

from datetime import datetime
print( datetime.now() )

from datetime import datetime as dt
print( dt.now() )

# 檔案位置
import os
'''
# 取得此程式碼檔案現在位置
path = os.getcwd()
print( path )
# 製作新資料夾之路徑(未實現)
path = os.path.join( path, 'directory' )
print( path )
# 建立指定空資料夾
os.mkdir( path )
# 刪除指定空資料夾
os.rmdir( path )
# 檢查指定資料夾是否存在
os.path.exists( path )

# 練習1：檢查路徑是否存在資料夾directory，若無則建立該資料夾，如有則刪除該資料夾
current_dir = os.getcwd()
dir_path = os.path.join( current_dir, "directory" )
if not os.path.exists( dir_path ):
    os.mkdir( dir_path )
    print( "已建立資料夾" )
else:
    os.rmdir( dir_path )
    print( "已刪除資料夾" )
# 練習1：老師解法
path = os.getcwd()
path = os.path.join( path, 'directory' )
if os.path.exists( path ):
    os.rmdir(path)
else:
    os.mkdir(path)
'''

# 以寫入模式開啟檔案，可建立新檔，會覆蓋舊資料
file = open( 'new.txt', 'w' )
# 寫入內容
file.write( 'Hello World!' )
# 關閉檔案
file.close()
# 以讀取模式開啟檔案，不可建立新檔
file = open( 'new.txt', 'r' )
print( file.read() )
file.close()
# 以寫入模式開啟檔案，可建立新檔(append)，從資料尾端接續寫入
file = open( 'new.txt', 'a' )
file.write( '\nHello Python!' )
file.close()
# 以寫入模式開啟檔案，可建立新檔，會覆蓋舊資料
file = open( 'new.txt', 'w+' )
file.write( 'Hello Programmer!' )
# 移動輸入指示的位置 seek( [ 向後移動位元數, 預設為0 ], 0：資料開頭，1：現在位置不變，2：資料尾端 )
file.seek( 2, 0 )
print( file.read() )
file.close()
# 也可用with open語法，自動關閉檔案
with open( 'new.txt', 'w+' ) as file:
    file.write( 'Hello Programmer!' )
    # 移動輸入指示的位置 seek( [ 向後移動位元數, 預設為0 ], 0：資料開頭，1：現在位置不變，2：資料尾端 )
    file.seek( 2, 0 )
    print( file.read() )