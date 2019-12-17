#!/usr/bin/env python
# encoding: utf-8

# Created by simon at 2018/11/11 10:13 PM


from pptx import Presentation
from pptx.util import Inches, Cm, Pt
from pptx.chart.data import ChartData
from pptx.enum.text import PP_ALIGN
from docx.enum.dml import MSO_THEME_COLOR
from pptx.dml.color import RGBColor
import os
# import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

import openpyxl 
from openpyxl.utils import get_column_letter, column_index_from_string

para = {
    "week_num": "W43",
    "r_date": "19.10.20",
    "nums":190,
    "camera_nums":100
}

para_old = {
    "week_num": "W37",
    "r_date": "19.10.20"
}

RootPath = r"C:\Users\16930\Desktop\python 测试"
pptx_path = os.path.join(RootPath,"Y'19 10月_MS Audit Monthly Report_091023_1620.pptx")
new_pptx_path = os.path.join(RootPath,"{} MS_Audit_Weekly_Report{}.pptx".format(para["week_num"],para["r_date"]))
exl_path =os.path.join(RootPath,"W38-W41_过渡data_191028_1430.xlsx")

# print(new_pptx_path)
wb = openpyxl.load_workbook(exl_path,data_only=True,read_only = True)
# ws =wb["Appendix得分和问题分析"]




slide_layout_index = 1

#打开ppt

prs = Presentation(pptx_path)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#设置字体格式函数,
def setfont(myrange,fsize=9, fname="Microsoft YaHei",alig = PP_ALIGN.CENTER,fbold = False,fitalic = False,r=0x00,g=0x00,b=0x00):
    # Set font = textbox.TextFrame.TextRange.Font
    for paragraph in myrange.text_frame.paragraphs:
        # Set Font_ = paragraph
        paragraph.alignment = alig
        for run in paragraph.runs:
            run.font.size = Pt(fsize)
            run.font.name = fname
            run.font.bold = fbold
            run.font.italic = fitalic
            run.font.color.rgb = RGBColor(r,g,b)
            # run.font.color.theme_color  = fcolor  fcolor =MSO_THEME_COLOR.DARK_1
            # run.fill.solid()
            # run.fill.fore_color.rgb = RGBColor(r,g,b),r=0xFA,g=0x00,b=0x37
            # alig 参数不需要引号,  PP_ALIGN.LEFT 左对齐

# #取list最大值
def getmax(inlist,nums,small=None):
    inlist.sort(reverse=True) 
    out_list=[]
    for i in inlist:
        i = str(i)
    if small:
        for i in range(len(inlist)-1,len(inlist)-nums-1,-1):
            out_list.append(inlist[i])
    else:
        out_list=inlist[0:nums]
    return out_list
# print(getmax(list_,nums=2,small=-1))

#判断值是否在列表里面
def isinlist(list_in,testnum):
    for i in list_in:
        if str(i)==str(testnum) :
            return True
    return False

#获取ppt table 里面的最大行和最大列
def get_maxrow_maxcol(table):
    row = table.rows
    col = table.columns
    return [len(row),len(col)]
#获取chart区域的行数和列数
def get_shapeofrange(ishape):
    plot = ishape.chart.plots[0]
    row = len(plot.categories)+1
    col = len(plot.series)+1
    return [row,col]
def get_data_chart(ishape):
    # for p in ishape.chart.plots:
    plot = ishape.chart.plots[0]
    series = iter(plot.series)
    list_out=[]
    for i in range(1,get_shapeofrange(ishape)[1]):
        list_out.append(list(next((series)).values))
    return list_out



