import pygame
import random
# import main
from Setting import Settings
import classs


class Game:
    def __init__(self):
        self.space_ship = classs.SpaceShip(Settings.spaceship_speed, Settings.ship_size, Settings.space_ship_live)
        self.spaceship_shots_group = pygame.sprite.Group()
        self.alien_shots_group = pygame.sprite.Group()
        self.aliens_group = classs.AliensGroup()
        self.shot = classs.Shot
        self.big_alien_group = classs.BigAlienGroup()
        self.big_alien = False
        self.font = pygame.font.Font(None, 40)
        self.win = classs.Object(Settings.default_location, 'win.jpeg', size=Settings.screen_size)
        self.game_over = classs.Object(Settings.default_location, 'game over.png', size=Settings.screen_size)
        self.background = classs.Object(Settings.default_location, 'background.jpeg', size=Settings.screen_size)
        self.dict = {'win': self.win, 'game_over': self.game_over, 'background': self.background}
        self.clock = pygame.time.Clock()
        self.color = Settings.red_color
        self.text_rect = ()
        self.dt = self.clock.tick(60) / 1000
        self.score = 0
        self.bullet_speed_alien = Settings.bullet_speed_alien
        self.bullet_speed_ship = Settings.bullet_speed_ship
        self.ship_speed = Settings.ship_speed
        self.level = Settings.start_level
        self.shot_frequency = Settings.shot_frequency
        self.game_started = False
        self.initialize = False

    def initialization(self, raw_col):
        raw, col = raw_col
        self.aliens_group.init_aliens_group(raw, col)

    def changes_colors(self):
        self.text_rect = self.draw_text("Start Playing", self.font, self.color, Settings.screen_width // 2,
                                        Settings.screen_height // 2)
        # Check for collision
        if self.text_rect.collidepoint(pygame.mouse.get_pos()):
            self.color = Settings.green_color  # Change color to green if there is a collision
        else:
            self.color = Settings.red_color  # Change color back to red if there is no collision

    def update(self):
        self.aliens_group.update()
        self.alien_shots_group.update()
        self.spaceship_shots_group.update()
        self.big_alien_group.group.update()

    def draw(self):
        self.aliens_group.draw(Settings.screen)
        self.alien_shots_group.draw(Settings.screen)
        self.spaceship_shots_group.draw(Settings.screen)
        self.big_alien_group.group.draw(Settings.screen)

    def key_space(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a shot from the spaceship
                self.spaceship_shots_group.add(
                    self.shot(self.space_ship.rect.midtop, "bullet.png", self.bullet_speed_ship, (20, 40)))

    def key_move(self):
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.space_ship.rect.x > 0:
            self.space_ship.rect.x -= Settings.spaceship_speed * self.dt * self.ship_speed
        if keys[pygame.K_RIGHT] and self.space_ship.rect.x < Settings.screen_width - 50:
            self.space_ship.rect.x += Settings.spaceship_speed * self.dt * self.ship_speed
        # self.space_ship.rect.center = (mouse_x, mouse_y)
        # if mouse_x > self.space_ship.rect.x:  # Move right
        #     self.space_ship.rect.x += 5
        # elif mouse_x < self.space_ship.rect.x:  # Move left
        #     self.space_ship.rect.x -= 5
        if click[0] == 1:
            self.spaceship_shots_group.add(
                self.shot(self.space_ship.rect.midtop, "bullet.png", self.bullet_speed_ship, (20, 40)))

    def blit(self):
        Settings.screen.blit(self.space_ship.image, (self.space_ship.rect.x, self.space_ship.rect.y))
        font_score = self.font.render(f'score {self.score}', True, 'red')
        font_life = self.font.render(f'live {self.space_ship.live}', True, 'red')
        Settings.screen.blit(font_score, (55, 20))
        Settings.screen.blit(font_life, (1100, 20))

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        Settings.screen.blit(text_surface, text_rect)
        return text_rect

    def collisions(self):
        if pygame.sprite.groupcollide(self.aliens_group.group, self.spaceship_shots_group, True, True):
            self.score += 10
        if pygame.sprite.groupcollide(self.alien_shots_group, self.spaceship_shots_group, True, True):
            self.score += 1
        if pygame.sprite.spritecollide(self.space_ship, self.alien_shots_group, True):
            self.space_ship.live -= 1
        if pygame.sprite.groupcollide(self.big_alien_group.group, self.spaceship_shots_group, True, True):
            self.score += 50
        if pygame.sprite.spritecollide(self.space_ship, self.aliens_group.group, False):
            self.you_loss()

    def alien_shot(self):
        if random.randint(1, self.shot_frequency) == 1 and len(self.aliens_group.group):
            self.alien_shots_group.add(
                self.shot((random.choice(self.aliens_group.group.sprites()).rect.center), "boom.png",
                          self.bullet_speed_alien, Settings.enemy_shot_size))
        if random.randint(1, 100) == 1 and len(self.big_alien_group.group) == 1:
            self.alien_shots_group.add(self.shot(self.big_alien_group.big_alien.rect.center, "bullet.png", 5, Settings.big_enemy_shot_size))

    def check_win(self):
        if self.space_ship.live == 0:
            self.you_loss()
        if len(self.aliens_group.group) < 1:
            if self.level == 2:
                self.you_win()
            else:
                self.level += 1
                self.updates_a_level()

    def updates_a_level(self):
        if self.level == 1:
            self.initialization(Settings.amount_of_enemies_stage_1)
            self.bullet_speed_alien = Settings.bullet_speed_alien
            self.bullet_speed_ship = Settings.bullet_speed_ship
            self.space_ship.live = Settings.space_ship_live
            self.ship_speed = Settings.ship_speed
            self.shot_frequency = Settings.shot_frequency
            self.big_alien = False
        if self.level == 2:
            self.restart_level()
            self.initialization(Settings.amount_of_enemies_stage_2)
            self.bullet_speed_alien = Settings.bullet_speed_alien + 2
            self.bullet_speed_ship = Settings.bullet_speed_ship
            self.space_ship.live += Settings.extra_lives_for_level_2
            self.ship_speed = Settings.ship_speed + 15
            self.shot_frequency = Settings.shot_frequency - 20
            self.big_alien = True

    def presents(self, img, flip):
        Settings.screen.blit(self.dict[img].image, Settings.default_location)
        if flip:
            pygame.display.flip()

    def you_win(self):
        self.presents('win', True)
        pygame.time.delay(Settings.time_delay)
        self.game_started = False
        self.restart_the_game()
        self.updates_a_level()

    def you_loss(self):
        self.presents('game_over', True)
        pygame.time.delay(Settings.time_delay)
        self.game_started = False
        self.restart_the_game()
        self.updates_a_level()

    def good_bye(self):
        pygame.font.init()
        font = pygame.font.Font(None, 100)
        game_over_text = font.render("good bye", True, 'red')
        Settings.screen.blit(game_over_text, (Settings.screen_width // 2 - 150, Settings.screen_height // 2))
        pygame.display.flip()

        # Wait for a few seconds before exiting
        pygame.time.delay(700)

    def run(self):
        self.check_win()
        if self.level < 3 and self.space_ship.live > 0:
            self.key_move()
            self.draw()
            self.update()
            if self.big_alien:
                self.big_alien_group.add_to_group()
            self.blit()
            self.collisions()
            self.alien_shot()
            pygame.display.flip()

    def restart_the_game(self):
        self.level = 0
        self.score = 0
        self.restart_level()
        self.aliens_group.on_screen = True

    def restart_level(self):
        self.spaceship_shots_group.empty()
        self.alien_shots_group.empty()
        self.aliens_group.group.empty()
        self.big_alien_group.group.empty()
