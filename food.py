import pygame
from snake import *
import random

class Food:
    def __init__(self, snake):
        self.randomize(snake)

    def randomize(self, snake):
        self.x = random.randint(0, 19) * 30
        self.y = random.randint(0, 19) * 30

        for piece in snake.pieces:
            if [self.x, self.y] == piece:
                self.randomize(snake)



