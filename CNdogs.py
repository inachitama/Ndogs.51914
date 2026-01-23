import pygame
import random
pygame.init()


class Game:
    def __init__(self):
        self.all_joueur = pygame.sprite.Group()
        self.joueur = Joueur(self)
        self.all_joueur.add(self.joueur)
        self.all_mechant = pygame.sprite.Group()
        self.kill = 0
        self.max_kill = 5
        self.touche = {}
        self.spaw_mechant()
        self.espace_appuye = False

    def spaw_mechant(self):
         mechant = Mechant(self)
         self.all_mechant.add(mechant)

    def collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False, pygame.sprite.collide_mask)


class Joueur(pygame.sprite.Sprite):
    def __init__(self,game ):
        super().__init__()
        self.fin_degat = 0
        self.game = game
        self.vie = 100
        self.max_vie = 100
        self.attack = 10
        self.deplacement = 2
        self.image = pygame.image.load("chien.png")  # --> mettre l'image du chien
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 465

        self.last_degat_time = 0
        self.degat_cooldown = 1000

    def degat(self,montant):
        actuel = pygame.time.get_ticks()
        if actuel - self.fin_degat >= 1000 :
            self.vie -= montant
            self.fin_degat = actuel

    def barre_vie(self, surface):
            pygame.draw.rect(surface, (240, 14, 14), [self.rect.x + 50, self.rect.y -20, self.max_vie, 10])
            pygame.draw.rect(surface, (45, 212, 21), [self.rect.x + 50, self.rect.y -20, self.vie, 10])

    def mouvements_droite(self):
        if not self.game.collision(self,self.game.all_mechant):
              self.rect.x += self.deplacement

    def mouvements_gauche(self):
            self.rect.x -= self.deplacement


class Mechant(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.vie = 100
        self.max_vie = 100
        self.attack = 5
        self.image = pygame.image.load("caca.png")  # --> mettre l'image du caca
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(500,800)
        self.rect.y = random.randint(520,520)

    def degats(self,montant):
        self.vie -= montant
        if self.vie <= 0:
            self.game.kill += 1
            self.kill()
            if self.game.kill < self.game.max_kill :
                self.game.spaw_mechant()
    def mourir(self) :
        self.game.all_mechant.remove(self)
            

    def forward(self):
        if self.game.joueur.rect.colliderect(self.rect) :
            now = pygame.time.get_ticks()
        if now - self.game.joueur.last_degat_time > self.game.joueur.degat_cooldown:
            self.game.joueur.degat(self.attack)
            self.game.joueur.last_degat_time = now

    def barre_vie(self, surface):
        pygame.draw.rect(surface, (240, 14, 14), [self.rect.x + 10, self.rect.y - 20, self.max_vie, 10])
        pygame.draw.rect(surface, (45, 212, 21), [self.rect.x + 10, self.rect.y - 20, self.vie, 10])


# fenetre jeu
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1500, 800))
game = Game()
font = pygame.font.SysFont("arial",30)

#boucle de jeu 
running = True
while running:
    fond.fill((0,0,0))
    texte = font.render(f"KILL : {game.kill} /5" , True , (255,255,255))
    fond.blit(texte,(20,20))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            game.touche[event.key] = True
            if event.key == pygame.K_SPACE:
                game.espace_appuye = True
        if event.type == pygame.KEYUP:
            game.touche[event.key] = False
 

    fond.blit(game.joueur.image, game.joueur.rect)
    game.all_mechant.draw(fond)
    game.joueur.barre_vie(fond)

    for mechant in game.all_mechant:

        mechant.barre_vie(fond)

        if game.joueur.rect.colliderect(mechant.rect):

            if game.touche.get(pygame.K_SPACE):
                mechant.degats(1)
                if mechant.vie <= 0:
                    mechant.vie < mechant.max_vie
                    mechant.degats(5)
            else :
                game.joueur.degat(5)


    # touche fleche
    if game.touche.get(pygame.K_RIGHT):
        game.joueur.mouvements_droite()
    if game.touche.get(pygame.K_LEFT):
        game.joueur.mouvements_gauche()



    pygame.display.flip()
    
    
pygame.quit()
