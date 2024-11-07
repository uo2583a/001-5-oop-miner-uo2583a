import pygame
from Mob import Mob

class Chicken(Mob):
    def __init__(self, window, windowWidth, windowHeight):
        super().__init__(window, windowWidth, windowHeight, "chicken.png")
        self.speed_x = 2  # Chicken moves horizontally only

        def update(self):
            self.rect.x += self.speed_x
            if self.rect.left <= 0 or self.rect.right >= self.window_width:
                self.speed_x *= -1

