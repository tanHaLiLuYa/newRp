import os


# path = r'D:\tp\网易数据分析\视频\【代码+软件+课后答案】课程资料\CLASSDATA_ch02基础语言入门：从零开始学习Python\jiuba.txt'  # 创建路径变量
# f = open(path,'r',encoding='utf8')  # 读取txt文件
# m = []  # 新建一个空列表，用于存储数据
# for line in f.readlines():
#     name_=line.split(':')[0]
#     other_=line.split(':')[1]
#     other_list=other_.split(',')
    
#     dic_={"name":name_,"lng":other_list[0],"lat":other_list[1],"address":other_list[2].strip()}
#     m.append(dic_)

# print(m)

# path =r'D:\tp\网易数据分析\视频\【代码+软件+课后答案】课程资料\CLASSDATA_ch02基础语言入门：从零开始学习Python\test_write - 副本.txt' 
# f = open(path, 'w', encoding = 'utf8')
# lst = ['a','b','c','d','e']
# f.writelines(lst)
# f.close()

# 小作业

# 两个列表[1~10],[a~j]，写入一个txt，变成以下格式

# 1,a

# 2,b
# lst1=[str(i) for i in range(1,11)]
# lst2 = ['a','b','c','d','e','f','g','h','i','j']
# path =r'D:\tp\网易数据分析\视频\【代码+软件+课后答案】课程资料\CLASSDATA_ch02基础语言入门：从零开始学习Python\test_write2.txt' 
# f = open(path, 'w', encoding = 'utf8')
# lst=[]
# for i in range(10):
#     lst.append(lst1[i]+','+lst2[i]+'\n')
#     # print([lst1[i],',',lst2[i]+'/n'])
# f.writelines(lst)
# f.close()

os.chdir(r"D:\tp\网易数据分析\视频\【代码+软件+课后答案】课程资料\CLASSDATA_ch02基础语言入门：从零开始学习Python")

import pickle

data = {'a':[1,2,3,4], 'b':('string','abc'), 'c':'hello'}
print(data)

pic =open("test.pkl","wb")

pickle.dump(data,pic)
pic.close()
f=open("test.pkl","rb")
st =pickle.load(f)
print(st)