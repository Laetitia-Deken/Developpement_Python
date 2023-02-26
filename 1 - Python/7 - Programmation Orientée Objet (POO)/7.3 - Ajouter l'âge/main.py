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
class Personne:
    def __init__(self, nom: str, age: int): # Passer les données dans le constructeur, et pas la méthode SePresenter
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        print("Constructeur personne " + nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")


# --- UTILISATION ---
personne1 = Personne("Jean", 30)   # Je cree une personne
personne2 = Personne("Paul", 25)   # Je cree une personne

personne1.nom = "toto"

# Personne.SePresenter(personne1)
personne1.SePresenter()
personne2.SePresenter()  # méthode d'instance


print("nom1: " + personne1.nom)


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
