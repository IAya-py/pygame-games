import pygame
import os
import random
from color import *

HEIGHT = 600
WIDTH = 800

FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Wars")
clock = pygame.time.Clock()


running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass

    screen.fill(BLACK)
    pygame.display.flip()

pygame.quit()