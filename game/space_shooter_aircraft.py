import pygame
import sys
import random
import math
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (200, 0, 255)
PINK = (255, 105, 180)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🚀 SPACE SHOOTER ULTIMATE - Aircraft Edition!")

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Font
font_large = pygame.font.Font(None, 80)
font_medium = pygame.font.Font(None, 40)
font_small = pygame.font.Font(None, 28)

# Load images or create them if they don't exist
def create_aircraft_images():
    """Create aircraft-like images using pygame drawing"""

    # Player aircraft (blue fighter jet)
    player_img = pygame.Surface((60, 40), pygame.SRCALPHA)
    # Main body
    pygame.draw.polygon(player_img, CYAN, [(30, 5), (50, 35), (10, 35)])
    # Wings
    pygame.draw.polygon(player_img, CYAN, [(15, 20), (25, 15), (35, 20), (45, 15)])
    # Cockpit
    pygame.draw.circle(player_img, WHITE, (30, 15), 5)
    # Engine glow
    pygame.draw.circle(player_img, YELLOW, (30, 35), 3)

    # Enemy aircraft (red fighter)
    enemy_img = pygame.Surface((50, 35), pygame.SRCALPHA)
    # Main body
    pygame.draw.polygon(enemy_img, RED, [(25, 5), (40, 30), (10, 30)])
    # Wings
    pygame.draw.polygon(enemy_img, RED, [(12, 18), (20, 12), (30, 18), (38, 12)])
    # Details
    pygame.draw.circle(enemy_img, YELLOW, (25, 12), 3)
    pygame.draw.circle(enemy_img, ORANGE, (25, 30), 2)

    # Boss aircraft (purple heavy bomber)
    boss_img = pygame.Surface((100, 60), pygame.SRCALPHA)
    # Main body
    pygame.draw.ellipse(boss_img, PURPLE, (20, 10, 60, 40))
    # Wings
    pygame.draw.polygon(boss_img, PURPLE, [(10, 25), (20, 15), (80, 15), (90, 25), (80, 35), (20, 35)])
    # Engines
    pygame.draw.circle(boss_img, PINK, (15, 30), 5)
    pygame.draw.circle(boss_img, PINK, (85, 30), 5)
    # Cockpit
    pygame.draw.circle(boss_img, WHITE, (50, 20), 8)
    # Weapons
    pygame.draw.rect(boss_img, RED, (45, 45, 10, 8))

    return player_img, enemy_img, boss_img

# Try to load images, if not create them
try:
    # If you have PNG files, uncomment these lines:
    # player_image = pygame.image.load('player_aircraft.png').convert_alpha()
    # enemy_image = pygame.image.load('enemy_aircraft.png').convert_alpha()
    # boss_image = pygame.image.load('boss_aircraft.png').convert_alpha()

    # For now, create images programmatically
    player_image, enemy_image, boss_image = create_aircraft_images()

except:
    # Fallback to created images
    player_image, enemy_image, boss_image = create_aircraft_images()

# Sound effects (generated)
def create_sound(frequency, duration):
    """Generate a simple beep sound"""
    sample_rate = 22050
    frames = int(sample_rate * duration)
    arr = pygame.sndarray.array("H", pygame.Sound(buffer=bytes(frames * 2)))
    for i in range(frames):
        arr[i] = int(32767 * 0.3 * math.sin(2.0 * math.pi * frequency * i / sample_rate))
    sound = pygame.mixer.Sound(buffer=arr)
    return sound

# Create sound effects
try:
    shoot_sound = create_sound(800, 0.1)
    explosion_sound = create_sound(200, 0.3)
    powerup_sound = create_sound(1200, 0.2)
    boss_sound = create_sound(100, 0.5)
except:
    # If sound creation fails, create dummy sounds
    shoot_sound = pygame.mixer.Sound(buffer=bytes(100))
    explosion_sound = pygame.mixer.Sound(buffer=bytes(100))
    powerup_sound = pygame.mixer.Sound(buffer=bytes(100))
    boss_sound = pygame.mixer.Sound(buffer=bytes(100))

