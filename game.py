import pygame
import os
import random
from color import *
from snake import Snake

HEIGHT = 600
WIDTH = 600

FPS = 12

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cool Snake Hisss")
clock = pygame.time.Clock()

snake = Snake(screen, 50, 50)

running = True
x = 1
while running:
    print(x)
    x += 1
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



    screen.fill(BLACK)
    for z in snake.pieces:
        pygame.draw.rect(screen, BLUE, (z[0], z[1], 30, 30 ))

    pygame.display.flip()

pygame.quit()