"""
文件的写入操作
    文件：
        1.分类：
            .avi
            .mp4
            .txt
            .doc
            .gif
            .jpg
            .py
        2.特点：
            数据持久化
        3.文件操作：
            （1）打开文件
                file = open()，系统函数
            （2）读/写（文件内容的操作）
                write("内容")
            （3）关闭文件（自动保存）
                close()
        4.文件的绝对路径
            （1）windows需要把\改为 /，\有转义的意思
                D:/app_uiautomation/AirtestCases_XNG
            （2）windows需要加上\
                D:\\app_uiautomation\\AirtestCases_XNG
        5.open() 函数的参数
            （1）model='r','w','a'，'w'和'a',没有文件都会创建文件
                'r'读取
                'w'写入
                'a'追加
                ‘b’二进制的读取，按字节的形式
            （2）encoding="utf-8"

"""

import locale

# 获取当前默认编码方式
# cp936  类似gbk
# GBK是国标  UTF-8是国际通用的，兼容性更强
print(locale.getpreferredencoding())
# 个
print("%c" % 20010)

# 将”HelloWorld“写到123.txt中
# file:如果不写绝对路径，则在当前文件夹创建
# model = 'w'  如果文件不存在，会创建一个文件;如果文件存在，会把里面的内容覆盖掉替换成新的内容
file = open("123.txt", 'w', encoding="utf-8")
file.write("liyingying")
file.close()

