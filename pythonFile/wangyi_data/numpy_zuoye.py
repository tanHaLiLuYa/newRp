# 	作业1：分别按照要求，生成一个一维数组、二维数组，并且查看其shape
import numpy as np
ar1 = np.array([1,2,"a","heoel",[1,2,3],{"teo":3,"rew":32}])
ar2 =np. array([[1,2,3,4,57,76],["a","b","c","d","e","ds"],[True,True,False,False,True,True]])
# print(ar2,ar2.shape)
ar2= np.arange(5,15)
# print(ar2)
ar3=np.zeros((4,3))

ar4=np.ones((2,3))

ar5=np.eye(5)
# print(ar5)

# 	作业1：创建一个20个元素的数组，分别改变成两个形状：(4,5),(5,6) （提示：超出范围用resize）
ar1 =np.arange(20).reshape(4,5)
ar2 =np.resize(ar1,(5,6))
# print(ar1,ar2)
ar1 =np.ones((4,4),dtype=np.str)
# print(ar1)
ar1 =np.arange(16).reshape(4,4)
ar2 =ar1*10+100
result_avg =np.average(ar2)
result_sum =np.sum(ar2)
# print(ar1,ar2)
# print(result_avg,result_sum)

# 	作业1：按照要求创建数组，通过索引，其ar[4]、ar[:2,3:]、ar[3][2]分别是多少
# ar=np.arange(25).reshape(5,5)
# print(ar[4],ar[:2,3:],ar[3][2])

    # ar = np.arange(10).reshape(2,5)
    # ar1 = ar[ar>5]
    # print(ar1)


# 	作业1：请按照要求创建数组ar，再将ar[:2,:2]的值改为[0,1)的随机数
# ar=np.arange(25.0).reshape(5,5)
# ar1 =np.random.rand(2,2)
# print(ar1)
# ar[:2,:2]=ar1
# print(ar)

# 	作业2： 创建2个包含10个元素的正太分布一维数组
# ar1 =np.random.randn(10).reshape(2,5)
# print(ar1)
# ar2 =np.random.randn(5).reshape(1,5)


#______________________________________________________
import os
os.chdir(r'D:\tp\网易数据分析\视频\【代码+软件+课后答案】课程资料\【非常重要】Python数据分析师微专业_课程资料\CLASSDATA_ch03重点工具掌握：数据解析核心技巧\CH01科学计算工具：Numpy')

# ar = np.random.rand(5,5)
# print(ar)
# np.save('arraydata.npy', ar)
# 也可以直接 np.save('C:/Users/Hjx/Desktop/arraydata.npy', ar)

# 读取数组数据 .npy文件

# ar_load =np.load('arraydata.npy')
# print(ar_load)

# 存储/读取文本文件

ar = np.random.randint(low=1,high=100,size=(5,5))
np.savetxt('array.txt',ar,fmt='%.1e', delimiter=',')
# np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')：存储为文本txt文件

ar_loadtxt = np.loadtxt('array.txt', delimiter=',')
print(ar_loadtxt)
# 也可以直接 np.loadtxt('C:/Users/Hjx/Desktop/array.txt')