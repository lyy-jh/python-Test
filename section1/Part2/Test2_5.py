"""
需求：求1-100中所有偶数的和

嵌套层次不超过3层

"""
import random
# i = 1
# num_sum = 0

# i = i + 1
# while i <= 100:
#     num_sum = num_sum+i
#     i = i+2
# print(num_sum)

# while i <= 100:
#     if i % 2 == 0:
#         num_sum += i
#     i += 1
# print(num_sum)

"""
猜数字游戏：
随机给出一个数字(1,100)
输出结果：
    猜大了
    猜小了
    猜对了
统计猜测的次数
"""

# rand_num = random.randint(1, 100)
# input_num = int(input("请输入1-100之间的数字：\n"))
# count = 1

# while rand_num != input_num:
#     if input_num < rand_num:
#         input_num = int(input("猜小了，请重新输入1-100之间的数字：\n"))
#         count += 1
#     else:
#         input_num = int(input("猜大了，请重新输入1-100之间的数字：\n"))
#         count += 1
# if 1 <= count <= 3:
#     print("超神")
# elif 4 <= count <= 6:
#     print("菜鸟")
# else:
#     print("脑子是个好东西，可惜你没有")
rand_num = random.randint(1, 100)
count = 0
End = True  # 设置一个状态值,用来控制循环是否结束

while End:
    input_num = int(input("请输入1-100之间的数字：\n"))
    count += 1
    if input_num < rand_num:
        print("猜小了")
    elif input_num > rand_num:
        print("猜大了")
    else:
        print("猜中了")
        # 根据猜测次数进行评级
        if 1 <= count <= 3:
            print("超神")
        elif 4 <= count <= 6:
            print("菜鸟")
        else:
            print("脑子是个好东西，可惜你没有")
        # 结束循环
        End = False

