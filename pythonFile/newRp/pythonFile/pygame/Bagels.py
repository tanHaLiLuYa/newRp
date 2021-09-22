import random
def game_info():
    print('欢迎来到数字推理游戏')
    print('系统会随机抽取三位不相同的数字')
    print('根据系统提示来推理出这3位数字')

def Double_choice(a,b,hint):
    '''双选择验证函数
    :param a 第一个选项值
    :param b 第二个选项值
    :param hint 选项信息
    :return 返回输入值'''
    choice=''
    while choice.lower() !=a and choice.lower() !=b:
        print(hint)
        choice=input()
    return choice
def number_limited(number):
    '''用户输入限制
    :param number 用户输入数字
    :return 返回用户输入数字'''
    #用户限制思路 检查必须是整数,限制3位数字,检查数字不能重复
    while True:
        if not number.isdigit():
            print('请输入整数数字')
        elif len(number)!=3:
            print('请输入三位数字')
        elif len(set(list(number)))!=3:
            print('三个数字不能重复')
        else:
            break
        number=input()
    return number
def random_number_list(count):
    '''随机抽取数字
    :param count 抽取数字的位数 最大不能超过10
    :return 返回随机抽取的3位不重复数字'''
    number_list=[]
    random_list=list(range(10))
    random.shuffle(random_list)#打乱顺序
    for i in range(count):
        random_number=random.choice(random_list)
        random_list.remove(random_number)
        number_list.append(str(random_number))
    return number_list
def judge_prompt(user_list,number_list):
    '''数字判断提示
    :param user_list 用户数字列表
    :param number_list 随机数字列表
    :return True 猜对了 False猜错了'''
    #判断思路,先判断都相等,有几个数字是数字和位置对的,没有的话查找数字对的,在没有的话就是都猜错了
    pico=0 #数字对了位置不对
    fermi=0 #位置数字对了
    if user_list==number_list:
        return True
    for i in range(len(user_list)):
        if user_list[i]==number_list[i]:
            fermi+=1
        elif user_list[i] in number_list:
            pico+=1
    if fermi:
        print('猜中了数字和位置(%d个)'%fermi)
    if pico:
        print('猜中了数字没有猜中位置(%d个)' % pico)
    if not fermi and not pico:
        print('没有一个数字和位置是对的')
    return False
def game_start():
    '''游戏判断核心'''
    number_list = random_number_list(count=3)
    count=9
    while count:
        print('猜猜看(%d次机会)'%count)
        user_number=number_limited(input())
        if judge_prompt(list(user_number),number_list):
            break
        count-=1
    if count==0:
        print('你输了,这个数字是%s'%''.join(number_list))
    else:
        print('玩家获胜,这个数字是%s'%''.join(number_list))

def game_shell():
    '''外壳程序'''
    game_info()  # 游戏开始提示
    game_start()
    while True:
        message='你想在玩一次吗(Y or N)'
        again_flag=Double_choice('y','n',message)
        if again_flag=='n':
            break
        game_start()

game_shell()