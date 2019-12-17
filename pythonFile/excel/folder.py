#!/usr/bin/env python
# encoding: utf-8

import os
import csv
import sys
import datetime

def get_folder(rootDir, tier=2):
    if not isinstance(tier, int):
        pass
    else:
        list_dirs = os.walk(rootDir)
        rootDir_depth = rootDir[:].count(os.sep)
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(os.path.join(rootDir, f"{current_time}.csv"), "w+", newline="") as save_f:
            
            for root, dirs, files in list_dirs:
                for d in dirs:
                    fd = os.path.join(root, d)
                    fd_depth = fd[:].count(os.sep)
                    if fd_depth == rootDir_depth + tier:
                        row= fd.split(os.sep)[rootDir_depth+1:]
                        
                        writer.writerow(row)
            print(f"文件已写入---{rootDir}----目录中")

# the_root = "/Users/simon/_work/素材"
# # the_root = "G:\三星\w48"文件


if __name__ == "__main__":
    rootDir = str(sys.argv[1])
    tier = int(sys.argv[2])
    get_folder(rootDir, tier)
