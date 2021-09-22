import hashlib

def md5(arg):
    md = hashlib.md5()
    md.update(bytes(arg, encoding='utf-8'))
    return md.hexdigest()

# a= "12,343t,yp"

# print(md(a))
def register(user,passwd):
#用户注册的时候把密码加密添加到文件
    with open("db", 'a') as f:
        tmp = "\n" + user + "|"+ md5(passwd)[-8:] +md5(passwd)[:24]
        f.write(tmp)
        return True
def login(user,passwd):
#用户登录时候认证
    with open('db','r') as f:
        for i in f:
            c = i.strip()
            s = c.split("|")
            passwdJ=md5(passwd)[-8:] +md5(passwd)[:24]
            if s[0]== user and s[1] == passwdJ:
                return True
sum = input("输入1登录 输入2注册：")
if sum == "1"or sum == "2":
    user = input("请输入账号:")
    passwd = input("请输入密码:")
    if sum =="1":
        if login(user,passwd):
            print("登录成功")
        else:
            print("登录失败")
    if sum =="2":
        if register(user,passwd):
            print("注册成功")
else:
    print("输入错误")