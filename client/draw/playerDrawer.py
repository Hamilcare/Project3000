import pygame
import sys
sys.path.append("../core")
from player import Player
class PlayerDrawer:
    def __init__(self, ecran, image_path, attached_player):
        self.ecran = ecran
        self.image = pygame.image.load(image_path).convert_alpha()
        self.attached_player = attached_player

    def render(self):
        self.ecran.blit(self.image, (self.attached_player.abs, self.attached_player.ord))