class Particle(pygame.sprite.Sprite):
    """Explosion particle effect"""
    def __init__(self, x, y, vx, vy, color, lifetime=30):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = vx
        self.vy = vy
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.color = color

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.vy += 0.2  # Gravity
        self.lifetime -= 1

        if self.lifetime <= 0:
            self.kill()

        # Fade effect
        alpha = int(255 * (self.lifetime / self.max_lifetime))
        self.image.set_alpha(alpha)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = player_image.copy()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 7
        self.shoot_cooldown = 0
        self.health = 100
        self.max_health = 100
        self.weapon_type = 0  # 0: Single, 1: Dual, 2: Triple, 3: Laser
        self.weapon_levels = [0, 1, 2, 3]

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
            if self.weapon_type == 0:  # Single shot
                bullet = Bullet(self.rect.centerx, self.rect.top, 0)
                all_sprites.add(bullet)
                bullets.add(bullet)
                self.shoot_cooldown = 8
                shoot_sound.play()

            elif self.weapon_type == 1:  # Dual shot
                bullet1 = Bullet(self.rect.centerx - 10, self.rect.top, -2)
                bullet2 = Bullet(self.rect.centerx + 10, self.rect.top, 2)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                self.shoot_cooldown = 10
                shoot_sound.play()

            elif self.weapon_type == 2:  # Triple spread
                bullet1 = Bullet(self.rect.centerx, self.rect.top, 0)
                bullet2 = Bullet(self.rect.centerx - 15, self.rect.top, -3)
                bullet3 = Bullet(self.rect.centerx + 15, self.rect.top, 3)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(bullet3)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(bullet3)
                self.shoot_cooldown = 12
                shoot_sound.play()

            elif self.weapon_type == 3:  # Laser beam
                laser = Laser(self.rect.centerx, self.rect.top)
                all_sprites.add(laser)
                lasers.add(laser)
                self.shoot_cooldown = 5
                shoot_sound.play()

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle_offset=0):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -12
        self.angle_offset = angle_offset

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.angle_offset
        if self.rect.bottom < 0:
            self.kill()

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((8, SCREEN_HEIGHT))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.lifetime = 8

    def update(self):
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = enemy_image.copy()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)
        self.shoot_cooldown = random.randint(40, 120)
        self.health = 20
        self.max_health = 20

    def update(self):
        self.rect.y += self.speed
        self.shoot_cooldown -= 1

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

        if self.shoot_cooldown == 0:
            self.shoot()
            self.shoot_cooldown = random.randint(40, 120)

    def shoot(self):
        enemy_bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(enemy_bullet)
        enemy_bullets.add(enemy_bullet)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.create_explosion()
            self.kill()

    def create_explosion(self):
        for i in range(15):
            angle = (360 / 15) * i
            vx = math.cos(math.radians(angle)) * 3
            vy = math.sin(math.radians(angle)) * 3
            particle = Particle(self.rect.centerx, self.rect.centery, vx, vy, ORANGE, 20)
            all_sprites.add(particle)
            particles.add(particle)
        explosion_sound.play()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = boss_image.copy()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.top = -100
        self.speed = 2
        self.health = 300
        self.max_health = 300
        self.shoot_cooldown = 0
        self.move_direction = 1
        self.movement_timer = 0

    def update(self):
        # Oscillating movement
        self.movement_timer += 1
        if self.movement_timer > 60:
            self.move_direction *= -1
            self.movement_timer = 0

        self.rect.x += self.move_direction * 2

        # Move down until in position
        if self.rect.top < 100:
            self.rect.y += self.speed

        # Keep boss on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        self.shoot_cooldown -= 1

        if self.shoot_cooldown <= 0:
            self.shoot_pattern()
            self.shoot_cooldown = 30

    def shoot_pattern(self):
        # Spread shot
        for angle in range(-30, 31, 15):
            vx = math.sin(math.radians(angle)) * 5
            vy = 5
            enemy_bullet = EnemyBullet(self.rect.centerx + vx * 5, self.rect.bottom, vx, vy)
            all_sprites.add(enemy_bullet)
            enemy_bullets.add(enemy_bullet)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.create_big_explosion()
            self.kill()

    def create_big_explosion(self):
        for i in range(40):
            angle = (360 / 40) * i
            vx = math.cos(math.radians(angle)) * 5
            vy = math.sin(math.radians(angle)) * 5
            particle = Particle(self.rect.centerx, self.rect.centery, vx, vy, PURPLE, 30)
            all_sprites.add(particle)
            particles.add(particle)
        boss_sound.play()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vx=0, vy=5):
        super().__init__()
        self.image = pygame.Surface((7, 12))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, ptype):
        super().__init__()
        self.type = ptype  # 0: health, 1: weapon upgrade, 2: shield

        if ptype == 0:
            self.image = pygame.Surface((20, 20))
            self.image.fill(GREEN)
            pygame.draw.circle(self.image, WHITE, (10, 10), 8)
        elif ptype == 1:
            self.image = pygame.Surface((20, 20))
            self.image.fill(YELLOW)
            pygame.draw.polygon(self.image, WHITE, [(10, 2), (18, 10), (10, 18), (2, 10)])
        else:
            self.image = pygame.Surface((20, 20))
            self.image.fill(CYAN)
            pygame.draw.circle(self.image, WHITE, (10, 10), 8)
            pygame.draw.circle(self.image, CYAN, (10, 10), 4)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
lasers = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
particles = pygame.sprite.Group()
bosses = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Game variables
score = 0
lives = 3
enemy_spawn_rate = 60
spawn_counter = 0
game_over = False
wave = 1
boss_wave = False
boss_health_bar_color = GREEN

