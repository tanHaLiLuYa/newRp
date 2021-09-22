import time
# import os
import sys

from playsound import playsound
import tkinter as tk


rest_min = 25  # 默认休息时间开始 为25分钟之后


def callback():
    global rest_min, loop
    if e.get() == "exit":
        sys.exit()
    elif e.get().isdigit():
        rest_min = int(e.get())
    loop = False


def timestart():
    global start
    if e.get() == "exit":
        sys.exit()
    else:
        start=True


soundFile = 'music.mp3'
for i in range(20):
    loop = True  # 防止意外退出 未点击输入时间
    start = False
    while loop:
        master = tk.Tk()
        master.title("tomato time .tp")
        master.iconbitmap("tomato.ico")
        master.geometry('400x120')

        e = tk.Entry(master, font=("Microsoft Yahei", 12))
        e.pack()

        e.focus_set()  # 窗口锁定到输入框

        b = tk. Button(master, text="输入时间/exit", bg='gray',
                       font=("Microsoft Yahei", 12), command=callback)
        b.pack(side="left")

        startbutton = tk.Button(master=master,text="开始/结束", bg='gray', font=(
            "Microsoft Yahei", 12), command=timestart)
        startbutton.pack(side="right")
        if start:
            t = time.time()
            while time.time()-t <= rest_min*60:
                time.sleep(30)
            else:
                playsound(soundFile)
        tk.mainloop()

    # tk.mainloop()
    # print(i)

'''
获取时间信息 默认是25分钟

记录时间t1
记录时间t2
每隔30s检查时间是否开始休息

'''
