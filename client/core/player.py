import pygame
from pygame import locals as const

class Player:
    def __init__(self):
        self.abs = 0
        self.ord = 0
        self.move = 20

    def process_event(self, event: pygame.event):
        if event.key == const.K_w:
            self.ord = self.ord-self.move
            print("going up")
        elif event.key == const.K_s:
            self.ord = self.ord+self.move
            print("going down")
        elif event.key == const.K_a:
            self.abs = self.abs - self.move
        elif event.key == const.K_d:
            self.abs = self.abs + self.move
    
    
