import math
import pygame
from GMB.Particles.particles import Explosion

WIDTH, HEIGHT = 640, 384

pygame.mixer.init()
grenade_blast_fx = pygame.mixer.Sound('Sounds/grenade blast.wav')
grenade_blast_fx.set_volume(0.6)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, color, type_, win):
        super(Bullet, self).__init__()

        self.x = x
        self.y = y
        self.direction = direction
        self.color = color
        self.type = type_
        self.win = win

        self.speed = 10
        self.radius = 4
        # Create a surface for the bullet
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (4, 4), 4)

        # Use the image's rect for positioning
        self.rect = self.image.get_rect(center=(x, y))

        # self.rect = pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)

    def update(self, screen_scroll, world):
        if self.direction == -1:
            self.x -= self.speed + screen_scroll
        if self.direction == 0 or self.direction == 1:
            self.x += self.speed + screen_scroll
        if self.rect.right < 0 or self.rect.left > WIDTH or self.collide(world):
            self.kill()
        self.rect = pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)

    def collide(self, world):
        # Check collision with world objects
        for tile in world.ground_list + world.rock_list:
            if self.rect.colliderect(tile[1]):
                return True
        return False


class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, win):
        super(Grenade, self).__init__()

        self.x = x
        self.y = y
        self.direction = direction
        self.win = win
        self.pos = 0
        self.speed = 10
        self.vel_y = -11
        self.timer = 15
        self.radius = 4

        if self.direction == 0:
            self.direction = 1

        pygame.draw.circle(self.win, (200, 200, 200), (self.x, self.y), self.radius + 1)
        self.rect = pygame.draw.circle(self.win, (255, 50, 50), (self.x, self.y), self.radius)
        pygame.draw.circle(self.win, (0, 0, 0), (self.x, self.y), 1)

    def update(self, screen_scroll, p, enemy_group, explosion_group, world):
        self.vel_y += 1
        dx = self.direction * self.speed
        dy = self.vel_y
        hit_enemies = pygame.sprite.spritecollide(self, enemy_group, False)
        if hit_enemies:
            for enemy in hit_enemies:
                enemy.health -= 100  # Adjust damage as necessary
                self.explode(explosion_group)

        # Explode if timer runs out without hitting anything
        if self.timer <= 0:
            self.explode(explosion_group)
        for tile in world.ground_list:
            if tile[1].colliderect(self.rect.x, self.rect.y, self.rect.width, self.rect.height):
                if self.rect.y <= tile[1].y:
                    dy = 0
                    self.speed -= 1
                    if self.speed <= 0:
                        self.speed = 0

        for tile in world.rock_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                self.direction *= -1
                dx = self.direction * self.speed
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                if self.rect.y <= tile[1].y:
                    dy = 0
                    self.speed -= 1
                    if self.speed <= 0:
                        self.speed = 0

        if self.rect.y > WIDTH:
            self.kill()

        if self.speed == 0:
            self.timer -= 1
            if self.timer <= 0:
                grenade_blast_fx.play()
                for _ in range(30):
                    explosion = Explosion(self.rect.centerx,self.rect.centery,self.rect.center,self.win)
                    # explosion = Explosion(self.x, self.y, self.win)
                    explosion_group.add(explosion)

                p_distance = math.sqrt((p.rect.centerx - self.x) ** 2 + (p.rect.centery - self.y) ** 2)
                if p_distance <= 100:
                    if p_distance > 80:
                        p.health -= 20
                    elif p_distance > 40:
                        p.health -= 50
                    elif p_distance >= 0:
                        p.health -= 80
                    p.hit = True

                self.kill()

        self.x += dx + screen_scroll
        self.y += dy

        pygame.draw.circle(self.win, (200, 200, 200), (self.x, self.y), self.radius + 1)
        self.rect = pygame.draw.circle(self.win, (255, 50, 50), (self.x, self.y), self.radius)
        pygame.draw.circle(self.win, (0, 0, 0), (self.x, self.y), 1)

    def explode(self, explosion_group):
        grenade_blast_fx.play()

        # Create an explosion
        explosion = Explosion(self.rect.centerx,self.rect.centery,self.rect.center,self.win)

        explosion_group.add(explosion)

        self.kill()