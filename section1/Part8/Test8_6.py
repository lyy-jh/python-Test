"""
统计某个文件夹中所有的.py文件代码总行数
"""
import os

# 统计某个文件夹中所有的.py文件代码总行数
count = 0


def show_all_files_in_dir(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(path+"/"+file):
            show_all_files_in_dir(path+"/"+file)
        elif os.path.isfile(path+"/"+file):
            if file.endswith(".py"):
                global count
                count += section1.Part8.Test8_5.iris_code_counter(path + "/" + file)
    return count


# print(os.getcwd())
print(show_all_files_in_dir("/"))


