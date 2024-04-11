import pygame
import random
import time
from pygame.locals import *

pygame.init()  

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINSCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

pygame.mixer.Sound("background.wav").play()
background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("blue.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, "Yellow", (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect.center = check_col(E1)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.kill()

    def reset(self):
        self.rect.top = 0
        self.rect.center = check_col(E1)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("red.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

def check_col(enemy):
    x1, y1 = enemy.rect.topleft
    x2, y2 = enemy.rect.bottomright
    while True:
        x, y = (random.randint(20, SCREEN_WIDTH - 20), 0)
        if x < x1 or x > x2:
            return x, y

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN, 5000 // SPEED)

game_over_played = False  
while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
        if event.type == SPAWN:
            coin = Coin()
            coins.add(coin)
            coin.reset()
            all_sprites.add(coin)

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coinscore = font_small.render(str(COINSCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    x, y = coinscore.get_rect().topright
    DISPLAYSURF.blit(coinscore, (SCREEN_WIDTH - x - 10, y + 10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollideany(P1, enemies):
        if not game_over_played:
            pygame.mixer.Sound("crash.wav").play()
            game_over_played = True
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()

    if pygame.sprite.spritecollideany(P1, coins):
        s = pygame.sprite.spritecollide(P1, coins, False)
        for i in s:
            i.kill()
        COINSCORE += 1

    pygame.display.update()
    FramePerSec.tick(FPS)