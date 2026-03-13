board = [0] * 12


def init_board():
    board[0] = 10
    board[6] = 10

    for i in range(1, 6):
        board[i] = 5
    for i in range(7, 12):
        board[i] = 5

def print_board():

    print("      ", end="")
    for i in range(11,6,-1):
        print(board[i], end=" ")
    print()

    print(board[0], "             ", board[6])

    print("      ", end="")
    for i in range(1,6):
        print(board[i], end=" ")
    print("\n")

def move(pos, direction):

    stones = board[pos]
    board[pos] = 0

    while True:

        # rải quân
        while stones > 0:
            pos = (pos + direction) % 12
            board[pos] += 1
            stones -= 1

        next_pos = (pos + direction) % 12
        next_next = (pos + 2 * direction) % 12

        # ô kế tiếp có quân -> bốc tiếp
        if board[next_pos] > 0 and next_pos not in [0, 6]:
            stones = board[next_pos]
            board[next_pos] = 0
            pos = next_pos
            continue

        # ô kế tiếp trống và ô sau có quân -> ăn
        if board[next_pos] == 0 and board[next_next] > 0:

            while board[next_pos] == 0 and board[next_next] > 0:
                print("Ăn", board[next_next], "quân ở ô", next_next)

                board[next_next] = 0

                pos = next_next
                next_pos = (pos + direction) % 12
                next_next = (pos + 2 * direction) % 12

            break

        # các trường hợp còn lại -> hết lượt
        else:
            break


def game():

    init_board()
    player = 1

    while True:

        print_board()

        pos = int(input(f"Player {player} chọn ô: "))
        direction = int(input("Hướng (1 phải, -1 trái): "))

        move(pos, direction)

        player = 3 - player


game()