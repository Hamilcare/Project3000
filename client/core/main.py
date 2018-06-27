import pygame
from pygame import locals as const
from game import Game


def main():
    try:
        print("Appuyez sur n'importe quelle touche pour lancer la partie !")
        pygame.init()
        
        ecran = pygame.display.set_mode((800, 600))

        continuer = True
        jeu = Game(ecran)

        while continuer:
            for event in pygame.event.get():
                if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                    # echap ou la croix
                    continuer = 0
                if event.type == const.KEYDOWN:            
                    jeu.start()


            pygame.display.flip()

        pygame.quit()
    except pygame.error:
        print(str(Error))
        pygame.quit()


if __name__ == '__main__':
    main()
