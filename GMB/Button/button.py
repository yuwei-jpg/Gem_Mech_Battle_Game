import pygame


class Button():
    def __init__(self, x, y, image, scale, text=None, xoff=None):
        self.width = int(image.get_width() * scale)
        self.height = int(image.get_height() * scale)
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.text = None
        if text:
            self.text = text
            if xoff:
                self.xoff = xoff
            else:
                self.xoff = self.text.get_width() // 2
            self.yoff = self.text.get_height() // 2

        self.clicked = False

    def draw(self, surface):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                # Add hover effect
            hover_image = pygame.transform.scale(self.image, (int(self.width * 1.1), int(self.height * 1.1)))
            surface.blit(hover_image, hover_image.get_rect(center=self.rect.center))
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:

                clicked_image = pygame.transform.scale(self.image, (int(self.width * 0.95), int(self.height * 0.95)))
                surface.blit(clicked_image, clicked_image.get_rect(center=self.rect.center))
                self.clicked = True
                action = True
        else:

            surface.blit(self.image, (self.rect.x, self.rect.y))
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        surface.blit(self.image, (self.rect.x, self.rect.y))
        if self.text:
            text_surface = self.text
            text_offset = 12

            text_x = self.rect.x + (self.width // 2) - (text_surface.get_width() // 2) + text_offset
            text_y = self.rect.y + (self.height // 2) - (text_surface.get_height() // 2)
            # Draw the text onto the screen surface, not onto the button image
            surface.blit(text_surface, (text_x, text_y))

        return action
