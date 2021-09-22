import time 

t1 =time.time()
# print(t1)

#排序法
def Solution1(str1,str2):
    a = list(str1)
    b = list(str2)
    a.sort()
    b.sort()
    i = 0
    while i<len(a)  :
        if a[i] != b[i]:
            return False
        else:
            i = i +1
    return  True

# 暴力法

# import itertools
# def Solution(str1,str2):
#     a= list(str1)
#     totalList =[]
#     for i in itertools.permutations(str2,len(str2)):
#         totalList.append(list(i))
#     if a in totalList:
#         return True
#     else:
#         return False

#计数法
def Solution2(str1,str2):
    count1 = [0]*26
    count2 = [0]*26
    for i in str1:
        # print(ord(i))
        count1[ord(i)-ord("a")] +=1
    for i in str2:
        # print(ord(i))
        count2[ord(i)-ord("a")] +=1
    # return count1 , count2
    i = 0
    while i<len(count1):
        if count1[i] !=count2[i]:
            return False
        i += 1
    return True

# a = Solution1("frtrrrrrrrrrrrrrrrrsdfsasdfsadfadsedfraddsfg","frtrrrrrrrrrrerrrrrrrsdfsasdfsadfadsdfaddsfg")
a = Solution2("frtrrrrrrrrrrrrrrrrsdfrteeeeeeeertetetertooklsdsasdfsadfadsdrtfaddsfg","frtrrrrrrrrrrrrolkpwjkjkdfjksdjfkasjfksdrrrrsdfstrasdfsadfadsdfaddsfg")
print(a)
t2 = time.time()
print(t2-t1)
# t = time.time()-t1
# print(t)