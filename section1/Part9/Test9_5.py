"""
类的封装
    1.创建类的语法：
        class 类名（）：
            # 属性

            #方法、行为、动态特征、能力
            def 方法名（self, 其他参数...）： # self表示当前类的一个对象，有self是方法，没有self是函数
                pass

    2.创建对象的语法
        变量名 = 类名（）
    3.调用对象方法的语法
        变量名.方法名（）

"""


# 创建类
# 如果类没有继承关系，后面的括号可以省去
class Driver:
    def drive(self):
        print("1.踩离合")
        print("2.打火")
        print("3.挂挡")
        print("4.松离合/加油门")
        print("嘀嘀嘀，一起去嗨皮")


# 创建对象
# 创建一个对象，并把对象存储到driver1中
driver1 = Driver()
# 调用对象的方法
driver1.drive()