# Game loop
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                # Reset game
                game_over = False
                score = 0
                lives = 3
                wave = 1
                boss_wave = False
                enemy_spawn_rate = 60
                all_sprites.empty()
                enemies.empty()
                bullets.empty()
                lasers.empty()
                enemy_bullets.empty()
                powerups.empty()
                particles.empty()
                bosses.empty()
                player = Player()
                all_sprites.add(player)

    if not game_over:
        # Update
        all_sprites.update()

        # Spawn boss at certain waves
        if wave % 5 == 0 and not boss_wave and len(enemies) == 0:
            boss_wave = True
            boss = Boss()
            all_sprites.add(boss)
            bosses.add(boss)

        # Spawn regular enemies
        if not boss_wave:
            spawn_counter += 1
            if spawn_counter >= enemy_spawn_rate:
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)
                spawn_counter = 0
                if enemy_spawn_rate > 25:
                    enemy_spawn_rate -= 0.3

        # Bullet-enemy collisions
        collisions = pygame.sprite.groupcollide(enemies, bullets, False, True)
        for enemy in collisions:
            enemy.take_damage(15)
            score += 10

        # Laser-enemy collisions
        for laser in lasers:
            hit_enemies = pygame.sprite.spritecollide(laser, enemies, False)
            for enemy in hit_enemies:
                enemy.take_damage(5)
                score += 5

        # Bullet-boss collisions
        collisions = pygame.sprite.groupcollide(bosses, bullets, False, True)
        for boss in collisions:
            boss.take_damage(20)
            score += 50

        # Laser-boss collisions
        for laser in lasers:
            hit_bosses = pygame.sprite.spritecollide(laser, bosses, False)
            for boss in hit_bosses:
                boss.take_damage(10)
                score += 25

        # Power-up collisions
        powerup_collisions = pygame.sprite.spritecollide(player, powerups, True)
        for powerup in powerup_collisions:
            if powerup.type == 0:  # Health
                player.health = min(player.health + 30, player.max_health)
                score += 25
            elif powerup.type == 1:  # Weapon upgrade
                player.weapon_type = (player.weapon_type + 1) % 4
                score += 50
            else:  # Shield
                player.health = player.max_health
                score += 75
            powerup_sound.play()

        # Enemy bullet-player collisions
        if pygame.sprite.spritecollide(player, enemy_bullets, True):
            player.take_damage(10)
            if player.health <= 0:
                lives -= 1
                player.health = player.max_health
                if lives <= 0:
                    game_over = True

        # Wave completion
        if len(enemies) == 0 and not boss_wave:
            wave += 1
            enemy_spawn_rate = max(25, 60 - (wave * 3))

        # Boss defeated
        if boss_wave and len(bosses) == 0:
            boss_wave = False
            wave += 1
            score += 500

    # Draw
    screen.fill(BLACK)

    # Draw stars background
    for i in range(20):
        x = (i * 60 + pygame.time.get_ticks() // 20) % SCREEN_WIDTH
        y = (i * 40) % SCREEN_HEIGHT
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 1)

    # Draw sprites
    all_sprites.draw(screen)

    # Draw health bar for player
    pygame.draw.rect(screen, RED, (10, 10, 200, 20))
    pygame.draw.rect(screen, GREEN, (10, 10, int(200 * player.health / player.max_health), 20))
    pygame.draw.rect(screen, WHITE, (10, 10, 200, 20), 2)

    # Draw health bar for boss
    if len(bosses) > 0:
        boss = bosses.sprites()[0]
        boss_bar_width = 300
        pygame.draw.rect(screen, RED, (SCREEN_WIDTH // 2 - boss_bar_width // 2, 10, boss_bar_width, 20))
        pygame.draw.rect(screen, PURPLE, (SCREEN_WIDTH // 2 - boss_bar_width // 2, 10, int(boss_bar_width * boss.health / boss.max_health), 20))
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - boss_bar_width // 2, 10, boss_bar_width, 20), 2)
        boss_text = font_small.render("BOSS AIRCRAFT", True, PURPLE)
        screen.blit(boss_text, (SCREEN_WIDTH // 2 - 60, 35))

    # Draw UI
    score_text = font_medium.render(f"Score: {score}", True, WHITE)
    lives_text = font_medium.render(f"Lives: {lives}", True, WHITE)
    wave_text = font_medium.render(f"Wave: {wave}", True, CYAN)
    weapon_names = ["Single", "Dual", "Triple", "Laser"]
    weapon_text = font_small.render(f"Weapon: {weapon_names[player.weapon_type]}", True, YELLOW)

    screen.blit(score_text, (10, 40))
    screen.blit(lives_text, (10, 85))
    screen.blit(wave_text, (SCREEN_WIDTH - 250, 40))
    screen.blit(weapon_text, (SCREEN_WIDTH - 250, 85))

    # Draw instructions
    if wave == 1 and spawn_counter < 10:
        instructions = font_small.render("Pilot your aircraft! Use ARROW KEYS to move, SPACE to shoot!", True, YELLOW)
        screen.blit(instructions, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 30))

    # Game over screen
    if game_over:
        game_over_text = font_large.render("MISSION FAILED", True, RED)
        final_score_text = font_medium.render(f"Final Score: {score}", True, WHITE)
        final_wave_text = font_medium.render(f"Waves Survived: {wave}", True, WHITE)
        restart_text = font_small.render("Press R to Restart Mission or Q to Quit", True, YELLOW)

        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))
        final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        final_wave_rect = final_wave_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(final_score_text, final_score_rect)
        screen.blit(final_wave_text, final_wave_rect)
        screen.blit(restart_text, restart_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
