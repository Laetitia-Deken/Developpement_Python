###
# VOS PREMIERS PAS EN POO (PROGRAMMATION ORIENTÉE OBJET)
###
# - Différence programmation impérative (demander...) --> à transformer en objet
# - Le plus simple possible
# - Exercices, mises en situation

# Personne  (entité -> class) entité -> objet. Il faut raisonner sur les entités en POO. On fait en sorte que les fonctions puissent accéder à certaines données par rapport à l'entité en question.
#    Données : nom, age
#    Actions :  (méthodes)
#       - SePresenter()
#       - DemanderNom() / input
#  [Personne "Jean"]     [Personne "Paul"]

def afficher_informations_personne(nom, age): # Découpage entre les fonctions qui exécutent du code et les données
    print(f"La personne s'appelle {nom}, son age est {age} ans")

def demander_nom_personne():
    nom = input("Quel est votre nom ?")
    return nom

nom1 = "Jean"
age1 = 30

nom2 = "Paul"
age2 = 25

afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)

nom3 = demanger_nom_personne()
age3 = 18
afficher_informations_personne(nom3, age3)
