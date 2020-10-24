"""
匿名函数（lambda）的使用
    概念：
        用lambda关键字创建的简单的没有函数名的函数，这种函数不用def声明
    关键字：
        lambda ,没有def
    语法：
        1.lambda 参数... :表达式    (可以有多个参数)
        2.可以把匿名函数存到某个变量中，例如 get_sum1 = lambda a, b: a+b,其中get_sum1是变量，lambda表示匿名函数，a, b是参数， a+b 表达式
        匿名函数存在方法区内，它有一个内存地址，变量中存储匿名函数的地址
        变量的类型是function
    注意：
        1.在匿名函数中不能使用return
        2.可以有0，1，多个参数
        3.只能返回一个值
    优点:
        在程序中只使用一次，不需要定义函数名，节省内存中变量定义空间
    正常函数返回值问题：
        正常函数是可以返回1个或多个值的
            (1)正常函数返回多个值，如果用一个变量接收，那么多个值会放到一个tuple中返回
            （2）如果个数匹配的变量去接收，那么会分开赋值（必须返回值个数和接收变量个数相等）
"""


def get_sum(a, b):
    return a+b


# 打印函数的地址：<function get_sum at 0x0000017659BE6708>
print(get_sum)


get_sum1 = lambda a, b: a+b  # 匿名函数存在方法区内，它有一个内存地址，变量中存储函数的地址
# <class 'function'>
print(type(get_sum1))
# <function <lambda> at 0x000001E8F09E6438>
print(get_sum1)

# 调用匿名函数
print(get_sum1(10, 20))


# 正常函数返回多个值
def test():
    return 1, 2


result = test()
# <class 'tuple'>
print(type(result))
# (1, 2)
print(result)

v1, v2 = test()
# <class 'int'>
print(type(v1))
# 1
print(v1)
# <class 'int'>
print(type(v2))
# 2
print(v2)

# 匿名函数的地址<function <lambda> at 0x00000208C74668B8>
print(lambda x, y: x ** y)
