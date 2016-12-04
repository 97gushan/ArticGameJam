import pygame

class Player:

    def __init__(self, xpos, ypos):
        self.startvalues = [xpos,ypos]
        self.xpos = xpos
        self.ypos = ypos

        self.speed = 1
        self.speed_y = 1

        self.image = pygame.image.load("img/player.png")
        self.image_rect = self.image.get_rect()
        self.upper_box = (self.xpos, self.ypos, 64, 2)
        self.lower_box = (self.xpos, self.ypos+100, 64, 2)
        self.left_box = (self.xpos- 32, self.ypos -52, 2, 104)
        self.right_box = (self.xpos + 32, self.ypos - 52, 2, 104)

        self.is_grounded = False
        self.tmp = 0

    def reset(self):
        self.xpos = self.startvalues[0]
        self.ypos = self.startvalues[1]
        self.speed_y = 0

    def render(self, screen):
        screen.blit(self.image, self.image_rect)
        self.image = pygame.transform.scale(self.image,(64, 104))


        pygame.draw.rect(screen, (0,255,255),self.upper_box, 2)
        pygame.draw.rect(screen, (0,255,255),self.lower_box, 2)
        pygame.draw.rect(screen, (0,255,0),self.left_box, 2)
        pygame.draw.rect(screen, (0,255,0),self.right_box, 2)


    def update(self, dt):
        self.gravity(dt)
        #print(self.speed_y)
        self.image_rect.center = (self.xpos-24,self.ypos-36)

        self.upper_box = (self.xpos-30, self.ypos-52, 62, 6)
        self.lower_box = (self.xpos-30, self.ypos+54, 62, 8)
        self.left_box = (self.xpos-40, self.ypos -52, 6, 104)
        self.right_box = (self.xpos + 37, self.ypos - 52, 6, 106)

    def gravity(self, dt):

        if(not self.is_grounded):
            self.speed_y += 9.82 / 7500 * (1+dt)
            self.ypos += self.speed_y * (1 + dt) * 0.3

    def jump(self, dt):
        if(self.is_grounded):
            self.ypos -= 5
            self.speed_y = -1.5

    def move_left(self, dt):
        self.xpos -= 0.2 * (1 + dt)

    def move_right(self, dt):
        self.xpos += 0.2 * (1 + dt)

    def get_rect(self):
        return pygame.Rect(self.upper_box), pygame.Rect(self.lower_box), pygame.Rect(self.left_box), pygame.Rect(self.right_box)

    def set_grounded(self, state):
        self.is_grounded = state

    def set_speed(self, speed):
        self.speed_y = speed

    def get_xpos(self):
        return self.xpos
