import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanjiro vs Inosuke - Demon Slayer Fight")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
BLUE = (50, 100, 255)
BROWN = (139, 69, 19)
SKIN = (255, 220, 180)

# Player setup
gravity = 1
jump_strength = 15

players = {
    "tanjiro": {"x": 200, "y": HEIGHT-120, "vy": 0, "on_ground": True,
                "health": 6, "punch": False, "kick": False, "dir": 1},
    "inosuke": {"x": 650, "y": HEIGHT-120, "vy": 0, "on_ground": True,
                "health": 6, "punch": False, "kick": False, "dir": -1}
}

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

def draw_tanjiro(x, y, punching, kicking, facing):
    """Draw stickman styled as Tanjiro"""
    head_radius = 20

    # Head
    pygame.draw.circle(screen, SKIN, (x, y), head_radius)
    pygame.draw.circle(screen, BLACK, (x, y), head_radius, 2)

    # Body with checkered jacket
    pygame.draw.rect(screen, GREEN, (x-15, y+head_radius, 30, 50))

    # Legs
    pygame.draw.line(screen, BLACK, (x, y+head_radius+50),
                     (x-15, y+head_radius+80), 3)
    pygame.draw.line(screen, BLACK, (x, y+head_radius+50),
                     (x+15, y+head_radius+80), 3)

    # Arms
    if punching:
        pygame.draw.line(screen, BLACK, (x, y+head_radius+10),
                         (x + facing*50, y+head_radius+5), 3)
    elif kicking:
        pygame.draw.line(screen, BLACK, (x, y+head_radius+50),
                         (x + facing*40, y+head_radius+70), 3)
    else:
        pygame.draw.line(screen, BLACK, (x, y+head_radius+10),
                         (x-25, y+head_radius+20), 3)
        pygame.draw.line(screen, BLACK, (x, y+head_radius+10),
                         (x+25, y+head_radius+20), 3)

    # Katana
    pygame.draw.line(screen, BLACK, (x, y+head_radius+20),
                     (x + facing*70, y+head_radius+20), 4)

def draw_inosuke(x, y, punching, kicking, facing):
    """Draw stickman styled as Inosuke"""
    head_radius = 20

    # Head (boar mask color)
    pygame.draw.circle(screen, (180, 180, 200), (x, y), head_radius)
    pygame.draw.circle(screen, BLACK, (x, y), head_radius, 2)

    # Body (blue pants + bare chest)
    pygame.draw.rect(screen, SKIN, (x-15, y+head_radius, 30, 25))
    pygame.draw.rect(screen, BLUE, (x-15, y+head_radius+25, 30, 25))

    # Legs
    pygame.draw.line(screen, BLACK, (x, y+head_radius+50),
                     (x-15, y+head_radius+80), 3)
    pygame.draw.line(screen, BLACK, (x, y+head_radius+50),
                     (x+15, y+head_radius+80), 3)

    # Arms
    if punching:
        pygame.draw.line(screen, BLACK, (x, y+head_radius+10),
                         (x + facing*50, y+head_radius+5), 3)
    elif kicking:
        pygame.draw.line(screen, BLACK, (x, y+head_radius+50),
                         (x + facing*40, y+head_radius+70), 3)
    else:
        pygame.draw.line(screen, BLACK, (x, y+head_radius+10),
                         (x-25, y+head_radius+20), 3)
        pygame.draw.line(screen, BLACK, (x, y+head_radius+10),
                         (x+25, y+head_radius+20), 3)

    # Katana
    pygame.draw.line(screen, BROWN, (x, y+head_radius+20),
                     (x + facing*70, y+head_radius+20), 4)

def draw():
    screen.fill(WHITE)

    # Draw Tanjiro
    t = players["tanjiro"]
    draw_tanjiro(t["x"], t["y"], t["punch"], t["kick"], t["dir"])

    # Draw Inosuke
    i = players["inosuke"]
    draw_inosuke(i["x"], i["y"], i["punch"], i["kick"], i["dir"])

    # Health
    t_text = font.render(f"Tanjiro HP: {t['health']}", True, BLACK)
    i_text = font.render(f"Inosuke HP: {i['health']}", True, BLACK)
    screen.blit(t_text, (20, 20))
    screen.blit(i_text, (WIDTH-220, 20))

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
            if event.key == pygame.K_f:
                players["tanjiro"]["punch"] = True
            if event.key == pygame.K_g:
                players["tanjiro"]["kick"] = True
            if event.key == pygame.K_k:
                players["inosuke"]["punch"] = True
            if event.key == pygame.K_l:
                players["inosuke"]["kick"] = True
            if event.key == pygame.K_w and players["tanjiro"]["on_ground"]:
                players["tanjiro"]["vy"] = -jump_strength
                players["tanjiro"]["on_ground"] = False
            if event.key == pygame.K_UP and players["inosuke"]["on_ground"]:
                players["inosuke"]["vy"] = -jump_strength
                players["inosuke"]["on_ground"] = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                players["tanjiro"]["punch"] = False
            if event.key == pygame.K_g:
                players["tanjiro"]["kick"] = False
            if event.key == pygame.K_k:
                players["inosuke"]["punch"] = False
            if event.key == pygame.K_l:
                players["inosuke"]["kick"] = False

    keys = pygame.key.get_pressed()

    # Move Tanjiro (A/D)
    if keys[pygame.K_a]:
        players["tanjiro"]["x"] -= 5
        players["tanjiro"]["dir"] = -1
    if keys[pygame.K_d]:
        players["tanjiro"]["x"] += 5
        players["tanjiro"]["dir"] = 1

    # Move Inosuke (Left/Right)
    if keys[pygame.K_LEFT]:
        players["inosuke"]["x"] -= 5
        players["inosuke"]["dir"] = -1
    if keys[pygame.K_RIGHT]:
        players["inosuke"]["x"] += 5
        players["inosuke"]["dir"] = 1

    # Apply gravity + jumping
    for p in players.values():
        p["y"] += p["vy"]
        if not p["on_ground"]:
            p["vy"] += gravity
        if p["y"] >= HEIGHT-120:
            p["y"] = HEIGHT-120
            p["vy"] = 0
            p["on_ground"] = True

    # Collision (attack range)
    t, i = players["tanjiro"], players["inosuke"]

    if t["punch"] and abs(t["x"] - i["x"]) < 60 and abs(t["y"] - i["y"]) < 60:
        i["health"] -= 1
        t["punch"] = False
    if t["kick"] and abs(t["x"] - i["x"]) < 70 and abs(t["y"] - i["y"]) < 60:
        i["health"] -= 1
        t["kick"] = False

    if i["punch"] and abs(i["x"] - t["x"]) < 60 and abs(i["y"] - t["y"]) < 60:
        t["health"] -= 1
        i["punch"] = False
    if i["kick"] and abs(i["x"] - t["x"]) < 70 and abs(i["y"] - t["y"]) < 60:
        t["health"] -= 1
        i["kick"] = False

    # Game over
    if t["health"] <= 0:
        game_over("Inosuke")
    if i["health"] <= 0:
        game_over("Tanjiro")

    draw()
    clock.tick(60)
