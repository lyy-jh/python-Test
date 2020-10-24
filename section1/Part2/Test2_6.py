"""

嵌套循环
print语句
    print() 相当于 print(end="\n")
    默认是print("",end="\n")   默认换行
    print("",end="")  打印完后什么也不做
    print(""," ") 打印完后加个空格
    print("","\t") 打印完后加tab空格
    print("","abc") 打印完后加abc

    外循环控制行数，内循环控制列数
"""
i = 0
while i <3:
    j = 0
    while j < 5:
        print("*", end="")
        j += 1
    print()
    i += 1
