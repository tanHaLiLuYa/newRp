import pandas as pd
import akshare as ak
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.charts import Timeline
import os,random,phantomjs
from pyecharts.render import make_snapshot

import json


# from snapshot_phantomjs import snapshot
os.chdir(r"C:\Users\16930\Desktop\python\21 python-数据分析\12-人工智能阶段-数据分析\数据分析资料\TEST")

# df1 = pd.read_json("timeseries.json",orient="index")
raw_data = open(r".\CSSEGISandData\timeseries0404.json")
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
# print(df1.head(),df1.shape)

# df1 = df1[["country","confirmed","recovered","deaths","date"]]

# for key,value in nameMap.items():
#     df1["country"].replace(key,value,inplace=True)
# print(df1)
# print(df1.head(),df1.shape)



# 修改数据格式为日期格式
df1["date"]=pd.to_datetime(df1.date)
# df1 = df1[df1["updateTime"]<"2020-03-15"]



# df2.eval('现存确诊 = province_confirmedCount - province_curedCount - province_deadCount' , inplace=True)
# df2['现存确诊']=df2["province_confirmedCount"]-df2["province_curedCount"]-df2["province_deadCount"] 
# df2 = df2.assign(provinceExistConfirmedCount = lambda x : x["province_confirmedCount"]-x["province_curedCount"]-x["province_deadCount"]  )
df1['现存确诊']=""
df1.loc[df1["confirmed"]-df1["recovered"]-df1["deaths"] > 0,"现存确诊"] = df1["confirmed"]-df1["recovered"]-df1["deaths"]
df1.loc[df1["confirmed"]-df1["recovered"]-df1["deaths"] <= 0,"现存确诊"] = 0


#对数据进行透视
df2 = df1[['country',"现存确诊","date"]]
# df2.set_index("date",inplace=True)
df2 = df2.pivot("date",'country',"现存确诊")
# print(df2.head())
df2 = df2.fillna(0)
# print(df2.shape)

attr = df2.columns.tolist()

# print(attr)
# attr =['Azerbaijan', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', \
    'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',\
    'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', \
    'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', \
    'Cape Verde', 'Cayman Islands', 'Central African Rep', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', \
    'Congo', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cruise Ship', 'Cuba', 'Curacao', \
    'Cyprus', 'Czech Republic', 'Czechia', 'Denmark', 'Diamond Princess', 'Djibouti', 'Dominica',\
    'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', \
    'Eswatini', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'Gabon', 'Gambia',\
    'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe',\
    'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras',\
    'Hong Kong', 'Hong Kong SAR', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', \
    'Iraq', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', \
    'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Liechtenstein',\
    'Lithuania', 'Luxembourg', 'MS Zaandam', 'Macao SAR', 'Macau', 'Madagascar', 'Malawi', 'Malaysia',\
    'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova, Republic of',\
    'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', \
    'Nicaragua', 'Niger', 'Nigeria', 'North Ireland', 'North Macedonia', 'Norway', 'Oman', 'Others', 'Pakistan', \
    'Palestine, State of', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', \
    'Puerto Rico', 'Qatar', 'Ireland', 'Republic of Moldova', 'Republic of the Congo', 'Reunion', 'Romania', \
    'Russia', 'Rwanda', 'Saint Barthelemy', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin',\
    'Saint Vincent and the Grenadines', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', \
    'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'Korea', 'Spain', 'Sri Lanka', 'St. Martin', \
    'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taipei and environs', 'Taiwan', \
    'Tanzania, United Republic of', 'Thailand', 'The Bahamas', 'The Gambia', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', \
    'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', \
    'United States', 'Uruguay', 'Uzbekistan', 'Vatican City', 'Venezuela', 'Viet Nam', 'Vietnam',\
    'West Bank and Gaza', 'Zambia', 'Zimbabwe', 'Palestine']

n = len(df2.index)

timeLine =Timeline()



#定义每日地图绘制函数
def map_visualmap(sequence, date) -> Map:
    c =Map()
    c.add(date, sequence, maptype="world",label_opts=opts.LabelOpts(is_show=False,font_size=8))
    c.set_global_opts(title_opts=opts.TitleOpts(title="CBIC：全球各国现存确诊_至4月2号",subtitle="数据来源Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)"),
        legend_opts=opts.LegendOpts(is_show=True),visualmap_opts=opts.VisualMapOpts(max_=1000,range_color=["#F8F8FF",'#FF0909']))
    # c = (
    #     Map()
    #     .add(date, sequence, maptype="china")
    #     .set_global_opts(
    #         title_opts=opts.TitleOpts(title="全国疫情动态地图_确诊累计人数_截至至3月14号"),
    #         visualmap_opts=opts.VisualMapOpts(max_=1400)
    #     )
    # )
    return c

for i in range(n):
    #取每日数据
    row = df2.iloc[i,].tolist()
    #将数据转换为二元的列表
    sequence_temp = list(zip(attr,row))
    #对日期格式化以便显示
    time = format(df2.index[i], "%Y-%m-%d")
    #创建地图
    map_temp = map_visualmap(sequence_temp,time)
    #将地图加入时间轴对象
    timeLine.add(map_temp,time).add_schema(play_interval=500,is_auto_play=False)
# 地图创建完成后，通过render()方法可以将地图渲染为html 
timeLine.render('全球疫情动态地图.html')



# provincesList = df2["provinceName"].drop_duplicates().values.tolist()
# print(df2.shape)
# print(df2["provinceName"])
# df2 = df2.set_index(df2["provinceName"].drop_duplicates().values.tolist())
# print(df2.head())



# writer =pd.ExcelWriter('疫情数据.xlsx')

# df2.to_excel(writer)

# writer.save()#文件保存

# writer.close()
