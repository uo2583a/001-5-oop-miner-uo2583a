import pygame

from Mob import Mob

class Cow(Mob):
    def __init__(self, window, windowWidth, windowHeight):
        super().__init__(window, windowWidth, windowHeight, "cow.jpg")
        self.speed_y = 2  # Cow moves vertically only

        def update(self):
            self.rect.y += self.speed_y
            if self.rect.top <= 0 or self.rect.bottom >= self.window_height:
                self.speed_y *= -1
            self.rect.bottom = 0