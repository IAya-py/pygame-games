from color import *

class Snake:
    
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.reset()

    def reset(self):
        self.pieces = []
        self.pieces.append([30, 30])
        self.movement = 2

    def update(self):
        [headX, headY] = self.pieces[0]

        if self.movement == 1:    
            head = [headX, headY - 30]

        elif self.movement == 2:
            head = [headX + 30, headY]

        elif self.movement == 3:
            head = [headX - 30, headY]

        elif self.movement == 4:
            head = [headX, headY + 30]

        self.pieces.insert(0, head)
        self.pieces.pop()

    def add(self):
        [tailX, tailY] = self.pieces[-1]

        tail = []
        if self.movement == 1:    
            tail = [tailX, tailY + 30]

        elif self.movement == 2:
            tail = [tailX - 30, tailY]

        elif self.movement == 3:
            tail = [tailX + 30, tailY]

        elif self.movement == 4:
            tail = [tailX, tailY - 30]

        self.pieces.append(tail)


    def move(self, keyPress):
        
        if keyPress == 'up':
            if self.movement == 4:
                return
            self.movement = 1

        elif keyPress == 'right':
            if self.movement == 3:
                return
            self.movement = 2

        elif keyPress == 'left':
            if self.movement == 2:
                return
            self.movement = 3

        elif keyPress == 'down':
            if self.movement == 1:
                return
            self.movement = 4
                