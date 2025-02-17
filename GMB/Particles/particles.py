import pygame
import random

from pygame import Vector2


class Trail(pygame.sprite.Sprite):
    def __init__(self, pos, color, win):
        super(Trail, self).__init__()
        self.color = color
        self.win = win

        self.x, self.y = pos
        self.y += 10
        self.dx = random.randint(0, 20) / 10 - 1
        self.dy = -2
        self.size = random.randint(4, 7)
        self.position = Vector2(pos)
        self.position.y += 10
        self.velocity = Vector2(random.uniform(-1, 1), -2)

        self.life = 1.0  # The trail will last until this reaches 0
        self.image = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)


    def update(self):
        self.position += self.velocity
        self.life -= 0.1  # Decrease life
        self.size -= 0.1  # Decrease size

        if self.life <= 0 or self.size <= 0:
            self.kill()
        else:
            self.draw()
        self.x -= self.dx
        self.y -= self.dy
        self.size -= 0.1

        if self.size <= 0:
            self.kill()

        self.rect = pygame.draw.circle(self.win, self.color, (self.x, self.y), self.size)

    def draw(self):
        # Clear the image
        self.image.fill((0, 0, 0, 0))
        # Draw the circle
        pygame.draw.circle(self.image, self.color + (int(255 * self.life),), (self.size, self.size), int(self.size))
        # Update rect
        self.rect = self.image.get_rect(center=self.position)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x,y,pos,win):
        super(Explosion, self).__init__()
        self.win = win
        self.pos = pos
        self.position = Vector2(pos)
        self.velocity = Vector2(random.uniform(-4, 4), random.uniform(-4, 4))
        self.x = x
        self.y = y
        self.size = random.randint(4, 9)
        self.life = 40  # Duration of the explosion
        self.lifetime = 0  # Current age of the explosion

        self.x_vel = random.randrange(-4, 4)
        self.y_vel = random.randrange(-4, 4)

        self.image = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=self.position)
        self.color = (150, 150, 150, 255)  # Explosion color with full alpha

    def update(self, screen_scroll):
        self.lifetime += 1
        if self.lifetime > self.life:
            self.kill()
            return

        # Update position
        self.position += self.velocity + Vector2(screen_scroll, 0)

        # Fade out the explosion
        alpha = max(0, 255 * (1 - self.lifetime / self.life))
        self.color = (self.color[0], self.color[1], self.color[2],int(alpha))

        # Update the size
        self.size = max(0, self.size - 0.2)
        self.image = pygame.transform.scale(self.image, (int(self.size) * 2, int(self.size) * 2))
        self.rect = self.image.get_rect(center=self.position)

        # Update the explosion's appearance
        self.image.fill((0, 0, 0, 0))  # Clear the image
        pygame.draw.rect(self.image, self.color, self.image.get_rect())  # Redraw the explosion

        if self.lifetime <= self.life:
            self.x += self.x_vel + screen_scroll
            self.y += self.y_vel
            s = int(self.size)
            pygame.draw.rect(self.win,self.color,(self.x,self.y, s, s))
        else:
            self.kill()
    def draw(self, surface):
        surface.blit(self.image, self.rect)