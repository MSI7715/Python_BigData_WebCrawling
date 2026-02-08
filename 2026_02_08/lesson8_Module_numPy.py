import numpy as np
import matplotlib.pylab as plt

# 一維陣列
np.array( [1, 2, 3, 4] )
# 二維陣列(矩陣)
np.array( [ [1, 2, 3, 4], [5, 6, 7, 8] ] )
# 三維陣列
np.array( [ [ [1, 2], [3, 4] ], [ [5, 6], [7, 8] ] ] )

a = np.array( [ [1, 2], [3, 4] ] )
b = np.array( [ [5, 6], [7, 8] ] )
print( a + b )
print( a - b )
print( a * b )
print( a / b )
print( a + 10 )
print( a @ b ) # *--以2*2為例( [[a11*b11 + a12*b21)(對應位置相乘 + 隔壁對角相乘), a11*b12 + a12*b22], [a21*b11 + a22*b21, a21*b12 + a22*b22]] )

# 產生等差數列(陣列)
c = np.arange( 27 )
print( c )
# 變成不同維度並分組
print( c.reshape( 3, 9) )
# 陣列的資料格式(幾行幾列)
print( c.shape )
# 幾維
print( c.ndim )
# 位元大小
print( c.itemsize )
# 資料個數
print( c.size )
# 資料型態
print( c.dtype )
# /====== 矩陣範例結束 ======/
# /====== 繪圖範例開始 ======/
# 讀取圖片
im = plt.imread('mat.png')
# x軸、y軸、顏色通道(rgb)
print( "原圖大小：", im.shape )
plt.imshow(im)
plt.show()

im2 = im[ ::, ::, ::-1 ] # rgb -> bgr
plt.imshow(im2)
plt.show()

im3 = im[ ::-1, ::, :: ] # 上下翻轉
plt.imshow(im3)
plt.show()

im4 = im[ ::, ::-1, :: ] # 左右翻轉
plt.imshow(im4)
plt.show()

im5 = im[ ::-1, ::-1, :: ] # 上下左右翻轉
plt.imshow(im5)
plt.show()

h, w = im.shape[0], im.shape[1]
im6 = im[ h//2:h, :w//3, : ] # 擷取部分圖片(下半部)
plt.imshow(im6)
plt.show()

ima = np.array( im )
im7 = np.roll( ima, (500, 300, 1), axis=(0, 1, 2) ) # 滾動(目標, 滾動量, 哪個維度)
plt.imshow(im7)
plt.show()

im8 = im[ ::2, ::2, :: ] # 降低解析度，每隔一個像素取一個(縮小圖片)
print( "Image 8尺寸：", im8.shape )
plt.imshow(im8)
plt.show()

# 圖片的數值運算，影響亮度，不影響圖片大小
im9 = im * 0.5
im10 = im * 2
plt.imshow(im9.astype('uint8'))  # 設置為8位元整數
plt.show()
im10 = np.clip( im10, a_min = None, a_max = 255 )  # rgb範圍0~255，超過255的部分設為255
plt.imshow(im10.astype('uint8'))
plt.show()

red = im.copy()
green = im.copy()
blue = im.copy()
red[ :, :, (1, 2) ] = 0 # 將綠色和藍色通道設為0，保留紅色通道 * : = 全部， :: = 反向
green[ :, :, (0, 2) ] = 0 # 將紅色和藍色通道設為0，保留綠色通道
blue[ :, :, (0, 1) ] = 0 # 將紅色和綠色通道設為0，保留藍色通道
con = np.concatenate( [ red, green, blue ], axis = 1 ) # 延伸
plt.imshow(con)
plt.show()
'''
print("<" + "-" * 20 + ">")
print(im)
'''