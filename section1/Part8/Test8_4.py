"""
文件夹及文件操作的常用方法
    文件：
        （1）重命名
            语法：
                rename("需要修改的文件名", "新的文件名")
            用法：
                注意：要修改的文件一定要保证没有被其他占用
                import os
                os.rename()
        （2）删除文件,该删除没有确认提示，不走回收站，直接删除
            语法：
                remove("待删除文件的名字")
            用法：
                import os
                os.remove()
    文件夹：
        (1)获取当前所在路径
            语法：
                getcwd()
            用法：
                import os
                os.getcwd()
        (2)改变默认目录
            语法：
              chdir()
            用法：
                import os
                os.chdir("要修改到的默认目录")
        (3)创建文件夹
            语法：
                mkdir()
            用法：
                import os
                os.mkdir()
        (4)删除文件夹
            语法：
              rmdir("文件夹路径")
            用法：
                import os
                os.rmdir("文件夹路径")

        （5）获取文件夹的所有子文件
            语法：
                listdir("指定文件夹")
            用法：
                import os
                os.listdir() 返回一个list

        （6）判断是否为文件
            语法：
                isfile()
            用法：
                import os
                os.path.isfile()
        （7）判断是否为文件夹
            语法：
                isdir()
            用法：
                import os
                os.path.isdir()


"""
import os
# 文件重命名
# os.rename("123.txt", "125.txt")
# os.rename("D:\\视频\\888.txt", "D:\\视频\\666.txt")

# 删除文件
# os.remove("125.txt")

# 获取当前路径
print(os.getcwd())

# 改变当前文件默认目录,改变之后，所有文件都去该目录下查找
# os.chdir("d:/")
# print(os.getcwd())

# 创建文件夹
# os.mkdir("123")

# 删除文件夹
# os.rmdir("123")

# 获取文件夹中的所有子文件
path = os.getcwd()
paths = os.listdir(path)
print(paths)

# 判断是否为文件
print(os.path.isfile("123.txt"))

# 判断是否为文件夹
print(os.path.isdir("123.txt"))
print(os.path.isdir(path))

files = os.listdir("//")
for filename in files:
    if os.path.isdir("D:/software/pythonProjects/Test/"+filename):
        print(filename)
        for name in os.listdir("D:/software/pythonProjects/Test/"+filename):
            print(name)
    else:
        print(filename)
