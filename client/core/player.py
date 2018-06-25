import pygame
import sys
sys.path.append("../network")
from stubNetwork import StubNetwork
sys.path.append("../utils")
from direction import Direction

from pygame import locals as const

class Player:
    def __init__(self):
        self.abs = 0
        self.ord = 0
        self.move = 20
        self.network_handler = StubNetwork()

    def process_event(self, event: pygame.event):
        if event.key == const.K_w:
            self.request_move(Direction.NORTH)
        if event.key == const.K_s:
            self.request_move(Direction.SOUTH)
        if event.key == const.K_a:
            self.request_move(Direction.WEST)
        if event.key == const.K_d:
            self.request_move(Direction.EAST)
    
    def request_move(self,movement):
        if self.network_handler.request_move(movement):
            self.apply_move(movement)

    def apply_move(self,movement):
        if movement == Direction.NORTH:
            self.ord = self.ord-self.move
        if movement == Direction.SOUTH:
            self.ord = self.ord+self.move
        if movement == Direction.WEST:
            self.abs = self.abs - self.move
        if movement == Direction.EAST:
            self.abs = self.abs+self.move
