import os
import zipfile
import shutil

root_path = r"/Users/simon/Desktop/991000042191-大理市/test"
back_path = os.path.join(root_path, "back")
dist_path = os.path.join(root_path, "dist")
print(f"root文件夹是{root_path}，\n back文件夹是{back_path},\n 输入文件夹是{dist_path}")



def livp2zip(f_path, back_path):
    f_name = f_path.split(os.sep)[-1]
    zip_file = f_path.replace(".livp", ".zip")
    print(f"文件名的路径是{f_path}，文件名是{f_name}")
    print(f"zip文件名为{zip_file}")
    os.rename(f_path, zip_file)
    # shutil.move(f_path, back_path)



def extract_zip(fname_zip, dist_path):
    myzip = zipfile.ZipFile(fname_zip)
    for f in myzip.namelist():
        if os.path.splitext(f)[-1].lower() in [".heic", ".jpg", ".jpeg"]:
            print(f)
            myzip.extract(f, dist_path)


def back_and_2zip(root,back_path):
    for root, dirs, files in os.walk(root):
        for f in files:

            if os.path.splitext(f)[-1] == ".livp":
                tmp_path = os.path.join(root, f)
                print(f"-------现在正在处理的文件为{tmp_path}")
                livp2zip(tmp_path,back_path)


def zip_to_dist(root,dist):
    for root, dirs, files in os.walk(root):
        for f in files:
            print(f)
            if os.path.splitext(f)[-1] == ".zip":
                zip_file = os.path.join(root,f)
                extract_zip(zip_file,dist)

# back_and_2zip(root_path, back_path)

zip_to_dist(root_path,dist_path)
