import heapq
from collections import OrderedDict
from collections import deque
import math

# 平均值函数


def avg(data):
    a = 0
    for i in data:
        a = a+i
    return round(a/len(data), 1)

# 去头尾 求平均值


def dropFL(data):
    _discard, *medi, _discard2 = data
    return avg(medi)


'''
data = [1,4,3,8,10,9]

data.reverse()
print(dropFL(data))

# 星号解压语法
records =[('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4)]

for arg, *args in records:
    # print(arg,"===",*arg)
    if arg == 'foo':
        print(*args)#智能用args表示多个数据，
    
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record# _表示要丢弃的变量
print(name,year)
'''


def sum(items):
    head, *tail = items
    print("head is ", head)
    return head + sum(tail) if tail else head

# items = [1, 10, 7, 4, 5, 9]
# print(sum(items))


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)
# Example use on a file
# if __name__ == '__main__':
    # with open(r'D:\github\pythonFile\每日一题\text.txt',encoding="utf-8") as f:
    #     for line, prevlines in search(f, '第三方', 5):
    #         for pline in prevlines:
    #             print(pline, end='')
    #         print(line, end='')
    #         print('-' * 20)


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# print(cheap,expensive)
a = {"a": [1, 2, 3], "b": [2]}

# 有序字典
# def ordered_dict():
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
# for key in d:
#     print(key, d[key])

# 字典排序 最大最小
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# zip() 函数创建的是一个只能访问一次的迭代器
tt = zip(prices.values(), prices.keys())
# print(min(tt),max(tt)) #会报错
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
# prices_sorted = sorted(zip(prices.values(), prices.keys()))
# print(min_price,max_price)
# print(prices_sorted)

#取最小值或最大值对应的键的信息 如果恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回
print(min(prices, key=lambda k: prices[k]) )
max(prices, key=lambda k: prices[k])