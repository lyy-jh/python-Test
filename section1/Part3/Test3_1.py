"""
需求：
    打印
    *
    **
    ***
    ****
    *****

"""
# line = 5
# i = 0
# while i < line:
#     j = 0
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1
"""
需求：
    打印
    *
    ***
    *****
    *******
"""
# 外循环控制打印的行数
# 内循环控制每行打印的*的个数
i = 0
while i < 4:
    j = 0
    while j < 2*i+1:
        print("*", end="")
        j += 1
    print()
    i += 1



