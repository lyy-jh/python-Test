"""
字符串常用操作
Zeal 查看方法的api文档

1.find/rfind(right find)
    如果找到了，则返回索引值；如果没有找到，则返回-1
    find为从左向右找,找到第一次出现的
    rfind为从右向左找，找到第一次出现的
2.index/rindex
    查找索引值，找到返回索引值，没有找到会报错
    与find()类似，唯一的区别是没有找到会报错, ValueError: substring not found
3.count
    返回目标字符串在str的start-end之间出现的次数
    找到返回出现的次数;没有找到返回0
4.replace
    将字符串中指定的目标字符用其他字符替换，默认替换所有找到的目标字符
    str2 = str1.replace(old, new, count) ,str1没有被改变，str2的内容被替换
    old为原字符，new为新字符，count为替换的次数
5. split
    以某一个内容作为边界进行拆分
6.splitlines()
    按换行(\n)进行拆分
    将目标字符串按照行进行分割，并返回一个列表
7.capitalize
    把字符串的第一个字符大写

"""
# 展示str中的所有方法
# result = dir(str)
# print(result)

str1 = "The difference between who you are and who you want to be is what you do."

# 1.find/rfind(right find),返回索引值

# 查找str1中有没有who，返回索引值

# 从左向右找，返回索引值23
print(str1.find('who'))
# 如果没有找到,返回索引值-1
print(str1.find("me"))

# 从右向左找，返回索引值为39
print(str1.rfind("who"))
# 从右向左找，返回索引值为-1
print(str1.rfind("me"))

# 2.index/rindex
# 查找str1中有没有who，返回索引值

# 从左向右找，返回索引值23
print(str1.index('who'))
# 如果没有找到,报错ValueError: substring not found
# print(str1.index("me"))

# 从右向左找，返回索引值为39
print(str1.rindex("who"))
# 从右向左找，没有找到，报错 ValueError: substring not found
# print(str1.rindex("me"))

# 3.count

# 查找who在str1中出现的次数，找到返回出现的次数
print(str1.count("who"))
# 没有找到返回0
print(str1.count("me"))

# 4.replace
# 用aaa替换who,替换2次, str1没有变，变化的是接收它的变量str2
str2 = str1.replace("you", "aaa", 2)
# 变化的是接收它的变量str2
print(str2)
# str1没有变
print(str1)

# 5.split
print(str1.split(" "))

# 按换行(\n)进行拆分
str3 = "The difference \nbetween who you are \nand who you want to be \nis what you do."
print(str3.splitlines())

# 6.capitalize ,把字符串的第一个字母大写
str4 = "you and me"
str5 = str4.capitalize()
print(str5)
