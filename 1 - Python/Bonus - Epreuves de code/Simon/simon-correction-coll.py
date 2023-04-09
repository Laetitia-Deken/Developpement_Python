"""
- Longueur séquence initiale : 4
- Durée de mémorisation : 3s
- A chaque tour : 1 chiffre
- Un nombre de vies
"""

NIVEAUX_DIFFICULTE = (
    {
        "titre": "Facile",
        "longueur_seq_initiale": 3,
        "duree_memorisation_sec": 4,
        "increment_sequence": 1,
        "nombre_essais": 2,
    },
    {
        "titre": "Normal",
        "longueur_seq_initiale": 4,
        "duree_memorisation_sec": 3,
        "increment_sequence": 1,
        "nombre_essais": 1,
    },
    {
        "titre": "Difficile",
        "longueur_seq_initiale": 5,
        "duree_memorisation_sec": 2,
        "increment_sequence": 2,
        "nombre_essais": 0,
    }
)

import time
import random
import os
 
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def demander_valeur_numerique_min_max(min, max):
    valeur = input(f"Rendrez une valeur entre {min} et {max} : ")
    try:
        valeur_int = int(valeur)
    except:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        return demander_valeur_numerique_min_max(min, max)
    if not (min <= valeur_int <= max):
        print(f"ERREUR : Vous devez rentrer une valeur numérique entre {min} et {max}")
        return demander_valeur_numerique_min_max(min, max)
    return valeur_int

def choix_niveau_difficulte(niveaux_difficulte):
    print("Choisissez votre niveau")
    index = 1
    for niveau in niveaux_difficulte:
        print(f"{index} - {niveau['titre']}")
        index += 1
    choix = demander_valeur_numerique_min_max(1, len(niveaux_difficulte))
    return niveaux_difficulte[choix-1]

def generer_sequence(n):
    sequence = ""
    for i in range(n):
        chiffre = random.randint(0, 9)
        sequence += str(chiffre)
    return sequence

# Choisir niveau de difficulté
niveau_difficulte_dict = choix_niveau_difficulte(NIVEAUX_DIFFICULTE)

# Génération de la séquence initiale
sequence = generer_sequence(niveau_difficulte_dict["longueur_seq_initiale"])

nb_essais_restants = niveau_difficulte_dict["nombre_essais"]

clear_screen()
print(f"Début du jeu - niveau {niveau_difficulte_dict['titre']}")

score = 0
while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(sequence)
    time.sleep(niveau_difficulte_dict["duree_memorisation_sec"])
    clear_screen()

    print(f"Nombre d'essais restants : {nb_essais_restants}")
    print(f"Votre score : {score}")
    seq_utilisateur = input("Votre réponse : ")
    if seq_utilisateur == sequence:
        score += 1
        sequence += generer_sequence(niveau_difficulte_dict["increment_sequence"])
        print("Bonne réponse !")
    else:
        nb_essais_restants -= 1
        if nb_essais_restants < 0:
            break
        print("Mauvaise réponse, réessayez")
    
    time.sleep(1)
    clear_screen()

print("Mauvaise réponse")
print(f"La séquence était {sequence}")
print(f"Votre score final est : {score}")