import pygame
from random import randint
# on cree la grille


def grille(taille):
    lignes = [((200, 0), (200, 600)), ((400, 0), (400, 600)),
              ((0, 200), (600, 200)), ((0, 400), (600, 400))]
    for ligne in lignes:
        pygame.draw.line(taille, (0, 0, 0), ligne[0], ligne[1], 2)


def definir_valeur(x, y, valeur):
    global compteur_on
    if plateau[y][x] == None:
        plateau[y][x] = valeur
        compteur_on = True


# on cree les formes
def affichage_croix(taille):
    for y in range(0, len(plateau)):
        for x in range(0, len(plateau)):
            if plateau[y][x] == 'X':
                pygame.draw.line(taille, (52, 152, 219), (x*200+55, y*200+200-55), (x*200+200-55, y*200+55), 3)
                pygame.draw.line(taille, (52, 152, 219), (x*200+200-55, y*200+200-55), (x*200+55, y*200+55), 3)


def affichage_cercle(taille):
    for y in range(0, len(plateau)):
        for x in range(0, len(plateau)):
            if plateau[y][x] == 'O':
                pygame.draw.circle(taille, (231, 76, 60), (100 + (x * 200), 100 + (y * 200)), 50, 3)


def definir_gagnant(taille):
    global fin_de_partie
    for colonne in range(0, 3):
        if plateau[0][colonne] == 'X' and plateau[1][colonne] == 'X' and plateau[2][colonne] == 'X':
            pygame.draw.line(taille, (52, 152, 219), (colonne*200+200 // 2, 15), (colonne * 200 + 200 // 2, 600-15), 8)
            print("X gagne")
            fin_de_partie = True

    for ligne in range(0, 3):
        if plateau[ligne][0] == 'X' and plateau[ligne][1] == 'X' and plateau[ligne][2] == 'X':
            pygame.draw.line(taille, (52, 152, 219), (15, ligne * 200 + 200 // 2), (600-15, ligne * 200 + 200 // 2), 8)
            print("X gagne")
            fin_de_partie = True

    if plateau[2][0] == 'X' and plateau[1][1] == 'X' and plateau[0][2] == 'X':
        pygame.draw.line(taille, (52, 152, 219), (15, 600-15), (600 - 15, 15), 8)
        print("X gagne")
        fin_de_partie = True

    elif plateau[0][0] == 'X' and plateau[1][1] == 'X' and plateau[2][2] == 'X':
        pygame.draw.line(taille, (52, 152, 219), (15, 15), (600 - 15, 600 - 15), 8)
        print("X gagne")
        fin_de_partie = True

    for colonne in range(0, 3):
        if plateau[0][colonne] == 'O' and plateau[1][colonne] == 'O' and plateau[2][colonne] == 'O':
            pygame.draw.line(taille, (231, 76, 60), (colonne*200+200 // 2, 15), (colonne * 200 + 200 // 2, 600-15), 8)
            print("O gagne")
            fin_de_partie = True

    for ligne in range(0, 3):
        if plateau[ligne][0] == 'O' and plateau[ligne][1] == 'O' and plateau[ligne][2] == 'O':
            pygame.draw.line(taille, (231, 76, 60), (15, ligne * 200 + 200 // 2), (600-15, ligne * 200 + 200 // 2), 8)
            print("O gagne")
            fin_de_partie = True

    if plateau[2][0] == 'O' and plateau[1][1] == 'O' and plateau[0][2] == 'O':
        pygame.draw.line(taille, (231, 76, 60), (15, 600-15), (600 - 15, 15), 8)
        print("O gagne")
        fin_de_partie = True

    elif plateau[0][0] == 'O' and plateau[1][1] == 'O' and plateau[2][2] == 'O':
        pygame.draw.line(taille, (231, 76, 60), (15, 15), (600 - 15, 600 - 15), 8)
        print("O gagne")
        fin_de_partie = True


def nouvelle_partie():
    global compteur
    screen.fill("#F2F3F4")
    grille(screen)
    for y in range(0, 3):
        for x in range(0, 3):
            plateau[y][x] = None
    compteur = 0


# on cree la fenetre
pygame.init()

taille_ecran = (600, 600)
screen = pygame.display.set_mode(taille_ecran)
pygame.display.set_caption('Tic Tac Toe')

# on initie les variables
jeu_en_cours = True
compteur = 0
compteur_on = False
position = 0
pos_X = 0
pos_Y = 0
pos_X_alea = 0
pos_Y_alea = 0
player_X = 'X'
player_O = 'O'
plateau = [[None for x in range(0, 3)] for y in range(0, 3)]
fin_de_partie = False

while jeu_en_cours:

    screen.fill("#F2F3F4") 
    grille(screen)
    # on fait choisir une position a l'ordinateur
    pos_X_alea = randint(0, 2)
    pos_Y_alea = randint(0, 2)

    # on voit si une touche est active
    for event in pygame.event.get():

        # on ferme la fenetre si le bouton croix est activer
        if event.type == pygame.QUIT:
            jeu_en_cours = False

            # on cree les ronds ou croix lorsque le clic gauche de la souris est presse
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and not fin_de_partie:

            # on recupere les donnees de la souris
            position = pygame.mouse.get_pos()
            pos_X = int(position[0] // 200)
            pos_Y = int(position[1] // 200)

            # on affiche soit une croix soit un rond
            if compteur % 2 == 0:
                definir_valeur(pos_X, pos_Y, player_X)
                if compteur_on:
                    compteur += 1
                    compteur_on = False
            else:
                definir_valeur(pos_X, pos_Y, player_O)
                if compteur_on:
                    compteur += 1
                    compteur_on = False

        # on lui permet de refaire une partie
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                nouvelle_partie()
                print("nouvelle partie")
                fin_de_partie = False

    affichage_cercle(screen)
    affichage_croix(screen)

    definir_gagnant(screen)
    pygame.display.flip()