import numpy as np
import os

# 创建数组：array()函数，括号内可以是列表、元组、数组、生成器等
ar = np.array([1,2,3,4,5,6,7])
# print(ar)
 # 输出数组，注意数组的格式：中括号，元素之间没有逗号（和列表区分）

# print(ar.ndim)    
 # 输出数组维度的个数（轴数），或者说“秩”，维度的数量也称rank

# print(ar.shape,ar.size,ar.dtype,ar.itemsize)
# shape (行数，列数)  size 为 n*m  dtype 为元素的数据类型 为方法不是函数

# a = np.array([1,2,3])  
 # a为一维数组
# a1 = np.array([[1,2,3]])
# a1为二维数组，1行3列
# a2 = np.array([[1],[2],[3]])
# a2为二维数组，3行1列

# print(a,a.shape)
# print(a1,a1.shape)
# print(a2,a2.shape) 

#二维数组 一维数据
# ar2 =np.array([[1,2,3],["1","b","c"]])
# print(ar2.dtype,ar2.shape)

# ar3 =np.array([[1,2,3],["1","b","c","H"]])
# print(ar3.dtype,ar3.shape)

# 创建数组：linspace():返回在间隔[开始，停止]上计算的num个均匀间隔的样本。
# ar1 = np.linspace(2.0, 3.0, num=5)
# ar2 = np.linspace(2.0, 3.0, num=5, endpoint=False)
ar3 = np.linspace(2.0, 3.0, num=5, retstep=True)
print(ar3,ar3[0].shape)
# print(ar1,type(ar1))
# print(ar2)
# print(ar3,type(ar3))

# 创建数组：arange()，类似range()，在给定间隔内返回均匀间隔的值。
# print(np.arange(10).reshape(2,5))

# 创建数组：zeros()/zeros_like()/ones()/ones_like()
# ar1 = np.zeros(5)  
# ar2 = np.zeros((2,2), dtype = np.int)
# print(ar1,ar1.dtype)
# print(ar2,ar2.dtype)
# ar3=np.arange(10).reshape(2,5)
# ar4 = np.zeros_like(ar3)
#这里ar4根据ar3的形状和dtype创建一个全0的数组
# print(ar4)

# 创建数组：eye() 单位矩阵
# print(np.eye(6))

# ___________________________________________________________________——————————————————————————————————————————

# 数组形状：.T/.reshape()/.resize()

# .T方法：转置，例如原shape为(3,4)/(2,3,4)，转置结果为(4,3)/(4,3,2) → 所以一维数组转置后结果不变
# ar3 = np.arange(10).reshape(2,5)
# ar5 = np.reshape(np.arange(10),(2,5))
# reshape 另外一种用法：参数内添加数组，目标形状
# ar4 = ar3.T
# print(ar5,ar3)

ar6 = np.resize(np.arange(5),(4,4))
# ar3 = np.arange(10).reshape(2,5)
# ar4 = ar3.resize(3,5) 不可以执行 只能将数组放在函数内的参数
# print(ar6)
#  numpy.resize(a, new_shape)：返回具有指定形状的新数组，如有必要可重复填充所需数量的元素。
# 注意了：.T/.reshape()/.resize()都是生成新的数组！！！


# 数组的复制

# ar1 = np.arange(10)
# ar2 = ar1
# print(ar2 is ar1)
# ar1[2] = 9
# print(ar1,ar2)
# 回忆python的赋值逻辑：指向内存中生成的一个值 → 这里ar1和ar2指向同一个值，所以ar1改变，ar2一起改变

# ar3 = ar1.copy()
# print(ar3 is ar1)
# ar1[0] = 9
# print(ar1,ar3)
# copy方法生成数组及其数据的完整拷贝
# 再次提醒：.T/.reshape()/.resize()都是生成新的数组！！！

# 数组类型转换：.astype()

# ar1 = np.arange(10,dtype=float)
# print(ar1,ar1.dtype)
# print('-----')
# 可以在参数位置设置数组类型

# ar2 = ar1.astype(np.int32)
# print(ar2,ar2.dtype)
# print(ar1,ar1.dtype)
# a.astype()：转换数组类型
# 注意：养成好习惯，数组类型用np.int32，而不是直接int32

# 数组堆叠
a = np.arange(5)    
# a为一维数组，5个元素
b = np.arange(5,9) 
# b为一维数组,4个元素
ar1 = np.hstack((a,b))  
# 注意:((a,b))，这里形状可以不一样

