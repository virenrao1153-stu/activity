import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My first game screen")

GREY = (58, 58, 58)

image = pygame.image.load("image.png")   
image = pygame.transform.scale(image, (300, 300))

image_rect = image.get_rect()
image_rect.center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GREY)

    screen.blit(image, image_rect)

    pygame.display.update()

pygame.quit()
sys.exit()