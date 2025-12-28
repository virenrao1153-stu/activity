import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add Sprites")


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def _init_(self, color, x, y):
        super()._init_()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


class Enemy(pygame.sprite.Sprite):
    def _init_(self, color, x, y):
        super()._init_()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)



player = Player(RED, 100, 150)
enemy = Enemy(GREEN, 400, 150)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()
sys.exit()