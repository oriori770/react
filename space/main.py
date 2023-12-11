import pygame
import random


class Settings:
    screen_width = 1280
    screen_height = 720
    screen_size = (screen_width, screen_height)
    spaceship_speed = 30
    alien_speed = 2
    bullet_speed = -5
    Shot_frequency = 20
    # Create the game window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load('background.jpeg')


class Game:
    def __init__(self):
        self.space_ship = SpaceShip(Settings.spaceship_speed, (30, 60), 3)
        self.spaceship_lives = 3
        self.score = 0
        self.spaceship_shots_group = pygame.sprite.Group()
        self.alien_shots_group = pygame.sprite.Group()
        self.aliens_group = AliensGroup()
        self.font = pygame.font.Font(None, 40)
        self.font = self.font.render(f'score {self.score}', True, 'red')
        self.background = Object((0, 0), 'background.jpeg', size=Settings.screen_size)
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000

    def initialization(self):
        self.aliens_group.init_aliens_group(12, 7)

    def update(self):
        self.aliens_group.update()
        self.alien_shots_group.update()
        self.spaceship_shots_group.update()

    def draw(self):
        self.aliens_group.draw(Settings.screen)
        self.alien_shots_group.draw(Settings.screen)
        self.spaceship_shots_group.draw(Settings.screen)

    def key_space(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a shot from the spaceship
                self.spaceship_shots_group.add(
                    Shot(self.space_ship.rect.midtop, "bullet.png", Settings.bullet_speed, (20, 40)))

    def key_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and game.space_ship.rect.x > 0:
            self.space_ship.rect.x -= Settings.spaceship_speed * dt * 30
        if keys[pygame.K_RIGHT] and game.space_ship.rect.x < Settings.screen_width - 50:
            self.space_ship.rect.x += Settings.spaceship_speed * dt * 30

    def blit(self):
        Settings.screen.blit(self.space_ship.image, (self.space_ship.rect.x, self.space_ship.rect.y))
        Settings.screen.blit(self.font, (55, 20))

    def collisions(self):
        pygame.sprite.groupcollide(self.aliens_group.group, self.spaceship_shots_group, True, True)
        pygame.sprite.groupcollide(self.alien_shots_group, self.spaceship_shots_group, True, True)
        if pygame.sprite.spritecollide(self.space_ship, self.alien_shots_group, True):
            self.space_ship.live -= 1

    def alien_shot(self):
        if random.randint(1, Settings.Shot_frequency) == 1:
            self.alien_shots_group.add(
                Shot((random.choice(self.aliens_group.group.sprites()).rect.center), "bullet.png", 5, (15, 40)))

    # def victory_and_loss(self):
    #     if self.spaceship_lives > 0:
    #         if len(self.aliens_group) == 0:
    #             pass

    def run(self):
        self.key_move()
        self.draw()
        self.update()
        self.blit()
        self.collisions()
        # self.alien_shot()
        pygame.display.flip()
        self.aliens_group.alien_shot()
        self.dt
        # game.victory_and_loss()


class Object(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, img, speed=None, size: tuple = (50, 50)):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed


class SpaceShip(Object):
    def __init__(self, speed, size, live=3):
        super().__init__((Settings.screen_width // 2, Settings.screen_height - 50), "ship.bmp", speed, size)
        self.live = live


class Aliens(Object):
    def __init__(self, pos, speed=Settings.alien_speed, img="alien.bmp"):
        super().__init__(pos, img, speed)

    def sets_a_direction(self):
        for alien in game.aliens_group:
            if alien.rect.left < 0 or alien.rect.right > Settings.screen_width:
                self.speed *= -1
                self.rect.y += 10
                break

    def update(self, flip=False) -> None:
        if flip:
            self.speed *= -1
            self.rect.y += 10
        self.rect.x += self.speed

    def alien_shot(self):
        if random.randint(1, Settings.Shot_frequency) == 1:
            game.alien_shots_group.add(
                Shot((random.choice(game.aliens_group.group.sprites()).rect.center), "bullet.png", 5, (15, 40)))


class Shot(Object):
    def __int__(self, pos, img, speed, size: tuple = None):
        # self.image = pygame.image.load(img)
        # self.image = pygame.transform.scale(self.image, (7, 45))
        super().__int__(pos, img, speed, size)

    def update(self) -> None:
        self.rect.y += self.speed
        if not 0 < self.rect.centery < Settings.screen_height:
            self.kill()


class AliensGroup:
    def __init__(self):
        self.group = pygame.sprite.Group()

    def init_aliens_group(self, rows, columns):
        raw_distance = Settings.screen_height // (rows + 1) // 1.5
        col_distance = Settings.screen_width // (columns + 1)
        for raw in range(1, rows + 1):
            for col in range(1, columns + 1):
                self.group.add(Aliens((col * col_distance, raw * raw_distance)))

    def alien_shot(self):
        if random.randint(1, 40) == 5:
            # if 5 == 5:
            game.alien_shots_group.add(
                Shot((random.choice(game.aliens_group.group.sprites()).rect.center), "bullet.png", 5, (35, 50)))
            # self.alien_shots_group.add(Shot((55, 55), "bullet.png", 5, (35, 50)))

    def update(self):
        flip = False
        for alien in self.group.sprites():

            if alien.rect.left < 0 or alien.rect.right > Settings.screen_width:
                flip = True
                break
        self.group.update(flip)

    def draw(self, screen):
        self.group.draw(screen)


# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initial positions


# Game loop
running = True
clock = pygame.time.Clock()
game = Game()
game.initialization()
game.clock
while running:
    Settings.screen.blit(game.background.image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game.key_space()
    game.run()
    dt = clock.tick(60) / 1000
    game.dt

# Game over message
font = pygame.font.Font(None, 100)
game_over_text = font.render("good bye ", True, RED)
Settings.screen.blit(game_over_text, (Settings.screen_width // 2 - 150, Settings.screen_height // 2))
pygame.display.flip()

# Wait for a few seconds before exiting
pygame.time.delay(700)

# Quit Pygame
pygame.quit()
