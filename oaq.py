import random

board = [0] * 12
player1_score = 0
player2_score = 0

def init_board():
    board[0] = 5
    board[6] = 5

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

def get_valid_move(player):
    while True:
        pos = int(input(f"Player {player} chọn ô: "))
        direction = int(input("Hướng (1 phải, -1 trái): "))

        if player == 1 and pos not in range(1,6):
            print("Player 1 chỉ được chọn ô từ 1 → 5")
            continue

        if player == 2 and pos not in range(7,12):
            print("Player 2 chỉ được chọn ô từ 7 → 11")
            continue

        if board[pos] == 0:
            print("Ô này không có quân, chọn lại")
            continue

        return pos, direction

def check_empty_side(player):
    if player == 1:
        return all(board[i] == 0 for i in range(1,6))
    else:
        return all(board[i] == 0 for i in range(7,12))

def refill(player):
    global player1_score, player2_score

    print(f"⚠️ Player {player} hết quân, rải lại (-5 điểm)")

    if player == 1:
        for i in range(1,6):
            board[i] = 1
        player1_score -= 5

    else:
        for i in range(7,12):
            board[i] = 1
        player2_score -= 5

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

        # bốc tiếp
        if board[next_pos] > 0 and next_pos not in [0, 6]:
            stones = board[next_pos]
            board[next_pos] = 0
            pos = next_pos
            continue

        # ăn quân
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

        else:
            break

def print_score():
    print("Điểm Player 1:", player1_score)
    print("Điểm Player 2:", player2_score)

def evaluate():
    return player2_score - player1_score

def ai_move():
    best_score = -9999
    best_move = None

    for i in range(7,12):
        if board[i] == 0:
            continue

        for direction in [1, -1]:

            # backup
            backup_board = board.copy()
            backup_p1 = player1_score
            backup_p2 = player2_score

            # AI đi
            move(i, direction, 2)

            # ===== giả lập người chơi phản công =====
            worst_case = 9999

            for j in range(1,6):
                if board[j] == 0:
                    continue

                for d in [1,-1]:

                    # backup lần 2
                    b2 = board.copy()
                    p1_2 = player1_score
                    p2_2 = player2_score

                    move(j, d, 1)

                    score = evaluate()
                    worst_case = min(worst_case, score)

                    # restore
                    for k in range(12):
                        board[k] = b2[k]
                    globals()['player1_score'] = p1_2
                    globals()['player2_score'] = p2_2

            # restore ban đầu
            for k in range(12):
                board[k] = backup_board[k]
            globals()['player1_score'] = backup_p1
            globals()['player2_score'] = backup_p2

            if worst_case > best_score:
                best_score = worst_case
                best_move = (i, direction)

    return best_move


def game():
    init_board()
    player = 1
    mode = int(input("Chọn chế độ (1: PvP, 2: PvAI): "))

    while True:

        print_board()
        print_score()

        # ===== kiểm tra hết quân =====
        if check_empty_side(player):
            refill(player)

        # ===== AI =====
        if mode == 2 and player == 2:
            print("🤖 AI đang suy nghĩ...")
            pos, direction = ai_move()
            print("AI chọn:", pos, "hướng", direction)
            move(pos, direction, 2)

        else:
            pos, direction = get_valid_move(player)
            move(pos, direction, player)

        player = 2 if player == 1 else 1


game()