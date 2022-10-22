# Para iniciarmos o jogo, precisamos importar o pygame.

import pygame, random
from pygame.locals import *

# Função para o alinhamento da cobra com a maçã, para ficarem no mesmo 'grid'. As pocições serão aleatórias, mas sempre múltiplas de 10:
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Para montarmos a "tela" do jogo, vamos precisar de uma matriz.
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

# Criação da cobra:
snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

# Criação da maçã:
apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = LEFT

# Para limitar a velocidade da cobra, usando Clock.tick():
clock = pygame.time.Clock()

# Evento de fechamento do jogo:
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

# Movimentação da cobra usando os comandos do teclado:
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    # Colisão da cobra com a maçã, gerando o aumento da cobra.
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break

    # Se a cobra colidir consigo mesma:
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

# Movimentação da cobra, de acordo com as teclas usadas no comando:
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()