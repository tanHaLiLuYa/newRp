import tkinter as tk


# 第1步，实例化object，建立窗口window
window = tk.Tk()

window.title("番茄time")

window.geometry('400x400')  # 长x宽

var = tk.StringVar()
e1 =tk.Entry(window,textvariable=var,font=("Microsoft Yahei",14))
e1.place(x=100,y=100)
# e1.focus_set()
a = e1.get()

#放置标签   
#test.place()



window.mainloop()
# print(e1.get())

for i in range(10):
    print(a)