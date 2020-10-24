"""
文件指针偏移处理
    文件指针：
        就是指光标
    方法：
        (1)查看光标的位置
            文件名.tell()
        (2)光标位置手动偏移
            文件名.seek(offset, whence)  offset偏移位置的个数，whence从哪个位置开始偏移
"""

# # 文件名.tell()的用法
# file = open("123.txt")
# # 查看光标的位置，刚打开的文件为0
# print(file.tell())
# # 读取了2个位置
# file.read(2)
# # 现在查看光标的位置为2
# print(file.tell())


# import io
# # whence 也可以取以下的值
# # io.SEEK_SET ---->0  文件头
# # io.SEEK_CUR ---->1  当前位置
# # io.SEEK_END ----->2 文件尾
# file = open("123.txt")
# # 从文件开头，向后偏移两个位置开始读
# file.seek(2, 0)  # 等同于file.seek(2, io.SEEK_SET)
# content = file.read()
# # yingying
# print(content)
# file.close()


# 如果要用io.SEEK_CUR 和 io.SEEK_END ，对文件打开方式有要求，要求用model='rb'的二进制方式打开文件(以字节流的方式去处理)
# 从文件末尾读取2个数据（如果是从尾部进行重定位的话，需要以二进制形式打开文件）
# import io
# file = open("123.txt", 'rb')
# # -2表示向前取值
# file.seek(-2, io.SEEK_END)
# content = file.read()
# # b'ng'  b代表binary
# print(content)
# file.close()


# 从当前位置向后偏移2个位置开始读
# 如果要用io.SEEK_CUR，要求用model='rb'的二进制方式打开文件
import io
file = open("123.txt", 'rb')
c1 = file.read(2)
# b'li'
print(c1)
# 当前位置在2，再向后偏移2个位置开始读
file.seek(2, io.SEEK_CUR)
content = file.read()
# b'ngying'
print(content)
file.close()




