import pygame


class Settings:
    screen_width = 1280
    screen_height = 720
    screen_size = (screen_width, screen_height)
    # Create the game window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load('background.jpeg')
    start_level = 0
    red_color = (230, 100, 78)
    green_color = (34, 255, 34)
    default_location = (0, 0)
    spaceship_speed = screen_width / 43
    alien_speed = screen_height / 360
    bullet_speed = -5
    Shot_frequency = 20
    space_ship_live = 20
    extra_lives_for_level_2 = 2
    ship_speed = screen_width / 50
    shot_frequency = 30
    bullet_speed_ship = screen_height / -90
    bullet_speed_alien = screen_height / 100
    amount_of_enemies_stage_1 = (4, 6)
    amount_of_enemies_stage_2 = (7, 8)
    ship_size = (30, 60)
    enemy_shot_size = (38, 38)
    big_enemy_shot_size = (50, 50)
    time_delay = 3500
