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

# ÉTAT
state = "menu"

# NOM 
player_name = ""
MAX_CHARS = 12
cursor_visible = True
cursor_timer = 0

# ================= BOUTONS =================
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
        return False


# MENU
play_btn = Button("PLAY", 600, 300)
options_btn = Button("OPTIONS", 600, 390)
quit_btn = Button("QUIT", 600, 480)

# OPTIONS
Skin_btn = Button("Skin", 600, 350)
Easteregg_btn = Button("Easter Egg", 600, 450)
MENU_btn = Button("MENU", 600, 550)

# ================= DESSINS =================
def draw_menu():
    screen.fill((35, 0, 50))
    title = title_font.render("MAIN MENU", True, (220, 180, 80))
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 150)))
    play_btn.draw()
    options_btn.draw()
    quit_btn.draw()


def draw_options():
    screen.fill((35, 0, 50))
    title = title_font.render("OPTIONS", True, WHITE)
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 150)))
    Skin_btn.draw()
    Easteregg_btn.draw()
    MENU_btn.draw()

#NOM JOUEUR
def draw_name_screen():
    global cursor_visible, cursor_timer

    screen.fill(BLACK)

    cursor_timer += clock.get_time()
    if cursor_timer > 500:
        cursor_visible = not cursor_visible
        cursor_timer = 0
        
    player_img = pygame.image.load("chien.jpg").convert_alpha()  # .convert_alpha() pour la transparence
    player_img = pygame.transform.scale(player_img, (470, 392))
        
     # Afficher image au centre
    img_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(player_img, img_rect)
    

    title_rect = pygame.Rect(430, 100, 640, 70)
    pygame.draw.rect(screen, WHITE, title_rect, 3)
    title = button_font.render("ENTREZ LE NOM DU PERSONNAGE", True, WHITE)
    screen.blit(title, title.get_rect(center=title_rect.center))

    name_rect = pygame.Rect(80, 650, 1340, 70)
    pygame.draw.rect(screen, WHITE, name_rect, 3)

    display_name = player_name + ("_" if cursor_visible else "")
    name_surf = button_font.render("Nom : " + display_name, True, WHITE)
    screen.blit(name_surf, (name_rect.x + 20, name_rect.y + 18))


# ================= BOUCLE PRINCIPALE =================
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

            elif options_btn.clicked(event):
                state = "options"

            elif quit_btn.clicked(event):
                running = False

        # OPTIONS 
        elif state == "options":
            if MENU_btn.clicked(event):
                state = "menu"

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = "menu"

        # NOM
        elif state == "name":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "menu"

                elif event.key == pygame.K_RETURN:
                    print("Nom choisi :", player_name)
                    state = "menu"

                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]

                else:
                    if len(player_name) < MAX_CHARS and event.unicode.isprintable():
                        player_name += event.unicode

    # AFFICHAGE
    if state == "menu":
        draw_menu()
    elif state == "options":
        draw_options()
    elif state == "name":
        draw_name_screen()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()



(TEST !!!!!!!)





















import pygame
import sys

pygame.init()

#  FENÊTRE 
WIDTH, HEIGHT = 1500, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MENU")
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

# ÉTAT
state = "menu"

# NOM 
player_name = ""
MAX_CHARS = 12
cursor_visible = True
cursor_timer = 0

# ================= BOUTONS =================
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.rect.collidepoint(event.pos)
        return False


# MENU
play_btn = Button("PLAY", 600, 300)
options_btn = Button("OPTIONS", 600, 390)
quit_btn = Button("QUIT", 600, 480)

# OPTIONS
Skin_btn = Button("Skin", 600, 350)
Easteregg_btn = Button("Easter Egg", 600, 450)
MENU_btn = Button("MENU", 600, 550)

# OPTIONS - SKIN !!!!!!! (A MODIF !!!!)

R_btn = Button("Roux", 600, 350)
M_btn = Button("Marron", 600, 450)
Be_btn = Button ("Beige", 600, 550)

# ================= DESSINS =================

def draw_menu():
    screen.fill((35, 0, 50))
    title = title_font.render("MAIN MENU", True, (220, 180, 80))
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 150)))
    play_btn.draw()
    options_btn.draw()
    quit_btn.draw()


def draw_options():
    screen.fill((35, 0, 50))
    title = title_font.render("OPTIONS", True, (220, 180, 80))
    screen.blit(title, title.get_rect(center=(WIDTH // 2, 150)))
    Skin_btn.draw()
    Easteregg_btn.draw()
    MENU_btn.draw()
    
def draw_skin():
    screen.fill((35, 0, 50))
    title = title_font.render("Skin", True, (220, 180, 80))
    screen.blit(title, title.get_rect(center=(WITH // 2, 150)))
    R_btn.draw()
    M_btn.draw()
    Be_btn.draw()

#NOM JOUEUR
def draw_name_screen():
    global cursor_visible, cursor_timer

    screen.fill(BLACK)

    cursor_timer += clock.get_time()
    if cursor_timer > 500:
        cursor_visible = not cursor_visible
        cursor_timer = 0
        
    player_img = pygame.image.load("chien.jpg").convert_alpha()  # .convert_alpha() pour la transparence
    player_img = pygame.transform.scale(player_img, (470, 392))
        
     # Afficher image au centre
    img_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(player_img, img_rect)
    

    title_rect = pygame.Rect(430, 100, 640, 70)
    pygame.draw.rect(screen, WHITE, title_rect, 3)
    title = button_font.render("ENTREZ LE NOM DU PERSONNAGE", True, WHITE)
    screen.blit(title, title.get_rect(center=title_rect.center))

    name_rect = pygame.Rect(80, 650, 1340, 70)
    pygame.draw.rect(screen, WHITE, name_rect, 3)

    display_name = player_name + ("_" if cursor_visible else "")
    name_surf = button_font.render("Nom : " + display_name, True, WHITE)
    screen.blit(name_surf, (name_rect.x + 20, name_rect.y + 18))


# ================= BOUCLE PRINCIPALE =================
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

            elif options_btn.clicked(event):
                state = "options"
                
            elif options_btn.clicked(event):
                state = "options"

            elif quit_btn.clicked(event):
                running = False

        # OPTIONS 
        elif state == "options":
            if MENU_btn.clicked(event):
                state = "menu"

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = "menu"

        # !!!!!!!  OPTIONS - SKIN
        elif state == "options":
            if Skin_btn.clicked(event):
                state = "Skin"

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                state = "options"
                
        # NOM
        elif state == "name":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "menu"

                elif event.key == pygame.K_RETURN:
                    print("Nom choisi :", player_name)
                    state = "menu"

                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]

                else:
                    if len(player_name) < MAX_CHARS and event.unicode.isprintable():
                        player_name += event.unicode

    # AFFICHAGE
    if state == "menu":
        draw_menu()
    elif state == "options":
        draw_options()
    elif state == "Skin":
        draw_skin()
    elif state == "name":
        draw_name_screen()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
