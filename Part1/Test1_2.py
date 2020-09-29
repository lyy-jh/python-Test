# 导入获取关键字的包
import keyword
"""
可以用在双引号里面的任意位置，不能用在变量前后

\t 制表符，相当于一个tab键
\n 换行符
"""
count1 = 2
count2 = 3
print(" count1 = %g\n count2 = %g" % (count1, count2))

"""
标识符 ：
    1.本质就是一个名字
        变量名、方法名、类名、文件名、包名...
    2.标识符命名规则
        组成部分：字母(包括汉字)、数字、下划线
        开头：字母或下划线，数字不能开头
        大小写敏感
        不能使用系统关键字

驼峰命名规则
    大驼峰：每个单词首字母大写  MaxNum
    小驼峰：除了第一个单词外其他单词首字母大写  maxNum
    
用下划线连接的命名规则
    max_num

关键字：
 
"""
# 获取关键字列表
result = keyword.kwlist
# 打印所有的关键字
print(result)
# 打印关键字个数
print(len(result))
