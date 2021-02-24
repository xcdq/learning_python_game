from tkinter import *
from tkinter.messagebox import *
import random
from PIL import Image, ImageTk
WIDTH = 312
HEIGHT = 450
IMAGE_WIDTH = WIDTH//3
IMAGE_HEIGHT = HEIGHT//3
ROWS = 3
COLS = 3
steps = 0
board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
root = Tk("拼图2021")
root.title('拼图')
Pics = []
for i in range(9):
    filename = 'images/girl_'+str(i)+".png"
    img = Image.open(filename)
    img = img.resize((104, 150))
    img = ImageTk.PhotoImage(img)
    # img = PhotoImage(img)
    # Canvas.scale(img, 100, 100)
    # pho = PhotoImage(file=filename)
    Pics.append(img)


class Square:
    def __init__(self, orderID):
        self.orderID = orderID

    def draw(self, canvas, board_pos):
        img = Pics[self.orderID]
        # pho = Canvas.scale(img, 100, 100)
        canvas.create_image(board_pos, image=img)


def play_game():
    global steps
    steps = 0
    init_board()


def init_board():
    L = list(range(9))
    random.shuffle(L)
    for i in range(ROWS):
        for j in range(COLS):
            idx = i*ROWS+j
            orderID = L[idx]
            if orderID is 8:
                board[i][j] = None
            else:
                board[i][j] = Square(orderID)


def drawBoard(canvas):
    canvas.create_polygon((0, 0, WIDTH, 0, WIDTH, HEIGHT,
                           0, HEIGHT), width=1, outline='Black')
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None:
                board[i][j].draw(
                    canvas, (IMAGE_WIDTH*(j+0.5), IMAGE_HEIGHT*(i+0.5)))


def mouseclick(pos):
    global steps
    r = int(pos.y//IMAGE_HEIGHT)
    c = int(pos.x//IMAGE_WIDTH)
    if r < 3 and c < 3:
        if board[r][c] is None:
            return
        else:
            current_square = board[r][c]
            if r-1 >= 0 and board[r-1][c] is None:
                board[r][c] = None
                board[r-1][c] = current_square
                steps += 1
            elif c + 1 <= 2 and board[r][c+1] is None:    # 判断右面
                board[r][c] = None
                board[r][c+1] = current_square
                steps += 1
            elif r + 1 <= 2 and board[r+1][c] is None:    # 判断下面
                board[r][c] = None
                board[r+1][c] = current_square
                steps += 1
            elif c - 1 >= 0 and board[r][c-1] is None:    # 判断左面
                board[r][c] = None
                board[r][c-1] = current_square
                steps += 1
            label1["text"] = str(steps)
            cv.delete('all')  # 清除canvas画布上的内容
            drawBoard(cv)
        if win():
            showinfo(title="恭喜", message="你成功了！")


def win():
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None and board[i][j].orderID != i * ROWS + j:
                return False
    return True


def callBack2():
    print("重新开始")
    play_game()
    cv.delete('all')  # 清除canvas画布上的内容
    drawBoard(cv)


cv = Canvas(root, bg='white', width=WIDTH, height=HEIGHT)
b1 = Button(root, text="重新开始", command=callBack2, width=20)
label1 = Label(root, text="0", fg="red", width=20)
label1.pack()
cv.bind("<Button-1>", mouseclick)

cv.pack()
b1.pack()
play_game()
drawBoard(cv)
root.mainloop()
