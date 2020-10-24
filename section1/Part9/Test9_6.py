"""
对象初始化 __init__（）的使用
    1.创建对象，拥有默认的属性
    2. __init__()方法
        （1）对象创建的时候被调用
        （2）可以给对象加默认属性，创建对象的时候，该对象已经拥有默认属性
    3.self
        可以理解为自己，类似与Java、C++中的this指针，表示对象自身
        哪个对象调用该方法，self表示的是谁

"""


# 创建类
# 如果类没有继承关系，后面的括号可以省去
class Driver:
    # __init__()方法
    def __init__(self, _id, name):
        # print("我是init方法")
        # 给self加默认属性
        self.id = _id
        self.name = name
        self.profession = "driver"

    # self,谁（哪个对象）调用该方法，self即表示谁
    def drive(self):
        print("工号%d %s为您服务" % (self.id, self.name))
        print("1.踩离合")
        print("2.打火")
        print("3.挂挡")
        print("4.松离合/加油门")
        print("嘀嘀嘀，一起去嗨皮")


# 创建对象
# 创建一个对象，并把对象存储到driver1中
driver1 = Driver(1002, '李师傅')

# 手动添加属性
# driver1.id = 1001
# 第二次再写相当于修改属性值
# driver1.id = 1002


# 调用对象的方法
driver1.drive()
