import pygame
from pygame.locals import *
from sys import exit
from random import randint

def snake_move(snake,pos):
    global x_screen, y_screen, x_snake, y_snake

    if pygame.key.get_pressed()[pygame.locals.K_DOWN] or pygame.key.get_pressed()[K_s]:
        y_snake += 50
        if y_snake > y_screen:
            y_snake = y_screen - 40
    if pygame.key.get_pressed()[pygame.locals.K_UP] or pygame.key.get_pressed()[K_w]:
        y_snake -= 50
        if y_snake < 0:
            y_snake = 0
    if pygame.key.get_pressed()[pygame.locals.K_LEFT] or pygame.key.get_pressed()[K_a]:
        x_snake -= 50
        if x_snake < 0:
            x_snake = 0
    if pygame.key.get_pressed()[pygame.locals.K_RIGHT] or pygame.key.get_pressed()[K_d]:
        x_snake += 50
        if x_snake > x_screen:
            x_snake = x_screen - 40

pygame.init()
# Valores das coordenadas
x_screen = 1000
y_screen = 500
x_snake = int(x_screen / 2)
y_snake = int(y_screen / 2)
x_apple = randint(20, 920)
y_apple = randint(20,450)

screen = pygame.display.set_mode((x_screen,y_screen))
pygame.display.set_caption('Snake Game')
font = pygame.font.SysFont('roboto', 35, True, False)
point = 0

clock = pygame.time.Clock()

while True:
    screen.fill((0,0,0))
    clock.tick(15)
    point_text = f'Point: {point}'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    point_text_format = font.render(point_text, False, (255,255,255))
    snake = pygame.draw.rect(screen, (0,200,0), (x_snake,y_snake, 40, 40))
    apple = pygame.draw.circle(screen, (150,0,0),(x_apple, y_apple), 10 )

    snake_move(snake, (x_snake,y_snake))
    
    if snake.colliderect(apple):
        x_apple = randint(20, 920)
        y_apple = randint(20,450)
        point += 1

    screen.blit(point_text_format, (820,20))
    pygame.display.update()