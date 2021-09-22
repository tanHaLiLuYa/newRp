import string
import pandas as pd 
import numpy as np

t= pd.Series(np.arange(15),index=list(\
    string.ascii_uppercase[:15]))
# print(t)

a ={string.ascii_letters[i]:i for i in range(11)}
s =pd.Series(a)
#
#  print(a,s)
#
#切片操作
# print(s[1:10:3])
# print(s[[2,4,5]])
# print(s.values,s.index)

df =pd.DataFrame (np.arange(12).reshape(3,4),index=list(string.\
    ascii_uppercase[:3]),columns=list(string.ascii_uppercase[-4:]))
# print(df.shape,df.ndim,df.values)
# print(df)  #index 代表行 横向索引  ；columns 代表列 纵向索引 

d1 ={"name":["xiaopeng","xiaoge"],"age":[20,32],"telphone":[10089,10001]}

# print(pd.DataFrame(d1))#每一行代表一个数据 所以 列索引是name age之类

d2 =[{"name":"xiaopeng","age":12,"tel":100098},{"name":"xioaxi","tel":12493},{"name":"tpp","te::":1000}]
# print(pd.DataFrame(d2))#会自动补上NaN