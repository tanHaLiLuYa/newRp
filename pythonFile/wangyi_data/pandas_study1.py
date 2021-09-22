import pandas as pd
import numpy as np
s = pd.Series(np.random.rand(5))

# print(s.index,type(s.index))
# print(s.values,type(s.values))
# .index查看series索引，类型为rangeindex
# .values查看series值，类型是ndarray

# 核心：series相比于ndarray，是一个自带索引index的数组 → 一维数组 + 对应索引
# 所以当只看series的值的时候，就是一个ndarray
# series和ndarray较相似，索引切片功能差别不大
# series和dict相比，series更像一个有顺序的字典（dict本身不存在顺序），其索引原理与字典相似（一个用key，一个用index）


# Series 创建方法一：由字典创建，字典的key就是index，values就是values
dic = {'a':1 ,'b':2 , 'c':3, '4':4, '5':'5'}
s = pd.Series(dic)
# print(s)
# key肯定是字符串，假如values类型不止一个会怎么样？  dtype 则为object

# Series 创建方法二：由数组创建(一维数组)
arr = np.arange(4)
s = pd.Series(arr)
s1 =pd.Series(arr,index=["a","b","c","d"],dtype=np.object)
# print(s,s1)
# 默认index是从0开始，步长为1的数字
# index参数：设置index，长度保持一致 为列表
# dtype参数：设置数值类型

# Series 创建方法三：由标量创建
s = pd.Series(10, index = range(4))
# print(s)
# 如果data是标量值，则必须提供索引。标量值会重复，来匹配索引的长度

# Series 名称属性：name
s2 = pd.Series(np.random.randn(5),name = 'test')
# print(s2)
# name为Series的一个参数，创建一个数组的 名称
# .name方法：输出数组的名称，输出格式为str，如果没用定义输出名称，输出为None

# ——————————————————————————++++++++++++++++++++++++++++++++++++++++

# Pandas数据结构Series：索引

# 位置下标，类似序列
s =pd.Series(np.random.rand(5))
# print(s[0],type(s[0]),s[0].dtype)
# print(float(s[0]),type(float(s[0])))
# print(s[-1])
# 位置下标从0开始
# 输出结果为numpy.float格式 对应的值，
# 可以通过float()函数转换为python float格式
# numpy.float与float占用字节不同
# s[-1]结果如何？ 报错

# 标签索引
s = pd.Series(np.random.rand(5), index = ['a','b','c','d','e'])
# print(s)
# print(s['a'],type(s['a']),s['a'].dtype)
# 方法类似下标索引，用[]表示，内写上index，注意index是字符串 类似字典key
sci = s[['a','b','e']]
# print(sci,type(sci))
# 如果需要选择多个标签的值，用[[]]来表示（相当于[]中包含一个列表）
# 多标签索引结果是新的series

# 切片索引

s1 = pd.Series(np.random.rand(5))
s2 = pd.Series(np.random.rand(5), index = ['a','b','c','d','e'])
# print(s1,"___________",s1[1:4],s1[4])
# print(s2,"___________",s2['a':'c'],s2['c'])
# print(s2[0:3],s2[3])
# print('-----')
# 注意：用index做切片是末端包含

# print(s2[:-1])
# print(s2[::2])
# [::2] 2 是step
# 下标索引做切片，和list写法一样

# 布尔型索引

s = pd.Series(np.random.rand(3)*100)
s[4] = None  # 添加一个空值
# print(s)
# bs1 = s > 50
# bs2 = s.isnull()
# bs3 = s.notnull()
# print(bs1, type(bs1), bs1.dtype)
# print(bs2, type(bs2), bs2.dtype)
# print(bs3, type(bs3), bs3.dtype)
# print('-----')
# 数组做判断之后，返回的是一个由布尔值组成的新的数组
# .isnull() / .notnull() 判断是否为空值 (None代表空值，NaN代表有问题的数值，两个都会识别为空值)

# print(s[s > 50])
# print(s[bs3])
# 布尔型索引方法：用[判断条件]表示，其中判断条件可以是 一个语句，或者是 一个布尔型数组！

# ——————————————————————————++++++++++++++++++++++++++++++++++++++++
# 数据查看 / 重新索引 / 对齐 / 添加、修改、删除值


# 数据查看
s = pd.Series(np.random.rand(50))
# print(s.head(10))
# print(s.tail())
# .head()查看头部数据
# .tail()查看尾部数据
# 默认查看5条

# 重新索引reindex
# .reindex将会根据索引重新排序，如果当前索引不存在，则引入缺失值

