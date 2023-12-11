from Setting import Settings
import random
import pygame


# from game import Game
class Object(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, img, speed=None, size: tuple = (50, 50)):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed


class SpaceShip(Object):
    def __init__(self, speed, size, live=3):
        super().__init__((Settings.screen_width // 2, Settings.screen_height - 50), "ship.bmp", speed, size)
        self.live = live


class BigAliens(Object):
    def __init__(self):
        super().__init__((Settings.screen_width, Settings.screen_height // 10), "ship.bmp", 5)
        self.life = False

    def update(self) -> None:
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()


class BigAlienGroup:
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.big_alien = BigAliens()

    def add_to_group(self):
        # if self.group.empty():
        if len(self.group) == 0 and random.randint(1, 100) == 1:
            self.big_alien = BigAliens()
            self.group.add(self.big_alien)


class Aliens(Object):
    def __init__(self, pos, speed=Settings.alien_speed, img="alien.bmp"):
        super().__init__(pos, img, speed)

    def update(self, flip=False) -> None:
        if flip:
            self.speed *= -1
            self.rect.y += 17
        self.rect.x += self.speed

    # def alien_shot(self):
    #     if random.randint(1, Settings.Shot_frequency) == 1:
    #         Game.alien_shots_group.add(
    #             Shot((random.choice(Game.aliens_group.group.sprites()).rect.center), "bullet.png", 5, (15, 40)))


class Shot(Object):
    def __init__(self, pos, img, speed, size: tuple = None):
        # self.image = pygame.image.load(img)
        # self.image = pygame.transform.scale(self.image, (7, 45))
        super().__init__(pos, img, speed, size)

    def update(self) -> None:
        self.rect.y += self.speed
        if not 0 < self.rect.centery < Settings.screen_height:
            self.kill()


class AliensGroup:
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.on_screen = True

    def init_aliens_group(self, rows, columns):
        raw_distance = Settings.screen_height // (rows + 1) // 1.5
        col_distance = Settings.screen_width // (columns + 1)
        for raw in range(1, rows + 1):
            for col in range(1, columns + 1):
                self.group.add(Aliens((col * col_distance, raw * raw_distance - 40)))

    # def alien_shot(self):
    #     if random.randint(1, 40) == 5:
    #         # if 5 == 5:
    #         Game.alien_shots_group.add(
    #             Shot((random.choice(Game.aliens_group.group.sprites()).rect.center), "bullet.png", 5, (35, 50)))
    #         # self.alien_shots_group.add(Shot((55, 55), "bullet.png", 5, (35, 50)))

    def update(self):
        flip = False
        for alien in self.group.sprites():
            if alien.rect.bottom > Settings.screen_height:
                self.on_screen = False
            if alien.rect.left < 0 or alien.rect.right > Settings.screen_width:
                flip = True
                break
        self.group.update(flip)

    def draw(self, screen):
        self.group.draw(screen)
