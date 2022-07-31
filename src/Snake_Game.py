import pygame
from pygame.locals import *
from sys import exit
from random import randint

def snake_move(snake):
    global x_screen, y_screen, x_snake, y_snake, x_control, y_control
    if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0

            if event.key == K_RIGHT:
                if x_control == -speed:
                    pass
                else:
                    x_control = speed
                    y_control = 0

            if event.key == K_DOWN:
                if y_control == -speed:
                    pass
                else:
                    x_control = 0
                    y_control = speed

            if event.key == K_UP:
                if y_control == speed:
                    pass
                else:
                    x_control = 0
                    y_control = -speed

def snake_body(snake_list):
    for pos in snake_list:
        pygame.draw.rect(screen, (0,200,0), (pos[0],pos[1], 20, 20))

def restart_game():
    global point, initial_length, x_snake, y_snake, snake_list,head_list, x_apple, y_apple, dead
    point = 0
    initial_length = 0
    x_snake = int(x_screen / 2)
    y_snake = int(y_screen / 2)
    snake_list = []
    head_list = []
    x_apple = randint(20, 920)
    y_apple = randint(20,450)
    dead = False

pygame.init()
# Valores das coordenadas
speed = 20
x_screen = 1000
y_screen = 500
x_snake = int(x_screen / 2)
y_snake = int(y_screen / 2)
x_apple = randint(20, 920)
y_apple = randint(20,450)
x_control = speed
y_control = 0

# Musica e efeitos sonoros
soundtrack = pygame.mixer.music.load('soundtrack.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound('fireball.wav')

# Definição de janela, fonte e etc..
screen = pygame.display.set_mode((x_screen,y_screen))
pygame.display.set_caption('Snake Game')
font = pygame.font.SysFont('arial', 40, True, True)
point = 0
clock = pygame.time.Clock()
snake_list = []
initial_length = 0
dead = False

# loop infinito do jogo
while True:
    screen.fill((240,240,240))
    clock.tick(10)
    point_text = f'Point: {point}'
    
    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Criação texto pontuação, cobra e maçã
    point_text_format = font.render(point_text, True, (0,0,0))
    snake = pygame.draw.rect(screen, (0,200,0), (x_snake,y_snake, 20, 20))
    apple = pygame.draw.circle(screen, (150,0,0),(x_apple, y_apple), 10 )

    # Ações do jogo
    snake_move(snake)
    if snake.colliderect(apple):
        x_apple = randint(20, 920)
        y_apple = randint(20,450)
        point += 1
        sound.play()
        initial_length += 1
        
    x_snake += x_control
    y_snake += y_control

    head_list = []
    head_list.append(x_snake)
    head_list.append(y_snake)
    snake_list.append(head_list)

    if snake_list.count(head_list) > 1:
        font2 = pygame.font.SysFont('arial', 40, True, True)
        game_over = 'GAME OVER! Press R to play again'
        game_over_format = font2.render(game_over, True, (0,0,0))
        text_rect = game_over_format.get_rect()
        dead = True

        while dead:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        restart_game()
            text_rect.center = (x_screen // 2, y_screen // 2 )
            screen.blit(game_over_format,text_rect)
            pygame.display.update()
    
    # Passa a cobra de um lado a outro na tela
    if x_snake > x_screen:
        x_snake = 0
    if x_snake < 0:
        x_snake = x_screen
    if y_snake > y_screen:
        y_snake = 0
    if y_snake < 0:
        y_snake = y_screen

    if len(snake_list) > initial_length:
        del snake_list[0]

    snake_body(snake_list)

    screen.blit(point_text_format, (790,20))
    pygame.display.update()
