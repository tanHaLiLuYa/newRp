'''请输入物流车的平面面积：
   请输入每个箱子平面面积的大小，用英文逗号间隔箱子面积：
   不能堆叠
   求最少需要多少物流车装？
'''
import re,math

class carNUmber():
    def __init__(self,carS,separator=","):
        self.carS = carS
        self.separator = separator
        self.m = r"(\d+\{})".format(separator)
        self.match =self.m + r"{4,100}\d+"#需要在分隔符前加上转义符\
    def inputStr(self):
        strOut = " "
        while not re.search(self.match,strOut):
            strOut = input("以英文逗号分隔输入")
        return re.search(self.match,strOut).group()#只返回匹配的字符串
    def splitStr(self,inStr):
        listOUt = inStr.split(self.separator)
        return listOUt
    # def minCarNums(self,listIN):
    #     totalS=0
    #     for i in listIN:
    #         totalS = totalS +int(i)
    #     return math.ceil(totalS/self.carS),totalS

    
    
      
    #主程序
    def run(self):
    #获取输入的数据，并转化为list
        dataBox = self.inputStr()
        dataList =self.splitStr(dataBox)

        
    '''思路 从全部箱子里面 取出 和=30的箱子 成组
        检查剩余的总和是否大于30 是 从全部箱子里取 和=29 整租
        重复第二行 知道剩余的总和小于30
    '''

if __name__ == '__main__':
    Q = carNUmber(carS=30)
    Q.run()
