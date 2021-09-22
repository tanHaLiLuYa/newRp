# -*- coding:utf-8 -*-
print(" ===================快递费用计算====================")  # 输出软件标题
express = input(" 请输入快递物品的长度、宽度和高度（用英文逗号间隔）：\n").split(",")
if len(express) == 3:
    money = int(express[0]) * int(express[1]) * int(express[2]) / 6000
    if money >= 8:
        print("该物品的快递费用为", int(money), "元")  # 输出快递费用
    else:
        print(" 该物品的快递费用为8元")  # 输出最低快递费用
else:
    print("输入数据有误！！")
