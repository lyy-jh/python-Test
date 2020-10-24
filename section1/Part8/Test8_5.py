"""
文件代码行数统计算法
    1.统计单个文件中的代码行数(注意：换行也是一行代码，它是\n)
        单行注释不统计
        多行注释不统计
    2.统计某个文件夹中所有的.py文件代码行数
"""


# 统计代码行数
def iris_code_counter(srcfile):
    # 打开文件
    file = open(srcfile, 'r', encoding="utf-8")
    # 代码总行数
    lines = 0
    # 控制是统计行数的开关
    add = True
    # 读取文件内容
    content = file.readline()
    while content != "":
        # 判断读取到的内容是否记录到行数中
        # 判断多行注释，用一个开关来控制
        str1 = '"""'
        if str1 in content:
            # 这样每遇到一次就会翻转
            add = not add
        if add:
            # 单行注释的判断，不能用是否以#开头来判断(因为注释往后缩的话是以空格开头的)
            # 用内容中是否包含#来判断
            if "#" not in content:
                lines += 1
        content = file.readline()
    # 关闭文件
    file.close()
    return lines


# print(iris_code_counter("Test8_1.py"))
