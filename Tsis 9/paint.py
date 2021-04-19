import pygame
import random
pygame.init()
pygame.font.init()
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
randCol=(random.randrange(256),random.randrange(256),random.randrange(256))
black = (0,0,0)
width = 800
height = 600
density = 1
WidthOfRec = 30
HeihtOfRec = 30
Radius = 30
RadiusOfLine = 5
lastPos = (0,0)
screen = pygame.display.set_mode((width,height))
def drawRect(screen, col, x, y, WidthOfRec, HeihtOfRec, density):
    pygame.draw.rect(screen,col,[x,y,WidthOfRec,HeihtOfRec], density)
def drawCircle(screen, col, x, y, radius, density):
    pygame.draw.circle(screen,col, (x,y),radius, density)
def drawErase(screen, x, y,radius ):
    pygame.draw.circle(screen,black,(x,y),radius)
def drawLine(screen, col, lastPos, curPos,RadiusOfLine):
    pygame.draw.circle(screen,col,lastPos,curPos,RadiusOfLine)
color={
    'red': red,
    'green': green,
    'blue': blue,
    'random_color': randCol
}
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.draw.rect(screen,(100,100,100),(0,0,200,600))
    pygame.display.flip()