s = pd.Series(np.random.rand(3), index = ['a','b','c'])
# print(s)
s1 = s.reindex(['b','a','d'])
# print(s1)
# .reindex()中也是写列表
# 这里'd'索引不存在，所以值为NaN

s2 = s.reindex(['c','b','a','d'], fill_value =s.mean())
# print(s2)
# fill_value参数：填充缺失值的值

# Series对齐
s1 = pd.Series(np.random.rand(3), index = ['Jack','Marry','Tom'])
s2 = pd.Series(np.random.rand(3), index = ['Wang','Jack','Marry'])
# print(s1)
# print(s2)
# print(s1+s2)
# Series 和 ndarray 之间的主要区别是，Series 上的操作会根据标签自动对齐
# index顺序不会影响数值计算，以标签来计算
# 空值和任何值计算结果扔为空值

# 删除：.drop

s = pd.Series(np.random.rand(5), index = list('ngjur'))
# print(s)
s1 = s.drop('n')
# print(s)
s.drop('n',inplace=True)
s2 = s.drop(['g','j'])

# print(s1)
# print(s2)
# print(s)
# drop 删除元素之后返回副本(inplace=False)

# 添加

s1 = pd.Series(np.random.rand(5))
s2 = pd.Series(np.random.rand(5), index = list('ngjur'))
# print(s1)
# print(s2)
# s1[5] = 100
# s2['a'] = 100
# print(s1)
# print(s2)
# print('-----')
# 直接通过下标索引/标签index添加值

s3 = s1.append(s2)
# print(s3)
# print(s1)
# 通过.append方法，直接添加一个数组
# .append方法生成一个新的数组，不改变之前的数组

# 修改
# s = pd.Series(np.random.rand(3), index = ['a','b','c'])
# print(s)
# s['a'] = 100
# s[['b','c']] = 200
# print(s)
# 通过索引直接修改，类似序列


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Dataframe 数据结构
# Dataframe是一个表格型的数据结构，“带有标签的二维数组”。
# Dataframe带有index（行标签）和columns（列标签）

data = {'name':['Jack','Tom','Mary'],
        'age':[18,19,20],
       'gender':['m','m','w']}
frame = pd.DataFrame(data)
# print(frame)  
# print(type(frame))
# print(frame.index,'\n该数据类型为：',type(frame.index))
# print(frame.columns,'\n该数据类型为：',type(frame.columns))
# print(frame.values,'\n该数据类型为：',type(frame.values))
# # 查看数据，数据类型为dataframe
# .index查看行标签
# .columns查看列标签
# .values查看值，数据类型为ndarray


# Dataframe 创建方法一：由数组/list组成的字典
# 创建方法:pandas.Dataframe()

data1 = {'a':[1,2,3],
        'b':[3,4,5],
        'c':[5,6,7]}
data2 = {'one':np.random.rand(3),
        'two':np.random.rand(3)}   # 这里如果尝试  'two':np.random.rand(4) 会怎么样？ 报错
# print(data1)
# print(data2)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# print(df2.shape)
# print(df1)
# print(df2)
# 由数组/list组成的字典 创建Dataframe，columns为字典key，index为默认数字标签
# 字典的值的长度必须保持一致！

# df1 = pd.DataFrame(data1, columns = ['b','c','a','d'])
# print(df1)
# df1 = pd.DataFrame(data1, columns = ['b','c'])
# print(df1)
# columns参数：可以重新指定列的顺序，格式为list，如果现有数据中没有该列（比如'd'），则产生NaN值
# 如果columns重新指定时候，列的数量可以少于原数据

# df2 = pd.DataFrame(data2, index = ['f1','f2','f3'])  # 这里如果尝试  index = ['f1','f2','f3','f4'] 会怎么样？ 报错
# print(df2)
# index参数：重新定义index，格式为list，长度必须保持一致

# Dataframe 创建方法二：由Series组成的字典

data1 = {'one':pd.Series(np.random.rand(2)),
        'two':pd.Series(np.random.rand(3))}  # 没有设置index的Series
data2 = {'one':pd.Series(np.random.rand(2), index = ['a','b']),
        'two':pd.Series(np.random.rand(3),index = ['a','b','c'])}  # 设置了index的Series
# print(data1)
# print(data2)
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# print(df1)
# print(df2)
# 由Seris组成的字典 创建Dataframe，columns为字典key，index为Series的标签（如果Series没有指定标签，则是默认数字标签）
# Series可以长度不一样，生成的Dataframe会出现NaN值

# Dataframe 创建方法三：通过二维数组直接创建

