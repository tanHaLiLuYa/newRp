from pptx import *
from pptx.chart.data import CategoryChartData,ChartData
from pptx.util import Inches,Cm
from pptx.enum.chart import XL_CHART_TYPE,XL_TICK_MARK
from pptx.util import Pt
from pptx.dml.color import RGBColor


prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[5])

#柱状图
chart_data = ChartData()
chart_data.categories =["east","west","mideast"]
chart_data.add_series("Q1",(46,45,89))
chart_data.add_series("Q2",(46,45,89))
chart_data.add_series("Q3",(46,45,89))
x,y,cx,cy = Inches(2),Inches(2),Inches(4),Inches(2)
graphic_frame = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,x,y,cx,cy,chart_data
)
chart = graphic_frame.chart
#插入表格
slide = prs.slides.add_slide(prs.slide_layouts[5])
shapes = slide.shapes

shapes.title.text = "报告"

name_objects = ["object1","object2","object3"]
name_AIs = ["AI1","AI2","AI3"]
val_AI1 = (312,34,53)
val_AI2 = (312,34,53)
val_AI3 = (312,34,53)
val_AIs = [val_AI1,val_AI2,val_AI3]
#表格样式
rows = 4
cols = 4
top = Cm(12.5)
left = Cm(0.5)
width = Cm(24)
height = Cm(5)

table = shapes.add_table(rows,cols,left,top,width,height).table
table.cell(0,1).text = name_objects[0]
table.cell(0,2).text = name_objects[1]
table.cell(0,3).text = name_objects[2]



prs.save("另存文件.pptx")