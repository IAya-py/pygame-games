import pygame
from snake import *
import random

class Food:
    def __init__(self):
        self.x = random.randint(0, 19) * 30
        self.y = random.randint(0, 19) * 30

