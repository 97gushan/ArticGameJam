import pygame

class Player:

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

        self.speed = 1
        self.speed_y = 1

        self.image = pygame.image.load("img/tmp.png")
        self.image_rect = self.image.get_rect()
        self.upper_box = (self.xpos, self.ypos, 50, 2)
        self.lower_box = (self.xpos, self.ypos+50, 50, 2)
        self.left_box = (self.xpos- 27, self.ypos -20, 2, 44)
        self.right_box = (self.xpos + 23, self.ypos - 20, 2, 44)

        self.is_grounded = False
        self.tmp = 0

    def render(self, screen):
        screen.blit(self.image, self.image_rect)

        pygame.draw.rect(screen, (0,255,255),self.upper_box, 2)
        pygame.draw.rect(screen, (0,255,255),self.lower_box, 2)
        pygame.draw.rect(screen, (0,255,0),self.left_box, 2)
        pygame.draw.rect(screen, (0,255,0),self.right_box, 2)


    def update(self, dt):
        self.gravity(dt)
        #print(self.speed_y)
        self.image_rect.center = (self.xpos,self.ypos)

        self.upper_box = (self.xpos-25, self.ypos-25, 50, 2)
        self.lower_box = (self.xpos-25, self.ypos+25, 50, 2)
        self.left_box = (self.xpos- 27, self.ypos -25, 2, 48)
        self.right_box = (self.xpos + 25, self.ypos -25, 2, 48)

    def gravity(self, dt):

        if(not self.is_grounded):
            self.speed_y += 9.82 / 2500
            self.ypos += self.speed_y * (1 + dt)

    def jump(self, dt):
        if(self.is_grounded):
            self.ypos -= 5
            self.speed_y = -1.5

    def get_rect(self):
        return pygame.Rect(self.upper_box), pygame.Rect(self.lower_box), pygame.Rect(self.left_box), pygame.Rect(self.right_box)

    def set_grounded(self, state):
        self.is_grounded = state

    def set_speed(self, speed):
        self.speed_y = speed
