import sys
import pygame
from pygame import locals as const
sys.path.append("../draw")
from worldDrawer import *
from playerDrawer import *

sys.path.append("../network")
from stubNetwork import NetworkStub

from player import Player



class Game:
    def __init__(self, ecran: pygame.Surface):
        self.ecran = ecran
        self.continuer = True
        self.network_handler = NetworkStub()
        self.player = Player(self.network_handler)
        self.toDraw = [WorldDrawer(ecran,"../content/img/otter.jpg",1), PlayerDrawer(ecran,"../content/img/ant.png",self.player)]
        
    
    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.continuer = True

    """Effectue les draw calls"""
    def update_screen(self):
        for drawable in self.toDraw:
            drawable.render()

    """Gere les inputs"""
    def process_event(self, event: pygame.event):
        if event.type == const.KEYDOWN:
            self.player.process_event(event)
        if event.type == const.QUIT:
            self.continuer = False

    """Appeler par le network handler pour changer la map"""
    def change_map(self, map):
        self.toDraw[0].change_map(map)
    
    def start(self):
        self.prepare()
        self.change_map(self.network_handler.request_map())
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.update_screen()
            
            
            pygame.display.flip()
