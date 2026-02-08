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
print( im.shape )
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
im6 = im[ h//2: h, :, : ] # 擷取部分圖片(下半部)
plt.imshow(im6)
plt.show()

ima = np.array( im )
im7 = np.roll( ima, (500, 300), axis=(1, 0) ) # 圖片平移
plt.imshow(im7)
plt.show()