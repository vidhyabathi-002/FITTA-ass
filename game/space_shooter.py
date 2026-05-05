import pygame
import sys
import random
import math
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 120, 255)
ORANGE = (255, 140, 0)
PURPLE = (170, 80, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter - Destroy the Invaders!")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Font
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, "assets")


def load_sprite(filename, size, fallback_color):
    path = os.path.join(ASSET_DIR, filename)
    try:
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(image, size)
    except pygame.error:
        fallback = pygame.Surface(size, pygame.SRCALPHA)
        fallback.fill(fallback_color)
        return fallback


def add_sprite_glow(image, glow_color, padding=6):
    glow_image = pygame.Surface(
        (image.get_width() + padding * 2, image.get_height() + padding * 2),
        pygame.SRCALPHA,
    )
    outline = pygame.mask.from_surface(image).to_surface(
        setcolor=glow_color,
        unsetcolor=(0, 0, 0, 0),
    )
    for offset_x, offset_y in ((0, -2), (2, 0), (0, 2), (-2, 0), (0, 0)):
        glow_image.blit(outline, (padding + offset_x, padding + offset_y))
    glow_image.blit(image, (padding, padding))
    return glow_image


PLAYER_IMAGE = load_sprite("player_aircraft.png", (40, 50), CYAN)
ENEMY_IMAGE = add_sprite_glow(
    load_sprite("enemy_aircraft.png", (55, 55), RED),
    (255, 50, 50, 150),
)
BACKGROUND_IMAGE = load_sprite("space_background.png", (SCREEN_WIDTH, SCREEN_HEIGHT), BLACK)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMAGE.copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 6
        self.shoot_cooldown = 0
        self.weapon_level = 1
        self.max_weapon_level = 3
        self.max_health = 100
        self.health = self.max_health
        self.max_shield = 100
        self.shield = 0
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def shoot(self):
        if self.shoot_cooldown == 0:
            bullet_positions = [(self.rect.centerx, self.rect.top, 0)]
            if self.weapon_level == 2:
                bullet_positions = [
                    (self.rect.centerx - 10, self.rect.top + 5, -1),
                    (self.rect.centerx + 10, self.rect.top + 5, 1),
                ]
            elif self.weapon_level >= 3:
                bullet_positions = [
                    (self.rect.centerx, self.rect.top, 0),
                    (self.rect.centerx - 14, self.rect.top + 7, -2),
                    (self.rect.centerx + 14, self.rect.top + 7, 2),
                ]

            for bullet_x, bullet_y, drift in bullet_positions:
                bullet = Bullet(bullet_x, bullet_y, drift)
                all_sprites.add(bullet)
                bullets.add(bullet)
            self.shoot_cooldown = max(5, 10 - self.weapon_level)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, wave=1):
        super().__init__()
        self.image = ENEMY_IMAGE.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.wave = wave
        self.speed = random.randint(5, 8) + wave
        self.shoot_cooldown = random.randint(30, max(40, 100 - wave * 5))
    
    def update(self):
        self.rect.y += self.speed
        self.shoot_cooldown -= 1
        
        # Remove if off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        
        # Enemy shoots randomly
        if self.shoot_cooldown <= 0:
            self.shoot()
            self.shoot_cooldown = random.randint(30, 100)
    
    def shoot(self):
        speed = 9 + (self.wave * 0.5)
        enemy_bullet = EnemyBullet(self.rect.centerx, self.rect.bottom, speed=speed)
        all_sprites.add(enemy_bullet)
        enemy_bullets.add(enemy_bullet)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, drift=0):
        super().__init__()
        self.image = pygame.Surface((6, 18), pygame.SRCALPHA)
        pygame.draw.rect(self.image, YELLOW, (2, 0, 2, 18))
        pygame.draw.circle(self.image, ORANGE, (3, 3), 3)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10
        self.drift = drift
    
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.drift
        if self.rect.bottom < 0:
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=7, drift=0):
        super().__init__()
        self.image = pygame.Surface((5, 12))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed = speed
        self.drift = drift
    
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.drift
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Boss(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        base_image = ENEMY_IMAGE.copy()
        self.image = pygame.transform.smoothscale(base_image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.y = -150
        self.max_health = 300 + (level * 200)
        self.health = self.max_health
        self.speed_x = 3 + (level * 0.5)
        self.speed_y = 2
        self.shoot_cooldown = 60
        self.level = level
        self.direction = 1

    def update(self):
        if self.rect.y < 50:
            self.rect.y += self.speed_y
        else:
            self.rect.x += self.speed_x * self.direction
            if self.rect.right >= SCREEN_WIDTH - 20:
                self.direction = -1
            elif self.rect.left <= 20:
                self.direction = 1

        self.shoot_cooldown -= 1
        if self.shoot_cooldown <= 0:
            self.shoot()
            self.shoot_cooldown = max(20, 80 - (self.level * 5))

    def shoot(self):
        speed = 8 + (self.level * 0.5)
        # Spread pattern
        for drift in [-3, -1.5, 0, 1.5, 3]:
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom, speed=speed, drift=drift)
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, kind):
        super().__init__()
        self.kind = kind
        self.image = pygame.Surface((28, 28), pygame.SRCALPHA)
        color = {
            "weapon": YELLOW,
            "health": GREEN,
            "shield": BLUE,
        }[kind]
        pygame.draw.circle(self.image, color, (14, 14), 13)
        pygame.draw.circle(self.image, WHITE, (14, 14), 13, 2)
        label = {
            "weapon": "W",
            "health": "+",
            "shield": "S",
        }[kind]
        label_text = font_small.render(label, True, BLACK)
        label_rect = label_text.get_rect(center=(14, 14))
        self.image.blit(label_text, label_rect)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 4
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.max_frames = 15

    def update(self):
        self.frame += 1
        if self.frame >= self.max_frames:
            self.kill()
        else:
            self.image.fill((0, 0, 0, 0))
            radius = int(30 * (self.frame / self.max_frames))
            alpha = int(255 * (1 - (self.frame / self.max_frames)))
            color = (255, random.randint(100, 200), 0, alpha)
            pygame.draw.circle(self.image, color, (30, 30), radius)

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Game variables
score = 0
lives = 3
enemy_spawn_rate = 50
spawn_counter = 0
game_over = False
level = 1
start_screen = True
paused = False
enemies_killed = 0
boss_active = False
boss = None

