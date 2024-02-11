import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60
PLAYER_SIZE = 30
OBSTACLE_WIDTH = 40
OBSTACLE_HEIGHT = 300
OBSTACLE_GAP = 200
HEALTH_BAR_WIDTH = 200
HEALTH_BAR_HEIGHT = 20
MAX_HEALTH = 100
HEALTH_REGEN_TIME = 2000  # 2 seconds in milliseconds
GAME_DURATION = 180000  # 3 minutes in milliseconds
HEAD_START_TIME = 3000  # 3 seconds in milliseconds
INITIAL_OBSTACLE_SPEED = 2  # Initial speed of obstacles
MAX_OBSTACLE_SPEED = 10  # Maximum speed of obstacles
SPEED_INCREASE_INTERVAL = 5000  # Increase speed every 5 seconds
MOVE_BACK_AMOUNT = 5  # Number of moves back when hit an obstacle
HEALTH_LOST = 2  # Health lost when hitting an obstacle

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level 4")

# Load images
player_image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player_image.fill(RED)
obstacle_image = pygame.Surface((OBSTACLE_WIDTH, HEIGHT))
obstacle_image.fill(GREEN)

# Load background image
background_image = pygame.image.load(os.path.join('assets/BG1.png')).convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load moon image
moon_image = pygame.image.load(os.path.join('assets/moon.png')).convert_alpha()
moon_image = pygame.transform.scale(moon_image, (260, 170))  # Scale down the moon image

# Fonts
font = pygame.font.Font(None, 36)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        self.velocity = 0
        self.health = MAX_HEALTH
        self.last_hit_time = 0

    def update(self):
        self.velocity += 0.5
        self.rect.centery += self.velocity

        # Gravity
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

        # Health regeneration
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit_time >= HEALTH_REGEN_TIME and self.health < MAX_HEALTH:
            self.health += 1

    def jump(self):
        self.velocity = -10

    def reduce_health(self):
        self.health -= HEALTH_LOST
        self.last_hit_time = pygame.time.get_ticks()

    def move_back(self):
        self.rect.x -= MOVE_BACK_AMOUNT

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, y, top=True):
        super().__init__()
        self.image = obstacle_image
        gap_size = 30  # Adjust the gap size as needed
        if top:
            self.rect = self.image.get_rect(midbottom=(WIDTH + OBSTACLE_WIDTH // 2, y - gap_size // 2))
        else:
            self.rect = self.image.get_rect(midtop=(WIDTH + OBSTACLE_WIDTH // 2, y + gap_size // 2))
        self.speed = INITIAL_OBSTACLE_SPEED

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

def increase_speed():
    for obstacle in obstacles:
        obstacle.speed += 0.1

# Create groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Timer variables
start_time = pygame.time.get_ticks()
speed_increase_time = pygame.time.get_ticks()

# Load floor image
floor_image = pygame.image.load(os.path.join('Tiles/8.png')).convert()
floor_image = pygame.transform.scale(floor_image, (10, 10))  # Scale the floor image

# Determine the number of tiles needed to cover the width of the screen
num_tiles = WIDTH // floor_image.get_width() + 2

# Calculate the total width of the tiles
total_tiles_width = num_tiles * floor_image.get_width()

# Game loop
running = True
game_over = False
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            # Check if the user clicked the button to restart the game
            if WIDTH - 170 <= event.pos[0] <= WIDTH - 20 and HEIGHT - 70 <= event.pos[1] <= HEIGHT - 20:
                game_over = False
                all_sprites.empty()
                obstacles.empty()
                player = Player()
                all_sprites.add(player)
                start_time = pygame.time.get_ticks()
                speed_increase_time = pygame.time.get_ticks()
                continue

    # Provide a 3-second head start
    current_time = pygame.time.get_ticks()
    if current_time - start_time < HEAD_START_TIME:
        remaining_time = (HEAD_START_TIME - (current_time - start_time)) // 1000 + 1
        screen.fill(BLACK)
        text_surface = font.render(f"Starting in {remaining_time}...", True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
        continue

    # Spawn obstacles
    if len(obstacles) == 0 or obstacles.sprites()[-1].rect.right < WIDTH - OBSTACLE_GAP:
        obstacle_y = random.randint(HEIGHT // 4, HEIGHT - OBSTACLE_GAP - HEIGHT // 4)
        top_obstacle_y = obstacle_y - OBSTACLE_GAP // 30  # Adjust for the top obstacle
        top_obstacle = Obstacle(top_obstacle_y, top=True)
        bottom_obstacle = Obstacle(obstacle_y + OBSTACLE_GAP // 2, top=False)
        obstacles.add(top_obstacle, bottom_obstacle)
        all_sprites.add(top_obstacle, bottom_obstacle)

    # Update sprites
    all_sprites.update()

    # Collision detection
    hits = pygame.sprite.spritecollide(player, obstacles, False)
    if hits:
        player.reduce_health()
        player.move_back()

    # Check for game over
    if player.health <= 0 or pygame.time.get_ticks() - start_time >= GAME_DURATION:
        game_over = True

    # Increase obstacle speed over time
    if pygame.time.get_ticks() - speed_increase_time >= SPEED_INCREASE_INTERVAL:
        increase_speed()
        speed_increase_time = pygame.time.get_ticks()

    # Draw everything
    screen.blit(background_image, (0, 0))

    # Draw moon image
    screen.blit(moon_image, (10, 10))

    # Draw floor tiles
    for i in range(num_tiles):
        screen.blit(floor_image, (i * floor_image.get_width(), HEIGHT - floor_image.get_height()))

    all_sprites.draw(screen)

    # Draw health bar
    pygame.draw.rect(screen, GREEN, (10, 10, player.health * HEALTH_BAR_WIDTH // MAX_HEALTH, HEALTH_BAR_HEIGHT))
    pygame.draw.rect(screen, WHITE, (10, 10, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT), 2)

    # Draw timer
    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = max(0, GAME_DURATION - elapsed_time)
    timer_text = font.render(f"Time: {remaining_time // 1000}", True, WHITE)
    screen.blit(timer_text, (WIDTH - timer_text.get_width() - 10, 10))

    # Draw restart button
    if game_over:
        pygame.draw.rect(screen, GREEN, (WIDTH - 170, HEIGHT - 70, 150, 50))
        restart_text = font.render("Restart", True, WHITE)
        restart_text_rect = restart_text.get_rect(center=(WIDTH - 95, HEIGHT - 45))
        screen.blit(restart_text, restart_text_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()