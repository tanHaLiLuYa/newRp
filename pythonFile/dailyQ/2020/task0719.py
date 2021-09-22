# 基督徒如何做选择
import tkinter
import tkinter.messagebox #弹窗库
from tkinter import *
top = Tk()
top.withdraw()


# A1 = input("你的选择圣经许可吗？\n（y/n?):")

# if "y" in A1:
#     A2 = input("你的选择良心许可吗？\n（y/n?):")
#     if "y" in A2:
#         B1, B2, B3 = input("对其他基督徒是否有好的影响？（爱比知识更重要）\n（y/n?):"), input(
#             "对非基督徒是否有好的影响？（福音比权利更重要）\n（y/n?):"), input("对自己的灵命有好的影响？（灵命健康比自由更重要）\n（y/n?):")
#         print("这些是自由的领域，但是上帝掌管一切，希望你能做出智慧的选择！！")
#     else:
#         print("请不要做这件事情，你的良心会被控告！")

# else:
#     print("请不要做这件事情，上帝不喜悦！")

# 弹窗界面
A1 = tkinter.messagebox.askyesno("圣经所要求","你的选择圣经许可吗？")

if A1:
    A2 =tkinter.messagebox.askyesno("良心所要求","你的选择良心许可吗？")
    if A2:
        tkinter.messagebox.showinfo('提示','下列这些问题是自由的领域，但是上帝掌管一切，希望你能做出智慧的选择！！！')
        tkinter.messagebox.askyesno("智慧之子的提示","对其他基督徒是否有好的影响？（爱比知识更重要）")
        tkinter.messagebox.askyesno("智慧之子的提示","对非基督徒是否有好的影响？（福音比权利更重要）")
        tkinter.messagebox.askyesno("智慧之子的提示","对自己的灵命有好的影响？（灵命健康比自由更重要）")
        tkinter.messagebox.showinfo("Blessing","May God bless you !")
    else:
        tkinter.messagebox.showwarning('警告','请不要做这件事情，你的良心会被控告！')
else:
    tkinter.messagebox.showwarning('警告','请不要做这件事情，上帝不喜悦！')



