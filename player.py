import pygame

class Player:

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

        self.image = pygame.image.load("test.png")
        self.image_rect = self.image.get_rect()

    def render(self, screen):
        screen.blit(self.image, self.image_rect)


    def update(self):
        self.image_rect.center = (self.xpos,self.ypos)
        self.xpos += 0.1
