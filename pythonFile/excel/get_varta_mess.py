# encoding: utf-8

import os
import re
import shutil
import piexif

pic_file_types = [".jpg", ".jpeg", ".png"]
source_path = r"G:\VARTA"
desc_path = r"G:\VARTA_VPZ_PIC"

def get_mess_id(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            if "空置" in f:
                fname = os.path.join(root,f)
                print(fname)


class Main():
    def __init__(self):
        get_mess_id(source_path)

if __name__ == '__main__':
    Main()
    # pass