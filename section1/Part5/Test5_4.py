"""
dict字典的定义使用
    {key:value,key2:value2}
    {'CN':'China','JP':'Japan','CA':'Canada'}
    特点：
        key具有唯一性，再加相同的key，value会被新加的value替换
        不同的key,value可以相同
        key一般用字符串或数字类型,但提倡用字符串
dict中元素的访问
    dict1[key]
dict中常用方法
dict中元素遍历
"""
# countries = {'CN': 'China', 'JP': 'Japan', 'CA': 'Canada', 'JP': 123}
# 'JP'被替换
# 结果：{'CN': 'China', 'JP': 123, 'CA': 'Canada'}
# print(countries)

student = {'num_id': '1001', 'name': 'lyy', 'age': '25', 'gender': '女', 'score': '95'}
# 访问元素
print(student['name'])



