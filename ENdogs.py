#============== DISPLAY TEXT WHEN COLISION ============== V
import pygame

pygame.init()
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1500, 800))

text_font = pygame.font.Font(None, 28)

def draw_text(text, font, col, text_x, text_y):
    img = font.render(text, True, col)
    fond.blit(img, (text_x, text_y))

run = True
while run:
    
    fond.fill((0, 0, 0))
    draw_text("Cliquez sur la touche 'Espace' pour vaincre le caca.", text_font, (255, 255, 255), 500, 200)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()

#============== V ==============
#afficher du texte
text_x = 100
text_y = 720
col = (250, 250, 250)
def draw_text(text, font, col, text_x, text_y):
    img = font.trender(text, True, col)
    screen.blit(img, (text_x, text_y))

#============== DISPLAY TEXT WHEN COLISION ============== V
def collision():                                  # -> ligne 118 code Candice
  if game.joueur.image.colliderect(mechant.image):
    drax_text("Cliquez sur la touche 'Espace' pour vaincre le caca.", font, col, text_x, text_y)
#============== V ==============        
#quand jeu commence: (tutoriel)
  while not game.touche.get(pygame.K_LEFT):
    draw text("Cliquez sur la flèche gauche pour avancer vers la gauche.", font, col, text_x, text_y)
  while not game.touche.get(pygame.K_RIGHT):
    draw text("Cliquez sur la flèche droite pour avancer vers la droite.", font, col, text_x, text_y)







import pygame
pygame.init()
#fenetre jeu
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1000, 500))

#changer le fond qd collision w bord V1
font = pygame.image.load("font1.png")
if self.rect.x == 1000 - 235 and font == font1.png:
  self.rect.x = 0
  font = pygame.image.load("font2.png")
if self.rect.x == 1000 - 235 and font == font2.png:
  self.rect.x = 0
  font = pygame.image.load("font1.png")

#changer le fond qd collision w bord V2
import pygame
pygame.init()
pygame.display.set_caption("Ndogs.51914")
fond = pygame.display.set_mode((1000, 500))

font = pygame.image.load("font1.png")
def background():    
    if game.joueur.rect.x == 1000 - 235 :
        game.joueur.rect.x = 0
        if font == font1.png:
            font = pygame.image.load("font1.png")
        else:
            pygame.image.load("font2.png")
