import pygame
import sys
from oaq import *

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ô Ăn Quan")

clock = pygame.time.Clock()

# ===== LOAD FONT =====
TITLE_FONT = pygame.font.Font("BeVietnamPro-Bold.ttf", 64)
BTN_FONT = pygame.font.Font("BeVietnamPro-SemiBold.ttf", 28)
SMALL_FONT = pygame.font.Font("BeVietnamPro-SemiBold.ttf", 20)
SCORE_FONT = pygame.font.Font("BeVietnamPro-Bold.ttf", 40)

# ===== COLOR =====
BG_TOP = (10, 10, 30)
BG_BOTTOM = (25, 25, 60)

NEON = (0, 200, 255)
NEON_HOVER = (0, 255, 255)
WHITE = (255, 255, 255)
DARK = (15, 15, 35)
GRAY = (120, 120, 140)
BLUE = (50, 100, 200)

# ===== BACKGROUND =====
def draw_bg():
    for y in range(HEIGHT):
        t = y / HEIGHT
        r = int(BG_TOP[0]*(1-t) + BG_BOTTOM[0]*t)
        g = int(BG_TOP[1]*(1-t) + BG_BOTTOM[1]*t)
        b = int(BG_TOP[2]*(1-t) + BG_BOTTOM[2]*t)
        pygame.draw.line(screen, (r,g,b), (0,y), (WIDTH,y))