# Game loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if start_screen:
                if event.key == pygame.K_RETURN:
                    start_screen = False
            elif game_over:
                if event.key == pygame.K_r:
                    # Reset game
                    game_over = False
                    start_screen = True
                    score = 0
                    lives = 3
                    level = 1
                    enemy_spawn_rate = 50
                    enemies_killed = 0
                    boss_active = False
                    boss = None
                    all_sprites.empty()
                    enemies.empty()
                    bullets.empty()
                    enemy_bullets.empty()
                    powerups.empty()
                    player = Player()
                    all_sprites.add(player)
                elif event.key == pygame.K_q:
                    running = False
            else:
                if event.key == pygame.K_p:
                    paused = not paused
    
    if start_screen:
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        title_text = font_large.render("SPACE SHOOTER", True, CYAN)
        start_text = font_medium.render("Press ENTER to Start", True, WHITE)
        screen.blit(title_text, title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
        screen.blit(start_text, start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)))
        pygame.display.flip()
        continue

    if paused:
        pause_text = font_large.render("PAUSED", True, YELLOW)
        screen.blit(pause_text, pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        pygame.display.flip()
        continue

    if not game_over:
        # Update
        all_sprites.update()
        
        # Spawn enemies
        if not boss_active:
            enemies_to_kill = 15 + (level * 5)
            if enemies_killed < enemies_to_kill:
                spawn_counter += 1
                if spawn_counter >= enemy_spawn_rate:
                    enemy = Enemy(level)
                    all_sprites.add(enemy)
                    enemies.add(enemy)
                    spawn_counter = 0
                    # Increase difficulty
                    if enemy_spawn_rate > 15:
                        enemy_spawn_rate -= 0.5
            elif len(enemies) == 0:
                # Spawn boss
                boss_active = True
                boss = Boss(level)
                all_sprites.add(boss)
                enemies.add(boss)
        
        # Check bullet-enemy collisions
        for bullet in bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, False)
            for enemy in hit_enemies:
                bullet.kill()
                explosion = Explosion(bullet.rect.center)
                all_sprites.add(explosion)
                
                if isinstance(enemy, Boss):
                    enemy.health -= 10 + (player.weapon_level * 5)
                    if enemy.health <= 0:
                        enemy.kill()
                        score += 500
                        # drop multiple powerups
                        for _ in range(5):
                            kind = random.choice(["weapon", "health", "shield"])
                            pu = PowerUp(enemy.rect.centerx + random.randint(-50, 50), enemy.rect.centery + random.randint(-50, 50), kind)
                            all_sprites.add(pu)
                            powerups.add(pu)
                        boss_active = False
                        boss = None
                        level += 1
                        enemies_killed = 0
                        enemy_spawn_rate = max(15, 50 - (level * 5))
                else:
                    enemy.kill()
                    score += 10
                    enemies_killed += 1
                    if random.random() < 0.3:
                        kind = random.choice(["weapon", "health", "shield"])
                        powerup = PowerUp(enemy.rect.centerx, enemy.rect.centery, kind)
                        all_sprites.add(powerup)
                        powerups.add(powerup)
        
        # Check powerup-player collisions
        powerup_collisions = pygame.sprite.spritecollide(player, powerups, True)
        for powerup in powerup_collisions:
            score += 50
            if powerup.kind == "weapon":
                player.weapon_level = min(player.weapon_level + 1, player.max_weapon_level)
            elif powerup.kind == "health":
                player.health = min(player.health + 30, player.max_health)
            elif powerup.kind == "shield":
                player.shield = min(player.shield + 50, player.max_shield)

        # Check enemy-player collisions
        enemy_collisions = pygame.sprite.spritecollide(player, enemies, False)
        for enemy in enemy_collisions:
            explosion = Explosion(enemy.rect.center)
            all_sprites.add(explosion)
            
            damage = 20
            if isinstance(enemy, Boss):
                damage = 50
            else:
                enemy.kill()
                enemies_killed += 1
                
            if player.shield > 0:
                player.shield -= damage
                if player.shield < 0:
                    player.health += player.shield
                    player.shield = 0
            else:
                player.health -= damage

        # Check enemy bullet-player collisions
        if pygame.sprite.spritecollide(player, enemy_bullets, True):
            damage = 10
            if player.shield > 0:
                player.shield -= damage
                if player.shield < 0:
                    player.health += player.shield
                    player.shield = 0
            else:
                player.health -= damage
                
        if player.health <= 0:
            explosion = Explosion(player.rect.center)
            all_sprites.add(explosion)
            lives -= 1
            if lives <= 0:
                game_over = True
            else:
                player.health = player.max_health
                player.shield = 0
    
    # Draw
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    
    # Draw stars (background effect)
    for i in range(20):
        x = (i * 50 + pygame.time.get_ticks() // 10) % SCREEN_WIDTH
        y = (i * 35) % SCREEN_HEIGHT
        pygame.draw.circle(screen, WHITE, (x, y), 1)
    
    # Draw sprites
    all_sprites.draw(screen)
    
    # Draw UI
    score_text = font_medium.render(f"Score: {score}", True, WHITE)
    lives_text = font_medium.render(f"Lives: {lives}", True, WHITE)
    level_text = font_medium.render(f"Level: {level}", True, CYAN)
    
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))
    screen.blit(level_text, (SCREEN_WIDTH - 200, 10))
    
    # Draw Boss Health Bar
    if boss_active and boss is not None:
        pygame.draw.rect(screen, RED, (SCREEN_WIDTH // 2 - 200, 20, 400, 20))
        if boss.health > 0:
            pygame.draw.rect(screen, PURPLE, (SCREEN_WIDTH // 2 - 200, 20, int(400 * (boss.health / boss.max_health)), 20))
        boss_label = font_small.render("BOSS", True, WHITE)
        screen.blit(boss_label, boss_label.get_rect(center=(SCREEN_WIDTH // 2, 10)))
    else:
        # Progress to next boss
        enemies_to_kill = 15 + (level * 5)
        progress = min(enemies_killed / enemies_to_kill, 1.0)
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2 - 100, 20, 200, 10))
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 100, 20, int(200 * progress), 10))
        prog_label = font_small.render("LEVEL PROGRESS", True, WHITE)
        screen.blit(prog_label, prog_label.get_rect(center=(SCREEN_WIDTH // 2, 10)))
    
    # Draw Health Bar
    pygame.draw.rect(screen, RED, (10, 80, 150, 15))
    if player.health > 0:
        pygame.draw.rect(screen, GREEN, (10, 80, int(150 * (player.health / player.max_health)), 15))
    
    # Draw Shield Bar
    if player.shield > 0:
        pygame.draw.rect(screen, BLUE, (10, 100, int(150 * (player.shield / player.max_shield)), 10))
    
    if game_over:
        # Dark overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))
        
        # Game over screen
        game_over_text = font_large.render("GAME OVER", True, RED)
        final_score_text = font_medium.render(f"Final Score: {score}", True, WHITE)
        final_level_text = font_medium.render(f"Levels Survived: {level}", True, WHITE)
        restart_text = font_small.render("Press R to Restart or Q to Quit", True, YELLOW)
        
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        final_level_rect = final_level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))
        
        screen.blit(game_over_text, game_over_rect)
        screen.blit(final_score_text, final_score_rect)
        screen.blit(final_level_text, final_level_rect)
        screen.blit(restart_text, restart_rect)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False
    
    pygame.display.flip()

pygame.quit()
sys.exit()
