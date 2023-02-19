###
# VOS PREMIERS PAS EN POO (PROGRAMMATION ORIENTÉE OBJET)
###
# - Différence programmation impérative / objet
# - Le plus simple possible
# - Exercices, mises en situation

# Personne  (entité -> class)
#    Données : nom, age
#    Actions :  (méthodes)
#       - SePresenter()
#       - DemanderNom() / input
#  [Personne "Jean"]     [Personne "Paul"]


# --- DEFINITION --- On crée notre classe
class Personne:
    def __init__(self, nom): # self --> paramètre particulier = il est fourni automatiquement
        self.nom = nom   # crée une variable d'instance : nom
        print("Constructeur personne " + nom)

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)


# --- UTILISATION --- On va créer plusieurs personnes, et appeler des méthodes sur ces personnes
personne1 = Personne("Jean")   # Je cree une personne
personne2 = Personne("Paul")   # Je cree une personne

# Personne.SePresenter(personne1)
personne1.SePresenter()
personne2.SePresenter()  # méthode d'instance --> on travaille sur l'objet


"""def afficher_informations_personne(nom, age):
    print(f"La personne s'appelle {nom}, son age est {age} ans")

def demanger_nom_personne():
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
afficher_informations_personne(nom3, age3)"""
