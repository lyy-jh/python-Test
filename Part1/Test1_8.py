"""
比较运算符
    >
    <
    >=
    <=
    ==
    !=
比较结果：
    bool值
        True   Yes  非0
        False   No  0
逻辑运算符
    and
    or
    not
逻辑运算符的结果：
    bool
"""
import random

result = 10 > 9
print(result)
print(type(result))

random_num = random.randint(1, 6)
print(random_num)
# 判断表达式只有python可以这样写
if 1 <= random_num <= 3:
    print("小")
if 4 <= random_num <= 6:
    print("大")

# 如果为表达式结果为非0，则执行；如果表达式结果为0，则不会执行
if 3:
    print("执行")
if 0:
    print("不执行")

# 比较运算符,相同类型，拿左侧第一个字符和右侧第一个字符做比较
print("b" > "abc")  # True

# 结果5,其他语言不允许这样
print(1 and 5)

# 需求:给出用户名和密码，用户名和密码都正确之后，给出登录成功提示

account = input("请输入用户名\n")
password = input("请输入密码\n")

if (account == "lyy") and (password == "jh"):
    print("登录成功")

if (account != "lyy") or (password != "jh"):
    print("登录失败")