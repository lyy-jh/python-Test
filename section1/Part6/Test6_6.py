"""
可变参数的使用
    1.缺省参数
        形参为缺省参数时，在函数调用时，可以不给实参，此时，形参的值是给定的默认值
        如果在函数调用的时候给了实参。则形参的值为新给的实参的值
    2.可变参数
        (1)*args --tuple

            如果函数定义时，形参为可变参数（*args）
            调用的时候，实参可以给0个，1个或多个

            args类型为tuple

            如果可变参数与其他形参一块使用，可变参数要放后面.
            否则实参都会被可变参数接收，其他形参接收不到数据而报错。但其实写完可变参数，其他形参也没必要写
            def test3(a, b, *args):
                print(a, b)

        (2)**kwargs --dict
            同时使用 *args和 **kwargs时，必须 *args参数列要在 **kwargs前


            def test4(**kwargs):
                # for k, v in kwargs.items():
                #     print(k, v)
                print(kwargs)


            test4(a=2, c=4)


"""
# 结束程序，其实是把python解释器直接关闭了
# Process finished with exit code 0 表示程序正常结束
# exit()  # 不指定，默认为0,相当于  exit(code=0)
# exit(code=0)
# exit(0)

# Process finished with exit code 1  其他值表示程序非正常结束
# exit(1)
# exit(-1)


# 形参为code=1（缺省参数）,调用的时候，实参可给可不给
def test1(code=1):
    print(code)


# test1()
# test1(3)


def test2(*args):
    print(type(args))
    print(args)


test2(1)
test2()
test2(1, 2, 3, 4)
test2([7, 9])


# 求任意个整数的和
def get_sum(*args):
    result = 0
    for i in args:
        result += i
    return result


print(get_sum(1, 2, 3))


# 可变参数与其他形参一起使用
def test3(a, b, *args):
    print(a, b)


test3(1, 2)


def test4(**kwargs):
    # for k, v in kwargs.items():
    #     print(k, v)
    print(kwargs)

# TypeError: test4() takes 0 positional arguments but 2 were given
# test4(2, 4)


test4(a=2, b=4)
