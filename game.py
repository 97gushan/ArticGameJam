import pygame, player, ground, varg, lo, jarv, bjorn, snow
from time import clock

class Game:
    def __init__(self):
        self.world_x = 5500
        self.player = player.Player(500,590)

        self.boss_position = 10000
        self.boss_battle = False

        self.ground = [
        #bottom:


        #flying
        ground.Ground(200,450, 200, 50),
        ground.Ground(400,250, 200, 50),
        ground.Ground(800,450, 200, 50),
        ground.Ground(200*11-150,500, 200, 50),
        ground.Ground(4000,450, 200, 50),
        ground.Ground(4400,350, 200, 50),
        ground.Ground(4600,550, 200, 50),
        ground.Ground(5000,350, 200, 50),
        ground.Ground(5500,600, 200, 50),
        ground.Ground(7600,450, 200, 50),
        ground.Ground(8200,380, 200, 50),

                    #bossplatforms
                       ground.Ground(self.boss_position+100, 450, 200, 50),
                       ground.Ground(self.boss_position+700, 450, 200, 50),
                       ground.Ground(self.boss_position+400, 250, 200, 50)]

        for n in range(0,100):
            self.ground.append(ground.Ground(200*n,650,200, 50))

        self.ground.pop(len(self.ground)-96)
        self.ground.pop(len(self.ground)-95)
        self.ground.pop(len(self.ground)-91)
        self.ground.pop(len(self.ground)-90)
        self.ground.pop(len(self.ground)-89)
        for n in range(10):
            self.ground.pop(len(self.ground)-(80-n))
        self.ground.pop(len(self.ground)-68)








        self.lo = [lo.Lo(600,580,140, 80),lo.Lo(7200,580,140, 80)]
        self.bjorn = bjorn.Bjorn(11000, 410,140, 80, self.boss_position)

        self.boss_battle_ground = []
        self.bear_health = 3

        self.varg = [varg.Varg(1400,580,140, 80),varg.Varg(6800,580,140, 80)]
        self.jarv = [jarv.Jarv(3800,580, 140, 80),jarv.Jarv(8500,580, 140, 80)]


        self.prevent_movement = 0

        self.victory = False
        self.victory_img = pygame.image.load("img/winwin.png")
        self.victory_rect = self.victory_img.get_rect()

        self.hit_time = 0
        self.current_time = 0
        self.world_speed = 0.3

        #self.snow = snow.Snow()



    def die(self):
        #self.world_x = 0

        for n in self.jarv:
            n.reset()
        for n in self.lo:
            n.reset()
        for n in self.varg:
            n.reset()

        #self.player.reset()
        self.boss_battle = False
        self.bjorn.reset()
        self.bear_health = 3

    def check_collision(self,dt):
        roof_collision = False
        ground_collision = False
        left_collision = False
        right_collision = False

        ground = -1

        for n in self.ground:
            if(self.player.get_rect()[0].colliderect(n.get_rect())):
                roof_collision = True

            if(self.player.get_rect()[1].colliderect(n.get_rect())):
                ground_collision = True
                ground = n

            if(self.player.get_rect()[2].colliderect(n.get_rect())):
                left_collision = True

            if(self.player.get_rect()[3].colliderect(n.get_rect())):
                right_collision = True



        if(roof_collision):
            self.player.set_speed(0.1)

        if(ground_collision and not self.player.get_grounded()):
            self.player.set_grounded(True)
            self.player.set_speed(0)
            self.player.set_ypos(ground.get_ypos())

        elif(not ground_collision and self.player.get_grounded()):
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


        if(self.player.get_xpos() + self.world_x >= self.bjorn.attack_pos()):
            self.bjorn.begin_attack()

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


        # bear collisions
        self.current_time = clock()

        if self.player.get_rect()[1].colliderect(self.bjorn.get_rect()) and self.current_time - self.hit_time >= 0.1:
            self.player.set_grounded(True)
            self.player.jump(dt)
            self.player.set_grounded(False)
            self.bear_health -= 1
            self.hit_time = clock()

            if(self.bear_health == 0):
                print("CONGRATIOPSNAIONS!!!!")
                self.victory = True

        elif(self.player.get_rect()[0].colliderect(self.bjorn.get_rect()) or
            self.player.get_rect()[2].colliderect(self.bjorn.get_rect()) or
            self.player.get_rect()[3].colliderect(self.bjorn.get_rect())):
            self.die()

    def update(self, dt):
        self.check_collision(dt)
        self.player.update(dt)

        for n in self.ground:
            n.update(self.world_x)


        for n in self.varg:
            n.update(self.world_x, dt)

        for n in self.lo:
            n.update(self.world_x, dt)

        for n in self.jarv:
            n.update(self.world_x, dt)

        self.bjorn.update(self.world_x,dt)

        if self.player.ypos > 1050:
            self.die()


        if(self.world_x >= self.boss_position):
            self.boss_battle = True

        #self.snow.update(dt)


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

        self.bjorn.render(screen)

        if(self.victory):
            screen.blit(self.victory_img, self.victory_rect)

        #self.snow.render(screen)
    def input(self, dt):
        """ User input thingys"""

        key = pygame.key.get_pressed()

        if(key[pygame.K_a]):
            if(self.boss_battle):
                if(not self.prevent_movement == 1 and self.player.get_xpos() + self.world_x - 25 > self.boss_position):
                    self.player.move_left(dt)

            elif(not self.prevent_movement == 1 and self.world_x > - 400):
                self.world_x -= self.world_speed * (1 + dt)
        if(key[pygame.K_d]):
            if(self.boss_battle):
                if(not self.prevent_movement == 2 and self.player.get_xpos() + self.world_x + 25 < self.boss_position + 1000):
                    self.player.move_right(dt)

            elif(not self.prevent_movement == 2):
                self.world_x += self.world_speed * (1 + dt)
        if(key[pygame.K_w]):
            self.player.jump(dt)
