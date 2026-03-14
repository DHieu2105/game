import tkinter as tk

board = [0] * 12
player1_score = 0
player2_score = 0
player = 1
direction = 1   # tạm cho rải sang phải

def init_board():
    board[0] = 5
    board[6] = 5

    for i in range(1, 6):
        board[i] = 5
    for i in range(7, 12):
        board[i] = 5


def update_board():
    for i in range(12):
        buttons[i]["text"] = board[i]


def move(pos, direction, player):
    global player1_score, player2_score

    stones = board[pos]
    board[pos] = 0

    while True:

        while stones > 0:
            pos = (pos + direction) % 12
            board[pos] += 1
            stones -= 1

        next_pos = (pos + direction) % 12
        next_next = (pos + 2 * direction) % 12

        if board[next_pos] > 0 and next_pos not in [0, 6]:
            stones = board[next_pos]
            board[next_pos] = 0
            pos = next_pos
            continue

        if board[next_pos] == 0 and board[next_next] > 0:

            while board[next_pos] == 0 and board[next_next] > 0:

                eaten = board[next_next]

                if player == 1:
                    player1_score += eaten
                else:
                    player2_score += eaten

                board[next_next] = 0

                pos = next_next
                next_pos = (pos + direction) % 12
                next_next = (pos + 2 * direction) % 12

            break

        else:
            break


def click_cell(i):
    global player

    move(i, direction, player)

    update_board()

    if player == 1:
        player = 2
    else:
        player = 1


root = tk.Tk()
root.title("Game Ô Ăn Quan")

buttons = [None] * 12

# hàng trên
for i, col in zip(range(11, 6, -1), range(1, 6)):
    buttons[i] = tk.Button(root, width=6, height=3,
                           command=lambda x=i: click_cell(x))
    buttons[i].grid(row=0, column=col)

# quan trái
buttons[0] = tk.Button(root, width=6, height=3,
                       command=lambda: click_cell(0))
buttons[0].grid(row=1, column=0)

# quan phải
buttons[6] = tk.Button(root, width=6, height=3,
                       command=lambda: click_cell(6))
buttons[6].grid(row=1, column=6)

# hàng dưới
for i, col in zip(range(1, 6), range(1, 6)):
    buttons[i] = tk.Button(root, width=6, height=3,
                           command=lambda x=i: click_cell(x))
    buttons[i].grid(row=2, column=col)

init_board()
update_board()

root.mainloop()