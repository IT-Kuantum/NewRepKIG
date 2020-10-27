import pygame

W = 800
H = 600
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
YELLOW = (225, 225, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 50)

pygame.init()
pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((W, H))


font = pygame.font.SysFont('Arial', 50, True, False)
font_box = pygame.Surface((W - font.get_height(), font.get_height()))
font_rect = font_box.get_rect(center=(W - 200, H // 2))
font1 = pygame.font.SysFont('Arial', 26, True, False)
font1_box = pygame.Surface((W - font1.get_height(), font1.get_height()))
font1_rect = font1_box.get_rect(center=(W - 200, H // 2))

screen.fill(BLUE)
pygame.draw.rect(screen, (RED), (370, 180, 50, 50))
screen.blit(font.render('Всем привет', True, WHITE),(font_rect))
screen.blit(font1.render('задание на урок', True, YELLOW), (300, 350))


print (font_rect)

pygame.display.update()
run = True
while run:
     for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False