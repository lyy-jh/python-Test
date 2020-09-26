""""
数据类型:
    python是弱语言类型，可以根据值动态分配类型

    # 没有范围区分，不会溢出
    int   整数
    float 小数

    type(要查看的变量或者常量的名称)，得到该变量或常量所属的数据类型

    # 可以存储很多任意类型的值
    list  列表，
    tuple 元组
    dict  字典
    set   集合

    # 布尔类型，取值True/False
    bool




输出
    格式化输出
        %g : 输出整数或小数
        %d : 输出整数，如果变量是小数，则小数点之后的数字舍弃
        %f : 输出小数，一般会保留小数点后6位
        %s : 输出字符串

输入
    键盘输入的值为str类型
"""
num = 12
# 打印数据的类型，<class 'int'>
print(type(num))

PI = 3.14
# 打印数据的类型，<class 'float'>
print(type(PI))

# 格式化输出
# 输出3.14和12
print("PI = %g" % PI)
print("num = %g" % num)
# 输出3和12
print("PI = %d" % PI)
print("num = %g" % num)
# 输出3.140000和12
print("PI = %f" % PI)
print("num = %g" % num)

# 保留小数点后3位,%.3f
print("PI = %.3f" % PI)

# 输入
# 可乐的价格
price = 2.8
# 可乐的数量
count = input("请输入购买的数量\n")

# 从键盘输入的值为str，需要转换成int类型
count = int(count)

#
print("可乐的单价%g元，可乐的数量%d瓶，可乐的总价%g元" % (price, count, price * count))

