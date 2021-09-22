from tkinter import *


loop = True
def callback():
    global a,loop
    if e.get()=="exit":
        exit()
    # global 
    a = e.get()
    loop =False

while loop:
    master = Tk()

    e = Entry(master)
    e.pack()

    e.focus_set()  # 窗口锁定到输入框
    b = Button(master, text="get", width=10, command=callback)
    b.pack()

    mainloop()

print(a)