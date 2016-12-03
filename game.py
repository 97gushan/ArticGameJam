import pygame, player, ground, varg, lo

class Game:
    def __init__(self):
        self.world_x = 0
        self.player = player.Player(490,50)

        self.ground = [ground.Ground(300,600,500, 50), ground.Ground(600,300, 200, 50)]
        self.varg = varg.Varg(300,520,140, 80)
        self.lo = lo.Lo(700,520,140, 80)


    def check_collision(self):
        have_collided = 0
        for n in self.ground:
            if(self.player.get_rect()[0].colliderect(n.get_rect())):
                have_collided = 1
            if(self.player.get_rect()[1].colliderect(n.get_rect())):
                have_collided = 2

        if(have_collided == 1):
            self.player.set_speed(0)

        if(have_collided == 2):
            self.player.set_grounded(True)
        else:
            self.player.set_grounded(False)

    def update(self, dt):
        self.check_collision()
        self.player.update(dt)

        for n in self.ground:
            n.update(self.world_x)

        self.varg.update(self.world_x)
        self.lo.update(self.world_x)


    def render(self, screen):
        self.player.render(screen)
        self.varg.render(screen)
        self.lo.render(screen)

        for n in self.ground:
            n.render(screen)


    def input(self, dt):
        """ User input thingys"""

        key = pygame.key.get_pressed()

        if(key[pygame.K_a]):
            self.world_x -= 1
            #self.player.move_left(dt)
        if(key[pygame.K_d]):
            self.world_x += 1
            #self.player.move_right(dt)
        if(key[pygame.K_w]):
            self.player.jump(dt)
