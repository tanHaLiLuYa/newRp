# encoding: utf-8
from pptx import Presentation
from pptx.util import Inches, Cm, Pt
from pptx.chart.data import ChartData
from pptx.enum.text import PP_ALIGN
from docx.enum.dml import MSO_THEME_COLOR
from pptx.dml.color import RGBColor
from openpyxl.utils.dataframe import dataframe_to_rows
import openpyxl,os,time
from openpyxl.utils import get_column_letter, column_index_from_string

RootPath = r"E:\work\samsung\W46周报"
backup_path =r"E:\work\samsung\W46周报\备份"
file_name="W46MS_Audit_Weekly_Report_2019_11_20_13_59SD.pptx"
do_file_name = file_name[:25]+file_name[len(file_name)-5:len(file_name)]#文件名不包含日期，字符串为25个数字
# print(do_file_name)

#更新文件名称
back_file_name =do_file_name.replace(".pptx","_backup{}.pptx".format(time.strftime("_%Y_%m_%d_%H_%M", time.localtime())))
new_file_name  =do_file_name.replace(".pptx","{}.pptx".format(time.strftime("_%Y_%m_%d_%H_%M", time.localtime()))) 
pptx_path = os.path.join(RootPath,file_name)
pptx_path_back =os.path.join(backup_path,back_file_name)
new_pptx_path = os.path.join(RootPath,new_file_name)
exl_path =os.path.join(RootPath,"W46_过渡data_1120_1120.xlsx")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#打开ppt，excel
print("opening file ....................")
wb = openpyxl.load_workbook(exl_path,data_only=True,read_only = True)
prs = Presentation(pptx_path)

#备份ppt
# prs.save(pptx_path_back)
# !=
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>辅助函数
#获取slides id 并建立字典  注意 请确保每一页有title shape,title内容名称不重复，，否则会发生错误
def get_id_slide_bytitle(prs_=prs,title_name="total_title"):
    dic_={}
    list_id=[]
    list_title=[]
    # print(len(prs_.slides))
    for i in prs_.slides:
        list_id.append(i.slide_id)
    for t in range(0,len(prs_.slides)):
        page_name = prs_.slides[t]
        for shape in page_name.shapes:
            if shape.name == title_name:
                # print(shape.text)
                list_title.append(shape.text)
    for n in range(0,len(prs_.slides)):
        dic_[list_title[n]]=prs_.slides.index(prs_.slides.get(slide_id=list_id[n]))
    return dic_
#设置字体格式函数1,
def setfont(myrange,fsize=9, fname="微软雅黑",alig = PP_ALIGN.CENTER,fbold = False,fitalic = False,r=0x00,g=0x00,b=0x00):
    # # alig 参数不需要引号,  PP_ALIGN.LEFT 左对齐
    for paragraph in myrange.text_frame.paragraphs:
        paragraph.alignment = alig
        for run in paragraph.runs:
            run.font.size = Pt(fsize)
            run.font.name = fname
            run.font.bold = fbold
            run.font.italic = fitalic
            run.font.color.rgb = RGBColor(r,g,b)
#设置字体格式函数2,
def setrun(c_run,r_size,r_bold,r_name="微软雅黑",r_r=0x00,r_g=0x00,r_b=0x00):
    c_run.font.size = Pt(r_size)
    c_run.font.bold=r_bold
    c_run.font.name = r_name
    c_run.font.color.rgb = RGBColor(r_r,r_g,r_b)
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
# 取list最大值
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
#判断值是否在列表里面
def isinlist(list_in,testnum):
    for i in list_in:
        if str(i)==str(testnum) :
            return True
    return False
#获取ppt table 里面的最大行和最大列，返回列表
def get_maxrow_maxcol(table):
    row = table.rows
    col = table.columns
    return [len(row),len(col)]
#获取chart区域的行数和列数，返回列表
def get_shapeofrange(ishape):
    plot = ishape.chart.plots[0]
    row = len(plot.categories)+1
    col = len(plot.series)+1
    return [row,col]
