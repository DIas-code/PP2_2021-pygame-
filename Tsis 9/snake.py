import pygame
import random
import time
import json
pygame.init()
lev1=False
lev2=False
cnt=0
cnt2=0
screen = pygame.display.set_mode((700, 700))
pygame.font.init()
font = pygame.font.SysFont('microsofttaile', 72)
txt = font.render("Easy mode", True, (0, 0, 0), (255, 255, 255))
screen.blit(txt, (160, 275))
pygame.display.update()
time.sleep(2)
class Food:
    def __init__(self):
        self.x = random.randrange(30, 680, 20)
        self.y = random.randrange(30, 680, 20)
    def nextPos(self):
        self.x = random.randrange(30, 680, 20)
        self.y = random.randrange(30, 680, 20)
    def draw(self):
        pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 10)    
    
class Snake():
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x,y]]
        self.side = (20,20)
        self.dx = 20
        self.dy = 0
        self.speed = 5
        self.is_add = False
    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, (255,0,0),(element,self.side))
    
    def add_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy   
    
    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
            return True
        return False
    def death(self):
        x = self.elements[0][0]
        y = self.elements[0][1]
        snake1pos=(x,y)
        if x < 19 or x > 679 or y < 19 or y > 679:
            font = pygame.font.SysFont('microsofttaile', 72)
            txt = font.render("Snake 2 win", True, (0, 0, 0), (255, 255, 255))
            screen.fill((255,255,255))
            screen.blit(txt, (160, 275))
            pygame.display.update()
            time.sleep(2)
            exit()
        for i in range(self.size - 1, 0, -1):
            if self.elements[0][0] == self.elements[i][0] and self.elements[0][1] == self.elements[i][1]:
                font = pygame.font.SysFont('microsofttaile', 72)
                txt = font.render("Snake 2 win", True, (0, 0, 0), (255, 255, 255))
                screen.fill((255,255,255))
                screen.blit(txt, (160, 275))
                pygame.display.update()
                time.sleep(2)
                exit()
        if lev1 == True:
            rec1=pygame.draw.rect(screen,(100,100,100), (140,140, 20,20))
            rec2=pygame.draw.rect(screen,(100,100,100), (540,140, 20,20))
            rec3=pygame.draw.rect(screen,(100,100,100), (140,540, 20,20))
            rec4=pygame.draw.rect(screen,(100,100,100), (540,540, 20,20))
            if rec1.collidepoint(snake1pos) or rec2.collidepoint(snake1pos) or rec3.collidepoint(snake1pos) or rec4.collidepoint(snake1pos):
                font = pygame.font.SysFont('microsofttaile', 72)
                txt = font.render("Snake 2 win", True, (0, 0, 0), (255, 255, 255))
                screen.fill((255,255,255))
                screen.blit(txt, (160, 275))
                pygame.display.update()
                time.sleep(2) 
                exit()

        if lev2 == True:
            rect1=pygame.draw.rect(screen,(100,100,100), (240,240, 20,20))
            rect2=pygame.draw.rect(screen,(100,100,100), (440,240, 20,20))
            rect3=pygame.draw.rect(screen,(100,100,100), (240,440, 20,20))
            rect4=pygame.draw.rect(screen,(100,100,100), (440,440, 20,20))
            if rect1.collidepoint(snake1pos) or rect2.collidepoint(snake1pos) or rect3.collidepoint(snake1pos) or rect4.collidepoint(snake1pos):
                font = pygame.font.SysFont('microsofttaile', 72)
                txt = font.render("Snake 2 win", True, (0, 0, 0), (255, 255, 255))
                screen.fill((255,255,255))
                screen.blit(txt, (160, 275))
                pygame.display.update()
                time.sleep(2) 
                exit()

