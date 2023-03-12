# Méthodes d’instance, de classe et statiques

class Personne:
    TYPE = "Humain"
    def __init__(self, nom):
        self.nom = nom

    # Méthode d'instance
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self.nom)} - " + self.TYPE)

    # premier charactère en majuscule puis minuscules
    # méthode statique
    @staticmethod
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower()

    @classmethod
    def methode_de_classe(cls):
        print("Méthode de classe : " + cls.TYPE)


personne1 = Personne("jean")
personne1.se_presenter()

print(Personne.formater_chaine("toTo"))

Personne.methode_de_classe()