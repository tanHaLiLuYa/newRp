#创建text文件 并逐行写入
import os 

# ls =os.linesep#行的切换符号 适用于任何平台 Windows Unix
# print(ls)

class TextFlie:
    def __init__(self):
        self.fileName =input("please enter your file name:")
        

    def makeTextFlie(self):
        #检查filename 是否已存在
        
        #os.path.exists 处理异常
        # while True:
        #     if os.path.exists(self.fileName):
        #         print("Error: {} already exists".format(self.fileName))
        #     else:
        #         break
        #输入文本
        print("输入 quit 结束")
        allStrList =[]
        while True:
            entryStr = input("please enter your content:")
            if entryStr == "quit":
                break
            else:
                allStrList.append(entryStr)
        
        # print(["{}{}".format(x,ls) for x in allStrList])
        #写入text
        fileObj = open(self.fileName,"w")
        fileObj.writelines(["{}{}".format(x,"\n") for x in allStrList])
        fileObj.close()
        print("done......")

    def readTextFlie(self):
        fileObj = open(self.fileName,"r")   
        for l in fileObj:
            print(l)       
        fileObj.close()
if __name__ == '__main__':
    textf = TextFlie()
    textf.makeTextFlie()
    textf.readTextFlie()
