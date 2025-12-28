import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("My first game screen")


BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
WHITE = (255, 255, 255)


rect_width = 200
rect_height = 100
rect_x = (WIDTH - rect_width) // 2
rect_y = (HEIGHT - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


font = pygame.font.SysFont(None, 36)
text = font.render("Welcome to Pygame", True, WHITE)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(BLACK)

    
    pygame.draw.rect(screen, BLUE, rectangle)


    screen.blit(text, text_rect)

    
    pygame.display.update()

pygame.quit()
sys.exit()