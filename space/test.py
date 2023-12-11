import pygame
import sys

# התחברות ל-Pygame
pygame.init()

# הגדרת צבעים
WHITE = (255, 255, 255)

# גודל החלון
width, height = 800, 600

# יצירת החלון
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("משחק עכבר")

# יצירת אובייקט ריבוע
rect_size = 50
rect_color = (0, 128, 255)
rect = pygame.Rect((width - rect_size) // 2, (height - rect_size) // 2, rect_size, rect_size)

# הגדרת מהירות הזזה
speed = 5

# לולאת המשחק
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # קבלת מיקום העכבר
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # הזזת הריבוע למיקום העכבר
    rect.x += (mouse_x - rect.x) // speed
    rect.y += (mouse_y - rect.y) // speed

    # ציור הריבוע
    screen.fill(WHITE)
    pygame.draw.rect(screen, rect_color, rect)

    # עדכון התצוגה
    pygame.display.flip()

    # השהייה קצרה
    pygame.time.Clock().tick(60)

# סיום התוכנית
pygame.quit()
sys.exit()
