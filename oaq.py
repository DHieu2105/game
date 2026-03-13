board = [0] * 12
player1_score = 0
player2_score = 0

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

def move(pos, direction, player):

    global player1_score, player2_score


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


        # các trường hợp còn lại -> hết lượt
        else:
            break


def print_score():
    print("Điểm Player 1:", player1_score)
    print("Điểm Player 2:", player2_score)

def game():

    init_board()
    player = 1

    while True:

        print_board()
        print_score()

        pos = int(input(f"Player {player} chọn ô: "))
        direction = int(input("Hướng (1 phải, -1 trái): "))

        move(pos, direction,player)

        if player == 1:
            player =2
        else:
            player =1


game()