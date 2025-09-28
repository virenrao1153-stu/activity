import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2-Player Soccer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 100, 255)
GREEN = (50, 200, 50)

# Ball
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
ball_speed = [5, 5]

# Players
p1 = pygame.Rect(30, HEIGHT//2 - 40, 20, 80)
p2 = pygame.Rect(WIDTH-50, HEIGHT//2 - 40, 20, 80)

# Score
p1_score, p2_score = 0, 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw():
    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, p1)
    pygame.draw.rect(screen, BLUE, p2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    score_text = font.render(f"{p1_score} - {p2_score}", True, BLACK)
    screen.blit(score_text, (WIDTH//2 - 30, 10))
    pygame.display.flip()

def reset_ball():
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_speed[0] *= -1  # Change direction

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Player 1 movement (W/S)
    if keys[pygame.K_w] and p1.top > 0:
        p1.y -= 6
    if keys[pygame.K_s] and p1.bottom < HEIGHT:
        p1.y += 6

    # Player 2 movement (Arrow Up/Down)
    if keys[pygame.K_UP] and p2.top > 0:
        p2.y -= 6
    if keys[pygame.K_DOWN] and p2.bottom < HEIGHT:
        p2.y += 6

    # Move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Bounce ball off top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] *= -1

    # Bounce ball off players
    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_speed[0] *= -1

    # Score points
    if ball.left <= 0:
        p2_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        p1_score += 1
        reset_ball()

    draw()
    clock.tick(60)
