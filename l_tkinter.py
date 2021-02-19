# import tkinter
# win = tkinter.Tk()
# win.title('hello')
# win.geometry('800x600')  # 指定宽高
# win.minsize(200, 300)
# win.maxsize(1000, 800)
# win.mainloop()

# # pack
# root = tkinter.Tk()
# lable = tkinter.Label(root, text="hello,python")
# lable.pack()
# button1 = tkinter.Button(root, text='btn1')
# button2 = tkinter.Button(root, text='btn2')
# button1.pack(side=tkinter.LEFT)
# button2.pack(side=tkinter.RIGHT)
# root.mainloop()


# # grid
# from tkinter import *
# root = Tk()
# root.geometry('200x200+280+100')  # 280代表初始化时位置
# root.title("示例")
# L1 = Button(root, text='1', width=5, bg='yellow')
# L2 = Button(root, text='2', width=5)
# L3 = Button(root, text='3', width=5)
# L4 = Button(root, text='4', width=5)
# L5 = Button(root, text='5', width=5, bg='green')
# L6 = Button(root, text='6', width=5, bg='yellow')
# L7 = Button(root, text='7', width=5, bg='yellow')
# L8 = Button(root, text='8', width=5, bg='yellow')
# L9 = Button(root, text='9', width=5, bg='yellow')
# L0 = Button(root, text='0')
# Lp = Button(root, text='.')
# L1.grid(row=0, column=0)
# L2.grid(row=0, column=1)
# L3.grid(row=0, column=2)
# L4.grid(row=1, column=0)
# L5.grid(row=1, column=1)
# L6.grid(row=1, column=2)
# L7.grid(row=2, column=0)
# L8.grid(row=2, column=1)
# L9.grid(row=2, column=2)
# L0.grid(row=3, column=0, columnspan=2, sticky=E+W)
# Lp.grid(row=3, column=2, sticky=E+W)
# root.mainloop()

# # place
# from tkinter import *
# root = Tk()
# root.title("in")
# root['width'] = 200
# root['height'] = 80
# Label(root, text='name', width=6).place(x=1, y=1)
# Entry(root, width=20).place(x=45, y=1)
# Label(root, text='mim', width=6).place(x=1, y=20)
# Entry(root, width=20, show='*').place(x=45, y=20)
# Button(root, text='in', width=8).place(x=40, y=40)
# Button(root, text='not', width=8).place(x=110, y=40)
# root.mainloop()

# # entry
# from tkinter import *
# win = Tk()
# win.title("hello")
# lab1 = Label(win, text='hi', anchor='nw')
# lab1.pack()
# lab2=Label(win,bitmap='question')
# lab2.pack()
# bm=

from tkinter import *
import tkinter.font
root = Tk()
ft = tkinter.font.Font(family='Microsoft YaHei UI', size=20, weight='bold')
Label(root, text='hello', font=ft).grid()
root.mainloop()
# print(tkinter.font.families())
