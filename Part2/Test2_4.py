"""
循环
    1.while循环:
        语法：
        while 表达式：
            表达式成立执行的代码...
            迭代（趋向终止的条件）
    2.for循环:
"""
# 输出10个HelloWorld
# print("HelloWorld\t"*10)

# 使用while循环实现
# i = 0
# while i < 10:
#     print("HelloWorld")
#     i += 1
# 求1+2+3+...+100的和
j = 1
sum_num = 0
while j <= 100:
    sum_num += j
    j += 1
print("sum = %d" % sum_num)
