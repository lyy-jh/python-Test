"""
循环录入3个学生信息(包括name,age)
使用嵌套列表完成学生信息的存储
"""
# students = []
# for i in range(3):
#     name = input("请输入第%d个学生姓名\n" % (i+1))
#     age = input("请输入第%d个学生年龄\n" % (i+1))
#     students.append([name, age])
# print(students)

"""
存储学生信息
    students = [[姓名，年龄], [], []]
硬性要求：
    1.添加学生功能
    2.展示所有学生信息功能
    3.退出功能
页面展示
    欢迎光临学生管理系统v1.0
        1.添加学生
        2.查找学生
        3.展示所有学生信息
        4.删除学生
        5.修改学生
        6.退出系统

"""
print("欢迎光临学生管理系统v1.0")
print("1.添加学生")
print("2.查找学生")
print("3.展示所有学生信息")
print("4.删除学生")
print("5.修改学生")
print("6.退出系统")
students = []

while True:
    input_num = input("请选择你要进行的操作，输入1-6之间的数字\n")
    if input_num == '1':
        name = input("请输入要添加的学生姓名\n")
        age = input("请输入要添加的学生年龄\n")
        students.append([name, age])
    elif input_num == '2':
        name = input("请输入要查询的学生姓名\n")
        tag = False
        for student in students:
            if name == student[0]:
                tag = True
                print("学生姓名%s" % student[0])
                print("学生年龄%s" % student[1])
        if not tag:
            print("不存在该学生")
    elif input_num == '3':
        for student in students:
            print("学生的姓名:%s" % student[0], end="\t")
            print("学生的年龄:%s" % student[1])
    elif input_num == '4':
        name = input("请输入要删除的学生姓名\n")
        for student in students:
            if student[0] == name:
                students.remove(student)
    elif input_num == '5':
        name = input("请输入将要被修改的学生姓名\n")
        tag = False
        for student in students:
            if name == student[0]:   # 也可以写为 if name in student:
                tag = True
                new_name = input("请输入新的学生姓名\n")
                new_age = input("请输入新的学生年龄\n")
                student[0] = new_name
                student[1] = new_age
        if not tag:
            print("不存在该学生")
    elif input_num == '6':
        print("谢谢访问！欢迎下次访问")
        break
    else:
        print("输入有误，请重新输入")












