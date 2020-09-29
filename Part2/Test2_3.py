"""
分支语句的嵌套使用
if 表达式：
    if 表达式1：
        表达式1成立执行的代码
    else:
        表达式1不成立执行的代码
else:
    表达式不成立执行的代码

"""
"""
需求:
    先注册用户名密码
    使用用户名密码登录
    if 登录成功：
        if 输入验证码正确：
            登录成功
        else:验证码有误，请重新输入
    else：用户名或密码错误
"""
import random

print("请先注册：")
account = input("请输入用户名\n")
password = input("请输入密码\n")
print("请登录：")
acc = input("请输入用户名\n")
pwd = input("请输入密码\n")
if account == acc and password == pwd:
    # 生成一个六位的随机数验证码
    verification_code = str(random.randint(100000, 999999))
    print("您的验证码为：%s" % verification_code)
    code = input("请输入验证码：\n")
    if code == verification_code:
        print("登录成功")
    else:
        print("验证码输入有误，请过一分钟后重新获取")
else:
    print("用户名或密码错误")
"""
和计算机猜剪刀石头布
"""
# 计算机的数字
com_num = random.randint(0, 2)
# print(random_num)
print("计算机已做好准备，该你了！")

input_num = int(input("请输入0:石头，1：剪刀：2布\n"))
# 如果计算机出0
if com_num == 0:
    if input_num == 0:
        print("计算机输出石头，你输入石头，平局")
    elif input_num == 1:
        print("计算机输出石头，你输入剪刀，你输了")
    elif input_num == 2:
        print("计算机输出石头，你输入布，你赢了")
elif com_num == 1:
    if input_num == 0:
        print("计算机输出剪刀，你输入石头，你赢了")
    elif input_num == 1:
        print("计算机输出剪刀，你输入剪刀，平局")
    elif input_num == 2:
        print("计算机输出剪刀，你输入布，你输了")
elif com_num == 2:
    if input_num == 0:
        print("计算机输出布，你输入石头，你输了")
    elif input_num == 1:
        print("计算机输出布，你输入剪刀，你赢了")
    elif input_num == 2:
        print("计算机输出布，你输入布，平局")
