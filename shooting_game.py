import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player
player_width = 50
player_height = 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Bullet
bullets = []
bullet_speed = 7

# Enemy
enemy_width = 40
enemy_height = 30
enemies = []
enemy_speed = 2

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:
            bullets.append([player_x + player_width // 2, player_y])

    # Update bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Spawn enemies
    if random.randint(1, 50) == 1:
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemies.append([enemy_x, 0])

    # Update enemies
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Check collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (
                enemy[0] < bullet[0] < enemy[0] + enemy_width
                and enemy[1] < bullet[1] < enemy[1] + enemy_height
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (bullet[0], bullet[1]), 5)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_width, enemy_height))

    # Draw score
    draw_text(f"Score: {score}", 10, 10)

    # Update display
    pygame.display.flip()

# Quit game
pygame.quit()
sys.exit()
# End of the game loop