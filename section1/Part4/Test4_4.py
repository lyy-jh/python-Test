"""
list的增删改查
    一、增加
        1.append（object）
            作用：通过append向指定列表添加元素(在列表尾部追加)
            语法：list1.append(object)  在list1尾部添加元素object
        2.extend(iterator)
            作用：通过extend可以将一个列表中的元素逐个添加到另一个列表中; 如果是字符串，会把字符串拆开逐个往里加
            语法：list1.extend(list2)  将list2列表中的元素添加到list1
        3.insert(index,object)
            作用：在列表指定的位置插入元素object
            语法：list1.insert(index,object)
    二、删除
        1.del obj
            作用：根据下标进行删除
            语法：del list1[0]
        2.pop(index)
            作用：根据下标进行删除,不写索引值默认删除最后一个元素
            语法：list1.pop()
        3.remove(obj)
            作用：根据元素的值进行删除
            语法：list1.remove(obj)
        4.clear()
            作用:将整个列表清空，但是列表还存在，为空列表
            语法：list1.clear()
        注意：如果要同时删除索引为1，3，5的数据，一定要从后往前删。因为删除前面的，后面的索引值会变。
    三、修改
        1.直接通过下标来修改元素
            语法：
                list1[index] =obj
        2.根据元素值来修改
             步骤如下：
                1.先判断”xz“是否存在该列表
                2.”xz“在该列表存在，判断索引值
                3.根据索引值修改值
            语法：
                if "xz" in list1:
                    index = list1.index("xz")
                    list1[index] = "wyb"
                else:
                    print("'xz'不存在列表中")
                print(list1)
    四、查询
        1.in
            作用：如果存在，返回True,否则返回False
            语法：
                obj in list1
        2.not in
            作用：如果不存在，返回True,否则返回False
            语法：
                obj not in list1

        3.index
            作用：返回元素在列表中的索引值，如果列表中不包含查询元素会报错:ValueError: 'jh' is not in list
            语法：
                list1.index(obj)
                index(obj,fromIndex,toIndex) 区间位置为前闭后开

        4.count
            作用：返回元素在列表中出现的次数，没有找到的元素返回0，不会报错
            语法：
                list1.count(obj)
"""
# 创建一个空的列表
list1 = []
# 增加

list2 = ["dl", "wjk", "lhy"]

# append
# 结果：['lx']
list1.append("lx")
print(list1)

# extend
# 结果：['lx', 'dl', 'wjk', 'lhy']
list1.extend(list2)
print(list1)

# insert
# 结果：['lx', 'lyy', 'dl', 'wjk', 'lhy']
list1.insert(1, "lyy")
print(list1)
# 结果：['lx', 'lyy', 'dl', 'wjk', 'xz', 'lhy']
# -1表示放在最后一个，现在将新加入的放到原来最后一个的位置上，原来的最后一个向后移
list1.insert(-1, "xz")
print(list1)

# 查询
# index
print(list1.index("dl"))
# 报错，不包含索引值3
# print(list1.index("wjk", 0, 3))

# count 元素在列表中出现的次数
# 1代表该值出现1次
print(list1.count("lyy"))
# 0代表列表中没有改值
print(list1.count("jh"))

# in
# True
print("xz" in list1)
# False
print("jh" in list1)

# not in
# False
print("xz" not in list1)
# True
print("jh" not in list1)

# 修改
list1[-1] = "jh"
# 打印结果：
print(list1)

# 给列表中的”xz“改名为"wyb"
# 步骤如下：
# 1.先判断”xz“是否存在该列表
# 2.”xz“在该列表存在，判断索引值
# 3.根据索引值修改值
if "xz" in list1:
    index = list1.index("xz")
    list1[index] = "wyb"
else:
    print("'xz'不存在列表中")
print(list1)

# 删除
# remove 按元素的值删除
list1.remove("dl")
# 结果：['lx', 'lyy', 'wjk', 'xz', 'lhy']
print(list1)

# pop 不写索引值默认删除列表的最后一个元素
list1.pop()
# 结果：['lx', 'lyy', 'wjk', 'xz']
print(list1)

# 按索引值删除
list1.pop(0)
# 结果：['lyy', 'wjk', 'xz']
print(list1)

# del 根据下标删除
del list1[1]
# 结果：['lyy', 'xz']
print(list1)
# 删除整个列表，列表都不存在了
# del list1
# 打印报错：NameError: name 'list1' is not defined
# print(list1)

# 删除列表中所有元素,但是列表还存在
list1.clear()
# 结果：[]
print(list1)

