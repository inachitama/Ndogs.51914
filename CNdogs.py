import pygame

pygame.init()


class Game:
    def __init__(self):
        self.all_joueur = pygame.sprite.Group()
        self.joueur = Joueur(self)
        self.all_joueur.add(self.joueur)
        self.all_mechant = pygame.sprite.Group()
        self.touche = {}
        self.spaw_mechant()

    def spaw_mechant(self):
         mechant = Mechant(self)
         self.all_mechant.add(mechant)


class Joueur(pygame.sprite.Sprite):
    def __init__(self,game ):
        super().__init__()
        self.game = game
        self.vie = 20
        self.max_vie = 20
        self.poison = 1
        self.deplacement = 5
        self.image = pygame.image.load("dog.png")  # --> mettre l'image du chien
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300

    def mouvements_droite(self):
        self.rect.x += self.deplacement

    def mouvements_gauche(self):
        self.rect.x -= self.deplacement


class Mechant(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.vie = 10
        self.max_vie = 10
        self.perte_vie = 1
        self.image = pygame.image.load("caca.png")  # --> mettre l'image du caca
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 300
    def forward(self):
        pass

    def barre_sante(self,surface):
        bar_color = (45, 212, 21)
        back_color = (240, 14, 14)

        bar_position = [self.rect.x + 10 , self.rect.y - 20,self.vie,5]
        back_bar_position = [self.rect.x +10,self.rect.y -20,self.max_vie,5]


        pygame.draw.rect(surface,back_color,back_bar_position)
        pygame.draw.rect(surface,bar_color,bar_position)



# fenetre jeu
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1500, 800))
game = Game()


running = True
while running:
    fond.fill((255,255,255))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            game.touche[event.key] = True
        if event.type == pygame.KEYUP:
            game.touche[event.key] = False

    fond.blit(game.joueur.image, game.joueur.rect)
    game.all_mechant.draw(fond)


    for mechant in game.all_mechant:
        mechant.barre_sante(fond)


    # touche fleche
    if game.touche.get(pygame.K_RIGHT):
        game.joueur.mouvements_droite()
    if game.touche.get(pygame.K_LEFT):
        game.joueur.mouvements_gauche()

    pygame.display.flip()
