import pygame
import sys

pygame.init()

#  FENÊTRE 
WIDTH, HEIGHT = 1500, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("menu -> nom")

clock = pygame.time.Clock()

#  COULEURS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (90, 90, 90)
LIGHT_GRAY = (140, 140, 140)

#  POLICES
title_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 28)


#  ÉTATS 
state = "menu"   

#  VARIABLES NOM 
player_name = ""
MAX_CHARS = 12
cursor_visible = True
cursor_timer = 0

#  BOUTONS 
class Button:
    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.Rect(x, y, 300, 70)

    def draw(self):
        color = LIGHT_GRAY if self.rect.collidepoint(pygame.mouse.get_pos()) else GRAY
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 3)

        txt = button_font.render(self.text, True, WHITE)
        screen.blit(txt, txt.get_rect(center=self.rect.center))

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

play_btn = Button("PLAY", 600, 300)
options_btn = Button("OPTIONS", 600, 390)
quit_btn = Button("QUIT", 600, 480)

#  MENU 
def draw_menu():
    screen.fill((35, 0, 50))

    title = title_font.render("MAIN MENU", True, (220, 180, 80))
    screen.blit(title, title.get_rect(center=(WIDTH//2, 150)))

    play_btn.draw()
    options_btn.draw()
    quit_btn.draw()

#  ÉCRAN NOM 
def draw_name_screen():
    global cursor_visible, cursor_timer

    screen.fill(BLACK)

    # Curseur clignotant
    cursor_timer += clock.get_time()
    if cursor_timer > 500:
        cursor_visible = not cursor_visible
        cursor_timer = 0

    # Cadre titre
    title_rect = pygame.Rect(430, 100, 640, 70)
    pygame.draw.rect(screen, WHITE, title_rect, 3)

    title = button_font.render("ENTREZ LE NOM DU PERSONNAGE", True, WHITE)
    screen.blit(title, title.get_rect(center=title_rect.center))

    # Cadre nom
    name_rect = pygame.Rect(80, 650, 1340, 70)
    pygame.draw.rect(screen, WHITE, name_rect, 3)

    display_name = player_name + ("_" if cursor_visible else "")
    name_surf = button_font.render("Nom : " + display_name, True, WHITE)
    screen.blit(name_surf, (name_rect.x + 20, name_rect.y + 18))

    help_text = small_font.render("ENTRÉE pour valider  |  ESC pour revenir", True, (180, 180, 180))
    screen.blit(help_text, help_text.get_rect(center=(WIDTH//2, 740)))

#  BOUCLE PRINCIPALE 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #  MENU 
        if state == "menu":
            if play_btn.clicked(event):
                state = "name"
                player_name = ""

            if quit_btn.clicked(event):
                running = False

        #  ÉCRAN NOM 
        elif state == "name":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "menu"

                elif event.key == pygame.K_RETURN:
                    print("Nom choisi :", player_name)
                    # le jeu
                    state = "menu"

                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]

                else:
                    if len(player_name) < MAX_CHARS and event.unicode.isprintable():
                        player_name += event.unicode

    if state == "menu":
        draw_menu()
    elif state == "name":
        draw_name_screen()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
