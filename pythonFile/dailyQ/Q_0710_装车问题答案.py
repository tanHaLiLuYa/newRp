def car(s,many):
    #排序
    int_sort =sorted(many,reverse=True) 
    #计算车辆数量
    count=0
    #转化为文本列表
    str_sort =[str(i) for i in int_sort]
    while len(str_sort)>0:#str sort 列表未清空时：
        all=[]#创建 all 并每次清空all 列表
        m=len(str_sort)#判断当前 str sort 长度
        # i=0        
        for l in range(1,m):
            #每次从当前 str sort第一个元素为开始（一直在变），从第二个加 检查和是否等于s
            lin=[str_sort[0]]#记录0 num(也就是第一个元素)到 lin中
            sum=int(str_sort[0])
            sum+=int(str_sort[l])#sum为 l num 与0 num 之和

            #根据上面的sum与s的比较 分情况判断
            if sum==s:#等于 
                lin.append(str_sort[l])#记录l num到 lin中
                all.append([sum,lin])#记录lin到 all中
                sum=0#sum清0
                break     #推出当前for 循环           

            elif sum>s:#大于
                continue #退出本次l 循环,进入下次l+1 for循环
            elif sum<s:#小于
                lin.append(str_sort[l]) #记录l num到 lin中
                j=l+1
                while j<m:
                    sum+=int(str_sort[j])# sum 为 ：j num  与 l num 与0 num 之和
                    if sum>s:
                        sum-=int(str_sort[j])#sum去掉上一步操作，为 l num 与0 num 之和
                        j+=1
                        continue#退出本次j 循环,进入下次j+1 for循环
                    else:#sum<=s的时候
                        lin.append(str_sort[j])    #记录j num到 lin中                  
                        j+=1
                else:#当j >= m的时候，j为最后一个元素
                    all.append([sum,lin])      
        if len(all)>=1:
            all.sort(reverse=True)#根据all列表里面的列表的数字部分（也就是sum）按降序排序，
            print("第",count+1,"车，装载：",",".join(all[0][1]))#取第一个元素，为列表（即sum最大的）的第二个元素（即要求的组合），
            for item in all[0][1]:
                str_sort.remove(item) #删除已用求和的数据
        else:#未给all赋值，表明第一个num 等于或者很接近于 目的值 加上其他任何一个值 都大于S
            print("第",count+1,"车，装载：",str_sort[0])#取第一个元素
            str_sort.remove(str_sort[0])
            
        count+=1   
    #str_sort 元素清空，结束while循环，
    print('最少需要使用',count,'个平面面积为',s,'的物流车')


input_s=int(input("请输入物流车的平面面积：\n"))
input_m=input("请输入每个箱子平面面积的大小，用英文逗号间隔箱子平面面积：\n").split(",")
new=[int(i) for i in input_m]
car(input_s,new)


'''思路总结：复制输入列表
    降序
    当列表长度大于0：


'''
   

