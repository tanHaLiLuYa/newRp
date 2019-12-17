from pptx import Presentation
from pptx.util import Inches, Cm, Pt
from pptx.chart.data import ChartData
from pptx.enum.text import PP_ALIGN
from docx.enum.dml import MSO_THEME_COLOR
from pptx.dml.color import RGBColor
from openpyxl.utils.dataframe import dataframe_to_rows
import openpyxl,os,time
from openpyxl.utils import get_column_letter, column_index_from_string

RootPath = r"C:\Users\16930\Desktop\1112\W45周报"
backup_path =r"C:\Users\16930\Desktop\1112\W45周报\备份"
file_name="W45MS_Audit_Weekly_Report.pptx"
do_file_name = file_name[:25]+file_name[len(file_name)-5:len(file_name)]#文件名不包含日期，字符串为25个数字
# print(do_file_name)

#更新文件名称
back_file_name =do_file_name.replace(".pptx","_backup{}.pptx".format(time.strftime("_%Y_%m_%d_%H_%M", time.localtime())))
new_file_name  =do_file_name.replace(".pptx","{}.pptx".format(time.strftime("_%Y_%m_%d_%H_%M", time.localtime()))) 
pptx_path = os.path.join(RootPath,file_name)
pptx_path_back =os.path.join(backup_path,back_file_name)
new_pptx_path = os.path.join(RootPath,new_file_name)
exl_path =os.path.join(RootPath,"W45_过渡data_1113_0800 .xlsx")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#打开ppt，excel
print("opening file ....................")
# wb = openpyxl.load_workbook(exl_path,data_only=True,read_only = True)

#打开ppt
# prs = Presentation(pptx_path)
import win32api,win32con
# win32api.MessageBox(None,"Hello,pywin32!","pywin32",win32con.MB_OK)
import win32com.client.dynamic
import win32com.client
# Open PowerPoint
App = win32com.client.Dispatch("PowerPoint.Application")
# Presentation = Application.Presentation.Open(pptx_path)
# print(dir(Application.presentations.add))
App.Visible =True
Presentation= App.Presentations.Open(pptx_path)


slidenr = Presentation.Slides.Count    
print(slidenr)
slide = Presentation.slides(slidenr)

# shape1 = slide.Shapes.AddTextbox(Orientation=0x1,Left=100,Top=100,Width=100,Height=100)
# shape1.TextFrame.TextRange.Text='Hello, world'    


# prs = Application.presentations
# print(dir(Application.presentations))
# Add a presentation
# Presentation = Application.Presentations.Add()

# Add a slide with a blank layout (12 stands for blank layout)
Base = Presentation.Slides.Add(1, 11)


# Add an oval. Shape 9 is an oval.
oval = Base.Shapes.Addobject()
# Presentation.PresentationSave(new_file_name)