import pygame
import random

pygame.init()
FPS = pygame.time.Clock()
player = pygame.image.load("Player.png")
screen = pygame.display.set_mode((600, 800))
speed = random.randint(1, 5)
pygame.display.set_caption("CarsGame")
enemy = pygame.image.load("Enemy.png")

x = 290
y = 780
a = random.randint(40, 530)
b = 50
enemies = pygame.sprite.Group()
enemies.add(enemy)
sprites = pygame.sprite.Group()
sprites.add(player)
sprites.add(enemy)
don = False
while not don:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            don = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and x > 25 and x < 530:
        x -= 1
    if pressed[pygame.K_RIGHT] and x > 25 and x < 530:
        x += 1
    if pressed[pygame.K_LEFT] and x > 25 and x < 531:
        x -= 1
    if pressed[pygame.K_RIGHT] and x > 24 and x < 530:
        x += 1
    if b >= 800:
        b = 0
        speed = random.randint(1, 5)
        a = random.randint(40, 530)
    b += speed

    screen.fill((128, 128, 128))
    for i in range(50, 800, 260):
        pygame.draw.rect(screen, (255, 255, 255), (190, i, 25, 175))
        pygame.draw.rect(screen, (255, 255, 255), (380, i, 25, 175))
    pygame.draw.rect(screen, (255, 255, 0), (23, 0, 2, 800))
    pygame.draw.rect(screen, (255, 255, 0), (573, 0, 2, 800))
    screen.blit(player, (x, 700))
    screen.blit(enemy, (a, b))
    if pygame.sprite.spritecollideany(player, enemy):
        screen.fill((255, 0, 0))
    FPS.tick(60)
pygame.quit()