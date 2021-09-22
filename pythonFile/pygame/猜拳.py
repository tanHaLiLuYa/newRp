import random


while True:
    # 1电脑从 石头剪刀布 里面选一个
    石头剪刀布 = ["石头", "剪刀", "布"]#列表 

    电脑的选择 = random.choice(石头剪刀布)

    # 2玩家从   选一个
    while True:
        玩家的选择 = input("请选择石头剪刀布：") 
        if 玩家的选择 in 石头剪刀布:    
            break
        print("请输入 石头 剪刀 布")

    if 玩家的选择 != 电脑的选择:
        if (玩家的选择 == "石头" and 电脑的选择 == "剪刀") or \
            (玩家的选择 == "剪刀" and 电脑的选择 == "布") or  \
                (玩家的选择 == "布" and 电脑的选择 == "石头"):
            print("玩家获胜 电脑的选择是：{}".format(电脑的选择))
        else:
            print("电脑获胜 电脑的选择是：{}".format(电脑的选择))
        break
    else:
        print("平局 电脑的选择也是：{}，请重新出拳！！！".format(电脑的选择))
