"""
文件的复制
    需求：
        将123.txt复制一份----->123-副本.txt
    步骤：
        （1）打开目标文件
        （2）读取文件内容
        （3）新建目标文件并写入读取的内容
            此处需要注意新文件的名字处理：123-副本.txt
        （4）关闭两个文件
切片操作复习
    字符串[start:end:step]
        包括start,不包括end
        -1,最后一个

"""


def copy_file(filepath, filename):
    # 从右向左找到.的位置
    index = filename.rindex(".")
    # 截取.前面的内容
    name = filename[0:index]
    # 截取.及以后的内容
    suffix = filename[index:]
    # 新文件名称
    new_filename = name+"-副本"+suffix
    # 读取原文件内容
    file = open(filepath+filename, 'r', encoding="utf-8")
    content = file.read()
    # 写到新文件
    new_file = open(filepath+new_filename, 'w', encoding="utf-8")
    new_file.write(content)
    # 关闭原文件和新文件
    file.close()
    new_file.close()


copy_file("C:/Users/liyingying/Desktop/", "123.txt")

