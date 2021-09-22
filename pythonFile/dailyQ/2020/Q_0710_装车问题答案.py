def car(s,many):
    i_sort =sorted(many,reverse=True) 
    count=0
    m_sort =[str(i) for i in i_sort]
    while len(m_sort)>0:
        all=[]
        m=len(m_sort)
        i=0        
        for l in range(1,m):
            lin=[m_sort[0]]
            sum=int(m_sort[0])
            sum+=int(m_sort[l])
            if sum==s:
                lin.append(m_sort[l])
                all.append([sum,lin])
                sum=0
                break                

            elif sum>s:
                continue
            lin.append(m_sort[l])
            j=l+1
            while j<m:
                sum+=int(m_sort[j])
                if sum>s:
                    sum-=int(m_sort[j])
                    j+=1
                    continue
                lin.append(m_sort[j])                     
                j+=1
            else:
                all.append([sum,lin])      
        if len(all)>=1:
            all.sort(reverse=True)
            print("第",count+1,"车，装载：",",".join(all[0][1]))
            for item in all[0][1]:
                m_sort.remove(item)
            all.clear()
        else:
            print("第",count+1,"车，装载：",m_sort[0])
            m_sort.remove(m_sort[0])
            
        count+=1   
    print('最少需要使用',count,'个平面面积为',s,'的物流车')
input_s=int(input("请输入物流车的平面面积：\n"))
input_m=input("请输入每个箱子平面面积的大小，用英文逗号间隔箱子平面面积：\n").split(",")
new=[int(i) for i in input_m]
car(input_s,new)