# print(a,a.shape)
# print(b,b.shape)
# print(ar1,ar1.shape)
a = np.array([[1],[2],[3]])  
 # a为二维数组，3行1列
b = np.array([['a'],['b'],['c']])  
# b为二维数组，3行1列
ar2 = np.hstack((a,b)) 
 # 注意:((a,b))，这里形状必须一样
# print(a,a.shape)
# print(b,b.shape)
# print(ar2,ar2.shape)
# print('-----')
# numpy.hstack(tup)：水平（按列顺序）堆叠数组

# a = np.arange(5)
# b = np.arange(5,10)
#a b 两个一维数组(长度均且为n)是"水平摆放"的 按垂直方向 堆叠 就是两行 n列
# ar1 = np.vstack((a,b))
# ar1是一个二维数组了
# print(a,a.shape)
# print(b,b.shape)
# print(ar1,ar1.shape)
# a = np.array([[1],[2],[3]])   
# b = np.array([['a'],['b'],['c'],['d']])   
# ar2 = np.vstack((a,b)) 
 # 这里形状可以不一样

# print(a,a.shape)
# print(b,b.shape)
# print(ar2,ar2.shape)
# numpy.vstack(tup)：垂直（按列顺序）堆叠数组

# a = np.arange(5)    
# b = np.arange(5,10)
# ar1 = np.stack((a,b))
# ar2 = np.stack((a,b),axis = 1)
# print(a,a.shape)
# print(b,b.shape)
# print(ar1,ar1.shape)
# print(ar2,ar2.shape)

# a = np.arange(8).reshape(2,4)
# b = np.arange(8).reshape(2,4)
# c = np.arange(8).reshape(2,4)
# ar1 =np.stack((a,b,c),axis=0)
# ar2 =np.stack((a,b,c),axis=1)
# ar3 =np.stack((a,b,c),axis=2)
# print(ar1.shape,ar2.shape,ar3.shape)

# numpy.stack(arrays, axis=0)：沿着新轴连接数组的序列，形状必须一样！
# 重点解释axis参数的意思，假设两个数组[1 2 3]和[4 5 6]，shape均为(3,0)

# axis=0：[[1 2 3] [4 5 6]]，shape为(2,3)
# axis=1：[[1 4] [2 5] [3 6]]，shape为(3,2)
#a b c 3个数组 新增的维度值为3 axis=0 默认放在shape的第一个参数上 （3,2,4）
# axis =1 则放在shape的第二个参数上 （2,3，4） axis=2 则为（2,4,3）

# 数组拆分 

# ar = np.arange(16).reshape(4,4)
# ar1 = np.hsplit(ar,2)
# print(ar)
# print("_____________")
# print(ar1,type(ar1))
# numpy.hsplit(ary, indices_or_sections)：将数组水平（逐列）拆分为多个子数组 (equal 相同的数组结构) → 按列拆分
# 输出结果为列表，列表中元素为数组

# ar2 = np.vsplit(ar,4)
# print(ar2,type(ar2))
# numpy.vsplit(ary, indices_or_sections)：:将数组垂直（行方向）拆分为多个子数组 → 按行拆

# 数组简单运算

ar = np.arange(6).reshape(2,3)
# print(ar + 10)   # 加法
# print(ar * 2)   # 乘法
# print(1 / (ar+1))  # 除法
# print(ar ** 2)  # 幂
# 与标量的运算

# print(ar.mean())  # 求平均值
# print(ar.max())  # 求最大值
# print(ar.min())  # 求最小值
# print(ar.std())  # 求标准差
# print(ar.var())  # 求方差

# print(ar.sum(), np.sum(ar,axis = 1)) 
# a = np.arange(8).reshape(2,4)
# b = np.arange(8,16).reshape(2,4)
# c = np.arange(16,24).reshape(2,4)
# ar1 =np.stack((a,b,c))
# print(ar1,ar1.shape)
# print(np.sum(ar1,axis=0))
# print(np.sum(ar1,axis=1))
# print(np.sum(ar1,axis=2))
 # 求和，np.sum() → axis为0，shape（2,3） 秩值为2的维度用于求和 剩下的为shape（3，）；axis为1，shape（2,3） 值为2的维度用于求和 剩下（2，）

# print(np.sort(np.array([1,4,3,2,5,6])))  # 排序



#____________________________________________________________________________
# 基本索引及切片

# ar = np.arange(20)
# print(ar)
# print(ar[4])
# print(type(ar[3:6]))
# print('-----')
# 一维数组索引及切片