# 获取chart中数据，返回列表的列表，不包含标题行即series .name
def get_data_chart(ishape):
    plot = ishape.chart.plots[0]
    series = iter(plot.series)
    list_out=[]
    for i in range(1,get_shapeofrange(ishape)[1]):
        list_out.append(next((series)).values)
    # for i in ishape.chart.series:
    #     print(i.name)
    return list_out


#》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》主函数
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>主函数
#设置粘贴值函数 for table 更新20191127
def copy_table(sheetnames,excel_range,
                ppt_title,ppt_shapename,
                ppt_begin_index,rank_col=False,color_num=False,
                color_str_min="粉色",color_str_max="蓝色" ,f_size=9,
                reverse_fill=None):
    #excel range 输入格式为"A3:D54“,ppt_begin_index 为行列的列表，例如[2,1]表示从第2行第1列开始写入数据
    #rank col 第一个参数是排名列 第二个是前n/或者后n
    ws=wb[sheetnames]
    ws_range=ws[excel_range]
    # "p"+str(ppt_slidesindex+1)#没有0页的PPT需要加1，有的不需要
    #用ppttitle获取index 返回某一页
    page_name = prs.slides[get_id_slide_bytitle()[ppt_title]]
    
    for shape in page_name.shapes:
       
        if shape.name == ppt_shapename:
            ppt_max_r=get_maxrow_maxcol(shape.table)[0]
            ppt_max_c=get_maxrow_maxcol(shape.table)[1]
            b_col=ppt_begin_index[1]
            b_row=ppt_begin_index[0]
            list_rank=[]
            for col in range(b_col,ppt_max_c):
                for row in range(b_row,ppt_max_r):
                    c = shape.table.cell(row, col)
                    c_select=ws_range[row-b_row][col-b_col]
                    if    c_select.number_format == "General" or c_select.number_format == "@":
                        c.text=str(c_select.value if c_select.value != None   else "--")
                    elif  c_select.number_format == "0.0":
                        c.text=str(round(c_select.value,1) if c_select.value != None and c_select.value != "--" else "--")      
                    elif  c_select.number_format == "0%":
                        c.text=str(round(c_select.value*100) if c_select.value != None and c_select.value != "--"  else " ") \
                                        + ("%" if c_select.value != None and c_select.value != "--"  else "--")
                    elif  c_select.number_format == "mm-dd-yy":
                        c.text=str(c_select.value)[:10].replace("-","/")  if c_select.value != None  and c_select.value != "--" else "--"
                    elif  c_select.number_format == "h:mm":
                        c.text=str(c_select.value)[:5]  if c_select.value != None  else "--"
                    else:
                        c.text=str(round(c_select.value)  if c_select.value != None and c_select.value != "--"  else "--")
                    setfont(c,f_size)
            if rank_col: 
                #写入rank list 
                for row in range(b_row+1,ppt_max_r):
                    # c = shape.table.cell(row,rank_col[0])
                    c_select=ws_range[row-b_row][rank_col[0]-b_col]
                    list_rank.append(c_select.value)
                # 匹对涂颜色
                for row in range(b_row+1,ppt_max_r):
                    c_select=ws_range[row-b_row][rank_col[0]-b_col]
                    if isinlist(getmax(list_rank,nums=color_num,small=reverse_fill),c_select.value)and reverse_fill:
                        fill_c(ishape=shape,irow=row,range_area_begin=0,
                                    range_area_end=ppt_max_c-1,
                                    r_color=color_str_min)
                    elif isinlist(getmax(list_rank,nums=color_num),c_select.value):
                        fill_c(ishape=shape,irow=row,range_area_begin=0,
                                    range_area_end=ppt_max_c-1,
                                    r_color=color_str_max)
                    else:
                        fill_c(ishape=shape,irow=row,range_area_begin=0,
                                    range_area_end=ppt_max_c-1,
                                    r_color="白色")        
    print("{}修改成功 in {}>>>>>>>>".format(ppt_shapename,(ppt_title+"--p"+str(get_id_slide_bytitle()[ppt_title]+1))))

