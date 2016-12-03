# -*- coding: utf-8 -*-

import sys, pygame
import game
pygame.init()

size = width, height = 1000, 700

screen = pygame.display.set_mode(size)

black = 0,0,0

game = game.Game()

delta_time = 0
clock = pygame.time.Clock()

while(1):
    delta_time = clock.tick(400)/1000


    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()


    game.input(delta_time)

    game.update(delta_time)

    screen.fill(black)

    game.render(screen)

    pygame.display.flip()
