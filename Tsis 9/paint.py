import pygame
import random
pygame.init()
pygame.font.init()
pygame.display.set_caption("Paint_Diasa")
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
width = 800
height = 600
density = 1
WidthOfRec = 50
HeihtOfRec = 50
RadiusOfCircle = 30
RadiusOfLineAndErase = 5
lastPos = (0,0)
screen = pygame.display.set_mode((width,height))
Rect = False
Circle =False
Erase = False
Line = True
def drawRect(screen, col, curpos, WidthOfRec, HeihtOfRec, density):
    x = curpos[0]
    y= curpos[1]
    pygame.draw.rect(screen,col,[x,y,WidthOfRec,HeihtOfRec], density)
def drawCircle(screen, col, curpos, RadiusOfCircle, density):
    x = curpos[0]
    y= curpos[1]
    pygame.draw.circle(screen,col, (x,y),RadiusOfCircle, density)
def drawLine(screen, col,start, end,Radius):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, col, (x, y), Radius)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, col, (x, y), Radius)
colors={
    'red': red,
    'green': green,
    'blue': blue,
}
mode = 'White'
painting = False
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.image.save(screen, 'paintDiasa.png')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'red'
            if event.key == pygame.K_b:
                mode = 'blue'
            if event.key == pygame.K_g:
                mode = 'green'
            if event.key == pygame.K_f:
                mode = 'randomColor'
            if event.key == pygame.K_1:
                Rect = False
                Circle =False
                Erase = False
                Line = True
            if event.key == pygame.K_2:
                Rect = True
                Circle =False
                Erase = False
                Line = False
            if event.key == pygame.K_3:
                Rect = False
                Circle =True
                Erase = False
                Line = False
            if event.key == pygame.K_4:
                Rect = False
                Circle =False
                Erase = True
                Line = False
            if event.key == pygame.K_UP:
                RadiusOfLineAndErase += 2
            if event.key == pygame.K_DOWN and RadiusOfLineAndErase>2:
                RadiusOfLineAndErase -= 2       
            if event.key == pygame.K_w:
                RadiusOfCircle += 2
                WidthOfRec += 2
            if event.key == pygame.K_s and RadiusOfCircle>2:
                RadiusOfCircle -= 2
                WidthOfRec -=2
            if event.key == pygame.K_p:
                HeihtOfRec += 2
            if event.key == pygame.K_m and HeihtOfRec>2:
                HeihtOfRec -= 2
            if event.key == pygame.K_d:
                density += 2
            if event.key == pygame.K_c and density>2:
                density -= 2
        if event.type == pygame.MOUSEBUTTONUP:
            curpos= pygame.mouse.get_pos()
            painting = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            painting = True
        if event.type == pygame.MOUSEMOTION and Line == True:
            if mode == 'White':
                color = (255,255,255)
            elif mode == 'randomColor':
                color = (random.randrange(256),random.randrange(256),random.randrange(256))
            else:
                color = colors[mode]
            if painting:
                drawLine(screen, color,lastPos,event.pos,RadiusOfLineAndErase)
            lastPos=event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and Rect == True:
            if mode == 'White':
                color = (255,255,255)
            elif mode == 'randomColor':
                color = (random.randrange(256),random.randrange(256),random.randrange(256))
            else:
                color = colors[mode]
            if painting:
                drawRect(screen,color, event.pos, WidthOfRec, HeihtOfRec,density)
            lastPos=event.pos
        if event.type == pygame.MOUSEMOTION and Erase == True:
            if painting:
                drawLine(screen, black,lastPos,event.pos,RadiusOfLineAndErase)
            lastPos=event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and Circle == True:
            if mode == 'White':
                color = (255,255,255)
            elif mode == 'randomColor':
                color = (random.randrange(256),random.randrange(256),random.randrange(256))
            else:
                color = colors[mode]
            if painting:
                drawCircle(screen, color, event.pos, RadiusOfCircle,density)
            lastPos=event.pos
    pygame.display.flip()