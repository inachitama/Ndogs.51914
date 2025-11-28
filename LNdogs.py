
import pygame
pygame.init()

# Fenêtre 
screen = pygame.display.set_mode((, ))
pygame.display.set_caption("Entrer le nom du personnage - Style Undertale")

#  Police pixel Undertale-like 
font = pygame.font.Font(None, 48)

#  Variables 
player_name = ""
active = True
clock = pygame.time.Clock()
running = True

#  Boucle principale 
while running:
    screen.fill((0, 0, 0))  # fond noir

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:   # Valider
                print("Nom choisi :", player_name)
                active = False

            elif event.key == pygame.K_BACKSPACE:  # Effacer
                player_name = player_name[:-1]

            else:
                player_name += event.unicode

    #  AFFICHAGE 

    # Cadre titre
    title_surf = font.render("ENTREZ LE NOM DU PERSONNAGE", True, (255, 255, 255))
    pygame.draw.rect(screen, (255, 255, 255), (80, 50, 640, 70), 3)
    screen.blit(title_surf, (100, 60))

    # Cadre du nom
    name_surf = font.render("Nom : " + player_name, True, (255, 255, 255))
    pygame.draw.rect(screen, (255, 255, 255), (150, 400, 500, 70), 3)
    screen.blit(name_surf, (170, 415))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
