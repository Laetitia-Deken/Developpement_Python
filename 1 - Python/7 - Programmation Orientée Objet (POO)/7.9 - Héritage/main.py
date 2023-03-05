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


#          EtreVivant            ## Classe parent
#      Chat         Personne     ## Classes enfant (classes dérivées)
class EtreVivant: # Rassemble les caractéristiques communes entre tous les êtres vivants
    ESPECE_ETRE_VIVANT = "(être vivant non identifié)"

    def AfficherInfosEtreVivant(self):
        print("Info être vivant : " + self.ESPECE_ETRE_VIVANT)

class Chat(EtreVivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"

class Personne(EtreVivant):
    ESPECE_ETRE_VIVANT = "Humain (Mammifère Homo sapiens)"   # variable de classe (1 pour toutes les Personnes)

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

# EtreVivant
# Personne
# Etudiant
class Etudiant(Personne):
    def __init__(self, nom: str, age: int, etudes: str):
        # self.nom = nom   # crée une variable d'instance : nom
        # self.age = age
        super().__init__(nom, age)
        self.etudes = etudes

    def SePresenter(self):  # surchargé la méthode SePresenter
        super().SePresenter()
        print("Je suis etudiant en " + self.etudes)

# --- UTILISATION ---
liste_personnes = [Personne("Jean", 30), 
                   Personne("Paul", 15),
                   Personne("Zoe", 20)]

# Personne.ESPECE_ETRE_VIVANT = "Mutant"

for personne in liste_personnes:
    personne.SePresenter()
    personne.AfficherInfosEtreVivant()
    print()

chat = Chat()
chat.AfficherInfosEtreVivant()

etreVivant = EtreVivant()
etreVivant.AfficherInfosEtreVivant()

etudiant = Etudiant("Marc", 22, "Ecole d'ingénieur informatique")
etudiant.SePresenter()
etudiant.AfficherInfosEtreVivant()

# Personne
#       -> Personne.espece_etre_vivant
#    personne1
#       -> self.espece_etre_vivant (copie de la variable de classe pour en faire une variable d'instance)
#    personne2
#       -> self.espece_etre_vivant
#    personne3
#       -> self.espece_etre_vivant

