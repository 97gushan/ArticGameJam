import pygame, player, ground, varg

class Game:
    def __init__(self):
        self.world_x = 0
        self.player = player.Player(490,50)

        self.ground = [ground.Ground(300,600,500, 50), ground.Ground(600,300, 200, 50)]
        self.varg = varg.Varg(300,520,140, 80)

        self.prevent_movement = 0


    def check_collision(self):
        roof_collision = False
        ground_collision = False
        left_collision = False
        right_collision = False
        for n in self.ground:
            if(self.player.get_rect()[0].colliderect(n.get_rect())):
                roof_collision = True

            if(self.player.get_rect()[1].colliderect(n.get_rect())):
                ground_collision = True

            if(self.player.get_rect()[2].colliderect(n.get_rect())):
                left_collision = True

            if(self.player.get_rect()[3].colliderect(n.get_rect())):
                right_collision = True


        if(roof_collision):
            self.player.set_speed(0)

        if(ground_collision):
            self.player.set_grounded(True)
        else:
            self.player.set_grounded(False)

        if(left_collision):
            self.prevent_movement = 1
        elif(right_collision):
            self.prevent_movement = 2
        else:
            self.prevent_movement = 0


    def update(self, dt):
        self.check_collision()
        self.player.update(dt)

        for n in self.ground:
            n.update(self.world_x)

        self.varg.update(self.world_x)


    def render(self, screen):
        self.player.render(screen)
        self.varg.render(screen)

        for n in self.ground:
            n.render(screen)


    def input(self, dt):
        """ User input thingys"""

        key = pygame.key.get_pressed()

        if(key[pygame.K_a]):
            if(not self.prevent_movement == 1):
                self.world_x -= 1
            #self.player.move_left(dt)
        if(key[pygame.K_d]):
            if(not self.prevent_movement == 2):
                self.world_x += 1
            #self.player.move_right(dt)
        if(key[pygame.K_w]):
            self.player.jump(dt)
