import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Custom Event")

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

class Box(pygame.sprite.Sprite):
    def _init_(self, color, x, y):
        super()._init_()
        self.image = pygame.Surface((60, 60))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        if self.color == RED:
            self.color = BLUE
        else:
            self.color = RED
        self.image.fill(self.color)

sprite1 = Box(RED, 150, 170)
sprite2 = Box(BLUE, 350, 170)

sprites = pygame.sprite.Group()
sprites.add(sprite1, sprite2)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill(BLACK)
    sprites.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()