"""
递归的使用
    概念：
        直接或间接的自己调用自己
    特点:
        1.只要能用循环解决的问题，用递归都能解决
        2.递归算法会比较快.小批量的计算会比较快，比循环要快(但是递归运算的次数太多会报错，一般在（996-998次）)
        3.计算次数较少的情况下，递归比循环快。但是递归有风险，递归所有的操作都可以在栈内操作，不停的压栈的话，栈会满，
        然后报错RecursionError: maximum recursion depth exceeded while calling a Python object
        错误的意思是:在调用python对象时超过了最大递归深度
    原理：
        压栈（栈：先进后出）



"""
count = 0


def test():
    global count
    count += 1
    print("递归调用的次数%d" % count)
    if count > 100:     # 递归结束条件
        return
    test()


# 报错RecursionError: maximum recursion depth exceeded while calling a Python object
test()


# 用递归写1+2+3+4+...+100
def add_sum(num):
    if num == 1:
        return 1
    else:
        return num + add_sum(num-1)


print(add_sum(100))


# 分别使用循环和递归计算 5!
def get_product1(num):
    product = 1
    for i in range(1, num+1):
        product *= i
    return product


def get_product2(num):
    if num == 1:
        return 1
    else:
        return num * get_product2(num-1)


print(get_product1(5))
print(get_product2(5))
