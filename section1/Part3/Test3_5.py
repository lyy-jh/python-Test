"""
数据类型:
    基本类型
        int
        float
        bool
    引用类型
        str
        list
        dict
        tuple
        set
str简介
    字符串的定义
        str1 = 'HelloWorld'
        str2 = "HelloWorld"
        单引号和双引号都可以
        '\n'也是字符串
    字符串的输出
        print("%s" % str1)
    字符串的输入
        str3 = input("请输入字符串\n")
    字符串的长度
        len(变量/常量)
    字符串的索引值
        str1[0] 第一个字符
        str[-1] 倒数第一个字符
        范围[0,字符串长度-1]
    字符串的切片操作
    操作字符串常用的方法
"""
str1 = "Hello"
str2 = '\n'
# 打印结果
# Hello
# World
print(str1 + str2 + "World")
# 打印结果
# HelloWorld
print(str1 + "World")

print("%s" % str1)

str3 = input("请输入字符串\n")
print(str3)

print(len(str3))  # 求变量str3中存储的字符串内容的长度
print(len("str3"))  # 求“str3”这个字符串的长度，长度为4

print(str1[0])  # 打印str1的第一个字符
print(str1[-1])  # 打印str1的倒数第一个字符
print(str1[-2])

# 使用循环完成字符串中每个字符的打印,使用\t隔开
str5 = "beautiful"
for i in range(len(str5)):
    print(str5[i], end="\t")

print()

i = 0
while i < len(str5):
    print(str5[i], end="\t")
    i += 1
print()
# for循环对字符串的操作
for i in str5:
    print(i, end="\t")

