import pygame
import math
pygame.init()
pygame.font.init()
black = (0, 0, 0)
screen = pygame.display.set_mode((1160, 800))
screen.fill((255, 255, 255))
pygame.draw.rect(screen, (0, 0, 0), (30, 10, 1112, 752), 3)
for i in range(26, 800, 90):
    pygame.draw.rect(screen, (0, 0, 0), (30, i, 1112, 1), 1)
    if i == 360 + 26:
        pygame.draw.rect(screen, (0, 0, 0), (30, i, 1112, 1), 3)
for i in range(46, 1160, 180):
    pygame.draw.rect(screen, (0, 0, 0), (i, 10, 1, 752), 1)
    if i == 540 + 30 + 16:
        pygame.draw.rect(screen, (0, 0, 0), (i, 10, 1, 752), 3)
pygame.draw.rect(screen, (255, 255, 255), (586 + 180, 27, 1, 88), 1)
for i in range(91, 1112, 45):
    if (i - 46) % 90 == 0:
        pygame.draw.rect(screen, (0, 0, 0), (i, 10, 1, 12), 1)
        pygame.draw.rect(screen, (0, 0, 0), (i, 752 - 2, 1, 12), 1)
    elif (i - 46) % 45 == 0:
        pygame.draw.rect(screen, (0, 0, 0), (i, 10, 1, 10), 1)
        pygame.draw.rect(screen, (0, 0, 0), (i, 752, 1, 10), 1)
for i in range(66, 1112, 45):
    pygame.draw.rect(screen, (0, 0, 0), (i, 10, 1, 8), 1)
    pygame.draw.rect(screen, (0, 0, 0), (i, 752 + 2, 1, 8), 1)
pygame.draw.rect(screen, (255, 255, 255), (586 + 180, 27, 1, 88), 1)
for i in range(71, 752, 45):
    pygame.draw.rect(screen, (0, 0, 0), (30, i, 12, 1), 1)
    pygame.draw.rect(screen, (0, 0, 0), (1130, i, 12, 1), 1)

for i in range(46, 752, 90):
    pygame.draw.rect(screen, (0, 0, 0), (30, i, 8, 1), 1)
    pygame.draw.rect(screen, (0, 0, 0), (1134, i, 8, 1), 1)
for i in range(96, 752, 90):
    pygame.draw.rect(screen, (0, 0, 0), (30, i, 8, 1), 1)
    pygame.draw.rect(screen, (0, 0, 0), (1134, i, 8, 1), 1)
height = 19
n = 1

font = pygame.font.SysFont('microsofttaile', 12)
for i in range(1, 10):
    tx = ''
    if n >= 0:
        tx += ' '
    else:
        tx = ''
    if str(n) == '0.5' or str(n) == '-0.5' or str(n) == '0.0' or str(n) == '-1.0':
        tx += str(n) + '0'
    elif n >= 0 and str(n) == 3:
        tx += str(n) + '0'
    elif len(str(n)) > 3:
        tx += str(n)
    else:
        tx += str(n) + '.00'

    txt = font.render(tx, True, (0, 0, 0), (255, 255, 255))
    screen.blit(txt, (0, height))
    height += 90
    n -= 0.25
width1 = 30+16+170 - 96
width2 = 40
a, b = -3, -5
font = pygame.font.SysFont('microsofttaile', 15)
for i in range(1, 7):
    if a == 0:
        tx1 = '0'
    else:
        tx1 = str(a) + 'n'
    if b > 0:
        tx2 = ' ' + str(b) + 'n/2'
    else:
        tx2 = str(b) + 'n/2'
    txt1 = font.render(tx1, True, (0, 0, 0), (255, 255, 255))
    screen.blit(txt1, (width2, 765))
    txt2 = font.render(tx2, True, (0, 0, 0), (255, 255, 255))
    screen.blit(txt2, (width1, 765))
    width1 += 180
    width2 += 180
    a += 1
    b += 2
txt3 = font.render('X', True, (0, 0, 0), (255, 255, 255))
screen.blit(txt3, (580, 780))
a = -3
font = pygame.font.SysFont('microsofttaile', 20)
width1 = 50
for i in range(1, 4):
    txt1 = font.render(str(a), True, (0, 0, 0), (255, 255, 255))
    screen.blit(txt1, (width1, 390))
    width1 += 180
    a += 1
font = pygame.font.SysFont('microsofttaile', 35)
for p in range(1, 2):
    tx1 = 'sin x'
    tx2 = 'cos x'
    txt1 = font.render(tx1, True, (0, 0, 0), (255, 255, 255))
    screen.blit(txt1, (706, 36))
    txt2 = font.render(tx2, True, (0, 0, 0), (255, 255, 255))
    screen.blit(txt2, (706, 70))
    pygame.draw.rect(screen, (255, 0, 0), (800, 60, 60, 1), 3)
    for i in range(0, 55, 35):
        pygame.draw.rect(screen, (0, 0, 255), (800+i, 93, 25, 1), 3)
c = 0
d = 0
for i in range(180, 1080+180):
    y = math.sin(i*math.pi/180) * 360
    if c != 0:
        d = y + 386 - c
        d = int(d)
        while d != 0:
            pygame.draw.rect(screen, (255, 0, 0), (46 + i - 180, y + 386+d, 1, 1), 1)
            pygame.draw.rect(screen, (255, 0, 0), (46 + i - 180, y + 386 + d+1, 1, 1), 1)
            pygame.draw.rect(screen, (255, 0, 0), (46 + i - 180, y + 386 + d - 1, 1, 1), 1)
            if d > 0:
                d -= 1
            else:
                d += 1
    pygame.draw.rect(screen, (255, 0, 0), (46+i-180, y + 386, 1, 1), 1)
    pygame.draw.rect(screen, (255, 0, 0), (46 + i - 180, y + 386-1, 1, 1), 1)
    pygame.draw.rect(screen, (255, 0, 0), (46 + i - 180, y + 386+1, 1, 1), 1)
    c = y + 386
c, d = 0, 0
i = 180
while i < 1080 + 180:
    x = math.cos(i*math.pi/180)*360
    if i % 10 != 0 and i % 5 == 0 and i > 180:
        i += 5
        continue
    pygame.draw.rect(screen, (0, 0, 255), (46+i-180, x+386, 1, 1), 1)
    pygame.draw.rect(screen, (0, 0, 255), (46 + i - 180, x + 386+1, 1, 1), 1)
    pygame.draw.rect(screen, (0, 0, 255), (46 + i - 180, x + 386-1, 1, 1), 1)
    pygame.draw.rect(screen, (0, 0, 255), (46 + i - 180, x + 386 + 2, 1, 1), 1)
    pygame.draw.rect(screen, (0, 0, 255), (46 + i - 180, x + 386 - 2, 1, 1), 1)
    pygame.draw.rect(screen, (0, 0, 255), (46 + i - 180, x + 386 + 3, 1, 1), 1)
    pygame.draw.rect(screen, (0, 0, 255), (46 + i - 180, x + 386 - 3, 1, 1), 1)
    i += 1
don = False
while not don:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            don = True
    pygame.display.flip()
pygame.quit()