#文本更新函数 for text_frame
def copy_text(sheetnames,ppt_title,ppt_shapename,para_index,\
                         excel_cell,f_size=[14],f_bold=[False]):
    ws=wb[sheetnames]
    # "p"+str(ppt_title+1)#没有0页的PPT需要加1，有的不需要
    page_name = prs.slides[get_id_slide_bytitle()[ppt_title]]
    
    for shape in page_name.shapes:
        if shape.name == ppt_shapename:
            c_p=shape.text_frame.paragraphs[para_index]
            if ":" not in  excel_cell :#len ws range[0] 返回第一行的 列数,len ws rang 直接返回行数
                c_p.text=str(ws[excel_cell].value)
                setfont(shape,fsize=f_size[0],alig=PP_ALIGN.LEFT,fbold=f_bold[0])
            else:
                c_p.text = ""
                for i in range(len(ws[excel_cell][0])):
                    run =c_p.add_run()
                    run.text=str(ws[excel_cell][0][i].value)
                    setrun(c_run=run,r_size=f_size[i],r_bold=f_bold[i])
     
    print("{}修改成功 in {}>>>>>>>>".format(ppt_shapename,(ppt_title+"--p"+str(get_id_slide_bytitle()[ppt_title]+1))))

#设置图表数据函数 for chart
def chart_in_data(sheetnames,excel_range,
                ppt_title,ppt_shapename,num_format="0"):
    ws=wb[sheetnames]
    ws_range=ws[excel_range]
    # "p"+str(ppt_title+1)#没有0页的PPT需要加1，有的不需要
    page_name = prs.slides[get_id_slide_bytitle()[ppt_title]]
    
    for shape in page_name.shapes:
        if shape.name == ppt_shapename:
            # get_data_chart(shape)
            chart_data = ChartData()
            max_row=len(ws[excel_range])
            max_col=len(ws[excel_range][0])
            dic_={}
            list_=[]
            ####读取excel数据
            for col in range(0,max_col):
                for row in range(0,max_row):
                    if ws_range[row][col].number_format == "General":
                        list_ .append((ws_range[row][col].value\
                                    if ws_range[row][col].value
                                    else None))
                    elif ws_range[row][col].number_format == "0":
                        list_.append(round(ws_range[row][col].value) 
                                    if ws_range[row][col].value
                                    else None    )
                    else:                      
                        list_ .append(ws_range[row][col].value  if ws_range[row][col].value else None)
                dic_[col]=list_
                list_=[] #清空历史数据   
            #####写入chart中            
            chart_data.categories = tuple(dic_[0][1:])
            for col in range(1,max_col):
                chart_data.add_series(name=dic_[col][0],values=tuple(dic_[col][1:]),number_format=num_format)
            # shape.chart.chart_type()
            
            shape.chart.replace_data(chart_data)
    print("{}修改成功 in {}>>>>>>>>".format(ppt_shapename,(ppt_title+"--p"+str(get_id_slide_bytitle()[ppt_title]+1))))

