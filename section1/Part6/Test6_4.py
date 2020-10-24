"""
函数的返回值问题
    返回值的关键字：return
"""
# 求1+2+3+4+...+n的和

# 第一种方法
# def add_sum(n):
#     return (1+n)*n/2


# 第二种方法
def add_for_sum(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


print(add_for_sum(10))


# 判断一个整数是否为偶数
def is_even(num):
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    # result = False
    # if num % 2 == 0:
    #     result = True
    # return result

    return num % 2 == 0


print(is_even(10))


# 求任意三个整数的平均数
def average_num(a, b, c):
    return (a+b+c)/3


print(average_num(11, 14, 35))


# 打印自定义*个数的直线
def print_start(num):
    print("*" * num)
    # for i in range(num):
    #     print("*", end="")


print_start(10)
print()


# 打印自定义行数，自定义*个数的直线
def print_start_line(line, num):
    for i in range(line):
        # print("*" * num)
        # 调用1的方法
        print_start(num)


print_start_line(3, 5)
