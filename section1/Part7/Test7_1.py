"""
练习：
1.判断一个数是否为质数
    大于1的自然数，只能被1和它本身整除
2.打印1-1000之间所有的质数，两个一排
"""


# 判断一个数是否为质数
def is_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
#
#
# print(is_prime_number(1))
#
#
# def is_prime_number2(number):
#     result = True
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 result = False
#                 break
#     else:
#         result = False
#     return result


# 打印1-1000之间所有的质数，两个一排
def print_prime():
    count = 0
    for i in range(1, 1001):
        if is_prime_number(i):
            count += 1
            print("%3d" % i, end=" ")  # %3d就是占3位，可以对齐操作
            if count % 2 == 0:
                print()


print_prime()
