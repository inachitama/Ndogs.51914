import pygame
pygame.init()


class Game:
     def __init__(self):
         self.joueur = Joueur()
         self.touche = {}


class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.vie = 20
        self.max_vie = 20
        self.poison = 1
        self.deplacement = 5
        self.image = pygame.image.load("dog.png") # --> mettre l'image du chien
        self.rect = self.image.get_rect()
        self.rect.x = -20
        self.rect.y = 300

    def mouvements_droite(self):
        self.rect.x += self.deplacement

    def mouvements_gauche(self):
        self.rect.x -= self.deplacement


class mechant :
    def __init__(self) :
         self.vie = 10
         self.max_vie = 10
         self.perte_vie = 1
         self.image = pygame.image.load("caca.png") # --> mettre l'image du caca
         self.rect = self.image.get_rect()



#fenetre jeu
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1500, 800))



joueur = Joueur()
game = Game()

running = True
while running :

    fond.blit(game.joueur.image,game.joueur.rect)
     #touche fleche
    if game.touche.get(pygame.K_RIGHT) :
        game.joueur.mouvements_droite()
    elif game.touche.get(pygame.K_LEFT) :
        game.joueur.mouvements_gauche()


    pygame.display.flip()
