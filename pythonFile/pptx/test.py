import win32com.client
import os ,time
import pptx
ppt_instance = win32com.client.Dispatch('PowerPoint.Application')

ppt_instance.Visible = True

prs = ppt_instance.Presentations.Open(r'E:\work\samsung\W48周报\test\W46MS_Audit_Weekly_Report_2019win32 - 副本.pptx')

s=prs.Slides(2)
for Shape in s.Shapes:
    if Shape.Name == "Picture Placeholder 10":
        s.Shapes.AddPicture(r'E:\work\samsung\W48周报\test\1575265620(1).jpg',LinkToFile=False,SaveWithDocument=True,\
                                        Left =100, Top =100)
    # print(Shape.Name)
# for sh in s.Shapes:
#     # print(sh.Name)
#     if sh.Name == "Object 69":
#         sh.ActionSettings(1).Hyperlink.Follow()
#         sh.OLEFormat.Doverb

#         sh.SaveAs(r'E:\work\samsung\W48周报\test\W46MS_Audit_Weekly_Report_20191122_1600.xlxs')
#         sh.Close()
        # print(sh.TextFrame.TextRange.Text,sh.TextFrame.TextRange.Font.Name)
        # sh.TextFrame.TextRange.Text="hahhhhhhhhsdafdfadsfddddddddddddddddddd__\n__ddddddddddddddddddddddddhhh"
        # print(sh.TextFrame.TextRange.Text,sh.TextFrame.TextRange.Font.Name)
        # print(type(sh.Chart.ChartData))
        # print(sh.Chart.ChartData.WorkBook)
        # print(sh.Chart)










# s.Delete()
# s.Copy()
# prs.Slides.Paste(Index = 4)
# for Slide in prs.Slides:

#     Slide.Shapes.AddPicture(r'E:\work\samsung\W48周报\test\1575265620(1).jpg',LinkToFile=False,SaveWithDocument=True,\
#                                         Left =100, Top =100)
    # Slide.Shapes.AddPicture(r'E:\work\samsung\W48周报\test\1575265620(1).jpg',LinkToFile=False,SaveWithDocument=True,\
    #                                     Left =100, Top =100)
    # Slide.Shapes.AddPicture(r'E:\work\samsung\W48周报\test\1575265620(1).jpg',LinkToFile=False,SaveWithDocument=True,\
    #                                     Left =100, Top =100)
    # Slide.Shapes.AddPicture(r'E:\work\samsung\W48周报\test\1575265620(1).jpg',LinkToFile=False,SaveWithDocument=True,\
    #                                     Left =100, Top =100)
    # Slide.Shapes.AddPicture(r'E:\work\samsung\W48周报\test\1575265620(1).jpg',LinkToFile=False,SaveWithDocument=True,\
    #                                     Left =100, Top =100)
prs.SaveAs(r'E:\work\samsung\W48周报\test\W46MS_Audit_Weekly_Report_201911111.pptx')

ppt_instance.Quit()

del ppt_instance





#
# for Slide in prs.Slides:
#     Slide.Shapes.AddPicture()
    #  for Shape in Slide.Shapes:
    #     #  print(Shape.name)
    #     if "Picture Placeholder" in Shape.name:
    #         Shape.AddPicture(r'E:\work\samsung\W48周报\my-image.jpg')
        # if Shape.TextFrame:
        #     Shape.TextFrame.TextRange.Font.Name = "Arial"

# prs.SaveAs(r'E:\work\samsung\W48周报\W46MS_Audit_Weekly_Report_2019_11_29_14_26.pptx')
# prs.Close()

#kills ppt_instance
