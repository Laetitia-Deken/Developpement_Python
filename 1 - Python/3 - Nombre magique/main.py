# Imoorter le module "Random" -> pour générer un nombre aléatoire
import random # -> a rajouter en haut du fichier

# Création de la fonction "Demander un nombre" :
def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0: # Pour boucler si on a le message d'erreur et qu'il faut réessayer.
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")  # -> nombre reçu de l'utilisateur
        # Pour gérer un cas d'erreur :
        try:
            nombre_int = int(nombre_str) # variable intermediaire. Pour gerer les cas d'erreurs
        except:
            print("ERREUR : Vous devez rentrer un nombre ! Réessayez.")
        else: # si la ligne try a fonctionne et pas de message d'erreur affiche
            if nombre_int < nb_min or nombre_int > nb_max: # Si le nb converti de l'utilisateur est inférieur au min ou supérieur au max :
                print(f"ERREUR : Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                nombre_int = 0 # force a reboucler vers while ci-dessus sans aller dans la suite du code
                # Remets a 0 le nombre_int dans CETTE condition.
    return nombre_int

# Création des constantes
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX) # -> Ce sont des nombres inclusifs : ici entre 1 et 10.
# random.randint() -> Permet de generer aleatoirement un nbre entier
NB_VIES = 4


""" 
# Pour limiter le nombre de vies avec une boucle "while" :
nombre = 0 # Declaration du nombre avant la boucle while sinon on ne pourra pas l'utiliser dans la condition
vies = NB_VIES # Variable initialisée avec le nbre de vies.
while not nombre == NOMBRE_MAGIQUE and vies > 0: # tant que le nbre magique n'est pas trouve et qu'il reste des vies
    print(f"Il vous reste {vies} vies.") # Affiche le nombre restant de vies.
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX) # ne pas oublier de mettre entre ().
    # Declaration du nombre dans cette fonction
    # Conditions : tester le nombre magique
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné !")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit.")
        vies -= 1 # Si l'utilisateur n'a pas trouve le bon nb, on decremente de 1 le nb de vies restantes
    else:
        print("Le nombre magique est plus grand.")
        vies -= 1

if vies == 0:
    print(f"Vous avez perdu ! Le nombre magique était : {NOMBRE_MAGIQUE}.")
    # S'il ne reste plus de vies et que le nbre n'est pas trouve, on sort de la boucle et affiche ceci.
    #Note : a chaque fois que les {} pparaissent, ajouter un "f" au début du print !!
"""

gagne = False # Variable placée a False par defaut car on considere qu'on a perdu par defaut.
# Pour limiter le nombre de vies avec une boucle "for" :
for i in range (0, NB_VIES):
    vies = NB_VIES-i # Calcul du nombre de vies -> ici : valeur maximale de vies - i
    print(f"Il vous reste {vies} vies.") # Affiche le nombre restant de vies.
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX) # ne pas oublier de mettre entre ().
    # Declaration du nombre dans cette fonction
    # Conditions : tester le nombre magique
    if nombre == NOMBRE_MAGIQUE:
        gagne = True # Si le nbre magique est trouve, on sort de la boucle.
        print("Bravo, vous avez gagné !")
        break # Si on gagne, on sort de la boucle et on passe à la suite -> ici if vies == 0.
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit.")
    else:
        print("Le nombre magique est plus grand.")


# if vies == 0:
if not gagne:
    print(f"Vous avez perdu ! Le nombre magique était : {NOMBRE_MAGIQUE}.")
    # Si on a pas gagne, on affiche ceci.
    #Note : a chaque fois que les {} apparaissent, ajouter un "f" au début du print !!