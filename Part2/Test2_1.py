"""
分支语句
    1.单分支
        if 表达式：
            表达式成立执行的代码
    2.双分支（二选一）
        if 表达式：
            表达式成立执行的代码
        else:
            表达式不成立执行的代码
    3.多分支(可以写任意多个)
        if 表达式1：
            表达式1成立执行的代码
        elif 表达式2：
            表达式2成立执行的代码
        elif 表达式3：
            表达式3成立执行的代码
        else：
            以上表达式都不成立执行的代码
"""
import random

random_num = random.randint(1, 6)
print(random_num)

if 1 <= random_num <= 3:
    print("小")
else:
    print("大")