# ===== BUTTON =====
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        mouse = pygame.mouse.get_pos()
        hover = self.rect.collidepoint(mouse)

        color = NEON_HOVER if hover else NEON

        # glow
        if hover:
            glow_rect = self.rect.inflate(20, 20)
            pygame.draw.rect(screen, color, glow_rect, border_radius=25)

        pygame.draw.rect(screen, DARK, self.rect, border_radius=20)
        pygame.draw.rect(screen, color, self.rect, 3, border_radius=20)

        txt = BTN_FONT.render(self.text, True, WHITE)
        screen.blit(txt, txt.get_rect(center=self.rect.center))

    def click(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# ===== CLOSE BUTTON =====
def draw_close():
    rect = pygame.Rect(WIDTH-50, 15, 35, 35)
    pygame.draw.rect(screen, (200,50,50), rect, border_radius=10)
    txt = BTN_FONT.render("X", True, WHITE)
    screen.blit(txt, txt.get_rect(center=rect.center))
    return rect

# ===== DRAW DOMINO WITH DOTS =====
def draw_domino(x, y, count, size=50):
    """Draw a domino with dot pattern showing stone count"""
    pygame.draw.rect(screen, GRAY, (x, y, size, size), border_radius=5)
    pygame.draw.rect(screen, WHITE, (x, y, size, size), 2, border_radius=5)
    
    # Draw dots pattern (1-6 dots arranged like dominos)
    dot_positions = {
        1: [(size//2, size//2)],
        2: [(size//3, size//3), (2*size//3, 2*size//3)],
        3: [(size//3, size//3), (size//2, size//2), (2*size//3, 2*size//3)],
        4: [(size//3, size//3), (2*size//3, size//3), (size//3, 2*size//3), (2*size//3, 2*size//3)],
        5: [(size//3, size//3), (2*size//3, size//3), (size//2, size//2), (size//3, 2*size//3), (2*size//3, 2*size//3)],
        6: [(size//3, size//3), (2*size//3, size//3), (size//3, size//2), (2*size//3, size//2), (size//3, 2*size//3), (2*size//3, 2*size//3)],
    }
    
    if count > 6:
        count = 6
    
    for dx, dy in dot_positions.get(count, []):
        pygame.draw.circle(screen, (50, 50, 50), (int(x + dx), int(y + dy)), 4)

# ===== DRAW PLAYERS =====
def draw_player_label(text, x, y):
    """Draw player name/label"""
    label = TITLE_FONT.render("●", True, BLUE)
    screen.blit(label, (x - 30, y - 25))
    txt = BTN_FONT.render(text, True, WHITE)
    rect = txt.get_rect(center=(x + 100, y))
    pygame.draw.rect(screen, BLUE, rect.inflate(20, 20), border_radius=15)
    screen.blit(txt, rect)

# ===== DRAW BOARD =====
def draw_game_board():
    """Draw the game board for Ô Ăn Quan"""
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    
    # ===== MAIN BOARD (OVAL) =====
    board_width = 850
    board_height = 280
    board_x = center_x - board_width//2
    board_y = center_y - board_height//2
    
    # Draw filled board
    pygame.draw.ellipse(screen, (80, 80, 100), (board_x, board_y, board_width, board_height))
    pygame.draw.ellipse(screen, WHITE, (board_x, board_y, board_width, board_height), 3)
    
    # ===== LEFT TREASURE (KHO A) =====
    treasure_width = 90
    treasure_height = 140
    treasury_a_x = 40
    treasury_a_y = center_y - treasure_height//2
    pygame.draw.ellipse(screen, (100, 100, 100), (treasury_a_x, treasury_a_y, treasure_width, treasure_height))
    pygame.draw.ellipse(screen, WHITE, (treasury_a_x, treasury_a_y, treasure_width, treasure_height), 2)
    
    # ===== RIGHT TREASURE (KHO B) =====
    treasury_b_x = WIDTH - 130
    pygame.draw.ellipse(screen, (100, 100, 100), (treasury_b_x, treasury_a_y, treasure_width, treasure_height))
    pygame.draw.ellipse(screen, WHITE, (treasury_b_x, treasury_a_y, treasure_width, treasure_height), 2)
    
    # ===== DRAW 10 CELLS (2 ROWS x 5 COLS) WITH DIVIDERS =====
    cell_width = board_width // 5
    cell_height = board_height // 2
    
    # Draw vertical dividers
    for col in range(1, 5):
        x = board_x + col * cell_width
        pygame.draw.line(screen, WHITE, (x, board_y), (x, board_y + board_height), 1)
    
    # Draw horizontal divider
    pygame.draw.line(screen, WHITE, (board_x, board_y + cell_height), (board_x + board_width, board_y + cell_height), 1)
    
    # ===== DRAW DOMINOES IN GRID =====
    # TOP ROW (5 dominoes)
    for col in range(5):
        x = board_x + col * cell_width + cell_width // 2
        y = board_y + cell_height // 2
        draw_domino(x - 20, y - 15, 5, size=55)
    
    # BOTTOM ROW (5 dominoes)
    for col in range(5):
        x = board_x + col * cell_width + cell_width // 2
        y = board_y + cell_height + cell_height // 2
        draw_domino(x - 20, y - 15, 5, size=55)
    
    # ===== SCORES =====
    # Top right score
    score_txt = BTN_FONT.render(str(player2_score), True, WHITE)
    screen.blit(score_txt, (WIDTH - 120, 50))
    label_txt = BTN_FONT.render("Người B", True, WHITE)
    screen.blit(label_txt, (WIDTH - 220, 20))
    
    # Bottom left score
    score_txt = BTN_FONT.render(str(player1_score), True, WHITE)
    screen.blit(score_txt, (40, HEIGHT - 80))
    label_txt = BTN_FONT.render("Người A", True, WHITE)
    screen.blit(label_txt, (40, HEIGHT - 120))

# ===== STATE =====
state = "start"

start_btn = Button("BẮT ĐẦU", 450, 380, 300, 90)
pvp_btn = Button("👤 Người vs Người", 150, 350, 400, 100)
ai_btn = Button("👤 Người vs Máy", 650, 350, 400, 100)
back_btn = Button("QUAY LẠI", 30, 600, 140, 50)

# ===== LOOP =====
while True:
    draw_bg()
    close_btn = draw_close()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if close_btn.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()

        if state == "start":
            if start_btn.click(event):
                state = "mode"

        elif state == "mode":
            if pvp_btn.click(event):
                state = "pvp"
                init_board()
            if ai_btn.click(event):
                state = "ai"
                init_board()

        elif state in ["pvp", "ai"]:
            if back_btn.click(event):
                state = "mode"

    # ===== DRAW =====
    if state == "start":
        title = TITLE_FONT.render("Ô ĂN QUAN", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 150)))
        start_btn.draw()

    elif state == "mode":
        title = TITLE_FONT.render("CHỌN CHẾ ĐỘ CHƠI", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 120)))
        pvp_btn.draw()
        ai_btn.draw()

    elif state == "pvp":
        draw_game_board()
        back_btn.draw()

    elif state == "ai":
        draw_game_board()
        back_btn.draw()

    pygame.display.flip()
    clock.tick(60)