#设置粘贴值函数
def copy_table(sheetnames,excel_range,
                ppt_slidesindex,ppt_shapename,
                ppt_begin_index
                ):
    #excel range 输入格式为"A3:D54“,ppt_begin_index 为行列的列表，例如[2,1]表示从第2行第1列开始写入数据
    
    ws=wb[sheetnames]
    ws_range=ws[excel_range]
    # "p"+str(ppt_slidesindex+1)#没有0页的PPT需要加1，有的不需要
    page_name = prs.slides[ppt_slidesindex]
    
    for shape in page_name.shapes:
       
        if shape.name == ppt_shapename:
            ppt_max_r=get_maxrow_maxcol(shape.table)[0]
            ppt_max_c=get_maxrow_maxcol(shape.table)[1]
            for col in range(ppt_begin_index[1],ppt_max_c):
                for row in range(ppt_begin_index[0],ppt_max_r):
                    c = shape.table.cell(row, col)
                    c.text=str(round(ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value) 
                                    if ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value
                                    else " ")
                    setfont(c,9)
    print("{}修改成功 in {}>>>>>>>>".format(ppt_shapename,("p"+str(ppt_slidesindex+1))))
#设置粘贴值函数,带小数点位数/百分数
def copy_table_format(sheetnames,excel_range,
                    ppt_slidesindex,ppt_shapename,
                    ppt_begin_index,differcol,
                    dec_num=None,per_dec=None,f_size=9,
                    
                    ):
    #excel range 输入格式为"A3:D54“,ppt_begin_index 为行列的列表，例如[2,1]表示从第2行第1列开始写入数据
    #differcol为列表，表示哪些列，float_yesorno_num 列表，表示是否小数点/百分号["dec"/"per",1]]
    ws=wb[sheetnames]
    ws_range=ws[excel_range]
    # "p"+str(ppt_slidesindex+1)#没有0页的PPT需要加1，有的不需要
    page_name = prs.slides[ppt_slidesindex]
    
    for shape in page_name.shapes:
        if shape.name == ppt_shapename:
            ppt_max_r=get_maxrow_maxcol(shape.table)[0]
            ppt_max_c=get_maxrow_maxcol(shape.table)[1]
            for col in range(ppt_begin_index[1],ppt_max_c):
                for row in range(ppt_begin_index[0],ppt_max_r):
                    c = shape.table.cell(row,col)
                    c.text =str(round(ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value*100 
                                        if isinlist(differcol,col) else ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value, None) \
                                        if ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value else " ")+ ("%" \
                                        if isinlist(differcol,col) else "")\
                                    if per_dec == 0    else\
                            str(round(ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value,dec_num if isinlist(differcol,col) else None) \
                                        if ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value else " ")         
                                        
                    setfont(c,f_size)
    print("{}修改成功 in {}>>>>>>>>".format(ppt_shapename,("p"+str(ppt_slidesindex+1))))
#设置粘贴值函数,带小数点位数/百分数,包含填充颜色
def copy_table_format_fill(sheetnames,excel_range,
                    ppt_slidesindex,ppt_shapename,
                    ppt_begin_index,differcol,rank_col,color_num,
                    dec_num=None,per_dec=None,f_size=9,reverse_fill=None,
                    color_str_min="粉色",color_str_max="蓝色"                                       
                    ):
    #excel range 输入格式为"A3:D54“,ppt_begin_index 为行列的列表，例如[2,1]表示从第2行第1列开始写入数据
    #differcol为列表，表示哪些列，float_yesorno_num 列表，表示是否小数点/百分号["dec"/"per",1]]
    ws=wb[sheetnames]
    ws_range=ws[excel_range]
    # "p"+str(ppt_slidesindex+1)#没有0页的PPT需要加1，有的不需要
    page_name = prs.slides[ppt_slidesindex]   
    for shape in page_name.shapes:
        if shape.name == ppt_shapename:
            ppt_max_r=get_maxrow_maxcol(shape.table)[0]
            ppt_max_c=get_maxrow_maxcol(shape.table)[1]
            list_rank=[]
            for col in range(ppt_begin_index[1],ppt_max_c):
                for row in range(ppt_begin_index[0],ppt_max_r):
                    c = shape.table.cell(row,col)
                    c.text =str(round(ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value*100 
                                        if isinlist(differcol,col) else ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value, None) \
                                        if ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value else " ")+ ("%" \
                                        if isinlist(differcol,col) else "")\
                                    if per_dec == 0    else\
                            str(round(ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value,dec_num if isinlist(differcol,col) else None) \
                                        if ws_range[row-ppt_begin_index[0]][col-ppt_begin_index[1]].value else " ")         
                    setfont(c,f_size)                   
                    if rank_col[0]==col and row != ppt_begin_index[0]:
                        list_rank.append(shape.table.cell(row,rank_col[0]).text)                
            for row in range(ppt_begin_index[0],ppt_max_r):
                c = shape.table.cell(row,rank_col[0])
                if isinlist(getmax(list_rank,nums=color_num,small=reverse_fill),shape.table.cell(row,rank_col[0]).text)and reverse_fill:
                    fill_c(ishape=shape,irow=row,range_area_begin=0,
                                    range_area_end=ppt_max_c-1,
                                    r_color=color_str_min)
                elif isinlist(getmax(list_rank,nums=color_num),shape.table.cell(row,rank_col[0]).text):
                    fill_c(ishape=shape,irow=row,range_area_begin=0,
                                    range_area_end=ppt_max_c-1,
                                    r_color=color_str_max)
                else:
                    fill_c(ishape=shape,irow=row,range_area_begin=0,
                                    range_area_end=ppt_max_c-1,
                                    r_color="白色") 
                                                       
    # print(list_rank)
    print("{}修改成功 in {}>>>>>>>>".format(ppt_shapename,("p"+str(ppt_slidesindex+1))))
