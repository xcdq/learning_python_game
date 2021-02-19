from tkinter import *
root = Tk()


def printkey(event):
    # event.showinfo("python",'hello')
    print('you', event.char)


def printRect(event):
    print('zuo')


def printRect2(event):
    print('you')


def printLine(event):
    print('line')


# cv = Canvas(root, bg="white")
# rt1 = cv.create_rectangle(10, 10, 110, 110, width=8, tags='r1')
# cv.tag_bind('r1', '<Button-1>', printRect)
# cv.tag_bind('r1', '<Button-3>', printRect2)
# cv.create_line(180, 70, 280, 70, width=10, tags='r2')
# cv.tag_bind('r2', '<Button-1>', printLine)
# cv.pack()
# root.mainloop()

root = Tk()
entry = Entry(root)
entry.bind('<KeyPress>', printkey)
entry.pack()
root.mainloop()
