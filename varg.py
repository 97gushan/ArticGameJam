import pygame

class Varg:

    def __init__(self, xpos, ypos, width, height):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.speed = 0.1
        self.bool1 = True

        self.world_x = 0

        self.image = pygame.image.load("img/varg.png")
        self.image_rect = (self.xpos, self.ypos, self.width, self.height)

    def render(self, screen):
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.image_rect= (self.xpos - self.world_x, self.ypos, self.width, self.height)

        screen.blit(self.image, self.image_rect)

    def update(self, world_x, dt):
        self.world_x = world_x

        if int(self.xpos) == 300:
            self.bool1 = True
            self.move_right(dt)

        elif int(self.xpos) == 500:
            self.bool1 = False
            self.move_left(dt)

        elif self.xpos < 500 and self.bool1 == True:
            self.move_right(dt)

        else:
            self.move_left(dt)

    def get_rect(self):
        return self.image_rect

    def move_right(self, dt):
        self.xpos += self.speed * (1 + dt)

    def move_left(self, dt):
        self.xpos -= self.speed * (1 + dt)
