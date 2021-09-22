import random
class Solution():
    def __init__(self):
        self.nums = input("幸运数字：")
        self.letters = input("幸运字母：")
        self.lenth =int(input("密码长度："))
    def splitStr(self, Str):
        a, b, c, d, e, f = Str
        return[a, b, c, d, e, f]

    def run(self):
        # 拆分为列表 合并
        listC = self.splitStr(self.nums) + self.splitStr(self.letters)
        #随机选取元素 输出Str
        strOut=""
        for i in range(self.lenth):
            a = random.choice(listC)
            strOut +=a
        print(strOut)

if __name__ == '__main__':
    a =Solution()
    a.run()