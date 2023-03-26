"""
# LES DICTIONNAIRES
# Collection comme les listes et les tuples, mais fonctionnent #
# Association de clés et de valeurs entre {}.

personne = {'nom': 'Mélanie', "Age": 25, "taille": 1.60}
print(personne)  # Afficher

print(personne['nom'])  # Afficher que le nom

# Les dicos sont mutables donc modifiables (comme les listes) :
personne['nom'] = "Claire"
print(personne)

# Ajouter de nouvelles clés :
personne['poste'] = "Développeur"
print(personne)

# Ajouter un tuple :
achat = ("Chocolat", "Beurre", "Fromage")
personne['achats'] = achat
print(personne)

# Boucle for pour boucler dans les collection (et le dico est une collection !)
for i in personne:
    print(f"clef: {i} - valeur: {personne[i]}")  # Afficher l'intégralité du contenu du dictionnaire
    print(personne[i])
"""

# PARTIE 2
# Listes VS Dictionnaires
# Chercher des données rapidement dans des listes longues

personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65),
]

def obtenir_informations(nom, liste):
    for i in liste:
        if i[0] == nom:  # Si l'elt du tuple = nom
            return i  # On retourne le tuple entier
    return None  # Sinon on ne retourne rien = objet vide

# Récupérer les informations sur Jacques
infos = obtenir_informations("Jacques", personnes)
# print(infos)
# Ici, on a dû boucler 3x pour récupérer les infos.


# Même chose mais en utilisant les dicos :
personnes_dict = {
    "Mélanie": (25, 1.6),  # Ici, Mélanie est une clé et on rentré les valeurs dans un tuple
    "Paul": (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)
}  # Le dictionnaire est prêt

infos = personnes_dict["Jacques"]
infos = personnes_dict.get("Martin")  # Chercher une personne
if not infos:
    print("La clef n'existe pas.")
else:
    print(infos)
# Avec les dicos, on a un accès direct aux infos, pas besoin de boulcer plusieurs fois comme ci-dessus.


