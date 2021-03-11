
import random

choix = "oui"
compteur_de_coups = 5

while choix.lower() == "oui" and compteur_de_coups > 0:

    nombre_aleatoire_1 = random.randint(1, 20)
    nombre_aleatoire_2 = random.randint(1, 20)
    print(f"l'ordinateur a choisi deux nombres aléatoires : {nombre_aleatoire_1} et {nombre_aleatoire_2}\n")

    if nombre_aleatoire_1 == nombre_aleatoire_2:
        print(f"Bravo!vous avez gagner le droit de rejouer !\n")
        compteur_de_coups = 5
        choix = input("Voulez-vous refaire une partie ? taper oui ou autre : ")
        print("\n")

    else:
        print(f"Il ne vous reste que {compteur_de_coups} tentatives!\n")
        compteur_de_coups = compteur_de_coups - 1
        choix = input("Voulez-vous réessayer ? taper oui ou autre : ")

    if compteur_de_coups == 0:
        print("vous n'avez plus de tentatives")
        compteur_de_coups = 5
        choix = input("voulez vous rejouez ? si oui tapez 'oui' sinon autre :\n ")

compteur_de_coups = 0
print("vous avez quitter le jeu. Revenez quand vous voulez !\n")
print("fin du programme")