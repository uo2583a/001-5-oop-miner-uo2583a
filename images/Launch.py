import pygame
import random
from Player import Player
from Creeper import Creeper
from Zombie import Zombie
from Cow import Cow
from Chicken import Chicken

pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Minecraft Collision Game")

# Initialize player and mobs
player = Player(window, window_width, window_height)
player.rect.center = (window_width // 2, window_height // 2)  # Center the player
mobs = []

# Helper function to spawn mobs away from the player
def random_position():
    return random.choice([0, window_width - 50]), random.choice([0, window_height - 50])

# Populate mobs list with separated initial positions
for _ in range(3): mobs.append(Creeper(window, window_width, window_height))
for _ in range(5): mobs.append(Chicken(window, window_width, window_height))
for _ in range(2): mobs.append(Zombie(window, window_width, window_height))
for _ in range(3): mobs.append(Cow(window, window_width, window_height))

# Set mobs in random positions
for mob in mobs:
    mob.rect.topleft = random_position()

# Game loop variables
clock = pygame.time.Clock()
running = True
start_time = pygame.time.get_ticks()  # Track start time for delay
collision_active = False
zombie_count = 2

# Game loop
while running:
    window.fill((255, 255, 255))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Delay collision detection by 2 seconds
    if pygame.time.get_ticks() - start_time > 2000:
        collision_active = True

    # Update player position
    player.update()

    for mob in mobs:
        mob.update()
        if collision_active and player.check_collide(mob):
            if isinstance(mob, Creeper):
                print("Game Over! Final Score:",player.score)
                running = False
            elif isinstance(mob, Zombie):
                player.score += 25
                mobs.remove(mob)
                zombie_count -= 1
                if zombie_count == 0:
                    print("Congratulations! Final Score:",player.score)
                    running = False
            elif isinstance(mob, Cow):
                player.score -= 10
                mobs.remove(mob)
            elif isinstance(mob, Chicken):
                player.score -= 5
                mobs.remove(mob)

    # Draw player and mobs
    player.draw()
    for mob in mobs:
        mob.draw()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()