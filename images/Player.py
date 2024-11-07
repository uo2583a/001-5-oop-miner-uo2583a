import pygame

class Player():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.window_width = windowWidth
        self.window_height = windowHeight
        self.image = pygame.image.load("player.jpg")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = windowWidth // 2
        self.rect.y = windowHeight // 2
        self.__score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < self.window_width:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_DOWN] and self.rect.bottom < self.window_height:
            self.rect.y += 5

    def check_collide(self, other_character):
        return self.rect.colliderect(other_character.get_rect())

    def get_rect(self):
        return self.rect

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if isinstance(value, int):
            self.__score = value

    def draw(self):
        self.window.blit(self.image, self.rect)