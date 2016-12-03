import pygame, player, ground, varg

class Game:
    def __init__(self):
        self.world_x = 0
        self.player = player.Player(490,50)

        self.ground = ground.Ground(300,600,500, 50, )
        self.varg = varg.Varg(300,520,140, 80)


    def check_collision(self):
        if(self.player.get_rect().colliderect(self.ground.get_rect())):
            self.player.set_grounded(True)
        else:
            self.player.set_grounded(False)

    def update(self, dt):
        self.check_collision()
        self.player.update(dt)
        self.ground.update(self.world_x)
        self.varg.update(self.world_x)


    def render(self, screen):
        self.player.render(screen)
        self.ground.render(screen)
        self.varg.render(screen)


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
