import tkinter as tk


# 第1步，实例化object，建立窗口window
windows = tk.Tk()

windows.title("番茄time")

windows.geometry('400x400')  # 长x宽


var = tk.StringVar()
#设置标签
test = tk.Label(windows,textvariable=var, bg='green',
                font=('Arial', 12), width=30, height=2)
test.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me \n ttt')
    else:
        on_hit = False
        var.set('')
#设置按钮
b = tk.Button(windows, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()
#放置标签
#test.place()

windows.mainloop()
