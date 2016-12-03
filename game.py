import pygame, player, ground, varg, lo, jarv

class Game:
    def __init__(self):
        self.world_x = 0
        self.player = player.Player(490,50)

        self.ground = [ground.Ground(300,600,1500, 50), ground.Ground(600,350, 200, 50)]
        self.varg = [varg.Varg(1000,520,140, 80)]
        self.jarv = [jarv.Jarv(1400,520, 140, 80)]
        self.lo = [lo.Lo(700,520,140, 80)]

        self.prevent_movement = 0

    def die(self):
        self.world_x = 0

        for n in self.jarv:
            n.reset()

        self.player.reset()

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
        for n in self.jarv:
            if(self.player.get_xpos() + self.world_x >= n.attack_pos()):
                n.begin_attack()


        # Animal collision-----------------------------------
        for n in self.player.get_rect():
            for m in self.varg:
                if(n.colliderect(m.get_rect())):
                    self.die()

            for m in self.lo:
                if(n.colliderect(m.get_rect())):
                    self.die()

            for m in self.jarv:
                if(n.colliderect(m.get_rect())):
                    self.die()


    def update(self, dt):
        self.check_collision()
        self.player.update(dt)

        for n in self.ground:
            n.update(self.world_x)

        for n in self.varg:
            n.update(self.world_x, dt)

        for n in self.lo:
            n.update(self.world_x, dt)

        for n in self.jarv:
            n.update(self.world_x, dt)

        if self.player.ypos > 650:
            self.die()




    def render(self, screen):
        self.player.render(screen)

        for n in self.varg:
            n.render(screen)

        for n in self.lo:
            n.render(screen)

        for n in self.jarv:
            n.render(screen)

        for n in self.ground:
            n.render(screen)


    def input(self, dt):
        """ User input thingys"""

        key = pygame.key.get_pressed()

        if(key[pygame.K_a]):
            if(not self.prevent_movement == 1 and self.world_x > - 200):
                self.world_x -= 0.2 * (1 + dt)
            #self.player.move_left(dt)
        if(key[pygame.K_d]):
            if(not self.prevent_movement == 2):
                self.world_x += 0.2 * (1 + dt)
            #self.player.move_right(dt)
        if(key[pygame.K_w]):
            self.player.jump(dt)