#设置箭头函数
def arrow_ration(sheetnames,ppt_title,excel_range):
    page_name = prs.slides[get_id_slide_bytitle()[ppt_title]]
    ws=wb[sheetnames]
    ws_range=ws[excel_range]
    for shape in page_name.shapes:
        for row in range(len(ws_range)):
            if shape.name == "down{}".format(row):    
                if    round(ws_range[row][0].value) >round(ws_range[row][1].value):               
                    if round(ws_range[row][0].value) >round(ws_range[row][1].value)+5:
                        shape.rotation= 5.0 #继续向下旋转
                    else:
                        shape.rotation=-5.0#回到初始位置，向下的箭头
                    shape.line.color.rgb = RGBColor(0xF4,0xB1,0x83)#粉色
                elif  round(ws_range[row][0].value) <round(ws_range[row][1].value):
                    shape.rotation=-5.0#回到初始位置，向下的箭头
                    if round(ws_range[row][0].value)+5 <round(ws_range[row][1].value):
                        shape.rotation=-30.0
                    else:
                        shape.rotation=-25.0
                    shape.line.color.rgb = RGBColor(0x9D,0xC3,0xE6)#蓝色
                else:
                    shape.line.color.rgb = RGBColor(0xFF,0xFF,0xFF)#白色

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("begin working ....................")
# copy_text(sheetnames="Appendix",excel_cell="B4:D4",ppt_title="Appendix.1 分公司别表现分析_整体得分",ppt_shapename="title-text",\
#                            f_size=[14,19,10],f_bold=[False,False,True], para_index=0)
# print(get_id_slide_bytitle(prs_=prs))#检查title和index是否对应，每一次换新的ppt都需要核实

# 2.本周主要结果- 指标别
chart_in_data(sheetnames="门店大项得分率_透视",excel_range="X4:Z11",ppt_title="2.本周主要结果- 指标别",ppt_shapename="总体结果-chart")
arrow_ration(sheetnames="门店大项得分率_透视",excel_range="Y5:Z11",ppt_title="2.本周主要结果- 指标别")
copy_text(sheetnames="门店大项得分率_透视",ppt_title="2.本周主要结果- 指标别",ppt_shapename="样本数量-text",
                            para_index=0,excel_cell="T15",f_size=[8],f_bold=[False])
# 
    


# # 2.本周主要结果—严重问题点-F/F违规行为 & 不在岗
# copy_table(sheetnames="严重问题",excel_range="C6:G17",ppt_title="2.本周主要结果—严重问题点-F/F违规行为 & 不在岗",ppt_shapename="不在岗汇总-table",ppt_begin_index=[3,1])

# # # 2.本周主要结果—问题门店复查改善情况
copy_table(sheetnames="严重问题",excel_range="B22:H31",ppt_title="2.本周主要结果—问题门店复查改善情况",ppt_shapename="复查门店汇总-table",ppt_begin_index=[2,0])
copy_table(sheetnames="严重问题",excel_range="B38:H41",ppt_title="2.本周主要结果—问题门店复查改善情况",ppt_shapename="未改善门店-table",ppt_begin_index=[2,0])

# # # # 3.Note 10点检-零售价格检查
# # copy_table(sheetnames="严重问题",excel_range="W5:AC16",ppt_title="3.Note 10点检-零售价格检查",ppt_shapename="低价-table",ppt_begin_index=[3,1])

# # # 3.Note 10/A90点检-新品氛围          
copy_table(sheetnames="NOTE10点检 EUP",excel_range="E8:S19",ppt_title="3.Note 10/A90点检-新品氛围",ppt_shapename="表格 7",ppt_begin_index=[2,1])
copy_text(sheetnames="NOTE10点检 EUP",ppt_title="3.Note 10/A90点检-新品氛围",ppt_shapename="title-text",
                            para_index=0,excel_cell="F2",f_size=[14],f_bold=[False])
# # # #3.Note 10/A90点检-真机体验
copy_table(sheetnames="NOTE10点检 EUP",excel_range="W8:AH19",ppt_title="3.Note 10/A90点检-真机体验",ppt_shapename="表格 7",ppt_begin_index=[2,1])
copy_text(sheetnames="NOTE10点检 EUP",ppt_title="3.Note 10/A90点检-真机体验",ppt_shapename="title-text",
                            para_index=0,excel_cell="V2",f_size=[14],f_bold=[False])
copy_text(sheetnames="NOTE10点检 EUP",ppt_title="3.Note 10/A90点检-真机体验",ppt_shapename="title-text",
                            para_index=1,excel_cell="V3",f_size=[14],f_bold=[False])
