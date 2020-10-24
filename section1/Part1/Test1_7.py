"""
if语句
    if 表达式：
        表达式成立执行的代码
需求
    模拟骰子大小 1-6
    1.随机数
    2.if判断
        1-3 输出小
        4-6 输出大
"""
# 导入随机数的包
import random

random_num = random.randint(1, 6)  # 产生1-6的随机整数
print(random_num)
if random_num <= 3:
    print("小")
if random_num >= 4:
    print("大")


