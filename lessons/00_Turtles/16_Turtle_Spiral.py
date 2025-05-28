import pygame
import sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Platformer")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
GREEN = (0, 255, 100)

# Player settings
player = pygame.Rect(100, 500, 50, 50)
player_speed = 5
gravity = 0.5
jump_strength = -10
velocity_y = 0
on_ground = False

# Platform
platform = pygame.Rect(0, 550, WIDTH, 50)

# Game loop
while True:
    screen.fill(WHITE)

    # Event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP] and on_ground:
        velocity_y = jump_strength
        on_ground = False

    # Apply gravity
    velocity_y += gravity
    player.y += velocity_y

    # Collision with platform
    if player.colliderect(platform):
        player.bottom = platform.top
        velocity_y = 0
        on_ground = True
    else:
        on_ground = False

    # Draw everything
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, GREEN, platform)

    # Update screen
    pygame.display.update()
    clock.tick(60)