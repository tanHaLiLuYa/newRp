# encoding: utf-8
from tqdm import tqdm
import PIL
import sys
import os
import openpyxl
import xlwings as xw
from openpyxl.drawing.image import Image

from tqdm import tqdm 

# 文件路径
excel_path = r"C:\Users\16930\Desktop\新建文件夹\照片\新建文件夹"
excel_new_path = r"C:\Users\16930\Desktop\新建文件夹\照片\aim"

# 照片路径
pic_dir = r"G:\导购员20190828"
pic_dirs = os.walk(pic_dir)
# 读取照片名称列表，字典
dic_ = {}
list_p_id = []
for root, dirs, files in pic_dirs:
    for f in files:
        dic_[f] = root
for key, value in dic_.items():
    list_p_id.append(key)


app = xw.App(visible=True, add_book=False)

for file in tqdm(os.listdir(excel_path)):
    
    # 打开excel，并获取最大行   
    wb = app.books.open(os.path.join(excel_path,file))
    ws = wb.sheets["Sheet1"]
    rng = ws.range("A1").expand("table")
    max_row = rng.rows.count
    rng.row_height =80
    # 写入照片，并在单元格内写入ID
    pic_id = 1
    for row in range(2, max_row+1):
        # ws.col(row).width
        id = str(ws.range(f"S{row}").value)+"__"+str(ws.range(f"T{row}").value)+"."
        for i in list_p_id:
            if id in i:
                pic_address = os.path.join(dic_[i], i)
                # print(id, os.path.join(dic_[i], i), pic_id)
                pic = ws.pictures.add(pic_address,
                                    left=ws.range(f"U{row}").left,
                                    top=ws.range(f"U{row}").top,
                                    width=80, height=80)
                pic.api.Placement = 1
                ws.range(f"U{row}").value = "Picture"+str(pic_id)
                ws.range(f"V{row}").value = i
                pic_id += 1
    wb.save(os.path.join(excel_new_path,file))
    wb.close()

app.quit()


if __name__ == '__main__':
    pass
