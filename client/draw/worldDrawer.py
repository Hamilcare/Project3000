import pygame
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


class WorldDrawer:
    def __init__(self, ecran, image_path, world):
        self.ecran = ecran
        self.image = pygame.image.load(image_path).convert_alpha()
        self.world = world #Objet world a créer si besoin
        self.world_map = None #Dans le mvp, une string contenant des coordonnées de rectangle stocke ici sous la forme d'un tableau 2D"""

    def render(self):
        self.ecran.blit(self.image, (0, 0))
        if self.world_map is not None :
            print('drawing world map')
            for rect in self.world_map:
                pygame.draw.rect(self.ecran, RED, rect)                




    #Reçoit la map sous forme de string et la parse pour en faire un [][]
    def change_map(self,world_map):
        tmp_rows = world_map.split('!')
        new_map = [[0 for x in range(4)] for y in range(len(tmp_rows))]
        for i in range(len(tmp_rows)):
            current_row = tmp_rows[i].split(' ')
            new_map[i][0] = int(current_row[0])
            new_map[i][1] = int(current_row[1])
            new_map[i][2] = int(current_row[2])
            new_map[i][3] = int(current_row[3])

        self.world_map = new_map
        print(self.world_map)
    
