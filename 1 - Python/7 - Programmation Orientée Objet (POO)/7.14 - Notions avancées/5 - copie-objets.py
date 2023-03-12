import copy
# COPIER DES OBJETS
# shallow copy / deep copy
# deepcopy : crée une copie de l'instance de jeu de données ainsi qu'une copie du jeu de données associé à l'instance
# shallow copy : copie superficielle

class Personne:
    def __init__(self, nom, age, amis):
        self.nom = nom
        self.age = age
        self.amis = amis

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")
        print("Amis : " + str(self.amis))

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age


personne1 = Personne("Jean", 20, ["Claire", "Marc", "Emilie"])
personne1.AfficherInfos()

personne2 = copy.deepcopy(personne1) 
# personne1.nom = "Toto"
personne1.amis[0] = "Chantale"
personne2.AfficherInfos()

print(personne1 == personne2)
print(personne1 is personne2)

print(personne1.__dict__ == personne2.__dict__)