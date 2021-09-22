from scipy import stats
import pandas as pd 
import os

os.chdir(r"D:\github\pythonFile\统计")


df = pd.read_excel("相关性研究.xlsx",sheet_name="检查方差齐性 与正态分布")

# print(df["三年级"])


# print(stats.kstest(df['三年级'], 'norm')[1])
# print(stats.anderson(df["三年级"],"norm"))
# print(stats.normaltest(df["三年级"]))

print(stats.bartlett(df["一年级"],df["二年级"],df["三年级"]))