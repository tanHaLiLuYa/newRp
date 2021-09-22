import numpy as np 
from matplotlib import pyplot as plt
# 创建数组
a =np.array([1,2,3,4,5])
b =np.array(range(1,6))
c =np.arange(1,6,step=2,dtype=float)
d =np.array([True,False,True])
# print(a,b,c)

#数组类名/数据类型
# print(type(a))
# print(c.dtype,d.dtype)

#指定数据类型创建  修改小数位数
aa =np.array([0,1,0,1,0,1],dtype=np.bool)
ab =aa.astype(np.float64)
ac =np.random.rand(4,3)#随机数组
ad =np.round(ac,1)
# print(ac,ad)
# print(aa,ab)

#查看、修改数组形状
# print(ad.reshape(2,6).shape,ad.shape)
# print(ad.flatten().shape,ad.reshape(1,12).shape)#左边的是一维数组，右边的是二位数组

#数组的计算!!!!!!!!!!!!!!!!
# print(ab+1,ab*2)
ba = np.arange(1,13).reshape(4,3)
# print(ba*ad,ad)
bb = np.arange(1,4)
bc = np.arange(1,5).reshape(4,1)
# print(ba,bb,bc)
# print(ba*bb,ba*bc)

#读取Comma Separated Value 逗号分隔文件
import os
os.chdir(r".\youtube_video_data")
# print("===",os.getcwd())
dataFromUs = np.loadtxt("US_video_data_numbers.csv",delimiter=",",dtype=int,encoding="utf8")
dataFromUk = np.loadtxt("GB_video_data_numbers.csv",delimiter=",",dtype=int,encoding="utf8")
# print(dataFromUk,dataFromUs)

#切片出来
# print(dataFromUs[:,0])#取行列
# print(dataFromUs[[1,2,3],:])
# print(dataFromUs)

#三元运算符 和裁剪
ca = np.arange(24).reshape(4,6)
# print(ca)
cb = np.where(ca<10,0,10)
cc = ca.clip(10,20)
# print(cb,cc)

#nan 和 inf
da = np.array([1,23,43,23,np.nan,np.nan,np.inf])
# print(np.count_nonzero(da!=da))#计算nan的个数，是利用了Nan与nan不等
# print(np.isnan(da),da[np.isnan(da)])#判断是否为nan
# print(da+1000000)

#常用统计函数
db = np.arange(24).reshape(4,6)
# print(db.sum(axis=None),db.mean())

#数组的拼接
# dd = np.arange(1,25).reshape(4,6)
# print(dd)
# print(db)
# e=np.vstack((dd,db))
# f=np.hstack((dd,db))
# print(f)

#合并英美两国数据 标记0,1
# mark_uk =np.zeros((dataFromUk.shape[0],1),dtype=int)
# mark_us =np.ones((dataFromUs.shape[0],1),dtype=int)
# marked_uk_data =np.hstack((dataFromUk,mark_uk))
# marked_us_data =np.hstack((dataFromUs,mark_us))

# combine_data =np.vstack((marked_uk_data,marked_us_data))
# print(combine_data)
# print(mark_uk.shape,dataFromUk.shape,marked_uk_data.shape)
#绘制直方图

# 取评论数据
# Us_comment_data =dataFromUs[:,-1]
# Us_comment_data =Us_comment_data[Us_comment_data<5000]

# #确定组数
# bins =int((max(Us_comment_data)-min(Us_comment_data))/50)
# # print(Us_comment_data)

# plt.hist(Us_comment_data,bins)

# plt.show()

