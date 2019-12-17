# encoding:utf-8

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

def make_bread():
    pdb.set_trace()
    return "I don't have time"
file_path = r"E:\work\samsung\2018-W46-\19_1209波哥\导出原库"
file_dirs = os.listdir(file_path)

app = xw.App(visible=False, add_book=False)



#根据关键字获取列数
def getcloumn(listIn, strIn):
    for i in range(len(listIn)):
        if listIn[i]:
            if strIn in listIn[i]:
                return i

# 遍历文件，读取数据
for file in file_dirs:
    wb = app.books.open(os.path.join(file_path, file))
    ws = xw.sheets.active
    
    List_head = ws.range("A1:T1").value
    InterviwerCol = getcloumn(List_head, "访问员姓名和电话")
    
    DoFile=file[:7] if file[:2] =="20" else  (str(2019)+file[:3])
    
    #获取最大行
    rng =ws.range("A1").expand("table")
    max_row =rng.rows.count
    # 开始每行遍历
    for i in tqdm(range(2,max_row+1)):
        List_second = ws.range(f"A{i}:G{i}").value
        StoreIdCol = getcloumn(List_second, "CS0")
    
        StroeIdValue = ws.range(i,StoreIdCol+1).value
        InterviwerValue = ws.range(i,InterviwerCol+1).value

        if InterviwerValue:
            with open(os.path.join(r"E:\work\samsung\2018-W46-\19_1209波哥\新建文件夹","myfile.csv"),"a",newline='',encoding="utf-8") as f:
                row = [DoFile,StroeIdValue,InterviwerValue]
                for i in row :
                    f.write(i+"!")
                f.write("\n")
        
    print(f"{max_row}行数据已处理好",file)

    wb.save()
    wb.close()
app.quit()
