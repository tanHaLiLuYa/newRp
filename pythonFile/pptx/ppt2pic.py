import win32com.client
import os 


def ppt2png(filename,dst_filename):
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    #是否展示打开的文件
    #ppt.Visible = True
    #屏蔽错误弹框提示
    ppt.DisplayAlerts = False
    #打开ppt
    pptSel = ppt.Presentations.Open(filename)
    #把ppt另存为图片
    pptSel.SaveAs(dst_filename,17)
    ppt.Quit()

ppt_dir =r"E:\work\samsung\W48周报\备份"#PPT所在的一个文件夹


for fn in (filenames for filenames in os.listdir(ppt_dir) if filenames.endswith(('.ppt','.pptx'))):
  try:
 
    file_name = os.path.splitext(fn)[0]
    ppt2png(ppt_dir+"\\"+fn,ppt_dir+"\\"+file_name+".jpg")
 
  except:
      continue



# test