class Snake2():
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x,y]]
        self.side = (20,20)
        self.dx = 0
        self.dy = 20
        self.speed = 5
        self.is_add = False
    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, (0,0,255),(element,self.side))
    
    def add_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy   
    
    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if foodx <= x <= foodx + 10 and foody <= y <= foody + 10:
            return True
        return False
    def death(self):
        x = self.elements[0][0]
        y = self.elements[0][1]
        snake2pos=(x,y)
        if x < 19 or x > 679 or y < 19 or y > 679:
            font = pygame.font.SysFont('microsofttaile', 72)
            txt = font.render("Snake 1 win", True, (0, 0, 0), (255, 255, 255))
            screen.fill((255,255,255))
            screen.blit(txt, (160, 275))
            pygame.display.update()
            time.sleep(2) 
            exit()
        for i in range(self.size - 1, 0, -1):
            if self.elements[0][0] == self.elements[i][0] and self.elements[0][1] == self.elements[i][1]:
                font = pygame.font.SysFont('microsofttaile', 72)
                txt = font.render("Snake 1 win", True, (0, 0, 0), (255, 255, 255))
                screen.fill((255,255,255))
                screen.blit(txt, (160, 275))
                pygame.display.update()
                time.sleep(2) 
                exit()
        if lev1 == True:
            rec1=pygame.draw.rect(screen,(100,100,100), (140,140, 20,20))
            rec2=pygame.draw.rect(screen,(100,100,100), (540,140, 20,20))
            rec3=pygame.draw.rect(screen,(100,100,100), (140,540, 20,20))
            rec4=pygame.draw.rect(screen,(100,100,100), (540,540, 20,20))
            if rec1.collidepoint(snake2pos) or rec2.collidepoint(snake2pos) or rec3.collidepoint(snake2pos) or rec4.collidepoint(snake2pos):
                font = pygame.font.SysFont('microsofttaile', 72)
                txt = font.render("Snake 1 win", True, (0, 0, 0), (255, 255, 255))
                screen.fill((255,255,255))
                screen.blit(txt, (160, 275))
                pygame.display.update()
                time.sleep(2) 
                exit()

        if lev2 == True:
            rect1=pygame.draw.rect(screen,(100,100,100), (240,240, 20,20))
            rect2=pygame.draw.rect(screen,(100,100,100), (440,240, 20,20))
            rect3=pygame.draw.rect(screen,(100,100,100), (240,440, 20,20))
            rect4=pygame.draw.rect(screen,(100,100,100), (440,440, 20,20))
            if rect1.collidepoint(snake2pos) or rect2.collidepoint(snake2pos) or rect3.collidepoint(snake2pos) or rect4.collidepoint(snake2pos):
                font = pygame.font.SysFont('microsofttaile', 72)
                txt = font.render("Snake 1 win", True, (0, 0, 0), (255, 255, 255))
                screen.fill((255,255,255))
                screen.blit(txt, (160, 275))
                pygame.display.update()
                time.sleep(2) 
                exit()
def score():
    font = pygame.font.SysFont('microsofttaile', 15)
    a=snake1.size-1
    tx = font.render("score RSnake "+str(a), True, (255, 255, 255), (100, 100, 100))
    screen.blit(tx, (0, 0))

    b=snake2.size-1
    tx = font.render("score BSnake "+str(b), True, (255, 255, 255), (100, 100, 100))
    screen.blit(tx, (580, 0))    
snake1 = Snake(100, 100)
snake2 = Snake2(160, 100)
food = Food()
d=20
m=10
h=20
def MediumWall(cnt):
    if lev1 == True:
        if cnt==0:
            font = pygame.font.SysFont('microsofttaile', 72)
            txt = font.render("Medium mode", True, (0, 0, 0), (255, 255, 255))
            screen.fill((0,0,0))
            screen.blit(txt, (160, 275))
            pygame.display.update()
            time.sleep(2)
            snake1.speed+=2
            
        rec1=pygame.draw.rect(screen,(100,100,100), (140,140, 20,20))
        rec2=pygame.draw.rect(screen,(100,100,100), (540,140, 20,20))
        rec3=pygame.draw.rect(screen,(100,100,100), (140,540, 20,20))
        rec4=pygame.draw.rect(screen,(100,100,100), (540,540, 20,20))
        rec1
        rec2
        rec3
        rec4
def HardWall(cnt2):
    if lev2 == True:
        if cnt2==0:
            font = pygame.font.SysFont('microsofttaile', 72)
            txt = font.render("Medium mode", True, (0, 0, 0), (255, 255, 255))
            screen.fill((0,0,0))
            screen.blit(txt, (160, 275))
            pygame.display.update()
            time.sleep(2)
            snake1.speed+=2
        rect1=pygame.draw.rect(screen,(100,100,100), (240,240, 20,20))
        rect2=pygame.draw.rect(screen,(100,100,100), (440,240, 20,20))
        rect3=pygame.draw.rect(screen,(100,100,100), (240,440, 20,20))
        rect4=pygame.draw.rect(screen,(100,100,100), (440,440, 20,20))
        rect1
        rect2
        rect3
        rect4
clock = pygame.time.Clock()
game = True
while game:
    choose=False
    clock.tick(snake1.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            if event.key == pygame.K_d and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d

            # if event.key == pygame.K_1:
            #     snake.is_add = True
    screen.fill((0, 0, 0))
    for i in range(0,700,20):
        pygame.draw.rect(screen, (200, 200, 200), (i, 0, 1, 700),1)
        pygame.draw.rect(screen, (200, 200, 200), (0, i, 700, 1),1)
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, 20, 700))
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, 700, 20))
    pygame.draw.rect(screen, (100, 100, 100), (681, 0, 20, 700))
    pygame.draw.rect(screen, (100, 100, 100), (0, 681, 700, 20))
    if snake1.eat(food.x-20, food.y-20):
        snake1.is_add = True
        food.nextPos()
    if snake2.eat(food.x-20, food.y-20):
        snake2.is_add = True
        food.nextPos()
    if lev1==False:
        if (snake1.size+snake2.size) % 12 == 0:
            lev1=True
    if lev2==False:
        if (snake1.size+snake2.size) % 22 == 0:
            lev2=True
    MediumWall(cnt)
    HardWall(cnt2)
    if lev1:
        cnt=1
    if lev2:
        cnt2=1
    snake1.move()
    snake2.move()
    snake1.draw()
    snake2.draw()
    food.draw()
    snake1.death()
    snake2.death()   
    score()

    pygame.display.update()   