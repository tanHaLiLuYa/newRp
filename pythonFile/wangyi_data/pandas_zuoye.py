import numpy as np
import pandas as pd
from pandas.core.indexes import period

#字典
dic_ = {"Jack": 90.0, "Marry": 92.0, "Tom": 89.0}
s = pd.Series(dic_, name="作业")
#列表
lst1 = ["Jack", "Marry", "TOm"]
lst2 = [90.0, 92.0, 89.0]
s2 = pd.Series(data=lst2, index=lst1, name="作业")

# print(s,s2)

# 	作业1：创建一个Series，包含10个元素，且每个值为0-100的均匀分布随机值，index为a-j，请分别筛选出：
# ① 标签为b，c的值为多少
# ② Series中第4到6个值是哪些？
# ③ Series中大于50的值有哪些？
s = pd.Series(np.random.rand(10) * 100,
              index=["a", "b", "c", "d", "e", "f", "j", "k", "l", "m"])
# print(s)
# print("b c的值：",s["b":"c"])
# print("4-6的值：",s[3:6])
# print(">50的值:",s[s>50])

# 如图创建Series，并按照要求修改得到结果
s = pd.Series(np.arange(10), index=list("abcdefghij"))
# print(s,"++++++++++++++++++")
s['a'] = 100
s['e':'f'] = 100
# print(s)

# 已有s1，s2（值为0-10的随机数），请求出s1+s2的值
s1 = pd.Series(np.random.rand(5) * 10, index=["a", "b", "c", "d", "e"])
s2 = pd.Series(np.random.rand(5) * 10, index=["c", "d", "e", "f", "g"])
# print(s1,s2)
# print(s1+s2)

# 用四种不同的方法，创建以下Dataframe（保证columns和index一致，值不做要求）
#由数组/list组成的字典
data1 = {
    'four': np.random.randint(1, 10, size=5),
    'one': np.random.randint(1, 10, size=5),
    'three': np.random.randint(1, 10, size=5),
    'two': np.random.randint(1, 10, size=5)
}
# print(np.random.randint(1,10,size=5))
s = pd.DataFrame(data1, index=["a", "b", "c", "d", "e"])
# print(s)

#series 组成的字典
data1 = {
    'four':
    pd.Series(np.random.randint(1, 10, size=5),
              index=["a", "b", "c", "d", "e"]),
    'one':
    pd.Series(np.random.randint(1, 10, size=5),
              index=["a", "b", "c", "d", "e"]),
    'three':
    pd.Series(np.random.randint(1, 10, size=5),
              index=["a", "b", "c", "d", "e"]),
    'two':
    pd.Series(np.random.randint(1, 10, size=5),
              index=["a", "b", "c", "d", "e"])
}
# print(data1)
s = pd.DataFrame(data1)
# print(s)

#二维数组直接创建
arr = np.random.randint(1, 10, size=(5, 4))

df = pd.DataFrame(arr,
                  index=["a", "b", "c", "d", "e"],
                  columns=['four', 'one', 'three', 'two'])
# print(df)

#由字典组成的列表
data1 = [{
    'four': 1,
    'one': 2,
    'three': 5,
    'two': 7
}, {
    'four': 5,
    'one': 2,
    'three': 5,
    'two': 7
}, {
    'four': 1,
    'one': 2,
    'three': 9,
    'two': 7
}, {
    'four': 1,
    'one': 9,
    'three': 5,
    'two': 7
}, {
    'four': 1,
    'one': 3,
    'three': 5,
    'two': 7
}]
df = pd.DataFrame(data1, index=["a", "b", "c", "d", "e"])
# print(df)

#由字典组成的字典

data1 = {
    'four': {
        'a': 9,
        'b': 8,
        'c': 7,
        'd': 5,
        'e': 0
    },
    'one': {
        'a': 0,
        'b': 89,
        'c': 78,
        'd': 54,
        'e': 90
    },
    'three': {
        'a': 5,
        'b': 89,
        'c': 78,
        'd': 54,
        'e': 90
    },
    'two': {
        'a': 8,
        'b': 89,
        'c': 78,
        'd': 54,
        'e': 90
    }
}
df = pd.DataFrame(data1)
# print(df)

# 	作业1：如图创建Dataframe(4*4，值为0-100的随机数)，通过索引得到以下值
# ① 索引得到b，c列的所有值
# ② 索引得到第三第四行的数据
# ③ 按顺序索引得到two，one行的值
# ④ 索引得到大于50的值

