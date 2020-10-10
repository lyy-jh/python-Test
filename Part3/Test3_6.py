"""
字符串的切片操作
    字符串变量名[start:end:step]
    包含start,不包含end
    start可以不写，默认从0开始  :不能丢
    step默认为1
    step为负时，表示从右往左取，start需要大于end，才会取到值
"""
str_num = "0123456789"
# 截取前两个字符,不包含end
result = str_num[0:2]
print(result)

# 截取前两个字符串，start可以省略，默认从0开始
result1 = str_num[:2]
print(result1)

# 截取两个字符，步长为2,隔一个取一个
result2 = str_num[:5:2]
print(result2)

# 什么都不写，默认取所有的
result3 = str_num[::]
print(result3)

result4 = str_num[:]
print(result4)

# 指定开头，不指定结尾,截取从指定位置（索引值，包含指定的索引值）到结尾的所有字符
result5 = str_num[2:]
print(result5)

# 截取指定位置到结尾
result6 = str_num[1:len(str_num)]
print(result6)

# 切片操作，多切是不会报索引值越界的异常（IndexError），只是后面切不到值
result7 = str_num[1:len(str_num)+100]
print(result7)

# 切片操作，结尾可以为负值,-1表示最后一个，但是取不到最后一个
result8 = str_num[2:-1]
print(result8)

# 切片操作的步长为负值,从start位置倒着切片
result9 = str_num[5:1:-1]
print(result9)

# 取到02468
result10 = str_num[::2]
print(result10)

# 取到13579
result11 = str_num[1::2]
print(result11)

# 将字符串倒过来
result12 = str_num[::-1]
print(result12)

# 倒着隔一个取一个，97531
result13 = str_num[::-2]
print(result13)

# 倒着隔一个取一个，86420
result13 = str_num[8::-2]
print(result13)

# step为负时，start需要大于end，才会取到值
result14 = str_num[5:3:-1]
print(result14)


