import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)

# Player (basket)
basket = pygame.Rect(WIDTH//2 - 40, HEIGHT - 30, 80, 20)

# Ball
ball = pygame.Rect(random.randint(0, WIDTH-20), 0, 20, 20)
ball_speed = 5

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

    # Move basket with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.left > 0:
        basket.x -= 7
    if keys[pygame.K_RIGHT] and basket.right < WIDTH:
        basket.x += 7

    # Move the ball
    ball.y += ball_speed
    if ball.y > HEIGHT:  # Missed ball → reset position
        ball.x = random.randint(0, WIDTH-20)
        ball.y = 0

    # Collision detection
    if basket.colliderect(ball):
        score += 1
        ball.x = random.randint(0, WIDTH-20)
        ball.y = 0

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, basket)
    pygame.draw.ellipse(screen, RED, ball)

    # Show score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
