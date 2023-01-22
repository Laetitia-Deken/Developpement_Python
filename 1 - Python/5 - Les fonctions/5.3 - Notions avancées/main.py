# NOTIONS AVANCEES : FONCTIONS RECURSIVES --> Une fonction qui s'appelle elle-même ! Avec une condition de sortie pour éviter de boucler à l'infini !

# Sert beaucoup pour le straitement de données, algorithmes et fonctions mathématiques.

# Exemple 1 -> fixer une limite pour eviter de boucler a l'infini :
""" def a(n, limit):  # Fonction normale
    if n > limit:
        return  # on arrete la recursion avant de depasser la limite.
        # return permet d'arreter la recursion et de casser la boucle infinie.
    print("n:", n)
    a(n*n, limit)
    # A chaque fois que l'on appele la fonction, on multiplie le nbre par lui-meme.
    # On s'arrête lorsque la valeur atteint une certaine limite.


# Appel de la fonction a.
a(2, 100000)  # 2 représente ici "n" et 100000 est la limite.

Cette fonction print ... puis s'appelle elle-meme, donc on re-rentre dans a, on rappelle ..."
Cela crée une boucle infinie.
Les fonctions récursives doivent tjs avoir une condition de sortie.
Elles sont souvent utilisees pour le traitement des donnees, algorithmes, fonctions maths """


# Exemple 2 -> Demander à l'utilisateur un nombre entre 1 et 4 :
""" def demander_choix_utilisateur(min, max):
    # On retourne ce choix au format chaine de caracteres :
    reponse_str = input("Quel est votre choix entre " + str(min) + " et " + str(max) + " ? ")
    # Cette conversion peut echouer donc on ajoute :
    try:
        reponse_int = int(reponse_str)  # Conversion au format numerique
        if not min <= reponse_int <= max: # Si la reponse n'est pas entre min et max
            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max, "!")
            return demander_choix_utilisateur(min, max)  # Fonction recursive
        return reponse_int
    except:
        print("ERREUR : Vous devez rentrer un nombre.")
        return demander_choix_utilisateur(min, max)
        # Ici, on ne sort pas tant que l'utilisateur n'a pas donne une bonne réponse.
        # Elle est là la fonction recursive !


# Appel de la fonction à l'utilisateur, choix entre 1 et 4 :
choix = demander_choix_utilisateur(1, 4)
print("Choix de l'utilisateur : ", choix)

Ici la recursion va servir à forcer l'utilisateur à donner une bonne reponse donc reposer la question.
"""

# DIFFERENCE ENTRE BREAK ET RETURN

""" def a():
    print("Début de la fonction.")
    for i in range(0, 100):
        if i > 20:
            break
        print(i)
    print("Fin de la fonction.")


a()

# Break : arrete l'exe d'une boucle, on casse la boucle. Boucle cassee avant d'atteindre la fin mais on continue l'exe de la fonction. Ne retourne pas de résultat.
# Return : même chose mais ici on sort de la fonction. La suite de la boucle n'est pas executee.
"""

# CALLBACKS ET LAMBDAS

""" def ma_fonction():
    print("Toto")
    return 1

a = 5  # Une variable prend une valeur
b = ma_fonction

print("a", a, "b", b())

# Callbacks : quand on fait des rappels de fonctions, on met des ().
# Stocker une fonction dans une variable ou la passer dans une autre variable = callback.

# Exemple :

# Fonction pour multiplier :
def mult_callback(a, b):
    return a*b

# Fonction pour additionner :
def add_callback(a, b):
    return a+b

# Fonction generique en utilisant les callbacks :
def afficher_table_(n, operateur_str, operation_cbk):
# On ajoute un operateur au format chaine de caractere.
# operateur_cbk -> fonction qui exécute l'operation
    for i in range(1, 10):
        print(i, operateur_str, n, "=", operation_cbk(i, n))


# Fonctions lambda -> fonctions qui n'ont pas de nom. On inscrit le code directement :
# C'est le cas ici pour mult_callback par exemple.
afficher_table_(2, "x", mult_callback)
-> afficher_table_(2, "x", lambda a, b : a * b)
print()
afficher_table_(2, "+", add_callback)
"""

# NOMBRE VARIABLE DE PARAMETRES

def a(age, taille, numero_tel):
    print("Toto", age, taille, numero_tel)

a(20, 1.75, "0610101010")

# Exemple avec * :
def somme(titre, *nombres):
    print("TITRE:", titre)
    resultat = 0
    for n in nombres:
        resultat += n
    return resultat

print(somme("somme des points", 5, 2, 4, 7, 8))

# Exemple avec ** :
def somme(titre, **nombres):
    print("TITRE:", titre)
    resultat = 0
    for n in nombres.values():
        resultat += n
    return resultat

print(somme("somme des notes", maths=15, geo=11, anglais=18))
# nombres.values() -> On récupère pas de nombres mais des valeurs