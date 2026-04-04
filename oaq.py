import random
import math

# ===== GLOBAL STATE =====
board = [0] * 12
player1_score = 0
player2_score = 0
difficulty = 2

# ===== INIT =====
def init_board():
    for i in range(12):
        board[i] = 0
    board[0] = board[6] = 5
    for i in range(1, 6):
        board[i] = 5
    for i in range(7, 12):
        board[i] = 5

# ===== UTIL =====
def print_board():
    print("      ", *[board[i] for i in range(11, 6, -1)])
    print(board[0], "             ", board[6])
    print("      ", *[board[i] for i in range(1, 6)], "\n")


def check_empty_side(player):
    return all(board[i] == 0 for i in (range(1, 6) if player == 1 else range(7, 12)))


def refill(player):
    global player1_score, player2_score
    print(f"⚠️ Player {player} hết quân, rải lại (-5 điểm)")
    indices = range(1, 6) if player == 1 else range(7, 12)
    for i in indices:
        board[i] = 1
    if player == 1:
        player1_score -= 5
    else:
        player2_score -= 5


# ===== MOVE LOGIC =====
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

        # Continue picking
        if board[next_pos] > 0 and next_pos not in (0, 6):
            stones = board[next_pos]
            board[next_pos] = 0
            pos = next_pos
            continue

        # Capture
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


# ===== GAME STATE =====
def is_game_over():
    return board[0] == 0 and board[6] == 0


def final_score():
    global player1_score, player2_score
    for i in range(1, 6):
        player1_score += board[i]
        board[i] = 0
    for i in range(7, 12):
        player2_score += board[i]
        board[i] = 0


def evaluate():
    return player2_score - player1_score


# ===== STATE SAVE / RESTORE =====
def save_state():
    return board.copy(), player1_score, player2_score


def restore_state(state):
    global player1_score, player2_score
    b, p1, p2 = state
    board[:] = b
    player1_score = p1
    player2_score = p2


# ===== AI =====
def get_possible_moves(player):
    moves = []
    indices = range(7, 12) if player == 2 else range(1, 6)
    for i in indices:
        if board[i] > 0:
            moves.append((i, 1))
            moves.append((i, -1))
    return moves


def ai_move():
    # EASY
    if difficulty == 1:
        moves = get_possible_moves(2)
        return random.choice(moves) if moves else None

    # HARD (Minimax depth = 2)
    best_score = -math.inf
    best_move = None

    for move_ai in get_possible_moves(2):
        state_ai = save_state()
        move(*move_ai, 2)

        worst_case = math.inf

        for move_p in get_possible_moves(1):
            state_p = save_state()
            move(*move_p, 1)

            score = evaluate()
            worst_case = min(worst_case, score)

            restore_state(state_p)

        restore_state(state_ai)

        if worst_case > best_score:
            best_score = worst_case
            best_move = move_ai

    return best_move


# ===== MAIN GAME =====
def game():
    global difficulty, player1_score, player2_score

    init_board()
    player1_score = player2_score = 0

    player = 1

    mode = int(input("Chọn chế độ (1: PvP, 2: PvAI): "))
    if mode == 2:
        difficulty = int(input("Độ khó AI (1: Dễ, 2: Khó): "))

    while True:
        if is_game_over():
            final_score()
            print_board()
            print("Player 1:", player1_score)
            print("Player 2:", player2_score)
            break

        print_board()
        print("P1:", player1_score, "| P2:", player2_score)

        if check_empty_side(player):
            refill(player)

        if mode == 2 and player == 2:
            print("🤖 AI đang suy nghĩ...")
            move_ai = ai_move()
            if move_ai:
                move(*move_ai, 2)
        else:
            pos = int(input(f"Player {player} chọn ô: "))
            direction = int(input("Hướng (1 phải, -1 trái): "))
            move(pos, direction, player)

        player = 2 if player == 1 else 1


if __name__ == "__main__":
    game()
