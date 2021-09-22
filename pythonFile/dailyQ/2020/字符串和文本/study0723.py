import re 

text = 'UPPER PYTHON, lower python, Mixed Python'

a = re.sub('python', 'snake', text, flags=re.IGNORECASE)

# print(a)
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
b =re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
# print(b)


import random as rd

# -----------被调用方----------------------------
def newRN(fn):  # 生成10个[0,1)之间小数
    print("开始执行")
    ns = []
    for i in range(10000):
        n = round(rd.random(), 2)
        ns.append(n)

    # 不用直接 return, 因为调用方 通知不接返回结果
    # 改成回调函数方式
    fn(ns)  # 调用是调用方函数，这一操作称之为回调


# ----------------调用方------------------------

# 定义回调函数
def abc(*args):
    # 进入到本函数内，意味着被调用方函数已执行完
    print('生成数据成功')
    print(args)
# newRN(abc)


