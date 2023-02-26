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


# --- DEFINITION ---
# nom : str
# age : int
# 1 - Si age == 0 
#   => Bonjour, je m'appelle Toto
#   => On affiche pas mineur
# 2 - Si nom == ""
#   => Demander nom à l'utilisateur
#   => DemanderNom(...) -> input("") -> nom
class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        info_personne = "Bonjour, je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + " ans"

        print(info_personne)

        if self.age != 0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18

    def DemanderNom(self):
        self.nom = input("Nom de la personne : ")


# --- UTILISATION ---
personne1 = Personne("Jean", 30)   # Je cree une personne
personne2 = Personne("Paul", 15)   # Je cree une personne

personne3 = Personne()
personne4 = Personne(age=20)

# Personne.SePresenter(personne1)
personne1.SePresenter()
personne2.SePresenter()  # méthode d'instance
personne3.SePresenter()
personne4.SePresenter()

# print("estMajeur2 : ", personne2.EstMajeur())

# print("nom1: " + personne1.nom)


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
