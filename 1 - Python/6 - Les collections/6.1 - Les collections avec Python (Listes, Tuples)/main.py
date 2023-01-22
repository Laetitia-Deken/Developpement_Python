# Collections : (Tableaux : Array), Listes, Tuples... PLusieurs elements.
# Tuple (): IMMUTABLE -> Non modifiable
# Liste [] : MUTABLE -> modifiable : rajouter/supprimer des elements ou modifier

# TUPLES
a = 5
b = "toto"

personnes = ("Mélanie", "Jean", "Martin", "Alice")  # C'est un tableau, un tuple chez Python.
# Tuple = lecture seule, pas de modification possible des elements ni de rajout.
print(personnes[0])  # Pour recuperer un element. Le 1er elt se situe tjs a l'index 0.
print(personnes[-1])  # Pour recuperer le dernier element -> nombre negatif = compte à partir de la fin.
print(len(personnes))  # len -> Pour connaitre le nombre d'elements dans le tableau (tuple)

for i in range(0, len(personnes)):  # Pour boucler sur les differents elts du tuple
    print(personnes[i])

for i in personnes:  # Boucle qui parcourt les elements.
    print(i)
    print(len(i))  # Recupere le nbre de caractere de chaque element.
    print(i[0])  # Recupere la 1ere lettre de chaque element. Se comporte comme un tuple.
    # Une chaine de caractères se comporte come un tuple de caractères.

# Le range est une collection. Fonctionne comme un tuple.
valeurs = range(0, 5)
print(valeurs[-1])
# Ici range se comporte comme si c'etait un tuple comportant (0, 1, 2, 3, 4).


# LISTES
# Les listes peuvent faire tout ce que les tuples peuvent faire -> donc ce qui est au-dessus reste valable.
personnes = ["Mélanie", "Jean", "Martin", "Alice"]
nouvelle_personne = "David"  # Variable pour ajouter une personne

print(personnes)
personnes.append(nouvelle_personne)  # Fonction pour ajouter une nouvelle personne à la liste
print(personnes)
del personnes[1]  # La personne a l'index 1 sera supprimee.

# Afficher dans une fonction :
def afficher_personnes(c):
   a[0] = 10

def modifier_valeur(a):
    a = 10

test = [1, 2, 3, 4]  # La liste est un conteneur. On peut modifier les valeurs a l'interieur de ce conteneur.
print(test)
modifier_valeur(test)
print(test)


afficher_personnes(personnes)


# FONCTIONS ET TUPLES -> Fonction qui retourne plusieurs valeurs.
def obtenir_informations():
    # return "Mélanie"  # -> Pour retourner une valeur
    return "Mélanie", 37, 1.60  #  Attention ! [0, 1, 2]
    # Pour retourner plusieurs valeurs, pas forcement du meme type

def afficher_informations(nom, age, taille):
    print(f"Informations: Nom: {nom}, age: {age}, Taille: {taille}")
    # On peut creer les 3 variables directement a gauche quand on a un tuple a droite.


infos = obtenir_informations()
afficher_informations(*infos)

print(infos)  # affiche 1 tuple/tuple (comme un tout)
print(*infos)  # affiche comme si on avait passe 3 parametres a la fonction print = on unpack le tuple.
# * -> sépare les valeurs du tuple et les passe dans les parametres.
# print("nom: " + infos[0])
# print("age: " + str(infos[1])
# print("taille: " + str(infos[2])

nom, age, taille = obtenir_informations()
afficher_informations(nom, age, taille)


# SLICES
# S'applique aux listes et aux tuples.

personnes = ("Mélanie", "Jean", "Martin", "Alice", "Pierre," "Paul")

for i in personnes[0:2]:  # Ajoutee des index pour n'afficher que un certain nombre de personnes.
    print(i)

# Syntaxe du slice : [x:x:x] -> [start:end:step]
# Step -> facultatif : permet de sauter des elements. S'applique aussi sur les chaines de caracteres.
