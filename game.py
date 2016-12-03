import pygame, player

class Game:
    def __init__(self):
        self.player = player.Player(50,50)

    def update(self):
        self.player.update()


    def render(self, screen):
        self.player.render(screen)


    def event(self, type):
        """ User input thingys"""
        pass
