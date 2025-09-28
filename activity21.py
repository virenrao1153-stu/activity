import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2-Player Battle Game")

# Colors
WHITE = (255, 255, 255)
RED = (200, 50, 50)
BLUE = (50, 100, 255)
BLACK = (0, 0, 0)

# Players
player1 = pygame.Rect(100, HEIGHT//2 - 25, 50, 50)
player2 = pygame.Rect(550, HEIGHT//2 - 25, 50, 50)

# Health
p1_health = 5
p2_health = 5
font = pygame.font.SysFont(None, 36)

# Bullets
p1_bullets = []
p2_bullets = []
bullet_speed = 7

clock = pygame.time.Clock()

def draw():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)

    for b in p1_bullets:
        pygame.draw.rect(screen, RED, b)
    for b in p2_bullets:
        pygame.draw.rect(screen, BLUE, b)

    # Show health
    p1_text = font.render(f"P1 Health: {p1_health}", True, BLACK)
    p2_text = font.render(f"P2 Health: {p2_health}", True, BLACK)
    screen.blit(p1_text, (10, 10))
    screen.blit(p2_text, (WIDTH-200, 10))

    pygame.display.flip()

def game_over(winner):
    text = font.render(f"{winner} Wins!", True, BLACK)
    screen.blit(text, (WIDTH//2 - 80, HEIGHT//2 - 20))
    pygame.display.flip()
    pygame.time.wait(2500)
    pygame.quit()
    sys.exit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Player 1 shoot
            if event.key == pygame.K_f:
                p1_bullets.append(pygame.Rect(player1.right, player1.centery - 5, 10, 10))
            # Player 2 shoot
            if event.key == pygame.K_k:
                p2_bullets.append(pygame.Rect(player2.left - 10, player2.centery - 5, 10, 10))

    keys = pygame.key.get_pressed()

    # Player 1 movement (WASD)
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += 5
    if keys[pygame.K_a] and player1.left > 0:
        player1.x -= 5
    if keys[pygame.K_d] and player1.right < WIDTH//2:
        player1.x += 5

    # Player 2 movement (Arrow Keys)
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += 5
    if keys[pygame.K_LEFT] and player2.left > WIDTH//2:
        player2.x -= 5
    if keys[pygame.K_RIGHT] and player2.right < WIDTH:
        player2.x += 5

    # Move bullets
    for b in p1_bullets[:]:
        b.x += bullet_speed
        if b.colliderect(player2):
            p1_bullets.remove(b)
            p2_health -= 1
        elif b.x > WIDTH:
            p1_bullets.remove(b)

    for b in p2_bullets[:]:
        b.x -= bullet_speed
        if b.colliderect(player1):
            p2_bullets.remove(b)
            p1_health -= 1
        elif b.x < 0:
            p2_bullets.remove(b)

    # Check for game over
    if p1_health <= 0:
        game_over("Player 2")
    if p2_health <= 0:
        game_over("Player 1")

    draw()
    clock.tick(60)
