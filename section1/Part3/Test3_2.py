"""
打印99乘法表
while循环
"""
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%dx%d=%d" % (j, i, i * j), end="\t")
#         j += 1
#     print()
#     i += 1
"""
for循环
    语法：
    for i in range(start,end，step)
    i为(start,end)内的依次循环的每个数
        i的范围包括start,不包括end
        如果不写start,默认从0开始
    step 步长，默认是1
    
用for循环打印从1到9的数字
"""
# 第一种方法
# for i in range(1, 10):
#     print(i)
# 第二种方法
# for i in range(10):
#     print(i)
"""
打印1，3，5，7，9
"""
# for i in range(1, 10, 2):
#     print(i)
# 倒序打印9->1
# for i in range(9, 0, -1):
#     print(i)
"""
用for循环打印99乘法表   
"""
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d x %d = %d" %(j, i, i * j), end="\t")
#     print()
# 倒序打印99乘法表
# for i in range(9, 0, -1):
#     for j in range(i, 0, -1):
#         print("%d x %d = %d" % (i, j, i * j), end="\t")
#     print()
# 倒序打印99乘法表(python特有的)
for i in range(1, 10).__reversed__():
    for j in range(1, i+1):
        print("%d x %d = %d" %(j, i, i * j), end="\t")
    print()
