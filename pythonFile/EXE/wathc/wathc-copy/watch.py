import time
import os
import sys

from playsound import playsound
import tkinter as tk


rest_min = 25#默认休息时间开始 为25分钟之后


def callback():
    global rest_min, loop
    if e.get()=="exit" :
        sys.exit()
    elif e.get().isdigit():
        rest_min = int(e.get())
    loop = False


soundFile = r'.\data\music.mp3'
for i in range(20):
    loop = True#防止意外退出 未点击输入时间
    while loop:
        master = tk.Tk()
        master.geometry('400x100')

        e = tk.Entry(master)
        e.pack()

        e.focus_set()  # 窗口锁定到输入框

        b = tk. Button(master, text="Enter time (min).\nEnter 'exit' to exit.", width=50, bg='gray',font=("Microsoft Yahei",12), command=callback)
        b.pack()

        # help_text = tk.Label(master,text="enter exit to exit")
        # help_text.pack()
        tk.mainloop()

    t = time.time()

    while time.time()-t <= rest_min*60:
        time.sleep(30)
    else:
        playsound(soundFile)
    i += 1
    # tk.mainloop()
    # print(i)

'''
获取时间信息 默认是25分钟

记录时间t1
记录时间t2
每隔30s检查时间是否开始休息

'''
