import pygame, sys
import random, time
from pygame.locals import *
pygame.init()
FPS = pygame.time.Clock()
screen = pygame.display.set_mode((600, 800))
Speed = 5
pygame.display.set_caption("CarsGame")
money = 0
pygame.font.init()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center=(290, 750))
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.left > 25 and self.rect.right < 530:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect.left > 25 and self.rect.right < 530:
            self.rect.move_ip(5, 0)
        if pressed[pygame.K_LEFT] and self.rect.left > 25 and self.rect.right < 531:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect.left > 24 and self.rect.right < 530:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center=(random.randint(40, 530), 100))
        self.speed = random.randint(1, 5)
    def move(self):
        Speed = self.speed
        self.rect.top += Speed
        if self.rect.top >= 800:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 530), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center=(random.randint(40, 530), 100))
        self.speed = random.randint(1,5)
    def move(self):
        Speed = self.speed
        self.rect.top += Speed
        if self.rect.top >= 800:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 530), 0)
player = Player()
enemy = Enemy()
enemies = pygame.sprite.Group()
enemies.add(enemy)
coin = Coin()
coins = pygame.sprite.Group()
coins.add(coin)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)

don = False
while not don:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            don = True



    screen.fill((128, 128, 128))
    for i in range(50, 800, 260):
        pygame.draw.rect(screen, (255, 255, 255), (190, i, 25, 175))
        pygame.draw.rect(screen, (255, 255, 255), (380, i, 25, 175))
    pygame.draw.rect(screen, (255, 255, 0), (23, 0, 2, 800))
    pygame.draw.rect(screen, (255, 255, 0), (573, 0, 2, 800))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()


        # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill((255, 0, 0))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()

    if pygame.sprite.spritecollideany(player, coins):
        money += 1
        pygame.display.update()
        font = pygame.font.SysFont('microsofttaile', 12)
        txt = font.render(str(money), True, (255,255,255), (0,0,0))
        screen.blit(txt, (20, 20))

    pygame.display.update()
    FPS.tick(60)
