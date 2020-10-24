"""
循环控制
    break
        循环遇到break，循环会结束（结束当前循环，外循环它控制不了）
    continue
        循环遇到continue，会跳过一次执行（continue后面的代码都跳过），继续执行下一次
"""
# for i in range(3):
#     print("我是外循环%d" % i)
#     for j in range(10):
#         print(j)
#         if j == 5:
#             break   # 结束当前的里循环

for j in range(10):
    if j == 5:
        continue   # 跳过当次循环，continue后面的代码都被跳过
    print(j)
    for i in range(3):
        print("我是内循环%d" % i)
