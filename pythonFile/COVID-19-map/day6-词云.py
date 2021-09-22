from jieba.analyse import *
from pyecharts.charts import WordCloud
import os 

os.chdir(r"E:\work\tpp\samsung\2021年\07月\W27")

with open('新建文本文档.txt',encoding="utf-8") as f:
    data = f.read()


dataAnlysed=[]
for keyword, weight in textrank(data, withWeight=True,topK=11):
    if keyword =="程序":
        keyword="小程序"
    dataAnlysed.append((keyword,weight))

dataAnlysed1 = [x for x in dataAnlysed if not (x[0] in ["督导"])]
# dataAnlysed1 = [x for x in dataAnlysed if not (x[0] in ["对比","方面","苹果","用户","手机","介绍","支持","没有","效果","优势"] )]
# # print(dataAnlysed)
print(dataAnlysed1)


wordcloud = WordCloud ()

wordcloud.add( "", dataAnlysed1,shape="cardioid" ,word_size_range=[20,100],rotate_step=180)

wordcloud.render( 'q1.html')