import pygame

class Lo:

    def __init__(self, xpos, ypos, width, height):
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

    def update(self, world_x):
        self.world_x = world_x
        print(int(self.ypos))
        if int(self.ypos) == 520 or int(self.ypos) == 519:
            self.ypos -= 5
            self.speed = -1.5

        else:
            self.speed += 9.82 / 2500
            self.ypos += self.speed


    def get_rect(self):
        return self.image_rect

    def move_down(self):
        self.ypos += self.speed
