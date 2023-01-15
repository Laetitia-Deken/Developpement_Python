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

def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse): # 1 fonction générique qui prend des paramètres pour éviter de répéter du code
    print("QUESTION")
    print("  " + question)
    print("  (a)", r1)
    print("  (b)", r2)
    print("  (c)", r3)
    print("  (d)", r4)
    print()
    reponse = input("Votre réponse : ")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")
    print()


poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")
