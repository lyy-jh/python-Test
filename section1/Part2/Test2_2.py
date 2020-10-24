"""
多分支(可以写任意多个)
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

# score = int(input("请输入你要查询的分数\n"))
#
# if 90 <= score <= 100:
#     print("A")
# elif 80 <= score < 90:
#     print("B")
# elif 70 <= score < 80:
#     print("C")
# elif 60 <= score < 70:
#     print("D")
# elif 0 < score < 60:
#     print("E")
"""
需求：和电脑猜剪刀石头布，打印输赢
电脑随机生成： 0-石头，1-剪刀，2-布
自己输入：0-石头，1-剪刀，2-布
自己猜拳结果：
    赢了
    平局
    输了
"""

random_num = random.randint(0, 2)
# print(random_num)
print("计算机已做好准备")

input_num = int(input("请输入0:石头，1：剪刀：2布\n"))
if input_num - random_num == -1 or input_num - random_num == 2:
    print("赢了")
elif random_num == input_num:
    print("平局")
else:
    print("输了")
