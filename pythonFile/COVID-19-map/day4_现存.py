import pandas as pd
import akshare as ak
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.charts import Timeline
import os,random,phantomjs
from pyecharts.render import make_snapshot

# from snapshot_phantomjs import snapshot
#


# epidemic_hist_all_df = ak.covid_19_baidu(indicator="中国分省份详情")
# print(epidemic_hist_all_df)

# covid_19_area_search_df = ak.covid_19_area_search(province="四川省", city="成都市")
# print(covid_19_area_search_df)

# covid_19_hist_province_df = ak.covid_19_history()
# print(covid_19_hist_province_df)

# covid_19_163_df = ak.covid_19_163(indicator="中国各地区累计数据")
# print(covid_19_163_df)

# covid_19_area_search_df = ak.covid_19_area_search(province="四川省", city="成都市", district=all)
# print(covid_19_area_search_df)

# writer =pd.ExcelWriter('疫情数据.xlsx')

# covid_19_hist_province_df.to_excel(writer)

# writer.save()#文件保存
# writer.close()

df = pd.read_csv(r".\CSSEGISandData\DXYArea0407.csv")
# print(df.head())
# print(df.columns)
df.drop(['continentName', 'continentEnglishName','countryEnglishName',  'provinceEnglishName',
       'province_zipCode', 'cityName', 'cityEnglishName', 'city_zipCode', 'city_confirmedCount',
       'city_suspectedCount', 'city_curedCount', 'city_deadCount'],axis=1,inplace=True)
# print(df.shape)

df1 = df[df["countryName"].str.contains("中国")]#去除其他国家数据
df1.index = range(len(df1))#重置索引
# print(df1.shape)

#去除省份里国家的数据
mediaData = df1["provinceName"]
delteNums =[]
for i in range(len(mediaData.values)):
    if mediaData.values[i]=="中国":
        delteNums.append(i) 
# print(delteNums)
df1.drop(delteNums,inplace=True) 

#去除重复数据
df1.drop_duplicates(inplace=True)
df1.index = range(len(df1))

# 修改数据格式为日期格式
df1["updateTime"]=pd.to_datetime(df1.updateTime)
# df1 = df1[df1["updateTime"]<"2020-03-15"]

# # print(df.info(),df.head())
# print(df1.head(),df1.shape)

# #排序 后 

df1 = df1.sort_values(by="updateTime",ascending=False)
df1.index = range(len(df1))
# df1.drop_duplicates([]inplace=True)

#分列
# df1["updateTime"].astype(str).split(' ',expand=True)
df2 = df1[["countryName","provinceName","province_confirmedCount","province_suspectedCount","province_curedCount","province_deadCount"]]
df2["date"] = df1["updateTime"].dt.date
df2["time"] = df1["updateTime"].dt.time

# df2.eval('现存确诊 = province_confirmedCount - province_curedCount - province_deadCount' , inplace=True)
# df2['现存确诊']=df2["province_confirmedCount"]-df2["province_curedCount"]-df2["province_deadCount"] 
# df2 = df2.assign(provinceExistConfirmedCount = lambda x : x["province_confirmedCount"]-x["province_curedCount"]-x["province_deadCount"]  )
df2['现存确诊']=""
df2.loc[df2["province_confirmedCount"]-df2["province_curedCount"]-df2["province_deadCount"] > 0,"现存确诊"] = df2["province_confirmedCount"]-df2["province_curedCount"]-df2["province_deadCount"]
df2.loc[df2["province_confirmedCount"]-df2["province_curedCount"]-df2["province_deadCount"] <= 0,"现存确诊"] = 0
# print(df2.head())



#去除 同一天 重复数据
df2.drop_duplicates(subset=["provinceName","date"],keep='first',inplace=True)
df2.index = range(len(df2))
#切片数据
pieces_list=[
        # {"max": 999999, "min": 5000, "label": "5000+"},
        {"max": 99999, "min": 1000, "label": "1000+"},
        {"max": 999, "min": 500, "label": "500-1000"},
        {"max": 499, "min": 100, "label": "100-500"},
        {"max": 99, "min": 50, "label": "50-100","color":"DarkGray"},
        {"max": 49, "min": 1, "label": "1-50","color":"Silver"},
        ]

# print(df2.head())

#定义每日地图绘制函数
def map_visualmap(sequence, date) -> Map:
    c =Map()
    c.add(date, sequence, maptype="china")
    c.set_global_opts(title_opts=opts.TitleOpts(title="CBIC：全国各省现存确诊_至4月8号",subtitle="数据来源于丁香园"),legend_opts=opts.LegendOpts(is_show=False),visualmap_opts=opts.VisualMapOpts(is_piecewise=True,\
        pieces=pieces_list))
    # c = (
    #     Map()
    #     .add(date, sequence, maptype="china")
    #     .set_global_opts(
    #         title_opts=opts.TitleOpts(title="全国疫情动态地图_确诊累计人数_截至至3月14号"),
    #         visualmap_opts=opts.VisualMapOpts(max_=1400)
    #     )
    # )
    return c

df3 = df2[["provinceName","现存确诊","date"]]
# df3.set_index("date",inplace=True)
df3 = df3.pivot("date","provinceName","现存确诊")

df3 = df3.fillna(method='ffill')
# df3.index =df3.index(dtype="to_datetime")
# df3 = df3[df3["date"] < "2020-03-15"]
# listIn =sorted(df3.max().tolist(),reverse=True)[:4]
# print(listIn)


attr = df3.columns.tolist()
# print(attr)

attr = ['上海', '云南', '内蒙古', '北京', '台湾', '吉林', '四川', '天津', '宁夏', '安徽', '山东', '山西', '广东', '广西', '新疆', '江苏', '江西',\
     '河北', '河南', '浙江', '海南', '湖北', '湖南', '澳门', '甘肃', '福建', '西藏', '贵州', '辽宁', '重庆', '陕西', '青海', '香港', '黑龙江']

n = len(df3.index)

timeLine =Timeline()

for i in range(n):
    #取每日数据
    row = df3.iloc[i,].tolist()
    #将数据转换为二元的列表
    sequence_temp = list(zip(attr,row))
    #对日期格式化以便显示
    time = format(df3.index[i], "%Y-%m-%d")
    #创建地图
    map_temp = map_visualmap(sequence_temp,time)
    #将地图加入时间轴对象
    timeLine.add(map_temp,time).add_schema(play_interval=360,is_auto_play=False,is_loop_play=False)
# 地图创建完成后，通过render()方法可以将地图渲染为html 
timeLine.render('./output/t0全国疫情现存确诊动态地图.html')



#

