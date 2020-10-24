"""
元组：tuple
    语法：（元素1，元素2，元素3）
    特点：不可变,相当于文件为只读属性；元组中存储的值，不可修改、不可删除、不可添加；类似于C语言中的指针
    查询：可以访问指定索引值的元素
        语法 tuple1[0]
    转换：
        list和tuple之间可以相互转换,相当于根据原来的元素创建了一个新的list或tuple
        语法：
            list1 = list(tuple1)  tuple转list

            list1[0] = 100
            
            # tuple1是被整体重新赋值了，而不是只改了其中的一个元素
            tuple1 = tuple(list1)  list转tuple


字典：dict
"""
tuple1 = ('学生1', 99, 9, 'www')
print(type(tuple1))

# 报错：AttributeError: type object 'tuple' has no attribute 'append'
# tuple.append(1992)


# 删除元素
# 报错：TypeError: 'tuple' object doesn't support item deletion
# del tuple1[-1]

# 修改
# 报错 TypeError: 'tuple' object does not support item assignment
# tuple1[1] = 100

# 查询
# 访问元素
print(tuple1[0])
# 循环遍历元素
for i in tuple1:
    print(i, end="\t")
print()

# 查某个元素的索引值
print(tuple1.index(99))
# 报错 ValueError: tuple.index(x): x not in tuple
# print(tuple1.index(00))

# count
print(tuple1.count(9))

# in
print(99 in tuple1)

# not in
print(99 not in tuple1)

# list和tuple之间可以相互转换,相当于根据原来的元素创建了新的list或tuple
list1 = list(tuple1)
print(list1)

list1[0] = 100
# tuple1是被整体重新赋值了，而不是只改了其中的一个元素
tuple1 = tuple(list1)

print(tuple1)