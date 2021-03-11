
import random
i = "oui"
nombre_aleatoire_1 = random.randint(1, 100)
nombre_aleatoire_2 = random.randint(1, 100)
somme = nombre_aleatoire_1 + nombre_aleatoire_2

# la valeur i permet de rejouer si ça valeur est égale à 'oui'
while i.lower() == "oui":
    print(f"l'ordinateur a choisi deux nombres aléatoires : {nombre_aleatoire_1} et {nombre_aleatoire_2}")
    reponse_utilisateur = input("entrez le résultat de la somme de ces deux nombres :")

    # on verifie que la valeur entrait par l'utilisateur est un nombre
    try:
        reponse_utilisateur_int = int(reponse_utilisateur)

    except:
        print("erreur de saisi \n")

    else:
        if reponse_utilisateur_int < 0:
            print("le résultat ne peut pas être négatif ! \n")
        elif reponse_utilisateur_int == somme:
            print(f"Vous êtes doué en calcul ! La réponse est bien {somme}\n")
            i = "non"
        elif reponse_utilisateur_int != somme:
            print("Il faut s'entrainer !")
            i = input("si vous voulez reessayer taper oui sinon autre :")

print("Vous avez quitter le jeu revenez quand vous voulez")
print("fin du programme")