# encoding: utf-8
import sys
import os
import ffmpeg

file_types = [".mp4",".mov", ".avi", ".wmv", ".mkv", ".rmvb", ".3gp"]

def get_bit_rate(filename):
    try:
        return int(ffmpeg.probe(filename)["streams"][0]["bit_rate"])
    except:
        return 0

def compress_video(rootDir):
    list_dirs = os.walk(rootDir)

    for root, dirs, files in list_dirs:
        for f in files:
            fname = os.path.join(root, f)
            fname_ext = os.path.splitext(f)[1]
            new_fname = fname.replace(fname_ext, "_compressed.mp4")
            if fname_ext.lower() in file_types:
                print("找到一个文件", fname)
                print("=====================================")
                if "_compressed" in fname:
                    pass
                elif os.path.exists(new_fname):
                    print("该文件已转换过,但可能没转换成功========")
                    os.remove(new_fname)
                
                elif get_bit_rate(fname) >2500*1000:
                    try:
                        ffmpeg.input(fname).output(new_fname,video_bitrate = 2000*1000).run()
                        print("转换完毕\n=======================即将删除文件============================")
                        os.remove(fname)
                        print("------原文件删除完毕------")
                    except Exception as e:
                        print("可能有些错误发生",e)
                        
                    




class Main():
    def __init__(self):
        try:
            folder = sys.argv[1]
            compress_video(r"{}".format(folder))
        except Exception as e:
            print(e)
            
        


if __name__ == '__main__':
    Main()