# ar = np.random.rand(9).reshape(3,3)
# print(ar)
# df1 = pd.DataFrame(ar)
# df2 = pd.DataFrame(ar, index = ['a', 'b', 'c'], columns = ['one','two','three'])  # 可以尝试一下index或columns长度不等于已有数组的情况
# print(df1)
# print(df2)
# 通过二维数组直接创建Dataframe，得到一样形状的结果数据，如果不指定index和columns，两者均返回默认数字格式
# index和colunms指定长度与原数组保持一致

# Dataframe 创建方法四：由字典组成的列表

# data = [{'one': 1, 'two': 2}, {'one': 5, 'two': 10, 'three': 20}]
# print(data)
# df1 = pd.DataFrame(data)
# df2 = pd.DataFrame(data, index = ['a','b'])
# df3 = pd.DataFrame(data, columns = ['one','two'])
# print(df1)
# print(df2)
# print(df3)
# 由字典组成的列表创建Dataframe，columns为字典的key，index不做指定则为默认数组标签
# colunms和index参数分别重新指定相应列及行标签

# Dataframe 创建方法五：由字典组成的字典

# data = {'Jack':{'math':90,'english':89,'art':78},
#        'Marry':{'math':82,'english':95,'art':92},
#        'Tom':{'math':78,'english':67}}
# df1 = pd.DataFrame(data)
# print(df1)
# 由字典组成的字典创建Dataframe，columns为字典的key，index为子字典的key

# df2 = pd.DataFrame(data, columns = ['Jack','Tom','Bob'])
# df3 = pd.DataFrame(data, index = ['a','b','c'])
# print(df2)
# print(df3)
# columns参数可以增加和减少现有列，如出现新的列，值为NaN
# index在这里和之前不同，并不能改变原有index，如果指向新的标签，值为NaN （非常重要！）


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Dataframe既有行索引也有列索引，可以被看做由Series组成的字典（共用一个索引）

# 选择列 / 选择行 / 切片 / 布尔判断
# 选择行与列

df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                   index = ['one','two','three'],
                   columns = ['a','b','c','d'])
# print(df.shape)

data1 = df['a']
data2 = df[['a','c']]
# print(data1,type(data1))
# print(data2,type(data2),data2.shape)
# print('-----')
# 按照列名选择列，只选择一列输出Series，选择多列输出Dataframe

data3 = df.loc['one']
data4 = df.loc[['one','two']]
# print(data3,type(data3),data3.shape)
# print(data4,type(data4),data4.shape)

# 按照index选择行，只选择一行输出Series，选择多行输出Dataframe

# df[] - 选择列
# 一般用于选择列，也可以选择行

df = pd.DataFrame(np.random.rand(12).reshape(3,4)*100,
                   index = ['one','two','three'],
                   columns = ['a','b','c','d'])
print(df)
print('-----')

data1 = df['a']
data2 = df[['b','c']]  # 尝试输入 data2 = df[['b','c','e']]
# print(data1)
# print(data2)
# df[]默认选择列，[]中写列名（所以一般数据colunms都会单独制定，不会用默认数字列名，以免和index冲突）
# 单选列为Series，print结果为Series格式
# 多选列为Dataframe，print结果为Dataframe格式

data3 = df[:1]
#data3 = df[0]
# data3 = df['one']
print(data3,type(data3))
# df[]中为数字时，默认选择行，且只能进行切片的选择，不能单独选择（df[0]）
# 输出结果为Dataframe，即便只选择一行
# df[]不能通过索引标签名来选择行(df['one'])

# 核心笔记：df[col]一般用于选择列，[]中写列名


# df.loc[] - 按index选择行

df1 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   index = ['one','two','three','four'],
                   columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.random.rand(16).reshape(4,4)*100,
                   columns = ['a','b','c','d'])
# print(df1)
# print(df2)
# print('-----')

data1 = df1.loc['one']
data2 = df2.loc[1]
# print(data1)
# print(data2)
# print('单标签索引\n-----')
# 单个标签索引，返回Series

data3 = df1.loc[['two','three','five']]
data4 = df2.loc[[3,2,1]]
# print(data3)
# print(data4)
# print('多标签索引\n-----')
# 多个标签索引，如果标签不存在，则返回NaN
# 顺序可变

data5 = df1.loc['one':'three']
data6 = df2.loc[1:3]
# print(data5)
# print(data6)
# print('切片索引')
# 可以做切片对象
# 末端包含

# 核心笔记：df.loc[label]主要针对index选择行，同时支持指定index，及默认数字index

####切换到jpynb 