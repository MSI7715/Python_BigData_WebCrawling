# 九九乘法表
# 我的解法
for i in range(1, 10):
    for j in range(1, 10):
        numbers = i * j
        print(f"{i} x {j} = {numbers}")
    print("----------")

# 老師解法
for i in range(1, 10):
    for j in range(1, 10):
        #print( i , j, i * j, end = "   " )
        print( f" {i} * {j} = {i * j:^3} ", end = "  " )   # print( f'' ) 字串格式化，end參數預設為換行，可改成空格或其他符號
    print()