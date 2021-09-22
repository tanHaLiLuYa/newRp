import  six, copy
from pptx import Presentation
from pptx.util import Inches, Cm, Pt
from pptx.chart.data import ChartData
from pptx.enum.text import PP_ALIGN
from docx.enum.dml import MSO_THEME_COLOR
from pptx.dml.color import RGBColor
from openpyxl.utils.dataframe import dataframe_to_rows
import openpyxl,os,time
from openpyxl.utils import get_column_letter, column_index_from_string

RootPath = r"E:\work\samsung\W48周报\test"
backup_path =r"E:\work\samsung\W48周报\test\备份"
file_name="W46MS_Audit_Weekly_Report_2019win32 - 副本.pptx"
do_file_name = file_name[:25]+file_name[len(file_name)-5:len(file_name)]#文件名不包含日期，字符串为25个数字
# print(do_file_name)

#更新文件名称
back_file_name =do_file_name.replace(".pptx","_backup{}.pptx".format(time.strftime("_%Y_%m_%d_%H_%M", time.localtime())))
new_file_name  =do_file_name.replace(".pptx","{}.pptx".format(time.strftime("_%Y_%m_%d_%H_%M", time.localtime()))) 
pptx_path = os.path.join(RootPath,file_name)
pptx_path_back =os.path.join(backup_path,back_file_name)
new_pptx_path = os.path.join(RootPath,new_file_name)
# exl_path =os.path.join(RootPath,"W46_过渡data_1120_1120.xlsx")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#打开ppt，excel
print("opening file ....................")
prs = Presentation(pptx_path)
# wb = openpyxl.load_workbook(exl_path,data_only=True,read_only = True)

def get_shapeofrange(ishape):
    plot = ishape.chart.plots[0]
    row = len(plot.categories)+1
    col = len(plot.series)+1
    return [row,col]
def get_id_slide_bytitle(prs_=prs,title_name="标题 1"):
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
def get_data_chart(ishape):
    plot = ishape.chart.plots[0]
    series= iter(plot.series)
    list_out=[]
    for serie in plot.series:
        print(serie.values)
    
    # for i in range(1,14):
        # list_out.append(next(series).values)
    # for i in ishape.chart.series:
    #     print(i.name)
    return list_out
def get_maxrow_maxcol(table):
    row = table.rows
    col = table.columns
    return [len(row),len(col)]
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

def duplicate_slide(prs,ppt_title):
        template = prs.slides[get_id_slide_bytitle()[ppt_title]]
        try:
            blank_slide_layout = prs.slide_layouts[6]
        except:
            blank_slide_layout = prs.slide_layouts[len(prs.slide_layouts)]

        copied_slide = prs.slides.add_slide(blank_slide_layout)

        for shp in template.shapes:
            el = shp.element
            newel = copy.deepcopy(el)
            copied_slide.shapes._spTree.insert_element_before(newel, 'p:extLst')

        for _, value in six.iteritems(template.part.rels):
            # Make sure we don't copy a notesSlide relation as that won't exist
            if "notesSlide" not in value.reltype:
                copied_slide.part.rels.add_relationship(value.reltype,
                                                value._target,
                                                value.rId)

        return copied_slide

def copy_slide_from_external_prs(prs):
    
    # copy from external presentation all objects into the existing presentation
    external_pres = Presentation("PATH/TO/PRES/TO/IMPORT/from.pptx")

    # specify the slide you want to copy the contents from
    ext_slide = external_pres.slides[0]

    # Define the layout you want to use from your generated pptx
    SLD_LAYOUT = 5
    slide_layout = prs.slide_layouts[SLD_LAYOUT]

    # create now slide, to copy contents to 
    curr_slide = prs.slides.add_slide(slide_layout)

    # now copy contents from external slide, but do not copy slide properties
    # e.g. slide layouts, etc., because these would produce errors, as diplicate
    # entries might be generated

    for shp in ext_slide.shapes:
        el = shp.element
        newel = copy.deepcopy(el)
        curr_slide.shapes._spTree.insert_element_before(newel, 'p:extLst')

    return prs

ppt_title ="门店环境"
page_name = prs.slides[get_id_slide_bytitle()[ppt_title]]
#插入图片 每个shape插

for shape in page_name.shapes:
    if "Picture Placeholder" in shape.name:
        # print(shape.shape_type)
        pic = shape.insert_picture(r'E:\work\samsung\W48周报\test\1575265620(1).jpg')
        # print(pic.shape_type,pic.image)
        print(pic.image.filename,pic.image.blob)
        # pic.name = "1575265620(1).jpg"

       # pic.name="this is a pic"
# for shape in page_name.shapes:
#     print(shape.name,shape.shape_type)    
# 删除某一页空白shape,但不删掉slide
# for pl in page_name.shapes.placeholders:
#     if pl.has_text_frame and pl.text_frame.text == "":
#         print("found one blank %s" % pl)
#         sp=pl._sp
#         sp.getparent().remove(sp)
#slide插入图片
# page_name.shapes.add_picture(r'E:\work\samsung\W48周报\test\my-image.jpg',Inches(1), Inches(1))


# slide = prs.slides.add_slide(prs.slide_layouts[8])
# placeholder = slide.placeholders[1]
# picture = placeholder.insert_picture(r'E:\work\samsung\W48周报\test\my-image.jpg')
# print(placeholder.name)
prs.save(new_pptx_path)
