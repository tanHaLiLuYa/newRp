from matplotlib import pyplot as plt
import os,random
# os.chdir(r"")
# print(os.getcwd())
# x =range(2,26,2)
# y =[15,13,14.5,17,20,25,26,26,27,22,18,15]
# fig =plt.figure(figsize=(10,5),dpi=80)
# plt.plot(x,y)

# plt.xticks(x[::3])
# plt.savefig("./sig_size.svg")
# plt.show()

#设置中文字体 
from matplotlib import font_manager,rc
font ={"family":"Microsoft Yahei","size":"10"}
rc("font",**font)
# font_ = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")



#设置图片大小 以及添加水印
# plt.figure(figsize=(20,8))
fig =plt.figure(figsize=(20,8))
fig.text(0.75, 0.45, '我的花花世界',
         fontsize=60, color='yellow',
         ha='right', va='bottom', alpha=0.4)

# x =range(120)

# random.seed(10)#设置随机种子 每次随机结果一致
# y =[random.uniform(20,35) for i in range(120)]
# x_ticks =["10点{}分".format(i) for i in x if i<60]
# x_ticks +=["11点{}分".format(i-60) for i in x if i>=60]
# # print(x_ticks)
# plt.plot(x_ticks,y)
# plt.xticks(list(x)[::5],x_ticks[::5],rotation=0,fontproperties=font_)
# plt.xlabel("时间",fontproperties=font_)
# plt.ylabel("温度 ℃",fontproperties=font_)
# plt.title("10点到12点每分钟温度随时间变化情况图表",fontproperties=font_)
# plt.show()

# b  =[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
# b2 =[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
# a =list(range(11,31))
# a_ = ["{}岁".format(i) for i in a]
# # print(a_)
# plt.plot(a,b,label="自己")
# plt.plot(a,b2,label="同桌",linestyle="--")

# plt.legend(loc="best")
# plt.xticks(a[::3],a_[::3])
# plt.yticks(range(0,8))

# plt.xlabel("年龄")
# plt.ylabel("女朋友个数")

# plt.grid(alpha=0.1)


# plt.show()


#绘制散点图
# a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
# # b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

# date_data = list(range(1,32))
# date_data_addchar =["3月{}号".format(i) for i in date_data]
# plt.scatter(date_data,a)
# plt.xticks(date_data[::4],date_data_addchar[::4])
# plt.yticks(range(0,25,3))

# plt.xlabel("日期")
# plt.ylabel("温度 ℃")
# plt.show()

#绘制条形图
# a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

# b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23] 
# plt.bar(a,b,width=0.3)
# plt.xticks(rotation=90)

# plt.xlabel("片名")
# plt.ylabel("票房 单位 亿")
# plt.title("2017年内地电影票房前20的电影")
# plt.show()

#绘制条形图2
# a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
# b_16 = [15746,312,4497,319]
# b_15 = [12357,156,2045,168]
# b_14 = [2358,399,2358,362]

# bar_width=0.2

# x_14 = list(range(len(a)))
# x_15 = [i +bar_width for i in x_14]
# x_16 = [i +bar_width*2 for i in x_14]
# plt.bar(x_14,b_14,width=bar_width,label="14号")
# plt.bar(x_15,b_15,width=bar_width,label="15号")
# plt.bar(x_16,b_16,width=bar_width,label="16号")

# plt.legend(loc="best")
# plt.xticks(x_15,a)#将tick 设置为 电影名称的内容
# plt.show()

# a=[131, 98,125,131,124,139,131,117,128,108,135,138,131,102,107,\
# 114,119,128,121,142,127,130,124,101,110,116,117,110,128,128,115,\
# 99,136,126,134,95,138,117,111,78,132,124,113,150,110,117,86,\
# 95,144,105,126,130,126,130,126,116,123,106,112,138,123,86,101,\
# 99,136,123,117,119,105,137,123,128,125,104,109,134,125,127,105,\
# 120,107,129,116,108,132,103,136,118,102,120,114,105,115,132,\
# 145,119,121,112,139,125,138,109,132,134,156,106,117,127,144,\
# 139,139,119,140,83,110,102,123,107,143,115,136,118,139,123,112,\
# 118,125,109,119,133,112,114,122,109,106,123,116,131,127,115,\
# 118,112,135,115,146,137,116,103,144,83,123,111,110,111,100,\
# 154,136,100,118,119,133,134,106,129,126,110,111,109,141,120,\
# 117,106,149,122,122,110,118,127,121,114,125,126,114,140,103,\
# 130,141,117,106,114,121,114,133,137,92,121,112,146,97,137,\
# 105,98,117,112,81,97,139,113,134,106,144,110,137,137,111,\
# 104,117,100,111,101,110,105,129,137,112,120,113,133,112,83,\
# 94,146,133,101,131,116,111,84,137,115,122,106,144,109,123,116,111,111,133,150]
# bins=int((max(a)-min(a))/3)
# plt.hist(a,bins)
# plt.xticks(list(range(min(a),max(a)+1))[::3])
# plt.show()

#p48-2.py