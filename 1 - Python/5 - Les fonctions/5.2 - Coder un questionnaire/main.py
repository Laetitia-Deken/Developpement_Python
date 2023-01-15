# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

def question_1():
    print("Question : Quelle est la capitale de la France ?")
    print("(a) Marseille")
    print("(b) Nice")
    print("(c) Paris")
    print("(d) Nantes")
    print()
    reponse = input("Votre réponse : ")
    if reponse == "c":
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")


def question_2():
    print()
    print("Question : Quelle est la capitale de l'Italie ?")
    print("(a) Rome")
    print("(b) Venise")
    print("(c) Pise")
    print("(d) Florence")
    print()
    reponse = input("Votre réponse : ")
    if reponse == "a":
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")

question_1()
question_2()

# Ok mais inutile car répétitions de code --> déconseillé
# les def ne servent à rien, on n'exploite pas les fonctions ici et à chaque fois les ? précédentes seront reposées
# --> Il faut factoriser le code !!