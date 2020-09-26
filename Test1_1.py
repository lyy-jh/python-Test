# 出现中文问题，可以加以下内容
# coding=utf-8

"""
多行注释

"""

"""
变量：用来存储数据的值

需求：
    购物小票
    2瓶可乐  2.8/瓶
    3个雪糕  2/个
    5个酸奶  5/瓶
    
    商品单价：
    商品数量：
    
    
    总价：

"""
# 可乐的数量和单价
count1 = 2
price1 = 2.8

# 雪糕的数量和单价
count2 = 3
price2 = 2

# 酸奶的数量和价格
count3 = 5
price3 = 5

money = count1 * price1 + count2 * price2 + count3 * price3
#  %g  代表小数或整数，money计算出来后就代替g的位置
print("应付款￥：%g 元" % money)
# 多个变量，用逗号隔开，用小括号括起来
print("雪糕的单价：%g元，可乐的单价：%g元，酸奶的单价：%g元" % (price1, price2, price3))

