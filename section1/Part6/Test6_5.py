"""
局部变量与全局变量
    全局变量：
        定义在函数外，所有函数中有效
    局部变量：
        定义在函数内，函数内部有效
        形参是局部变量，
    1.变量先定义，后使用，有上下顺序关系

    2.如果在函数中修改全局变量的值
        （1）如果全局变量是基本类型（int,float, bool），修改之前需要先使用global声明
        （2）如果全局变量是引用类型，可以直接修改，不需要声明
    3.在某一个函数中修改全局变量的值，全局变量的值会跟着改变。在后面其他函数中使用的是改变后的值
    4.函数中有和全局变量同名的局部变量时，优先使用局部变量的值（不提倡使用，尽量不要重名）

"""
c = 100
list1 = [1, 2, 3]


def test0():
    print(c)


def test1():
    # c += 100    #无法直接修改全局变量的值，报错 UnboundLocalError: local variable 'c' referenced before assignment
    # 需要先声明要修改的c就是全局变量的c
    global c
    c += 100
    print(c)


def test2():
    # 定义和全局变量名称一样的局部变量，优先使用局部变量的值
    c = 1000
    print(c)
    # 使用引用类型的全局变量，不需要声明，直接使用即可
    list1.append(4)
    print(list1)


test0()
test1()
test2()
