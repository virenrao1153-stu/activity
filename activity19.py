import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 50, 50)

# Player setup
player = pygame.Rect(WIDTH//2 - 20, HEIGHT - 40, 40, 20)

# Bullets
bullets = []

# Enemies
enemies = []
for i in range(5):
    x = random.randint(0, WIDTH-30)
    y = random.randint(-100, -40)
    enemies.append(pygame.Rect(x, y, 30, 30))

# Score
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Shoot bullet
                bullets.append(pygame.Rect(player.centerx - 5, player.top, 10, 20))

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 6
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 6

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= 7
        if bullet.y < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy.y += 3
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            x = random.randint(0, WIDTH-30)
            y = random.randint(-100, -40)
            enemies.append(pygame.Rect(x, y, 30, 30))

    # Collision detection
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                x = random.randint(0, WIDTH-30)
                y = random.randint(-100, -40)
                enemies.append(pygame.Rect(x, y, 30, 30))
                score += 1
                break

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, player)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Show score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
