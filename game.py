import pygame, player, ground

class Game:
    def __init__(self):
        self.player = player.Player(50,50)

        self.ground = ground.Ground(0,600,400, 50)

    def check_collision(self):
        if(self.player.get_rect().colliderect(self.ground.get_rect())):
            self.player.set_grounded(True)
        else:
            self.player.set_grounded(False)

    def update(self, dt):
        self.check_collision()
        self.player.update(dt)


    def render(self, screen):
        self.player.render(screen)
        self.ground.render(screen)


    def input(self, dt):
        """ User input thingys"""

        key = pygame.key.get_pressed()

        if(key[pygame.K_a]):
            self.player.move_left(dt)
        if(key[pygame.K_d]):
            self.player.move_right(dt)
        if(key[pygame.K_w]):
            self.player.jump(dt)
