import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

clock = pygame.time.Clock()

# Load images (JPEG)
player_img = pygame.image.load("car.jpeg")
enemy_img = pygame.image.load("enemy.jpeg")

player_img = pygame.transform.scale(player_img, (50, 80))
enemy_img = pygame.transform.scale(enemy_img, (50, 80))

# Player
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 100
player_speed = 6

# Enemy
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_speed = 5

# Road lines
line_y = 0
line_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((50, 50, 50))  # road color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 100:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)
        score += 1
        enemy_speed += 0.3

    # Road animation
    line_y += line_speed
    if line_y > HEIGHT:
        line_y = 0

    for i in range(0, HEIGHT, 100):
        pygame.draw.rect(screen, (255, 255, 255), (195, i + line_y, 10, 50))

    # Collision
    player_rect = pygame.Rect(player_x, player_y, 50, 80)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 80)

    if player_rect.colliderect(enemy_rect):
        running = False

    # Draw
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
print("Game Over! Final Score:", score)