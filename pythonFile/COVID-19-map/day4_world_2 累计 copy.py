import pandas as pd
import akshare as ak
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.charts import Timeline,Grid
import os,random,phantomjs
from pyecharts.render import make_snapshot

import json


# from snapshot_phantomjs import snapshot
os.chdir(r"C:\Users\16930\Desktop\python\21 python-数据分析\12-人工智能阶段-数据分析\数据分析资料\TEST")

# df1 = pd.read_json("timeseries.json",orient="index")
raw_data = open(r".\CSSEGISandData\timeseries0407.json")
raw_data1 = json.load(raw_data)
raw_data.close()

raw_data2 =[]

# raw_data2 = raw_data1["dailyReports"]
# print(raw_data2)
#字典下 单个key的 列表 下的 字典 内单个key的 列表 下 的字典

# for  oneDic in raw_data2:
#     # print(type(oneDic))
#     for i in oneDic["countries"]:
#         i["date"]=oneDic["updatedDate"]
#         raw_data3.append(i)

#字典下 列表 内 的字典 数据结构
for country in raw_data1:
#     # print(raw_data1[country])
#     # list_name.append(country)
    for i in raw_data1[country]:
        i["country"]=country
        raw_data2.append(i)
# print(len(raw_data2))


df1 = pd.DataFrame(raw_data2)
# df1 =df1.replace("US","United States")
# print(df1.head(),df1.shape)

# df1 = df1[["country","confirmed","recovered","deaths","date"]]

#修正 国家名称
nameMap ={"US":"United States","Korea, South":"Korea","Central African Republic":"Central African Rep.",\
    "Congo (Kinshasa)":"Dem. Rep. Congo","Congo (Brazzaville)":"Congo","Burma":"Myanmar","Dominican Republic":"Dominican Rep",\
        "Cote d'Ivoire":"Côte d'Ivoire","Laos":"Lao PDR","Dominican Rep":"Dominican Rep.","Czechia":"Czech Rep.",\
            "Bosnia and Herzegovina":"Bosnia and Herz.","North Macedonia":"Macedonia"}
for key,value in nameMap.items():
    df1["country"].replace(key,value,inplace=True)
# print(df1)
# print(df1.head(),df1.shape)



# 修改数据格式为日期格式 筛选3月号之后的数据
df1["date"]=pd.to_datetime(df1.date)

df1 = df1[df1["date"]>"2020-02-29"]



# df2.eval('现存确诊 = province_confirmedCount - province_curedCount - province_deadCount' , inplace=True)
# df2['现存确诊']=df2["province_confirmedCount"]-df2["province_curedCount"]-df2["province_deadCount"] 
# df2 = df2.assign(provinceExistConfirmedCount = lambda x : x["province_confirmedCount"]-x["province_curedCount"]-x["province_deadCount"]  )
df1['现存确诊']=""
df1.loc[df1["confirmed"]-df1["recovered"]-df1["deaths"] > 0,"现存确诊"] = df1["confirmed"]-df1["recovered"]-df1["deaths"]
df1.loc[df1["confirmed"]-df1["recovered"]-df1["deaths"] <= 0,"现存确诊"] = 0

#
#对数据进行透视
df2 = df1[['country',"confirmed","date"]]
# df2.set_index("date",inplace=True)
df2 = df2.pivot("date",'country',"confirmed")
# print(df2.head())
df2 = df2.fillna(method="ffill")   
# print(df2.shape)

attr = df2.columns.tolist()

# print(attr)
df2_now = df1[['country',"现存确诊","date"]]
# df2_now.set_index("date",inplace=True)
df2_now = df2_now.pivot("date",'country',"现存确诊")
# print(df2_now.head())
df2_now = df2_now.fillna(method="ffill")   
# print(df2_now.shape)

attr_now = df2_now.columns.tolist()


n = len(df2.index)

timeLine =Timeline()
# page = Page()
grid = Grid()
pieces_list=[
        {"min": 100000, "label": "10万+","color":"red"},
        {"max": 99999, "min": 50000, "label": "5-10万"},
        {"max": 49999, "min": 10000, "label": "1-5万"},
        {"max": 9999, "min": 5000, "label": "0.5-1万"},
        {"max": 4999, "min": 1000, "label": "1000-5000"},
        {"max": 999, "min": 100, "label": "100-1000","color":"DarkGray"},
        {"max": 99, "min": 1, "label": "1-100","color":"Silver"},
        ]
#定义每日地图绘制函数
def map_visualmap(sequence, date):
    c =Map()
    c.add(date, sequence, maptype="world",label_opts=opts.LabelOpts(is_show=False,font_size=8),is_map_symbol_show=False,is_roam=True)
    c.set_global_opts(title_opts=opts.TitleOpts(title="CBIC：全球各国累计确诊_至4月7号",subtitle="数据来源Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)"),
        legend_opts=opts.LegendOpts(is_show=False),visualmap_opts=opts.VisualMapOpts(is_piecewise=True,\
        pieces=pieces_list))
    return c

for i in range(n):
    #取每日数据
    row = df2.iloc[i,].tolist()
    row1 = df2_now.iloc[i,].tolist()
    #将数据转换为二元的列表
    sequence_temp = list(zip(attr,row))
    sequence_temp_now =list(zip(attr_now,row1))
    #对日期格式化以便显示
    time = format(df2.index[i], "%Y-%m-%d")
    #创建地图
    map_temp = map_visualmap(sequence_temp,time)
    map_temp_now = map_visualmap(sequence_temp_now,time)
    grid.add(map_temp,grid_opts=opts.GridOpts(pos_bottom="60%"))
    grid.add(map_temp_now,grid_opts=opts.GridOpts(pos_left="60%",width=10,height=20))
    #前十数据条形图
    
    #将地图加入时间轴对象
    timeLine.add(grid,time).add_schema(play_interval=360,is_auto_play=False,is_loop_play=False)
# 地图创建完成后，通过render()方法可以将地图渲染为html 
timeLine.render('全球疫情累计确诊动态地图-组合.html')
# 
# provincesList = df2["provinceName"].drop_duplicates().values.tolist()
# print(df2.shape)
# print(df2["provinceName"])
# df2 = df2.set_index(df2["provinceName"].drop_duplicates().values.tolist())
# print(df2.head())



# writer =pd.ExcelWriter('疫情数据.xlsx')

# df2.to_excel(writer)

# writer.save()#文件保存

# writer.close()
