"""
dict的常用方法
    增加
        添加只能用  dict1[key]  = value(可以为任意类型)
    删除
        1.dict1.pop(key)
            pop()方法中一定要写参数，否则报错 TypeError: pop expected at least 1 arguments, got 0
            删除不存在的key值，也会报错  KeyError: 'li'
        2.del dict[key]
            del dict1  删除掉整个字典
        3.dict1.clear()
            清空所有的值

    修改
        key值唯一，二次赋值的新值覆盖旧值
    查询
        keys
        values
        items
"""
students = {"张三": {"age": 18, "id": "1001"}, "李四": {"age": 20, "id": "1002"}, "王五": {"age": 21, "id": "1003"}}
# print(students["张三"])
# # 增加数据
# students["王五"] = {"age": 21, "id": "1003"}
# print(students)


# students = {}
# name = input("请输入名称\n")
# score = input("请输入分数\n")
# student = {'name': name, 'score': score}
# student = [name, score]
# students[name] = student
# print(students)
# 获取分数
# key值不存在会报错 KeyError: 'lyy'
# print(students[name]["score"])

# 删除元素
# del_name = input("请输入要删除的名字")
# 1.pop(key)
# dict1.pop("key") pop()方法中一定要写参数，否则报错 TypeError: pop expected at least 1 arguments, got 0
# 删除不存在的key值，也会报错  KeyError: 'li'
# students.pop(del_name)
# 2.del dict1[key]  删除不存在的key值，也会报错  KeyError: 'li'
# del students[del_name]

# 直接把字典删掉了
# del students

# 清空所有的值
# students.clear()
# print(students)

# 修改值
# upd_name = input("请输入要修改的名字")
# new_score = input("请输入新的分数")
# students[upd_name] = {'name': upd_name, 'score': new_score}
# print(students)

# 查询
# 列出所有的key值
# 结果：dict_keys(['张三', '李四', '王五'])
# keys = students.keys()
# 结果：dict_keys
# print(type(keys))
# dict_values([{'age': 18, 'id': '1001'}, {'age': 20, 'id': '1002'}, {'age': 21, 'id': '1003'}])
# print(students.values())
# dict_items([('张三', {'age': 18, 'id': '1001'}), ('李四', {'age': 20, 'id': '1002'}), ('王五', {'age': 21, 'id': '1003'})])
# print(students.items())

# 遍历字典
# for key in students.keys():
#     print(key, end="\t")
#     print(students[key])
#
# print("张三" in students.keys())

for value in students.values():
    print(value)

for item in students.items():
    print(item)
