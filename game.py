import pygame
import os
import random
from color import *
from snake import Snake
from food import Food

HEIGHT = 600
WIDTH = 600

FPS = 24

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cool Snake Hisss")
clock = pygame.time.Clock()

snake = Snake(screen, 50, 50)
food = Food()

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass

    key = pygame.key.get_pressed()

    if key[pygame.K_a]:
        snake.add()

    if key[pygame.K_LEFT]:
        snake.move('left')

    if key[pygame.K_RIGHT]:
        snake.move('right')

    if key[pygame.K_UP]:
        snake.move('up')

    if key[pygame.K_DOWN]:
        snake.move('down')

    snake.update()

    [hx, hy] = snake.pieces[0]

    if hx < 0 or hy < 0 or hx > HEIGHT-1 or hy > WIDTH-1:
        snake.reset()

    screen.fill(BLACK)
    print(food.x, food.y)
    pygame.draw.rect(screen, RED, (food.x, food.y, 30, 30))
    for piece in snake.pieces:
        pygame.draw.rect(screen, BLUE, (piece[0], piece[1], 30, 30 ))

    pygame.display.flip()

pygame.quit()