import pygame

class Bjorn:

    def __init__(self, xpos, ypos, width, height, bp):
        self.startvalues = [xpos,ypos,width,height]
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height

        self.speed_x = 1

        self.world_x = 0
        self.attacking = False

        self.image = pygame.image.load("img/varg.png")
        self.image_rect = (self.xpos, self.ypos, self.width, self.height)

        self.bp = bp
        self.move_right = True


    def reset(self):
        self.xpos = self.startvalues[0]
        self.ypos = self.startvalues[1]
        self.width = self.startvalues[2]
        self.height = self.startvalues[3]
        self.attacking = False
        self.speed_x = 1

    def render(self, screen):
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.image_rect= (self.xpos - self.world_x, self.ypos, self.width, self.height)

        screen.blit(self.image, self.image_rect)

    def update(self, world_x, dt):
        self.world_x = world_x


        if(self.attacking):
            if(self.xpos <= self.bp):
                self.move_right = True
                self.xpos += self.speed_x * (1+dt)

            elif(self.xpos >= self.bp+1000-self.width):
                self.xpos -= self.speed_x * (1+dt)
                self.move_right = False

            elif self.xpos <= self.bp+1000 -self.width and self.move_right == True:
                self.xpos += self.speed_x * (1+dt)

            else:
                self.xpos -= self.speed_x * (1+dt)

        """    ------------------------------------------------

            if int(self.xpos) <= self.startvalues[0] - 200:
                self.bool1 = True
                self.move_right(dt)

            elif int(self.xpos) >= self.startvalues[0] + 200:
                self.bool1 = False
                self.move_left(dt)

            elif self.xpos < self.startvalues[0] + 200 and self.bool1 == True:
                self.move_right(dt)

            else:
                self.move_left(dt)"""



    def begin_attack(self):
        self.attacking = True

    def attack_pos(self):
        return self.bp+400

    def get_rect(self):
        return self.image_rect
