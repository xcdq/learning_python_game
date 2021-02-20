#答题
from tkinter.messagebox import *
from tkinter import *
import tkinter
from os import kill
import sqlite3
conn = sqlite3.connect('db/exam.db')
cursor = conn.cursor()
cursor.execute('delete from exam')
cursor.execute(
    'create table if not exists [exam] ([question] NULL,[answer_a] NULL,answer_b NULL,[answer_c] NULL,[answer_d] NULL,[right_answer] NULL)')
cursor.execute(
    'insert into exam (question,answer_a,answer_b,answer_c,answer_d,right_answer) values ("哈雷彗星周期","54","56","73","83","c")')
cursor.execute(
    'insert into exam (question,answer_a,answer_b,answer_c,answer_d,right_answer) values ("夜郎哪里","贵州","云南","广西","福建","a")')
cursor.execute(
    'insert into exam (question,answer_a,answer_b,answer_c,answer_d,right_answer) values ("发明麻药","孙思邈","华佗","张仲景","扁鹊","b")')
cursor.execute(
    'insert into exam (question,answer_a,answer_b,answer_c,answer_d,right_answer) values ("花旦","年轻男子","年轻女子","年长男子","年长女子","b")')
cursor.execute(
    'insert into exam (question,answer_a,answer_b,answer_c,answer_d,right_answer) values ("篮球比赛","4","5","6","7","b")')
print(cursor.rowcount)
cursor.execute('select * from exam')
res = cursor.fetchall()
for line in res:
    # for h in line:
    #     print(h,)
    print(line)
# cursor.close()
cursor.close()
conn.commit()
conn.close()

conn = sqlite3.connect('db/exam.db')
cur = conn.cursor()
cur.execute('select * from exam')
values = cur.fetchall()
cur.close()
conn.close()


def callNext():
    global k
    global score
    useranswer = r.get()
    print(r.get())
    if useranswer == values[k][5]:
        showinfo('yes', 'right')
        score += 10
    else:
        showinfo('遗憾', "错误了")
    k = k+1
    if k >= len(values):
        showinfo('tip', 'have null')
        return
    timu['text'] = values[k][0]
    radio1['text'] = values[k][1]
    radio2['text'] = values[k][2]
    radio3['text'] = values[k][3]
    radio4['text'] = values[k][4]
    r.set('e')


def callResult():
    showinfo('score', str(score))


root = tkinter.Tk()
root.title("问答")
root.geometry("500x200")
r = tkinter.StringVar()
r.set('e')
k = 0
score = 0
timu = tkinter.Label(root, text=values[k][0])
timu.pack()
f1 = Frame(root)
f1.pack()
radio1 = tkinter.Radiobutton(f1, variable=r, value='a', text=values[k][1])
radio1.pack()
radio2 = tkinter.Radiobutton(f1, variable=r, value='b', text=values[k][2])
radio2.pack()
radio3 = tkinter.Radiobutton(f1, variable=r, value='c', text=values[k][3])
radio3.pack()
radio4 = tkinter.Radiobutton(f1, variable=r, value='d', text=values[k][4])
radio4.pack()
f2 = Frame(root)
f2.pack()
Button(f2, text='下一题', command=callNext).pack(side=LEFT)
Button(f2, text='结 果', command=callResult).pack(side=LEFT)
root.mainloop()
