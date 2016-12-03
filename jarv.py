import pygame

class Jarv:

    def __init__(self, xpos, ypos, width, height):
        self.startvalues = [xpos,ypos,width,height]
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

        self.speed_x = 0

        self.world_x = 0
        self.attacking = False

        self.image = pygame.image.load("img/varg.png")
        self.image_rect = (self.xpos, self.ypos, self.width, self.height)

    def reset(self):
        self.xpos = self.startvalues[0]
        self.ypos = self.startvalues[1]
        self.width = self.startvalues[2]
        self.height = self.startvalues[3]
        self.attacking = False
        self.speed_x = 0

    def render(self, screen):
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.image_rect= (self.xpos - self.world_x, self.ypos, self.width, self.height)

        screen.blit(self.image, self.image_rect)

    def update(self, world_x):
        self.world_x = world_x

        self.xpos -= self.speed_x

        if(self.attacking):

            self.speed_x = 2

    def begin_attack(self):
        self.attacking = True

    def get_rect(self):
        return self.image_rect

    def attack_pos(self):
        return self.xpos - 400
