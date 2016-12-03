import pygame, player, ground, varg, lo
import pygame, player, ground, varg, jarv

class Game:
    def __init__(self):
        self.world_x = 0
        self.player = player.Player(490,50)

        self.ground = [ground.Ground(300,600,1500, 50), ground.Ground(600,350, 200, 50)]
        self.varg = varg.Varg(10000,520,140, 80)
        self.jarv = jarv.Jarv(1400,520, 140, 80)
        self.ground = [ground.Ground(300,600,1500, 50), ground.Ground(600,350, 200, 50)]
        self.varg = varg.Varg(300,520,140, 80)
        self.lo = lo.Lo(700,520,140, 80)

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
            self.player.set_speed(0.1)

        if(ground_collision):
            self.player.set_grounded(True)
            self.player.set_speed(0)
        else:
            self.player.set_grounded(False)

        if(left_collision):
            self.prevent_movement = 1
        elif(right_collision):
            self.prevent_movement = 2
        else:
            self.prevent_movement = 0

        # Kolla om spelaren
        if(self.player.get_xpos() + self.world_x >= self.jarv.attack_pos()):
            self.jarv.begin_attack()


    def update(self, dt):
        self.check_collision()
        self.player.update(dt)

        for n in self.ground:
            n.update(self.world_x)

        self.varg.update(self.world_x, dt)
        self.lo.update(self.world_x, dt)

        self.jarv.update(self.world_x, dt)


    def render(self, screen):
        self.player.render(screen)
        self.varg.render(screen)
        self.lo.render(screen)
        self.jarv.render(screen)

        for n in self.ground:
            n.render(screen)


    def input(self, dt):
        """ User input thingys"""

        key = pygame.key.get_pressed()

        if(key[pygame.K_a]):
            if(not self.prevent_movement == 1 and self.world_x > 0):
                self.world_x -= 0.2 * (1 + dt)
            #self.player.move_left(dt)
        if(key[pygame.K_d]):
            if(not self.prevent_movement == 2):
                self.world_x += 0.2 * (1 + dt)
            #self.player.move_right(dt)
        if(key[pygame.K_w]):
            self.player.jump(dt)
