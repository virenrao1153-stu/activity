import pygame
import random

pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
MOVEMENT_SPEED = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

# Background
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill((255, 255, 255))

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def _init_(self, color, width, height):
        super()._init_()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

        # Keep inside screen
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

# Sprite group
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('black'), 30, 20)
sprite1.rect.topleft = (
    random.randint(0, SCREEN_WIDTH - sprite1.rect.width),
    random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
)

sprite2 = Sprite(pygame.Color('red'), 30, 20)
sprite2.rect.topleft = (
    random.randint(0, SCREEN_WIDTH - sprite2.rect.width),
    random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
)

all_sprites.add(sprite1, sprite2)

running = True
won = False

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    if won:
        text = font.render("You Win!", True, pygame.Color('black'))
        screen.blit(
            text,
            ((SCREEN_WIDTH - text.get_width()) // 2,
             (SCREEN_HEIGHT - text.get_height()) // 2)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()