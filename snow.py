import pygame
from random import randint

class Snow:

    def __init__(self):

        """self.xpos = [0,100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                    50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050,
                    25, 125, 225, 325, 425, 525, 625, 725, 825, 925, 1025,
                    75, 175, 275, 375, 475, 575, 675, 775, 875, 975, 1075]"""
        self.xpos = [-200,-75,0, 150, 300, 400, 550, 700, 800,950,1100, 1200]
        self.start_xpos = [-200,-75,0, 150, 300, 400, 550, 700, 800,950,1100, 1200]
        self.ypos = []

        self.image = []
        self.image_rect = []
        for n in range(len(self.xpos)):
            self.ypos.append(randint(-700, 0))
            self.image.append(pygame.image.load("img/bigsnow.gif"))
            self.image_rect.append((self.xpos[n], self.ypos[n], 200,200))

    def update(self, dt):
        for n in range(len(self.image)):
            if(self.ypos[n] > 300 or self.xpos[n] < -400):
                self.ypos[n] = randint(-700, 0)
                self.xpos[n] = self.start_xpos[n]
            self.ypos[n] += dt / 2
            self.xpos[n] -= dt / 4
            self.image_rect[n] = (self.xpos[n], self.ypos[n], 100,100)

    def render(self, screen):
        for n in range(len(self.xpos)):
            screen.blit(self.image[n], self.image_rect[n])
        #screen.blit(self.image[0], self.image_rect[0])
