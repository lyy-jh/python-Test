"""
列表中元素的排序
    1.sort()
        概述：
            按自然顺序进行排序（从小到大排序）
            排序后不返回任何值，只是对原列表的一个排序，没有新的备份生成
        语法：
            list1.sort()

    2.sort(reverse=True)
        概述：
            按从大到小排序，只要reverse = 的值不为0或False,就认为是从大到小排序
        语法：
            list1.sort(reverse=True)
            list1.sort(reverse=1)


嵌套列表的使用
    list2 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

嵌套列表中所有元素的遍历


"""
# 列表排序
list1 = [89, 67, 58, 97, 100, 78]
list1.sort()
# 结果：[58, 67, 78, 89, 97, 100]
print(list1)

# list1.sort(reverse=True)
list1.sort(reverse=1)
print(list1)

# 列表嵌套使用
list2 = [[1, 2, 3], 4, [6, 7, 8, 9]]

# 嵌套列表中所有元素的遍历
for sub_list in list2:
    # 判断sub_list是否为列表
    if type(sub_list) ==list:
        for i in sub_list:
            print(i, end="\t")
    else:
        print(sub_list, end="\t")
