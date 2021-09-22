#导入matplotlib模块pyplot对象并使用as给对象起个别名plt
import matplotlib.pyplot as plt    
import jieba                       #导入jieba分词模块
import wordcloud                   #导入词云图模块
from wordcloud import ImageColorGenerator
import numpy as np                 #导入numpy模块
from PIL import Image              #从Pillow（PIL）模块中导入Image对象
# 读取文本文件
text = open(r'bible.txt','r').read() #elsa.txt可以改成自己的文件
cut_text = jieba.cut(text)         #分词处理
word = ' '.join(cut_text)          #以空格分割文本
#读取图片
pic = np.array(Image.open(r'D:\github\pythonFile\每日一题\2020\python20191223code01\1594607923_1_-removebg-preview (1).png'))
image_colors = ImageColorGenerator(pic)  #生成图片颜色中的颜色
wd = wordcloud.WordCloud(
    mask=pic,                      #背景图形,如果根据图片绘制，则需要设置
    font_path='simhei.ttf',        #可以改成自己喜欢的字体
    background_color='white',      #词云图背景颜色可以换成自己喜欢的颜色
    )
wd.generate(word)                  #生成词云
# 图片颜色渲染词云图的颜色，用color_func指定
plt.imshow(wd.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis('off')#关闭显示x轴、y轴下标
plt.show()
