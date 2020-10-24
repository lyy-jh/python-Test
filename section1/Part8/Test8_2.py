"""
复制文件的另一种封装方法
"""


def copy_file(srcfile):
    index_filename = srcfile.rindex("/")
    filename = srcfile[index_filename+1:]
    filepath = srcfile[0:index_filename+1]
    # 从右向左找到.的位置
    index = filename.rindex(".")
    # 截取.前面的内容
    name = filename[0:index]
    # 截取.及以后的内容
    suffix = filename[index:]
    # 新文件名称
    new_filename = name+"-副本"+suffix
    # 读取原文件内容
    file = open(srcfile, 'r', encoding="utf-8")
    content = file.read()
    # 写到新文件
    new_file = open(filepath+new_filename, 'w', encoding="utf-8")
    new_file.write(content)
    # 关闭原文件和新文件
    file.close()
    new_file.close()


copy_file("C:/Users/liyingying/Desktop/123.txt")