# encoding:utf-8
import operator
import os
import re
import sys
import csv
from tqdm import tqdm 
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.styles import Color, Font, colors
from openpyxl.utils import column_index_from_string, get_column_letter
import xlwings as xw
import pdb

def getArea(i,n=1,firstA="A",lastZ="V"):
    stringOut =f"{firstA}{n}:{lastZ}{i}"
    return stringOut

file_path = r"C:\Users\16930\Desktop\新建文件夹\照片\aim"
file_dirs = os.listdir(file_path)
from PIL import ImageGrab
app = xw.App(visible=True, add_book=False)

wbJoin = app.books.open(r"C:\Users\16930\Desktop\新建文件夹\照片\北京·河北.xlsx")
wsJoin = xw.sheets.active
# print(wsJoin.pictures.count)
# for pic in wsJoin.pictures:
# pic=wsJoin.pictures[2]
# print(dir((pic.api)))
# for pic in wsJoin.pictures:
#     # print(pic.name)
#     if pic.name == "Picture 1":
#         print("find this pic")
#         pic.api.Copy()
#         img=ImageGrab.grabclipboard()
#         img.save(r"C:\Users\16930\Desktop\新建文件夹\照片\pic.png")
#         pic.delete()
rngJoin =wsJoin.range("A3:U3")
for pic in wsJoin.pictures:
    print(pic.left)

# 
# pic.api.copy()
#

headArea = getArea(1)
headerListJoin=wsJoin.range(headArea ).value

# 遍历文件，读取数据
for file in file_dirs:
    wb = app.books.open(os.path.join(file_path, file))
    ws = xw.sheets.active
    #获取最大行/列
    rng =ws.range("A1").expand("table")#A1单元格必须非空
    # max_row =rng.rows.count
    max_row = rng.last_cell.row
    max_col  = rng.last_cell.column
    # maxColString = get_column_letter(max_col)
    # print(max_col,max_row)
    print(ws.pictures.count)
    #检查表头
    headerList=ws.range(headArea ).value
    if  not  operator.eq(headerListJoin,headerList):
        print("表头不对，请检查。。。。。。")
        continue
    print("表头核对成功。。。。。。")
    # for p in ws.pictures:
    #     print(p)
    # copyArea = ws.range(getArea(i=max_row,n=2)).value
    # maxRowJoin =wsJoin.range("A1").expand("table").last_cell.row
    # wsJoin.range("A"+str(maxRowJoin+1) ).expand('table').value=copyArea

    wb.save()
    wb.close()

wbJoin.save()
wbJoin.close()
app.quit()
