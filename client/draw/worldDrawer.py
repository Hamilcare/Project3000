import pygame
class WorldDrawer:
    def __init__(self, ecran, image_path, world):
        self.ecran = ecran
        self.image = pygame.image.load(image_path).convert_alpha()
        self.world = world

    def render(self):
        self.ecran.blit(self.image, (0, 0))
