"""
需求
    使用嵌套循环打印菱形
       *
      ***
     *****
    *******
     *****
      ***
       *
"""


# row = 4
# for i in range(row):   # range(row) 指的是从0到row
#     for k in range(row-i-1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         print("*", end="")
#     print()
# for i in range(row+1, 2*row):
#     for k in range(i - row):
#         print(" ", end="")
#     for j in range((2*row-i)*2-1):
#         print("*", end="")
#     print()

row = 3
for i in range(row):   # range(row) 指的是从0到row
    for k in range(row-i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
for m in range(2 * row+1):
    print("*", end="")
print()
for i in range(row).__reversed__():   # range(row) 指的是从0到row
    for k in range(row-i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

"""
打印等腰三角形
      *
     ***  
    *****
   *******

"""
# range(row) 指的是从0到row
# row = 4
# for i in range(row):
#     # 打印*号前面的空格
#     for k in range(row-i-1):
#         print(" ", end="")
#     # 打印*号
#     for j in range(2 * i + 1):
#         print("*", end="")
#     print()

