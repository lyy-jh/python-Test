"""
字符串方法的使用
1.title()
    将字符串中的每个单词的首字母大写
2.startswith()
    检查字符串是否以指定单词开头,返回bool值 True/False
3.endswith()
    检查字符串是否以指定字符串结尾，返回bool值 True/False
4.lower()
    转换字符串中所有的大写字母为小写
5.upper()
    转换字符串中所有的小写字母为大写
6.ljust(width,fillchar)
    width:宽度
    fillchar:扩充使用的字符,默认为空格
    返回一个原字符串左对齐，并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
7.rjust(width,fillchar)
    返回一个原字符串右对齐，并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
8.center(width,fillchar)
    返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格
9.lstrip
    删除目标字符串左边的空格
10.rstrip
    删除目标字符串右边的空格
11 strip
    删除目标字符串两边的空格


"""
# title 将字符串中的每个单词首字母大写
str1 = "The difference between who you are and who you want to be is what you do."
str2 = str1.title()
print(str2)

# startswith
print(str1.startswith("The"))

# endsWith
print(str1.endswith("."))

# lower
str3 = str2.lower()
print(str3)

# upper
str4 = str3.upper()
print(str4)

# ljust
str5 = str1.ljust(100, "*")
print(str5)

# rjust
str6 = str1.rjust(100, "*")
print(str6)

# center
str7 = str1.center(100, "*")
print(str7)

# lstrip
str8 = "   123   "
print(str8)

print(str8.lstrip())
print(str8.rstrip())
print(str8.strip())



