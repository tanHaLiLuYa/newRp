import os
import xlrd
import pandas as pd
import re

# 生成文件路径列表
def file_name(file_dir):
    list = []
    for file in os.listdir(file_dir):
        if os.path.splitext(file)[1] == '.xls' or os.path.splitext(file)[1] == '.xlsx':
            list.append(file)
    return list

#文件名称对应门店类别
dicFiles = {"Report_10370.xlsx": "有投资",
            "Report_10371.xlsx": "无投资"}


def headFun(ilist, dic1):
    matchPattern = r"[A-W]{1,2}[1-9]{1,3}.{0,1}[1-9]{0,1}[.]"
    # headPattern = r"【[\u4e00-\u9fa5]+】"
    newlist = []
    for i in ilist:
        t = i.replace("、", ".")
        for s in ["~"," ","  "]:
            t = t.replace(s, "")
        t = t.replace("?", "？")
        # t= re.sub(headPattern,"",t)
        if re.search(matchPattern, t):
            words = re.sub(matchPattern, "", t)
            if words not in dic1.keys():
                dic1[words] = re.search(matchPattern, t).group()
            newlist.append(dic1[words] + words)
        else:
            newlist.append(t)
    return newlist


def merge_xlsx(path, filenames, sheet_num, output_filename):
      # 定义一个空list
    contentList = []
    dicHead = {}
    # 分次记录数据到data ，放入contentlist中
    for i in range(len(filenames)):
        data = []
        read_xlsx = xlrd.open_workbook(path + "\\" + filenames[i])
        sheet_num_data = read_xlsx.sheets()[sheet_num]  # 查看指定sheet_num的数据
        title = sheet_num_data.row_values(0)  # 表头

        # 处理表头
        title = headFun(title, dicHead)

        for j in range(1, sheet_num_data.nrows):  # 逐行记录到 data
            data.append(sheet_num_data.row_values(j))
        
        content = pd.DataFrame(data)  # 转换为DF
        content.columns = title
        # content["类别"] = dicFiles[filenames[i]]
       
        # # 类别放在第一列
        # content_file = content["类别"]
        # content = content.drop("类别", axis=1)
        # content.insert(0, "类别", content_file)

        contentList.append(content)

    # 合并数据
    # print(contentList)
    df1 = pd.concat(contentList,sort= False)

    # 写入excel文件
    output_path = path + "\\" + 'output'
    output_filename_xlsx = output_filename + '.xlsx'
    if not os.path.exists(output_path):
        print("output folder not exist, create it")
        os.mkdir(output_path)
    df1.to_excel((output_path + "\\" + output_filename_xlsx),
                 header=True, index=False)
    print("merge success")


path = r'F:\oldComputer\work\2021年\09月\W38\test'
filenames = file_name(path)
print(filenames)
merge_xlsx(path, filenames, 0, "合并文件")  # 合并文件中第一个表的数据，输出到 output中  test
