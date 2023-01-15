import random

# Définition des constantes :
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4


# Poser une question à l'utilisateur
def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)  # Tirer un nombre aleatoire
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)  # Tirer un 2eme nbre aleatoire

    # Choix entre Addition et Multiplication
    o = random.randint(0, 1)  # Tirage au sort d'un nombre entre 0 et 1. o = Operateur.
    # Si on tire eu sort 0 -> +
    # Si on tire au sort 1 -> *
    operateur_str = "+"  # par defaut
    if o == 1:
        operateur_str = "*"
    reponse_str = input(f"Calculez : {a} {operateur_str} {b} = ")
    # Reponse donnee au format "Chaîne de caractere" qu'il faudra convertir.
    reponse_int = int(reponse_str)  # Conversion de reponse_str au format numerique
    # Creation d'une condition Reponse correcte / incorrecte
    calcul = a+b  # Variable intermediaire
    if o == 1:
        calcul = a*b
    if reponse_int == calcul:
        return True
    else:
        return False


# Question 1 sur 4 :
nb_points = 0  # Pour la gestion du nombre de points
for i in range(0, NB_QUESTIONS):
    # Appel de la fonction :
    print(f"Question n°{i + 1} sur {NB_QUESTIONS} : ")  # i+1 -> evite que l'on commence par "Question n°0"
    if poser_question():
        print("Reponse correcte.")
        nb_points += 1
    else:
        print("Reponse incorrecte.")
    print()  # Laisse une ligne entre chaque question.

print(f"Votre note est {nb_points} / {NB_QUESTIONS}.")

moyenne = int(NB_QUESTIONS / 2)
# Conditions au niveau du nombre final de points :
if nb_points == NB_QUESTIONS:
    print("Excellent !")
elif nb_points == 0:
    print("Révisez vos maths !")
elif nb_points > moyenne:
    print("Pas mal !")
else:
    print("Peut mieux faire !")

# Conclusion :
# Les constantes permettent de readapter notre programme. Permettent de mettre des valeurs "en dur" dans le code.

