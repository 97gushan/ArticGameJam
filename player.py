import pygame

class Player:

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

        self.speed = 1
        self.speed_y = 1

        self.image = pygame.image.load("img/tmp.png")
        self.image_rect = self.image.get_rect()

        self.is_grounded = False

    def render(self, screen):
        screen.blit(self.image, self.image_rect)


    def update(self, dt):
        self.gravity(dt)
        print(self.speed_y)
        self.image_rect.center = (self.xpos,self.ypos)

    def move_right(self, dt):
        self.xpos += self.speed * (1 + dt)

    def move_left(self, dt):
        self.xpos -= self.speed * (1 + dt)

    def gravity(self, dt):

        if(not self.is_grounded):
            self.speed_y += 9.82 / 5000
            self.ypos += self.speed_y * (1 + dt)

    def jump(self, dt):
        if(self.is_grounded):
            self.ypos -= 5
            self.speed_y = -1

    def get_rect(self):
        return self.image_rect

    def set_grounded(self, state):
        self.is_grounded = state
