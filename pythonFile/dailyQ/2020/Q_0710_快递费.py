'''
某同城快递公司，快递物品按体积重量计算。
体积重量(kg)的计算方法为:长度(cm) x 宽度(cm) x 高度(cm) ÷6000，
如果计算的快递费用低于8元，按8元计算。请编写一个程序，帮助该快递公司根据输入的长度、宽度和高度自动计算快递费用。
'''
import re



class expressFee:
    def __init__(self,separator=","):
        self.separator = separator
        self.match =  r"\d+\{}\d+\{}\d+".format(separator,separator)#需要加上转意符
    
    def inputStr(self):
        strOut = " "
        while not re.search(self.match,strOut):
            strOut = input("长度(cm) 宽度(cm) 高度(cm)，以英文逗号分隔，不带单位：")
        return re.search(self.match,strOut).group()#只返回匹配的字符串
    def splitStr(self,inStr):
        a,b,c = inStr.split(self.separator)
        return int(a),int(b),int(c)
    def run(self):
        #获取输入字符串
        threeDStr = self.inputStr()
        #切割字符串
        length,width,height = self.splitStr(threeDStr)
 
        #计算邮费
        SumFee=length*width*height/6000
        if SumFee <=8:
            print(8)
        else:
            print(SumFee)

if __name__ == '__main__':
    expressF =expressFee()
    expressF.run()
