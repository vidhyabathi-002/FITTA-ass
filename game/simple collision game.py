import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Game")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Player properties
player_width = 100
player_height = 100
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height
player_speed = 5

# Enemy properties
enemy_width = 100
enemy_height = 100
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
enemy_y = -enemy_height
enemy_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_height:
        player_y += player_speed
    
    # Enemy movement
    enemy_y += enemy_speed
    
    # Reset enemy if it goes off screen
    if enemy_y > SCREEN_HEIGHT:
        enemy_y = -enemy_height
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        score += 1
    
    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    
    if player_rect.colliderect(enemy_rect):
        print(f"Game Over! Final Score: {score}")
        running = False
    
    # Draw everything
    screen.fill(BLACK)
    
    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    
    # Draw enemy
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
