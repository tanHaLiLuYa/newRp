import pandas as pd
# 分表所依据的列
the_col = "执行人"
# 待拆分的Excel文件位置
file = r"/Users/simon/Desktop/libo_test/zoukj/W28抽样总库-zkj.xlsx"
# 拆分后的文件存放位置
save_dir = r"/Users/simon/_work/CBIC/custom/samsung/201907/excel_拆分/W28/"
# 读取待拆分的Excel文件
df = pd.read_excel(file)
# 获取拆分条件：去重
the_list = df[the_col].unique()
print(the_list)

xl = pd.ExcelFile(file)
print(xl.sheet_names)




# 按拆分条件分别保存新的Excel文件
for a in the_list:
    child_wb = df[df[the_col] == a]
    child_wb.to_excel(save_dir + a + '.xlsx', index=False)
print('拆分完成！')
