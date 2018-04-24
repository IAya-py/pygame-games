import pygame
from snake import *

snake = Snake()

class Food:
    x = 0
    y = 0

    step = 44

    def __init__(self, x, y)
        self.x = x
        self.y = y

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

