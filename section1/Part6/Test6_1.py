# -*- encoding=utf8 -*-
"""
存储学生信息
    students = {name:{‘name’：name, 'age': age},{}}
硬性要求：
    1.添加学生功能
    2.展示所有学生信息功能
    3.退出功能
页面展示
    欢迎光临学生管理系统v1.1
        1.添加学生
        2.查找学生
        3.展示所有学生信息
        4.删除学生
        5.修改学生
        6.退出系统
"""
print("欢迎光临学生管理系统v1.1")
print("1.添加学生")
print("2.查找学生")
print("3.展示所有学生信息")
print("4.删除学生")
print("5.修改学生")
print("6.退出系统")
students = {}

while True:
    input_num = input("请选择你要进行的操作，输入1-6之间的数字\n")
    if input_num == '1':
        name = input("请输入要添加的学生姓名\n")
        age = input("请输入要添加的学生年龄\n")
        students[name] = {'name': name, 'age': age}
    elif input_num == '2':
        name = input("请输入要查询的学生姓名\n")
        tag = False
        for key in students.keys():
            if name == key:
                tag = True
                print("学生姓名%s" % students[key]['name'])
                print("学生年龄%s" % students[key]['age'])
        if not tag:
            print("不存在该学生")
    elif input_num == '3':
        for key in students.keys():
            print("学生的姓名:%s" % students[key]['name'], end="\t")
            print("学生的年龄:%s" % students[key]['age'])
    elif input_num == '4':
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
    elif input_num == '5':
        name = input("请输入将要被修改的学生姓名\n")
        tag = False
        print("修改前为:", students)
        for key in students.keys():
            if name == key:   # 也可以写为 if name in student:
                tag = True
                new_name = input("请输入新的学生姓名\n")
                new_age = input("请输入新的学生年龄\n")
                students[key] = {'name': new_name, 'age': new_age}
        print("修改后为:", students)
        if not tag:
            print("不存在该学生")
    elif input_num == '6':
        print("谢谢访问！欢迎下次访问")
        break
    else:
        print("输入有误，请重新输入")