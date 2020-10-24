"""
可变参数的补充
    **kwargs --dict
    调用时可以写0个、1个或多个键值对,例如 test1(a=1, b=2, c=3)
    键值对的key必须为变量，默认当作字符串处理

"""


def test1(**kwargs):
    print(type(kwargs))
    print(kwargs)


test1()
# {'a': 1, 'b': 2, 'c': 3}
test1(a=1, b=2, c=3)
# {'a': 1, 'b': [1, 2, 3, 4], 'c': {'id': 1002, 'age': 18}}
test1(a=1, b=[1, 2, 3, 4], c={'id': 1002, 'age': 18})


# *args, **kwargs可以分清楚传入的参数是谁的，因为*args要求传入值，**kwargs要求传入键值对
def test3(*args, **kwargs):
    print(args)
    print(kwargs)


test3(1, [2, 3, 4], a=5, b=[6, 7, 8])


# *args写在**kwargs之后直接报错
# def test4(**kwargs, *args):
#     print(args)
#     print(kwargs)
