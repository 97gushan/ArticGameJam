# -*- coding: utf-8 -*-

import sys, pygame
import game
pygame.init()

size = width, height = 1366, 768

screen = pygame.display.set_mode(size)
pygame.display.toggle_fullscreen()

black = 255,255,0

game = game.Game()

delta_time = 0
clock = pygame.time.Clock()

t = pygame.Surface((width,height))
t.set_alpha(180)
t.fill((0,0,0))

image = pygame.image.load("img/miljo.png")
image = pygame.transform.scale(image,(width, height))

while(1):
    delta_time = float(clock.tick(400))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()


    game.input(delta_time)

    game.update(delta_time)

    screen.blit(image,(0,0,width,height))


    game.render(screen)

    screen.blit(t, (0,0))

    pygame.display.flip()