df = pd.DataFrame((np.random.rand(16) * 100).reshape(4, 4),
                  columns=["a", "b", "c", "d"],
                  index=["one", "two", "three", "four"])
# print(df)
# df1 =df[["b","c"]]
# print(df1)

# df2 =df.loc["three":"four"]
# print(df2)
# df3 =df.iloc[[2,3]]
# print(df3)
# df4=df.iloc[[1,0]]
# print(df4)
# df5 =df[df>50]
# print(df5)

# 	作业1：创建一个3*3，
# 值在0-100区间随机值的Dataframe（如图）
# ，分别按照index和第二列值大小，降序排序
df = pd.DataFrame((np.random.rand(9) * 100).reshape(3, 3),
                  columns=["V1", "V2", "V3"],
                  index=["A", "B", "C"])
# print(df)
# print(df.sort_index(ascending=False))
# print(df.sort_values(["V2"],ascending=False))

df = pd.DataFrame((np.random.rand(10) * 100).reshape(5, 2),
                  columns=["V1", "V2"],
                  index=["A", "B", "C", "D", "E"])
df2 = df.T
del df2['E']
# print(df2)

# 	作业1：请调用datetime模块，输出以下时间信息

import datetime
# now_datetime =  datetime.datetime.now()
# print(now_datetime)
# t1 = datetime.datetime(2021,5,1,12,30,0)
# print(t1)
# t2 =datetime.datetime(2012,12,9)
# print(t2)

# # 	作业2：请创建时间变量‘2000年5月1日’，求出1000天之后是哪年哪月哪日？
# t3 =datetime.date(1992,12,8)
# print(t3+datetime.timedelta(10000))

t0 = datetime.date(2021, 5, 1)
date_list = []
for i in range(31):
    # t = str(t0)
    date_list.append(t0)
    t0 = t0 + datetime.timedelta(days=1)
# print(date_list)
time_stamp1 = pd.to_datetime(date_list)
# print(time_stamp1)
# print(time_stamp1[15])

# 	作业2：请如图创建一个包含时间日期的txt文件，通过open语句读取后转化成DatetimeIndex
import os

os.chdir(
    r"D:\tp\网易数据分析\视频\【代码+软件+课后答案】课程资料\CLASSDATA_ch03重点工具掌握：数据解析核心技巧\CH02数据分析工具：Pandas"
)

file_open = open("data1.txt", "r")
txt_str = file_open.read()
# print(txt_str)

date_list = txt_str.split(',')
# print(date_list)
time_stamp1 = pd.to_datetime(date_list)
# print(time_stamp1)

ts1 = pd.Series(np.random.rand(5), index=pd.date_range('20170101', '20170105'))

# print(ts1)
# ts2 = pd.Series(np.random.rand(4),
#               index = pd.date_range('20170101','20171204',freq="3M"))

# print(ts2)

# ts3 = pd.DataFrame(np.random.rand(16).reshape(4,4),
#               index = pd.date_range(start='20170101 00:00:00',periods=4,freq="10MIN"),
#               columns=["v1","v2","v3","v4"])

# print(ts3)
# # 	作业2：按要求创建时间序列ts1，并转换成ts2
# ts3 = pd.Series(np.random.rand(5),
#               index = pd.date_range(start='20170501 12:00:00',periods=5,freq="10MIN"))
# print(ts3)
# ts4 = ts3.asfreq('5MIN',method='ffill')
# print(ts4)

prng = pd.Series(np.random.rand(5),
                 index=pd.period_range('201701','201705', freq='M'))
# print(prng)
prng = pd.Series(np.random.rand(5),
                 index=pd.period_range('20170101','20170102', freq='2H')[:5])
# print(prng)
from datetime import datetime

# df = pd.DataFrame(np.random.rand(30).reshape(10,3)*100,
#     index=pd.date_range('20171201',periods=10,freq='12H'))
# print(df)
# # print(df['20171201':'20171202'])
# # print(df[:4])
# dt =datetime(year=2017,month =12,day =4,hour =12,minute =0)
# # print(df['20171204'].iloc[1])

# print(df['20171204':'20171205'])

# 	作业1：按要求创建时间序列ts1，通过降采样和升采样，转换成ts2，ts3

df = pd.Series(np.random.rand(10),
    index=pd.date_range('20170101',periods=10,freq='D'))
print(df)
df2 =df.resample('3D').mean()
print(df2)
df3 =df.resample('12H').ffill()
print(df3)