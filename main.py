# -*- coding: utf-8 -*-

import sys, pygame
import game
pygame.init()

size = width, height = 1000, 700

screen = pygame.display.set_mode(size)

black = 255,255,0

game = game.Game()

delta_time = 0
clock = pygame.time.Clock()

t = pygame.Surface((1000,700))
t.set_alpha(100)
t.fill((0,0,0))


while(1):
    delta_time = float(clock.tick(400))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()


    game.input(delta_time)

    game.update(delta_time)

    screen.fill(black)

    game.render(screen)

    screen.blit(t, (0,0))

    pygame.display.flip()
