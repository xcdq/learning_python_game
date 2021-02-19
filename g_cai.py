import tkinter as tk
import sys
import random
import re
from tkinter.constants import END
from typing import Text
number = random.randint(0, 1024)
runing = True
num = 0
nmaxn = 1024
nminn = 0


def labelqval(vText):
    label_val_q.config(label_val_q, text=vText)


def eBtnGuess(event):
    global nmaxn
    global nminn
    global num
    global runing
    if runing:
        val_a = int(entry_a.get())
        if val_a == number:
            labelqval('yes')
            num += 1
            runing = False
            numGuess()
        elif val_a < number:
            if val_a > nminn:
                nminn = val_a
                num += 1
                labelqval("xiao"+str(nminn)+"~"+str(nmaxn))
        else:
            if val_a < nmaxn:
                nmaxn = val_a
                num += 1
                labelqval("dala"+str(nminn)+"~"+str(nmaxn))
    else:
        labelqval('already ok')
    entry_a.delete(0, END)


def numGuess():
    if num == 1:
        labelqval('very good')
    elif num < 10:
        labelqval('just ok '+str(num))
    else:
        labelqval('not bed '+str(num))


def eBtnClose(event):
    root.destroy()


root = tk.Tk(className='guess number')
root.geometry('300x60+200+200')
label_val_q = tk.Label(root, width='80')
label_val_q.pack()
entry_a = tk.Entry(root, width='30')
btnGuess = tk.Button(root, text='guess')
entry_a.pack(side=tk.LEFT)
entry_a.bind('<Return>', eBtnGuess)
btnGuess.bind('<Button-1>', eBtnGuess)
btnGuess.pack(side=tk.LEFT)

btnClose = tk.Button(root, text='exit')
btnClose.bind('<Button-1>', eBtnClose)
btnClose.pack(side=tk.LEFT)
labelqval('in: ')
entry_a.focus_set()
print(number)
root.mainloop()
