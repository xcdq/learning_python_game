from tkinter import *
root = Tk()
# cv = Canvas(root, bg='white', width=300, height=120)
cv = Canvas(root, bg='white')
# cv.create_line(10, 10, 200, 80, width=2, dash=7)


# cv.create_rectangle(10, 10, 110, 110, tags=('r1', 'r2', 'r3'))
# cv.pack()
# cv.create_rectangle(20, 20, 80, 80, tags='r3')
# for item in cv.find_withtag('r3'):
#     cv.itemconfig(item, outline='blue')


cv.create_arc((10, 10, 110, 110),)
d = {1: PIESLICE, 2: CHORD, 3: ARC}
for i in d:
    cv.create_arc((10, 10+60*i, 110, 110+60*i), style=d[i])
    print(i, d[i])
cv.create_arc((150, 150, 250, 250), start=10, extent=120)
cv.pack()
root.mainloop()
