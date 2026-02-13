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
         
         while abs(mechant.rect.x - self.joueur.rect.x) < 300 :
             mechant.rect.x = random.randint(600,1200)
         mechant.rect.y = 570
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
        self.image_d = pygame.image.load('chien_d.jpg')
        self.image_d = pygame.transform.scale(self.image_d,(210,210))
        self.image_g = pygame.image.load('chien_g.jpg')
        self.image_g =pygame.transform.scale(self.image_g,(210,210))
        self.image = self.image_d
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
              self.image = self.image_d

    def mouvements_gauche(self):
            self.rect.x -= self.deplacement
            self.image = self.image_g

   

class Mechant(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.vie = 100
        self.max_vie = 100
        self.attack = 5
        self.image = pygame.image.load("caca.jpg")  # --> mettre l'image du caca
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(500,800)
        self.rect.y = random.randint(570,570)

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

 #BOUCLE DE JEU
def lancer_jeu():
    pygame.display.set_caption("Ndogs.51914")
    fond = pygame.display.set_mode((1500, 800))
    game = Game()
    font = pygame.font.SysFont("arial", 30)
    game_over_font = pygame.font.SysFont("arial", 100, bold=True)
    
# ========== METTRE UN FOND ========== 
    def background(image):
        size = pygame.transform.scale(image, (1500, 800))
        fond.blit(size, (0, 0))
    image = pygame.image.load("fond_ecran_1.png")

# ========== FONCTION POUR AFFICHER TEXTE ==========
    def draw_text(text, font, col, text_x, text_y):
        img = font.render(text, True, col)
        fond.blit(img, (text_x, text_y))
# ========== POLICE ET TAILLE TEXTE ==========        
    text_font = pygame.font.Font(None, 28)

    running = True
    game_over = False
    
    while running:
        fond.fill((0, 0, 0))
        background(image)
        texte = font.render(f"KILL : {game.kill} /5", True, (255, 255, 255))

        # ========== AFFICHE TEXTES ==========
        draw_text("Click on the 'Left' arrow to move to the left.", text_font, (255, 255, 255), 10, 750)
        draw_text("Click on the 'Right' arrow to move to the right.", text_font, (255, 255, 255), 1065, 750)
        
        fond.blit(texte, (20, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game.touche[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.espace_appuye = True
            if event.type == pygame.KEYUP:
                game.touche[event.key] = False
                
                
        if not game_over:
            fond.blit(game.joueur.image, game.joueur.rect)
            game.all_mechant.draw(fond)
            game.joueur.barre_vie(fond)

            for mechant in game.all_mechant:
                mechant.barre_vie(fond)
                if game.joueur.rect.colliderect(mechant.rect):

# ========== AFFICHE TEXTE QUAND COLISION ==========
                    draw_text("Click on the 'Space' bar to defeat the poop.", text_font, (255, 255, 255), 500, 200)
                    
                    if game.touche.get(pygame.K_SPACE):
                        mechant.degats(1)
                    else:
                        game.joueur.degat(5)
                        
# ========== COLLISION BORD ==========
            if game.joueur.rect.x >= 1300:
                game.joueur.rect.x = 10
            if game.joueur.rect.x == 0:
                game.joueur.rect.x = 1290
            if game.touche.get(pygame.K_RIGHT):
                game.joueur.mouvements_droite()
            if game.touche.get(pygame.K_LEFT):
                game.joueur.mouvements_gauche()


            if game.joueur.vie <= 0:
                game_over = True
                game_over_start_time = pygame.time.get_ticks()  

        else:
            
            game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
            rect = game_over_text.get_rect(center=(750, 400))
            fond.blit(game_over_text, rect)

            
            if pygame.time.get_ticks() - game_over_start_time > 2000:
                running = False

        pygame.display.flip()


    pygame.quit()
