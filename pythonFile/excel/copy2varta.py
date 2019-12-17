# encoding: utf-8

import os
import re
import shutil
import piexif

pic_file_types = [".jpg", ".jpeg", ".png"]
source_path = r"G:\VARTA"
desc_path = r"G:\VARTA_VPZ_PIC"
mystr = "G:\VARTA\广东\VJ02003-广州双树富华东路店\VJ02003-广州双树富华东路店"
vpz_id_re = re.compile(r"V[JS](\d){5}-([\u4e00-\u9fa5])+")
m = vpz_id_re.search(mystr)
result = re.findall(vpz_id_re, mystr)
print(m.group(0))
def findId(foldername):
    id_re =  re.compile(r"V[JS](\d){5}-([\u4e00-\u9fa5])+")
    result = id_re.search(foldername)
    return result.group(0) if result else None


def copy2folder(source, desc):
    list_dirs = os.walk(source)
    for root, dirs, files in list_dirs:
        for f in files:
            if os.path.splitext(f)[1].lower() in pic_file_types:
                fname = os.path.join(root, f)
                if len(re.findall(vpz_id_re,fname))>=2 and "问卷" not in fname:
                    desc_fname = fname.replace(source, desc).replace(findId(fname),"",1)
                    desc_folder = desc_fname.replace(f, "")
                    # print(desc_folder)
                    try:
                        if not os.path.exists(desc_folder):
                            print("正在创建目录", desc_folder)
                            os.makedirs(desc_folder)
                        elif os.path.exists(desc_fname):
                            pass
                        else:
                            print("正在拷贝文件......", fname)
                            shutil.copy(fname, desc_fname)
                            print("拷贝完毕====================================")
                    except Exception as e:
                        print(e, fname, desc_fname)




def rm_exif(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            fname = os.path.join(root, f)
            if os.path.splitext(f)[1].lower() in pic_file_types:
                try:
                    print("即将删除照片exif信息======", fname)
                    piexif.remove(fname)
                except:
                    print("可能有点问题")
                print("删除完毕====================================")





class Main():
    def __init__(self):
        # copy2folder(source_path, desc_path)
        rm_exif(desc_path)

if __name__ == '__main__':
    Main()
    # pass