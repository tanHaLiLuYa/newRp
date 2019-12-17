from pptx import Presentation
from pptx.util import Inches, Cm, Pt
from pptx.chart.data import ChartData
from pptx.enum.text import PP_ALIGN
from docx.enum.dml import MSO_THEME_COLOR
from pptx.dml.color import RGBColor
from openpyxl.utils.dataframe import dataframe_to_rows
import openpyxl,os,time
from openpyxl.utils import get_column_letter, column_index_from_string
from pptx.enum.shapes import MSO_CONNECTOR,MSO_SHAPE
from pptx.enum.dml import MSO_LINE
RootPath = r"E:\work\samsung\W45周报"
backup_path =r"E:\work\samsung\W45周报\备份"
file_name="W45MS_Audit_Weekly_Report.pptx"
do_file_name = file_name[:25]+file_name[len(file_name)-5:len(file_name)]#文件名不包含日期，字符串为25个数字
# print(do_file_name)
back_file_name =do_file_name.replace(".pptx","_backup{}.pptx".format(time.strftime("_%Y_%m_%d_%H_%M", time.localtime())))
new_file_name  =do_file_name.replace(".pptx","{}.pptx".format(time.strftime("_%Y_%m_%d_%H_%M", time.localtime()))) 
pptx_path = os.path.join(RootPath,file_name)
pptx_path_back =os.path.join(backup_path,back_file_name)
new_pptx_path = os.path.join(RootPath,new_file_name)
exl_path =os.path.join(RootPath,"W45_过渡data_1111_1100 .xlsx")

# wb = openpyxl.load_workbook(exl_path,data_only=True,read_only = True)
# #打开ppt 
# prs = Presentation(pptx_path)
# page_name = prs.slides[2]

# line  = page_name.shapes.add_connector(MSO_CONNECTOR.StraightArrow, Cm(2), Cm(2), Cm(10), Cm(10))
# line.line.dash_style = MSO_LINE.SQUARE_DOT
# left = top = Inches(1)
# width = Inches(0.5)
# height = Inches(0.05)
# page_name.shapes.add_shape(
#     MSO_SHAPE.RIGHT_ARROW, left, top, width, height)
# print(dir(MSO_CONNECTOR))
# print(line.shape_type)
# for shape in page_name.shapes:
#         if shape.name == "up1":
#             shape.line.fill.background()
            # print(shape.follow_master_background)

            # print(dir(shape))
            # line.begin_connect(shape, 1)
#             # line.end_connect  (shape, 0)
#         if shape.name == "直接连接符 19":
#             line.end_connect(shape, 0)

            # print(dir((shape.add_connector())))
            # print(shape.shape_id) 
            # line = shape.add_connector(MSO_CONNECTOR.STRAIGHT,begin_)
dice_= {"12":12,"123":32,"32ew":14}
print(len(dice_))


# prs.save(new_pptx_path)