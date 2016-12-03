import pygame

class Lo:

    def __init__(self, xpos, ypos, width, height):
        self.startvalues = [xpos,ypos,width,height]
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.speed = 1
        self.bool1 = True

        self.world_x = 0

        self.image = pygame.image.load("img/lo.png")
        self.image_rect = (self.xpos, self.ypos, self.width, self.height)

    def render(self, screen):
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.image_rect= (self.xpos - self.world_x, self.ypos, self.width, self.height)

        screen.blit(self.image, self.image_rect)

    def reset(self):
        self.xpos = self.startvalues[0]
        self.ypos = self.startvalues[1]
        self.width = self.startvalues[2]
        self.height = self.startvalues[3]

    def update(self, world_x, dt):
        self.world_x = world_x
        if int(self.ypos) <= 520 and int(self.ypos) >= 518:
            self.ypos -= 5
            self.speed = -1

        else:
            self.speed += 9.82 / 1500
            self.ypos += self.speed * (1 + dt) * 0.3


    def get_rect(self):
        return self.image_rect

    def move_down(self):
        self.ypos += self.speed
