"""
文件的读取操作
    1.文件写操作：
        文件关闭时默认刷新，如果文件不关闭，可能导致文件写不进入，内容在缓冲流中，没有刷新进去
        但是可以用file.flush()刷新操作
    2.文件读操作
        （1）read(n)  一次性读取所有的内容（小批量内容时用），返回的是字符串类型（所有内容拼装成一个字符串）<class 'str'>,n为读取的个数
        (2)readLine 一次只读一行内容,返回的也是字符串类型<class 'str'>
        (3)readLines 一次读完所有的行，以\n分割成一个元素，返回是一个list,<class 'list'>
        (4)readable 判断文件是否可读，返回true,false

"""


# 写一首古诗到文件
# 写入的过程是先从输入设备写到内存，再从内存写到磁盘上（文件中）
# model="a" 如果没有文件，创建文件；如果有文件，则在原文件后追加内容
def write_ancient_poetry(filename):
    file = open(filename, 'a', encoding='utf-8')
    for i in range(1, 5):
        content = input("请输入第%d句\n" % i)
        file.write(content)
        file.write("\n")
        # 刷新操作，放在这个位置，每写一句都会刷新到文件中
        file.flush()
    # 文件关闭时默认会刷新
    file.close()


# write_ancient_poetry("D:\\视频\\888.txt")


def read_content(filename):
    file = open(filename, 'r', encoding="utf-8")
    # 判断文件是否可读
    if file.readable():
        content = file.read()
        # <class 'str'>
        print(type(content))
        print(content)
    file.close()


def read_content1(filename):
    file = open(filename, 'r', encoding="utf-8")
    # 判断文件是否可读
    if file.readable():
        content = file.readline()
        print(type(content))
        while content != "":
            print(content, end="")
            content = file.readline()

    file.close()


def read_content2(filename):
    file = open(filename, 'r', encoding="utf-8")
    # 判断文件是否可读
    if file.readable():
        content = file.readlines()
        # <class 'list'>
        print(type(content))
        print(content)
    file.close()


read_content2("D:\\视频\\888.txt")