# 设置填充函数
def fill_c(ishape,irow,range_area_end,range_area_begin,r_color="粉色",r_c=0xFF,g_c=0xFF,b_c=0xFF):
    for col in range(range_area_begin,range_area_end+1):
        c=ishape.table.cell(irow,col)
        c.fill.solid()
        if r_color == "粉色":
            c.fill.fore_color.rgb = RGBColor(0xF8,0xCB,0xAD)
        elif r_color == "蓝色":
            c.fill.fore_color.rgb = RGBColor(0xBD,0xD7,0xEE)#蓝色
        elif r_color == "白色" :
            c.fill.fore_color.rgb = RGBColor(0xFF,0xFF,0xFF)#全部涂白用
        else:
            c.fill.fore_color.rgb = RGBColor(r_c,g_c,b_c)#自选色

#设置图表数据函数
# def chart(sheetnames,excel_range,
#                 ppt_slidesindex,ppt_shapename,chart_shape):
#     ws=wb[sheetnames]
#     ws_range=ws[excel_range]
#     # "p"+str(ppt_slidesindex+1)#没有0页的PPT需要加1，有的不需要
#     page_name = prs.slides[ppt_slidesindex]
    
#     for shape in page_name.shapes:
       
#         if shape.name == ppt_shapename:
#             chart_data = ChartData()
#             for row in range(0,)
    





# copy_table_format(sheetnames="Appendix得分和问题分析",
#                 excel_range="D7:N18",ppt_slidesindex=17,
#                 ppt_shapename="整体得分table",
#                 ppt_begin_index=[2,1],differcol=[2,4],
#                 dec_num= 2
#                 )
# 表格 15
# copy_table_format(sheetnames="Appendix得分和问题分析",
#                 excel_range="C115:G126",ppt_slidesindex=23,
#                 ppt_shapename="表格 15",
#                 ppt_begin_index=[3,1],differcol=[5],
#                 dec_num= None,per_dec=0
#                 )
# copy_table_format_fill(sheetnames="Appendix得分和问题分析",
#                 excel_range="C115:G126",ppt_slidesindex=23,
#                 ppt_shapename="表格 15",
#                 ppt_begin_index=[3,1],differcol=[3,2],color_num=2,
#                 dec_num=2,per_dec=1,rank_col=[1000]
#                 )


# copy_table(sheetnames="Appendix得分和问题分析",
#                 excel_range="D7:N18",ppt_slidesindex=17,
#                 ppt_shapename="整体得分table",
#                 ppt_begin_index=[2,1]
#                 )

    
    
    
        

    

   



# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# prs1 = Presentation(new_pptx_path)
# p1 = prs1.slides[1]
# p1.name = "封面"
# print(p1.name)
# print(p0.shapes[1].text)
# for shape in p0.shapes:
#     if shape.has_text_frame:
#         # print(shape.name)
#         #     f"名称是{shape.name}, id是---{shape.shape_id}, 形状类型为{shape.shape_type}, 里面的文字是：{shape.text}")
#         if shape.name == "title":
#             new_title = shape.text.replace(para_old["week_num"], para["week_num"])
#             shape.text = new_title
#             setfont(shape,40,fbold=True)
#             print("{}修改成功 in P0>>>>>>>>".format(shape.name))
#         elif shape.name == "date":
            
#             new_text = para["r_date"]
#             shape.text=new_text
#             setfont(shape,24)
#             print("{}修改成功 in P0>>>>>>>>".format(shape.name))


# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# p33= prs.slides[33]
# # print(p1.element)
# for shape in p33.shapes:
#     # print(shape.name)

#     if shape.name == "表格 12":
#         # print(shape.shape_type, shape.shape_id)
#         # print(shape.table.last_row)
#         # shape.table.apply_style(2)
#         for r in range(1, 11):
#             c = shape.table.cell(r, 2)
#             c.text="我是谁"#''''''''''''''''''''''''''''''''''''
#             c.fill.solid()
#             c.fill.fore_color.rgb = RGBColor(0xF8,0xCB,0xAD)
#             setfont(c,10,alig=PP_ALIGN.LEFT)
#         print("{}修改成功 in P1>>>>>>>>".format(shape.name))
    # elif shape.name == "TextBox 33":
        
    #     new_title_1 = shape.text.replace(para_old["week_num"], para["week_num"])
    #     shape.text = new_title_1
    #     # bullet_slide_layout = prs.slide_layouts[1]
    #     setfont(shape,16,alig=PP_ALIGN.LEFT)
        
    #     print("{}修改成功 in P1>>>>>>>>".format(shape.name))
        



# # #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# p2= prs.slides[2]
# # print(p1.element)
# for shape in p2.shapes:
#     # print(shape.name)

#     if shape.name == "图表 18":
#         #总体得分大项得分
#         chart_data = ChartData()
#         chart_data.categories = 'TTL', '门店形象', '新品氛围',"真机体验","F/F仪容仪表","F/F产品介绍","F/F主动性"
#         chart_data.add_series('上周', (80,80,80,80,80,80,80))
#         chart_data.add_series('本周', (90,90,90,90,90,90,90))
#         shape.chart.replace_data(chart_data)
#         print("{}修改成功 in P2>>>>>>>>".format(shape.name))
#     elif shape.name == "文本框 58":#N=xxx
#         shape.text = "N={}".format(para["nums"])
#         setfont(shape,8)
#         print("{}修改成功 in P2>>>>>>>>".format(shape.name))
#     elif shape.name == "表格 25":
#         #得分下降/上升原因
#         for r in range(1,4):
#             c = shape.table.cell(r, 2)
#             c.text="我是谁"#''''''''''''''''''''''''''''''''''''
#             setfont(c,10,alig=PP_ALIGN.LEFT)
#         print("{}修改成功 in P2>>>>>>>>".format(shape.name))
#     elif shape.name == "文本框 10":
#         shape.text_frame.text="ddsadsfsdasasd"#   增加text_frame 保留项目符号
#         setfont(shape,16,alig=PP_ALIGN.LEFT)
#         print("{}修改成功 in P2>>>>>>>>".format(shape.name))



# p18= prs.slides[17]
# i=0
# for shape in p18.shapes:
#     if shape.name == "整体得分table":

