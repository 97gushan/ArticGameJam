import pygame

from time import clock

class Player:

    def __init__(self, xpos, ypos):
        self.startvalues = [xpos,ypos]
        self.xpos = xpos
        self.ypos = ypos

        self.speed = 0.3
        self.speed_y = 1

        self.image_R1 = pygame.image.load("img/player.png")
        self.image_R2 = pygame.image.load("img/player2.png")
        self.image_L1 = pygame.image.load("img/playerL.png")
        self.image_L2 = pygame.image.load("img/playerL2.png")
        self.image_J = pygame.image.load("img/playerJ.png")
        self.current_image = self.image_R1
        self.is_image1 = True

        self.image_rect = self.current_image.get_rect()
        self.upper_box = (self.xpos, self.ypos, 64, 2)
        self.lower_box = (self.xpos, self.ypos+100, 64, 2)
        self.left_box = (self.xpos- 32, self.ypos -52, 2, 104)
        self.right_box = (self.xpos + 32, self.ypos - 52, 2, 104)

        self.is_grounded = False
        self.tmp = 0

        self.timer = 0
        self.last_time = 0

        self.is_moving = 0

    def reset(self):
        self.xpos = self.startvalues[0]
        self.ypos = self.startvalues[1]
        self.speed_y = 0

    def render(self, screen):
        if(self.is_grounded):
            if(self.is_moving == 1):
                if(self.is_image1):
                    screen.blit(self.image_R1, self.image_rect)
                else:
                    screen.blit(self.image_R2, self.image_rect)
            elif(self.is_moving == -1):
                if(self.is_image1):
                    screen.blit(self.image_L1, self.image_rect)
                else:
                    screen.blit(self.image_L2, self.image_rect)
            else:
                screen.blit(self.image_R1, self.image_rect)
        else:
            screen.blit(self.image_J, self.image_rect)


        self.image_R1 = pygame.transform.scale(self.image_R1,(64, 104))
        self.image_R2 = pygame.transform.scale(self.image_R2,(64, 104))
        self.image_L1 = pygame.transform.scale(self.image_L1,(64, 104))
        self.image_L2 = pygame.transform.scale(self.image_L2,(64, 104))
        self.image_J = pygame.transform.scale(self.image_J,(64, 104))

        pygame.draw.rect(screen, (0,255,255),self.upper_box, 2)
        pygame.draw.rect(screen, (0,255,255),self.lower_box, 2)
        pygame.draw.rect(screen, (0,255,0),self.left_box, 2)
        pygame.draw.rect(screen, (0,255,0),self.right_box, 2)


    def update(self, dt):
        self.gravity(dt)
        #print(self.speed_y)
        self.image_rect.center = (self.xpos-24,self.ypos-36)

        self.upper_box = (self.xpos-30, self.ypos-52, 62, 6)
        self.lower_box = (self.xpos-28, self.ypos+54, 58, 10)
        self.left_box = (self.xpos-42, self.ypos -52, 8, 104)
        self.right_box = (self.xpos + 37, self.ypos - 52, 8, 106)

        self.timer = clock()

        if(self.timer - self.last_time >= 0.5):
            if(self.is_image1):
                self.is_image1 = False
            else:
                self.is_image1 = True
            self.last_time = clock()

    def gravity(self, dt):

        if(not self.is_grounded):
            self.speed_y += 9.82 / 3000 * (1+dt)
            self.ypos += self.speed_y * (1 + dt) * 0.7

    def jump(self, dt):
        if(self.is_grounded):
            self.ypos -= 20
            self.speed_y = -1.5

    def move_left(self, dt):
        self.xpos -= self.speed * (1 + dt)

    def move_right(self, dt):
        self.xpos += self.speed * (1 + dt)

    def get_rect(self):
        return pygame.Rect(self.upper_box), pygame.Rect(self.lower_box), pygame.Rect(self.left_box), pygame.Rect(self.right_box)

    def set_grounded(self, state):
        self.is_grounded = state

    def set_speed(self, speed):
        self.speed_y = speed

    def get_xpos(self):
        return self.xpos

    def set_ypos(self, ypos):
        self.ypos = ypos - 55

    def get_grounded(self):
        return self.is_grounded

    def set_moving(self, direc):
        self.is_moving = direc
