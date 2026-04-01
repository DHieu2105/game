import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ô Ăn Quan")

clock = pygame.time.Clock()

# ===== LOAD FONT =====
TITLE_FONT = pygame.font.Font("BeVietnamPro-Bold.ttf", 64)
BTN_FONT = pygame.font.Font("BeVietnamPro-SemiBold.ttf", 28)

# ===== COLOR =====
BG_TOP = (10, 10, 30)
BG_BOTTOM = (25, 25, 60)

NEON = (0, 200, 255)
NEON_HOVER = (0, 255, 255)
WHITE = (255, 255, 255)
DARK = (15, 15, 35)

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

# ===== STATE =====
state = "start"

start_btn = Button("BẮT ĐẦU", 350, 320, 200, 70)
pvp_btn = Button("NGƯỜI vs NGƯỜI", 280, 230, 340, 70)
ai_btn = Button("NGƯỜI vs MÁY", 280, 330, 340, 70)
back_btn = Button("QUAY LẠI", 30, 450, 140, 50)

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
            if ai_btn.click(event):
                state = "ai"

        elif state in ["pvp", "ai"]:
            if back_btn.click(event):
                state = "mode"

    # ===== DRAW =====
    if state == "start":
        title = TITLE_FONT.render("Ô ĂN QUAN", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 180)))
        start_btn.draw()

    elif state == "mode":
        title = TITLE_FONT.render("CHỌN CHẾ ĐỘ", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 120)))
        pvp_btn.draw()
        ai_btn.draw()

    elif state == "pvp":
        title = TITLE_FONT.render("CHẾ ĐỘ 2 NGƯỜI", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 200)))
        back_btn.draw()

    elif state == "ai":
        title = TITLE_FONT.render("CHẾ ĐỘ AI", True, WHITE)
        screen.blit(title, title.get_rect(center=(WIDTH//2, 200)))
        back_btn.draw()

    pygame.display.flip()
    clock.tick(60)