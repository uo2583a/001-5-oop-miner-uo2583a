import pygame
import random
from Mob import Mob

class Creeper(Mob):
    def __init__(self, window, windowWidth, windowHeight):
        super().__init__(window, windowWidth, windowHeight, "creeper.png")
        self.speed_x = random.choice([-1, 1])
        self.speed_y = random.choice([-1, 1])
        self.speed = random.choice([1, 2])

    def update(self):
        self.rect.x += self.speed_x * self.speed
        self.rect.y += self.speed_y * self.speed

        if self.rect.left <= 0 or self.rect.right >= self.window_width:
            self.speed_x = random.choice([-1, 1])
        if self.rect.top <= 0 or self.rect.bottom >= self.window_height:
            self.speed_y = random.choice([-1, 1])



