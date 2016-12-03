# -*- coding: utf-8 -*-

import sys, pygame
import game
pygame.init()

size = width, height = 400, 400

screen = pygame.display.set_mode(size)

black = 0,0,0

game = game.Game()

while(1):

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()

        game.event(event.type)

    game.update()

    screen.fill(black)

    game.render(screen)

    pygame.display.flip()
