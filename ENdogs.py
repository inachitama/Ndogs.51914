import pygame
pygame.init()
#fenetre jeu
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1000, 500))

#changer le fond qd collision w bord
font = pygame.image.load("font1.png")
if self.rect.x == 1000 - 235 and font == font1.png:
  self.rect.x = 0
  font = pygame.image.load("font2.png")
if self.rect.x == 1000 - 235 and font == font2.png:
  self.rect.x = 0
  font = pygame.image.load("font1.png")

###
import pygame
pygame.init()
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1000, 500))

font = pygame.image.load("font1.png")
def background():    
    if self.rect.x == 1000 - :  # mettre moitié taille x chien
        self.rect.x = 0
        if font == font1.png:
            font = pygame.image.load("font1.png")
        else:
            pygame.image.load("font2.png")
text_x = 100
text_y = 720
col = (250, 250, 250)
def draw_text(text, font, col, text_x, text_y):
    img = font.trender(text, True, col)
    screen.blit(img, (text_x, text_y))

def collision():                                  # -> ligne 118 code Candice
    if joueur.image.colliderect(mechant.image):
        drax_text("Cliquez sur la touche 'Espace' pour vaincre le caca.", font, col, text_x, text_y)
        
#quand jeu commence:
  while not game.touche.get(pygame.K_LEFT):
    draw text("Cliquez sur la flèche gauche pour avancer vers la gauche.", font, col, text_x, text_y)
  while not game.touche.get(pygame.K_RIGHT):
    draw text("Cliquez sur la flèche droite pour avancer vers la droite.", font, col, text_x, text_y)
