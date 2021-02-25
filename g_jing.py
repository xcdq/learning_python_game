BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
# 全局变量
X = 'X'
O = 'O'
EMPTY = " "


def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def pieces():
    go_first = ask_yes_no('玩家是否先走 y/n : ')
    if go_first == 'y':
        print('\n玩家先走。')
        human = X
        computer = O
    else:
        print('\n机器人先走。')
        human = O
        computer = X
    return computer, human


def new_board():
    board = []
    for square in range(9):
        board.append(EMPTY)
    return board


def display_board(board):
    board2 = board[:]
    for i in range(len(board)):
        if board[i] == EMPTY:
            board2[i] = i
    print('\t', board2[0], '|', board2[1], '|', board2[2])
    print('\t', '---------')
    print('\t', board2[3], '|', board2[4], '|', board2[5])
    print('\t', '---------')
    print('\t', board2[6], '|', board2[7], '|', board2[8])
    # print('\t','----------')


def legal_moves(board):
    moves = []
    for square in range(9):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_num('你走哪个位置？ 0-8 : ', 0, 9)
        if move not in legal:
            print('\n已经下过')
    return move


def ask_num(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def computer_move(board, computer, human):
    board = board[:]
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print('1computer', move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print('2computer', move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print('3computer', move)
            return move


def winner(board):
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return 'TIE'
    return False
# def winner(board):
#     # 所有赢的可能情况，例如(0, 1, 2)就是第一行，(0, 4, 8), (2, 4, 6)就是对角线
#     # WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
#     #                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for row in WAYS_TO_WIN:
#         if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
#             winner = board[row[0]]
#             return winner  # 返回赢方
#     # 棋盘没有空位置
#     if EMPTY not in board:
#         return "TIE"  # "平局和棋，游戏结束"
#     return False


def main():
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    if the_winner == computer:
        print('computer win\n')
    elif the_winner == human:
        print('human win\n')
    elif the_winner == 'TIE':
        print('和局')


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


main()
input('按任意键退出')
