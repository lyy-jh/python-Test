"""
1.判断一个数字是否为水仙花数
    水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身,例如：1^3 + 5^3+ 3^3 = 153
2.打印所有的水仙花数
"""


# 判断一个数字是否为水仙花数
def is_daffodil_number(number):
    if number < 100 or number > 999:
        return False
    # 百位数
    n1 = number//100   # 取整除
    # 十位数
    n2 = number//10 % 10
    # 个位数
    n3 = number % 10
    return n1 ** 3 + n2 ** 3 + n3 ** 3 == number  # 两个 ** 表示求幂


print(is_daffodil_number(999))


# 打印所有的水仙花数
def print_all_daffodil_number():
    for i in range(100, 1000):
        if is_daffodil_number(i):
            print(i, end=" ")


print_all_daffodil_number()
