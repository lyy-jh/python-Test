"""
list的基本使用
    概念：
        存储多个数据（多个数据可以是任意类型）
    定义：
        scores = [89, 56, 38.5, 90, 95]   # 可以存储int和float
        names = ['lyy', 'jh', 'ljj']
    查询：
        使用索引值
        score = scores[0]
        索引值范围[0,len(scores)-1]
    遍历列表
         while循环
         for i in range
         for I in 列表变量

"""
scores = [89, 56, 38.5, 90, 95]
# 第一个分数
print(scores[0])
# 最后一个分数
print(scores[-1])
print(scores[len(scores)-1])

# list的长度
scores_len = len(scores)
print(scores_len)
# list越界：IndexError: list index out of range
# print(scores[len(scores)])

# 遍历列表
# while循环
i = 0
while i < scores_len:
    print(scores[i], end="\t")
    i += 1

print()
# for i in range
for i in range(scores_len):
    print(scores[i], end="\t")

print()
# for name in 列表变量
# name为临时变量，里面的值为列表中的数据
for name in scores:
    print(name, end="\t")
