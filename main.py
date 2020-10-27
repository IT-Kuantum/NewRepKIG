import pygame
import os

W = 800
H = 600
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
YELLOW = (225, 225, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((W, H))

pygame.draw.rect(screen, (RED), (370, 180, 50, 50))

font = pygame.font.SysFont('Arial', 50, True, False)
font1 = pygame.font.SysFont('Arial', 26, True, False)

path = os.path.dirname(os.path.abspath(__file__))
image = pygame.image.load

screen.blit(font.render('Всем привет', True, WHITE),(250, 250))
screen.blit(font1.render('задание на урок', True, YELLOW), (300, 310))
pygame.display.update()
run = True
while run:
     for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False