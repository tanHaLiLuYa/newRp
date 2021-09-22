
import time

# age =11

# while age<= 18:
#     print("你的年龄是{}岁 所以你不可以喝酒".format(age))
#     # time.sleep(1)
#     age = age +1
#     if age>=16:
#         print("你的年龄是{} 所以你可以喝酒".format(age ))
#         break
# print("执行完成")
# print("Hello Python")
# print("Hello Python")
# print("Hello Python")
# print("Hello Python")
# print("Hello Python")

# 计数 = 0

# while 计数<=4  :
#     print("Hello Python")
#     计数=计数+1


# 0. 定义最终结果的变量
# 结果 = 0

# # 1. 定义一个整数的变量记录循环的次数
# 计数 = 0

# # 2. 开始循环
# while 计数 <= 4:
#     # pr计数nt(计数)
#     print("Hello Python")
#     if 计数== 1:
#         结果 = 结果 +1
#     elif 计数 == 2:
#         结果 =结果 +2

#     # 处理计数器r
#     计数 = 计数 + 1

# print("0~5之间的数字求和结果 = {}".format(结果))

i = 0

while i < 10:

    # break 某一条件满足时，退出循环，不再执行后续重复的代码
    # i == 3
    if i == 3:
        i = i+1
        continue
    print(i)
    i += 1

print("over")