#         for col in range(1,12):
#         # col是列,row 是行，ppt中都是从0计数，excel中都是从1开始
#             for row in range(2, 14):
#                 c = shape.table.cell(row, col)
#                 #保留一位小数点
#                 if col == 2:#总分 第三列,需要保留一位小数
#                     c.text=str('%.1f'%(ws.cell(row=row+5,column = col+3).value))
#                     setfont(c,9)
#                 else:
#                     c.text=str(int(ws.cell(row=row+5,column = col+3).value) if ws.cell(row=row+5,column = col+3).value else " ")
#                     setfont(c,9)
#                 #先涂白,然后涂颜色
#                 if col == 3:#排名列
#                     if    c.text !="1" and c.text !="11":
#                         fill_c(irow=row,range_area_end=11,range_area_begin=0,r_color="白色")
#                     elif  c.text == "1":
#                         fill_c(irow=row,range_area_end=11,range_area_begin=0,r_color="蓝色")
#                     elif  c.text == "11":
#                         fill_c(irow=row,range_area_end=11,range_area_begin=0)
#         print("{}修改成功 in P18>>>>>>>>".format(shape.name))


# p24= prs.slides[23]

# list_rank = []
# m=115-3
# n=column_index_from_string("C")-1


# for row in range(116, 127):
#     list_rank.append("{:.1%}".format(ws.cell(row=row,column =7).value))
# print(len(list_rank))
# print(list_rank)
# for shape in p24.shapes:
#     if shape.name == "表格 15":
#         for col in range(1,6):
#             # col是列,row 是行，ppt中都是从0计数，excel中col是从1开始，row是从0开始
#             for row in range(3, 15):
#                 c = shape.table.cell(row, col)
#                 if col == 5:#百分号
#                     # c.text=str('%d%%'%(ws.cell(row=row+m,column = col+n).value))
#                     # c.text = str(int(ws.cell(row=row+m,column = col+n).value*100))+"%"
#                     c.text = "{:.1%}".format(ws.cell(row=row+m,column = col+n).value)
#                     setfont(c,9)
#                 else:
#                     c.text=str(int(ws.cell(row=row+m,column = col+n).value) if ws.cell(row=row+m,column = col+n).value else " ")
#                     setfont(c,9)
#                 # print(list_rank)
#                 # 先涂白,然后涂颜色
#                 fill_c(irow=row,range_area_end=5,range_area_begin=0,r_color="白色")
#                 if col == 5 :#排名列
#                     if    c.text == (getmax(list_rank,n=0)) or c.text ==str(getmax(list_rank,n=1)) or c.text ==str(getmax(list_rank,n=2)):
#                         print(type(c.text),type(getmax(list_rank,n=0)))

#                         fill_c(irow=row,range_area_end=5,range_area_begin=0,r_color="粉色")
# #         print("{}修改成功 in P24>>>>>>>>".format(shape.name))


  

# 
p1= prs.slides[3]
# print(p1.element)
for shape in p1.shapes:
    # print(shape.name)

    if shape.name == "图表 11":
        pl = get_shapeofrange(ishape=shape)  
        chart =shape.chart()
        chart_data = chart.chart_data
        wob =chart_data.Workbook
        print(type(wob))
        print(pl)
#         #总体得分大项得分
#         # chart_data = ChartData()
#         # chart_data.categories = 'TTL', '门店形象', '新品氛围',"真机体验","F/F仪容仪表","F/F产品介绍","F/F主动性"
#         # chart_data.add_series('上周', (80,80,80,80,80,80,80))
#         # chart_data.add_series('本周', (90,90,90,90,90,90,90))
#         # shape.chart.replace_data(chart_data)
#         # print(shape.chart.plots[0].categories)
#         plot = shape.chart.plots[1]
#         # for r in plot.categories:
#         #     print (r)
#         print(plot.categories)
#         print(len(plot.series))
#         # # initial_data =list(next(iter(plot.series)).values)
#         # # print(initial_data)
#         # print(next(iter(plot.series.Formula)).values)
#         print(next(iter(plot.series)).values)
#         # print(next(iter(plot.series)).values)
        



        print("{}修改成功 in P2>>>>>>>>".format(shape.name))


wb.close()
prs.save(new_pptx_path)
if __name__ == "__main__":
    pass

