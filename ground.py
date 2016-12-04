import pygame

class Ground:

    def __init__(self, xpos, ypos, width, height):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

        self.world_x = 0

        self.image = pygame.image.load("img/ledge.png")
        self.image_rect = (self.xpos, self.ypos, self.width, self.height)

    def render(self, screen):
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.image_rect = (self.xpos - self.world_x, self.ypos, self.width, self.height)

        screen.blit(self.image, self.image_rect)

    def update(self, world_x):
        self.world_x = world_x

    def get_rect(self):
        return self.image_rect

    def get_ypos(self):
        return self.ypos

    def get_xpos(self):
        return self.xpos

    def get_width(self):
        return self.width
