"""
字符串方法的使用
1.partition(str)
    有点像 find()和 split()的结合体
    从 str 出现的第一个位置起，把目标字符串分割成3 元 素 的 元 组 (string_pre_str,str,string_post_str）
    如果 string 中不包含str 则 string_pre_str == string,拆分情况为（string,'',''）
2.rpartition(str)
    从右向左，第一个str出现的位置分割成一个3元素的Tuple
3.splitlines()
    将目标字符串按照行进行分割，并返回一个列表
4.isalpha()
    判断目标字符串中是否所有的字符都为字母，返回值True/False
5.isdigit()
    判断目标字符串中是否所有的字符都为数字，返回值True/False
6.isalnum()
    判断目标字符串中是否所有的字符都为字母或者数字，返回值True/False
7.isspace()
    如果 string 中只包含空格，则返回 True，否则返回 False.
8.join(seq)
    以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    即在seq的每个字符之间插入string
    将字符串或者列表或者元组的每个元素使用指定字符串连接起来
9.字符串遍历的几种方式
    while /  for i in range / for i in 字符串变量
"""
# partition
str1 = "The difference between who you are and who you want to be is what you do."
# 结果：('The difference between ', 'who', ' you are and who you want to be is what you do.')
print(str1.partition("who"))
# 和split的区别
# ['The difference between ', ' you are and ', ' you want to be is what you do.']
print(str1.split("who"))
# rpartition
# 结果：('The difference between who you are and ', 'who', ' you want to be is what you do.')
print(str1.rpartition("who"))

# 如果找不到str,整个字符串都为string_pre_str
# ('The difference between who you are and who you want to be is what you do.', '', '')
print(str1.partition("me"))

# splitlines
str2 = "The difference \nbetween who you are \nand who you want to be \nis what you do."
print(str2.splitlines())

# isalpha
# 结果：False，有空格
print(str1.isalpha())
# True
print("abcd".isalpha())
# False
print("abcd123".isalpha())

# isdigit
# False
print(str1.isdigit())
# True
print("12345".isdigit())

# isalnum
# False
print(str1.isalnum())
# True
print("123abc".isalnum())
# True
print("12345".isalnum())
# True
print("abcd".isalnum())

# isspace
# False
print(str1.isspace())
# True
print("    ".isspace())

# join(seq)
# 运行结果：a123b123c
print("123".join("abc"))
str3 = "_"
li = ['one', 'two', 'three']
# 结果：one_two_three
print(str3.join(li))

# 字符串遍历的几种方式
str1 = "lyy and jh"

str1_len = len(str1)

# while循环遍历
i = 0
while i < str1_len:
    print(str1[i], end="")
    i += 1

print()

# for循环遍历
for i in range(str1_len):
    print(str1[i], end="")

print()

# for循环遍历
for i in str1:
    print(i, end="")
