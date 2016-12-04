import pygame

class Varg:

    def __init__(self, xpos, ypos, width, height):
        self.startvalues = [xpos,ypos,width,height]
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.speed = 0.1
        self.bool1 = True

        self.world_x = 0

        self.image = pygame.image.load("img/varg.png")
        self.image2 = pygame.image.load("img/vargL.png")
        self.image_rect = (self.xpos, self.ypos, self.width, self.height)

    def reset(self):
        self.xpos = self.startvalues[0]
        self.ypos = self.startvalues[1]
        self.width = self.startvalues[2]
        self.height = self.startvalues[3]

    def render(self, screen):
        self.image_rect= (self.xpos - self.world_x, self.ypos, self.width, self.height)
        if self.bool1:
            self.image = pygame.transform.scale(self.image,(self.width, self.height))
            screen.blit(self.image, self.image_rect)
        else:
            self.image2 = pygame.transform.scale(self.image2,(self.width, self.height))
            screen.blit(self.image2, self.image_rect)



    def update(self, world_x, dt):
        self.world_x = world_x

        if int(self.xpos) <= self.startvalues[0] - 200:
            self.bool1 = True
            self.move_right(dt)

        elif int(self.xpos) >= self.startvalues[0] + 200:
            self.bool1 = False
            self.move_left(dt)

        elif self.xpos < self.startvalues[0] + 200 and self.bool1 == True:
            self.move_right(dt)

        else:
            self.move_left(dt)

    def get_rect(self):
        return self.image_rect

    def move_right(self, dt):
        self.xpos += self.speed * (1 + dt)

    def move_left(self, dt):
        self.xpos -= self.speed * (1 + dt)
