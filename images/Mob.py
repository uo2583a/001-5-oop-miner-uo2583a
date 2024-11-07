import pygame

class Mob:
    def __init__(self, window, windowWidth, windowHeight, image_path):
        self.window = window
        self.window_width = windowWidth
        self.window_height = windowHeight
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (90, 90))  # Scale to 40x40 pixels
        self.rect = self.image.get_rect()
        self.rect.x = windowWidth // 2
        self.rect.y = windowHeight // 2

    def update(self):
        pass

    def get_rect(self):
        return self.rect

    def draw(self):
        self.window.blit(self.image, self.rect)