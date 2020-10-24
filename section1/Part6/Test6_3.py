"""
函数参数的使用
    def 函数名（参数...）:
        代码
    参数：
        形参：函数的定义中使用
        实参：函数调用的时候使用
    调用的时候实际参数的值赋值给形式参数
注意：
    1.如果定义的两个函数名称相同，以后面定义的函数为准
"""


# 参数的使用
# def print99(line):
#     for i in range(1, line):
#         for j in range(1, i + 1):
#             print("%d x %d = %d" % (j, i, i * j), end="\t")
#         print()
#
#
# # 打印5行
# print99(6)

"""
学生管理系统
使用函数封装
"""


# 定义添加学生
def add_student():
    name = input("请输入要添加的学生姓名\n")
    age = input("请输入要添加的学生年龄\n")
    students[name] = {'name': name, 'age': age}


# 查询某个学生信息
def search_student():
    name = input("请输入要查询的学生姓名\n")
    tag = False
    for key in students.keys():
        if name == key:
            tag = True
            print("学生姓名%s" % students[key]['name'])
            print("学生年龄%s" % students[key]['age'])
    if not tag:
        print("不存在该学生")


# 查询所有学生信息
def select_all():
    for key in students.keys():
        print("学生的姓名:%s" % students[key]['name'], end="\t")
        print("学生的年龄:%s" % students[key]['age'])


# 删除学生信息
def delete_student():
    name = input("请输入要删除的学生姓名\n")
    tag = False
    for key in students.keys():
        if key == name:
            tag = True
            break
            # 使用该方法报错：RuntimeError: dictionary changed size during iteration
            # students.pop(key)
    if tag:
        del students[name]
    else:
        print("你要删除的学生不存在")


# 修改学生姓名
def update_student():
    name = input("请输入将要被修改的学生姓名\n")
    tag = False
    print("修改前为:", students)
    for key in students.keys():
        if name == key:  # 也可以写为 if name in student:
            tag = True
            new_name = input("请输入新的学生姓名\n")
            new_age = input("请输入新的学生年龄\n")
            students[key] = {'name': new_name, 'age': new_age}
    print("修改后为:", students)
    if not tag:
        print("不存在该学生")


# 定义退出系统
def exit_sys():
    print("谢谢访问！欢迎下次访问")
    # break
    # exit()系统函数，退出系统，将运行的程序结束
    # exit(0) 正常退出
    exit(0)


# 定义菜单
def show_menu():
    print("欢迎光临学生管理系统v1.1")
    print("1.添加学生")
    print("2.查找学生")
    print("3.展示所有学生信息")
    print("4.删除学生")
    print("5.修改学生")
    print("6.退出系统")


students = {}
show_menu()
while True:
    input_num = input("请选择你要进行的操作，输入1-6之间的数字\n")
    if input_num == '1':
        add_student()
    elif input_num == '2':
        search_student()
    elif input_num == '3':
        select_all()
    elif input_num == '4':
        delete_student()
    elif input_num == '5':
        update_student()
    elif input_num == '6':
        # print("谢谢访问！欢迎下次访问")
        # break
        exit_sys()
    else:
        print("输入有误，请重新输入")
