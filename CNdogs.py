import pygame
pygame.init()


class Game:
     def __init__(self):
         self.joueur = Joueur(self)
          self.all_mechant = pygame.sprite.Group()
         self.touche = {}
          self.spam_mechant()
     def spaw_mechant(self) :
          mechant = Mechant()
          self.all_mechant.add(mechant)

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


class Mechant(pygame.sprite.Sprite) :
    def __init__(self) :
         super().__init__()
         self.vie = 10
         self.max_vie = 10
         self.perte_vie = 1
         self.image = pygame.image.load("caca.png") # --> mettre l'image du caca
         self.rect = self.image.get_rect()
         self.rect.x = 1000
         self.rect.y = 300

    def barre_sante(self) :
         
         



#fenetre jeu
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1500, 800))



joueur = Joueur()
mechant = Mechant{}
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