# # # # #4.人员问题—导购员和店员产品介绍对比
copy_table(sheetnames="NOTE10点检 EUP",excel_range="E29:R40",ppt_title="4.人员问题—导购员和店员产品介绍对比",ppt_shapename="表格 2",ppt_begin_index=[3,1],\
            rank_col=[5,3],color_num=3,reverse_fill=True,color_str_max="白色")
copy_text(sheetnames="NOTE10点检 EUP",ppt_title="4.人员问题—导购员和店员产品介绍对比",ppt_shapename="title-text",
                            para_index=0,excel_cell="C24",f_size=[14],f_bold=[False])

# # 6.门店问题—电子价签安装/更新
chart_in_data(sheetnames="门店大项得分率_透视",excel_range="AC1:AE14",ppt_title="6.门店问题—电子价签安装/更新",ppt_shapename="图表 18")
copy_text(sheetnames="门店大项得分率_透视",ppt_title="6.门店问题—电子价签安装/更新",ppt_shapename="title-text",
                            para_index=0,excel_cell="Y16:Z16",f_size=[14,14],f_bold=[False,True])
copy_text(sheetnames="门店大项得分率_透视",ppt_title="6.门店问题—电子价签安装/更新",ppt_shapename="title-text",
                            para_index=1,excel_cell="Y17:AB17",f_size=[14,14,14,14],f_bold=[False,True,False,True])
copy_text(sheetnames="门店大项得分率_透视",ppt_title="6.门店问题—电子价签安装/更新",ppt_shapename="文本框 30",
                            para_index=0,excel_cell="Z15",f_size=[8],f_bold=[False])

chart_in_data(sheetnames="门店大项得分率_透视",excel_range="AI1:AK14",ppt_title="7.门店问题— Retail Mode 自动播放",ppt_shapename="屏保-chart")
copy_text(sheetnames="门店大项得分率_透视",ppt_title="7.门店问题— Retail Mode 自动播放",ppt_shapename="文本框 43",
                            para_index=0,excel_cell="AH15",f_size=[8],f_bold=[False])
copy_text(sheetnames="门店大项得分率_透视",ppt_title="7.门店问题— Retail Mode 自动播放",ppt_shapename="title-text",
                            para_index=0,excel_cell="AH16",f_size=[14],f_bold=[False])
# # Appendix.1 分公司别表现分析
copy_table(sheetnames="Appendix",excel_range="D9:N20",ppt_title="Appendix.1 分公司别表现分析_整体得分",ppt_shapename="表格 1",ppt_begin_index=[2,1],\
                                    rank_col=[2,3],color_num=3,reverse_fill=True,color_str_max="白色")
copy_text(sheetnames="Appendix",ppt_title="Appendix.1 分公司别表现分析_整体得分",ppt_shapename="title-text",
                            para_index=0,excel_cell="C4:D4",f_size=[14,14],f_bold=[False,False])

copy_table(sheetnames="Appendix",excel_range="K45:AD56",ppt_title="Appendix.1 分公司别表现分析_陈列体验",ppt_shapename="表格 1",ppt_begin_index=[2,1],\
                                    rank_col=[1,3],color_num=3,reverse_fill=True,color_str_max="白色")  
copy_text(sheetnames="Appendix",ppt_title="Appendix.1 分公司别表现分析_陈列体验",ppt_shapename="TextBox 33",
                            para_index=0,excel_cell="K26:L26",f_size=[14,14],f_bold=[False,False])                                  

copy_table(sheetnames="Appendix",excel_range="D65:N76",ppt_title="Appendix.1 分公司别表现分析_F/F表现",ppt_shapename="表格 4",ppt_begin_index=[2,1],\
                                    rank_col=[1,3],color_num=3,reverse_fill=True,color_str_max="白色")   
copy_text(sheetnames="Appendix",ppt_title="Appendix.1 分公司别表现分析_F/F表现",ppt_shapename="TextBox 33",
                            para_index=0,excel_cell="B58:C58",f_size=[14,14],f_bold=[False,False])                                     

print("closing flie....................")
wb.close()
prs.save(new_pptx_path)

if __name__ == "__main__":
    pass