ar = np.arange(16).reshape(4,4)
# print(ar, '数组轴数为%i' %ar.ndim)   # 4*4的数组
# print(ar[2],  '数组轴数为%i' %ar[2].ndim)  # 切片为下一维度的一个元素，所以是一维数组
# print(ar[2][1]) # 二次索引，得到一维数组中的一个值
# print(ar[1:3],  '数组轴数为%i' %ar[1:3].ndim)  # 切片为两个一维数组组成的二维数组
# print(ar[2,2])  # 切片数组中的第三行第三列 → 10
# print(ar[:2,1:])  # 切片数组中的1,2行、2,3,4列 → 二维数组
# print('-----')
# 二维数组索引及切片

# 布尔型索引及切片
# ar = np.arange(12).reshape(3,4)
# i = np.array([True,False,True])
# j = np.array([True,True,False,False])
# print(ar)
# print(i)
# print(j)
# print(ar[i,:])  # 在第一维度做判断，只保留True，这里第一维度就是行，ar[i,:] = ar[i]（简单书写格式）
# print(ar[:,j])  # 在第二维度做判断，这里如果ar[:,i]会有警告，因为i是3个元素，而ar在列上有4个
# # 布尔型索引：以布尔型的矩阵去做筛选

# m = ar > 5
# print(m)  # 这里m是一个判断矩阵
# print(ar[m])  # ar[m]是一个一维矩阵   用m判断矩阵去筛选ar数组中>5的元素 → 重点！后面的pandas判断方式原理就来自此处


# 数组索引及切片的值更改、复制

# ar = np.arange(10)
# print(ar)
# ar[5] = 100
# ar[7:9] = 200
# print(ar)
# lst1=[1,2,3]
# lst1[1]=32
# print(lst1)
# 一个标量赋值给一个索引/切片时，会自动改变/传播原始数组       类似列表切片赋值也会更改列表

#___________________________________________________________________________________________________
# 随机数生成

# samples = np.random.normal(size=(4,4))
# print(samples)
# 生成一个标准正太分布的4*4样本值  loc=1,scale=10 loc为期望 scale为标准值
# The location (loc) keyword  specifies the mean.
# The scale (scale) keyword specifies the standard deviation.

# numpy.random.rand(d0, d1, ..., dn)：生成一个[0,1)之间的随机浮点数或N维浮点数组 —— 均匀分布

import matplotlib.pyplot as plt  # 导入matplotlib模块，用于图表辅助分析
# % matplotlib inline 
# 魔法函数，每次运行自动生成图表
a = np.random.rand()
# print(a,type(a))  # 生成一个随机浮点数

b = np.random.rand(4)
# print(b,type(b))  # 生成形状为4的一维数组

c = np.random.rand(2,3)
# print(c,type(c))  # 生成形状为2*3的二维数组，注意这里不是((2,3))

# samples1 = np.random.rand(1000)
# samples2 = np.random.rand(1000)
# plt.scatter(samples1,samples2)
# 生成1000个均匀分布的样本值
# samples1 = np.random.rand(1000)
# samples2 = np.random.rand(1000)
# plt.scatter(samples1,samples2)
# 生成1000个均匀分布的样本值

#  numpy.random.randn(d0, d1, ..., dn)：生成一个浮点数或N维浮点数组 —— 正态分布

# samples1 = np.random.randn(1000)
# samples2 = np.random.randn(1000)
# plt.scatter(samples1,samples2)
# randn和rand的参数用法一样
# 生成1000个正太的样本值

# numpy.random.randint(low, high=None, size=None, dtype='l')：生成一个整数或N维整数数组
# 若high不为None时，取[low,high)之间随机整数，否则取值[0,low)之间随机整数，且high必须大于low 
# dtype参数：只能是int类型下的 int8 uint8 等

# print(np.random.randint(2))
# # low=2：生成1个[0,2)之间随机整数  

# print(np.random.randint(2,size=5))
# # low=2,size=5 ：生成5个[0,2)之间随机整数

# print(np.random.randint(2,6,size=5))
# # low=2,high=6,size=5：生成5个[2,6)之间随机整数  

# print(np.random.randint(2,size=(2,3)))
# # low=2,size=(2,3)：生成一个2x3整数数组,取数范围：[0,2)随机整数 

# print(np.random.randint(2,6,(2,3),dtype=np.uint8))
# low=2,high=6,size=(2,3)：生成一个2*3整数数组,取值范围：[2,6)随机整数  