from operator import itemgetter
from itertools import groupby

#你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访问。  （最好直接在创建的时候使用多值字典）
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter("date"))#使用groupby需要提前排序
# print(rows)
# for date,items in groupby(rows,key=itemgetter("date")):
#     print(date)
#     for i in items:
#         print(" ",i)

#过滤系列元素

values =[1,2,4,"d ",0,None]
def is_int(val):
    if val or val==0:
        try:
            x = int(val) 
            return True
        except ValueError :
            return False
    else:
        return False
# ivals = list(filter(is_int, values))
# print(ivals)

#过滤字典元素

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

p200 = {key:values for key,values in prices.items() if values>200}

# print(p200)

#命名元组 代替字典的方法！


from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])#命名元组
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):#字典转换为元组
    return stock_prototype._replace(**s)
# print(stock_prototype)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
# print(dict_to_stock(b))


#转换 并同时计算数据
# Determine if any .py files exist in a directory
import os
files = os.listdir()
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')
# Output a tuple as CSV
s = ('ACME', 50, 123.45)
# print(','.join(str(x) for x in s))
# Data reduction across fields of a data structure
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
# print(min_shares)

min_shares =min(portfolio,key=lambda s: s["shares"])
# print(min_shares)


#现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，
# 比如查找值或者检查某些键是否存在。

from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c =ChainMap(a,b) #以前面的为准, 不是合并 只是支持字典的操作
c["w"]=5
# del c["y"]
d =dict(a)
d.update(b)#以后面的为准 合并了字典
print(c,"*"*20,d,)




