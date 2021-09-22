#!/usr/bin/env python
# encoding: utf-8

# Created by simon at 2018/11/11 10:13 PM

"""
@version: ??
@author: Fenghua Ye
@license: Apache Licence
@contact: wildplant@gmail.com
@site: http://www.fangworks.com
@software: PyCharm

问题描述：
-
-
-

"""

from pptx import Presentation
from pptx.util import Inches, Cm, Pt
from pptx.chart.data import ChartData
from pptx.enum.text import PP_ALIGN
import os,time
# from pptx.enum.shapes import MSO_SHAPE
#参数设置
para = {
    "week_num": "W43",
    "r_date": "19.10.20"
}
RootPath = r"E:\work\samsung\10月报\python 测试"
pptx_path = os.path.join(RootPath,"W37 MS_Audit_Weekly_Report.pptx")

new_path = os.path.join(RootPath,"{} MS_Audit_Weekly_Report{}.pptx".format(para["week_num"],para["r_date"]))
# print(new_path)
slide_layout_index = 1


#定义格式
# def PPT_format(font,):






prs = Presentation(pptx_path)
# layouts = prs.slide_layouts
# for l in layouts:
#     print(l)

# for i in range(len(prs.slides)):
#     s = prs.slides[i]
#     print(f"- --第{i}页-----，名称为--{s.name}, id为--{s.slide_id}")
# for shape in s.shapes:
#     print("--形状---", shape.name)
# slide_layout = prs.slide_layouts[slide_layout_index]
# slide = prs.slides.add_slide(slide_layout)
# print(prs.slides.index)
# for s in prs.slides:
#     print(s.slide_id, s.element)
# slide = prs.slide(2)
# shapes = slide.shapes
# left = top = width = height = Inches(3/2.54)
# shape = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
# fill = shape.fill
# print(fill.type)

# prs.save("test.pptx")


#设置字体格式函数,alig 参数不需要引号。
def setfont(myrange,fsize=9, fname="微软雅黑",alig = PP_ALIGN.CENTER):
    for paragraph in myrange.text_frame.paragraphs:
        paragraph.alignment = alig
        for run in paragraph.runs:
            run.font.size = Pt(fsize)
            run.font.name = fname



p0 = prs.slides[0]
# print(p0.shapes[1].text)
for shape in p0.shapes:
    if shape.has_text_frame:
        # print(shape.name)
        #     f"名称是{shape.name}, id是---{shape.shape_id}, 形状类型为{shape.shape_type}, 里面的文字是：{shape.text}")
        if shape.name == "title":
            text_frame = shape.text_frame
            new_title = shape.text.replace("W37", para["week_num"])#修改第一个参数！！！
            text_frame.clear()
            p = text_frame.paragraphs[0]
            run = p.add_run()
            run.text = new_title
            font = run.font
            font.name = '微软雅黑'
            font.size = Pt(40)
            font.bold = True
            font.italic = None
            print("{}修改成功 in P0>>>>>>>>".format(shape.name))
        elif shape.name == "date":
            text_frame = shape.text_frame

            # text_frame.clear()
            # p = text_frame.paragraphs[0]
            # run = p.add_run()
            # run.text = para["r_date"]
            # font = run.font
            # font.name = '微软雅黑'
            # font.size = Pt(24)
            # font.bold = False
            # font.italic = None
            # p = text_frame.paragraphs
            setfont(shape,10)
            print("{}修改成功 in P0>>>>>>>>".format(shape.name))






p1= prs.slides[1]
# print(p1.element)
for shape in p1.shapes:
    # print(shape.name)

    if shape.name == "执行明细说明-表格":
        # print(shape.shape_type, shape.shape_id)
        # print(shape.table.last_row)
        # shape.table.apply_style(2)
        for r in range(1, 21):
            c = shape.table.cell(r, 3)
            c.text="我是谁"
            setfont(c,10,)
            
            # shape.table.cell(r, 3).text_frame.paragraphs.runs.font.name = "Microsoft YaHei Light"

            
            # shape.table.apply_style(2)
            
        # for cell in iter_cells(shape.table):
        #     for paragraph in cell.text_frame.paragraphs:
        #         for run in paragraph.runs:
        #             run.font.size = Pt(12)
        #             font.name = "Microsoft YaHei Light"
        print("{}修改成功 in P1>>>>>>>>".format(shape.name))
# p2= prs.slides[2]
# # print(p1.element)
# for shape in p2.shapes:
#     # print(shape.name)

#     if shape.name == "图表 21":
#         # print(shape.shape_type, shape.shape_id)
#         # print(shape.table.last_row)
#         # shape.table.apply_style(2)
#         shape.ChartData.categories=['A', 'B', 'C', 'D','E','F',"G"]
            
  






prs.save(new_path)
if __name__ == "__main__":
    pass