import pandas as pd 

import numpy as np 

import matplotlib.pyplot as plt

import os 

# pathDir = r"C:\Users\16930\Desktop\python\21 python-数据分析\12-人工智能阶段-数据分析\数据分析资料\TEST"
# os.chdir(pathDir)
# # print(os.getcwd())
# fileName = "2018W46-2020W03门店得分数据库20200420_1030.xlsx"

# fileDir = os.path.join(pathDir,fileName)
# pdWorkbook = pd.read_excel(fileDir,index_col=[2,4,12,165])

# print(pdWorkbook.head(2))

# array1 = np.array([-3.2623, -6.0915, -6.663 ,  5.3731,  3.6182,  3.45  ,  5.0077])

# np.sqrt(array1,)

# print(array1)

points = np.arange(-5, 5, 0.01)
# print(points)

xs, ys = np.meshgrid(points, points)
# print(xs)

z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z, cmap=plt.cm.gray)

plt.colorbar()

plt.show()