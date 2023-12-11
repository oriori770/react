from game import Game
# from Setting import Settings
import pygame
import sys

pygame.font.init()
play = Game()
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
running = True
while running:
    play.presents('background', False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play.good_bye()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not play.game_started:
            # Check if the user clicked on the "start playing" text
            if play.text_rect.collidepoint(event.pos):
                play.game_started = True
        play.key_space(event)
    if not play.game_started:
        play.changes_colors()
    if play.game_started:
        play.run()
    dt = clock.tick(60) / 1000
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
