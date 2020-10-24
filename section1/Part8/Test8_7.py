"""
批量修改文件名
    注意：修改名称的时候一定要写绝对路径

"""
import os


def rename_files(path):
    files = os.listdir(path)
    for file in files:
        # 判断是否为文件夹需要用绝对路径
        if os.path.isdir(path+"/"+file):
            rename_files(path+"/"+file)
        # 判断是否为文件需要用绝对路径
        elif os.path.isfile(path+"/"+file):
            if file.endswith(".py"):
                # 修改名称的时候需要写绝对路径
                os.rename(path+"/"+file, path+"/"+"Te"+file[1:])


# print(os.getcwd())
rename_files("/section1/Part7")