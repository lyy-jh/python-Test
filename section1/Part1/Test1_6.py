""""
需求
    从键盘输入两个整型数字
    交换他们的值
数据类型转换
    - int(x,[,base])	将x转换为一个整数
    - float(x)		将x转换为一个浮点数
    - complex(real,[,imag])	创建一个复数
    - str(x)		将x转换为字符串
    - repr(x)		将对象x转换为表达式字符串
    - eval(str)		用来计算在字符串中的有效python表达式，并返回一个对象
    - tuple(s)		将序列s转换为一个元组
    - list(s)		将序列s转换为一个列表
    - hex(x)		将一个整数转换为一个十六进制的字符串
    - oct(x)		将一个整数转换为一个八进制的字符串
"""
a = int(input("请输入第一个值"))
b = int(input("请输入第二个值"))
print("交换前：a=%g,b=%g" % (a, b))
# 传统语言的方式，引入第三个变量 temp
temp = a
a = b
b = temp
print("交换后：a=%g,b=%g" % (a, b))


# python可以使用的方式(但是不推荐)，其他语言不要这样用，可能出现溢出
# 先把他们混合起来
a = a + b
# 把a的值赋给b
b = a - b
# 把a+b-a的值赋给a
a = a - b
print("交换后：a=%g,b=%g" % (a, b))

# python常用的交换方式
# 他们两个是同时进行的，不能拆开写 a = b b = a
a, b = b, a
print("交换后：a=%g,b=%g" % (a, b))
