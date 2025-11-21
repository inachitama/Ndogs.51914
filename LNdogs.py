
import pygame
pygame.init()

# cree Fenêtre
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Entrer le nom du personnage")

# Police
font = pygame.font.Font(None, 40)

# Texte saisi (nom)
player_name = ""
active = True #if joueur tape

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((30, 30, 30)) #couleur principal jeu

    for event in pygame.event.get(): #lit event jeu
        if event.type == pygame.QUIT:
            running = False

        if active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Valider par Entrée
                    print("Nom choisi :", player_name)
                    active = False  # on n'écrit plus ensuite
                elif event.key == pygame.K_BACKSPACE:  # Effacer
                    player_name = player_name[:-1]
                else:
                    # Ajouter le caractère tapé
                    player_name += event.unicode

    # Affichage
    txt_surface = font.render("Nom : " + player_name, True, (255, 255, 255))
    screen.blit(txt_surface, (50, 180))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
