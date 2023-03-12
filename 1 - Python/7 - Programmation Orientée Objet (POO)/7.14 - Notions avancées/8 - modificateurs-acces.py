# Modificateurs d’accès : Public, private, protected

# public : accès depuis l'intérieur et l'extérieur de la classe
# private : accès depuis l'intérieur de la classe uniquement (__a)
# protected : accès depuis l'intérieur de la classe et des classes dérivées (_a)

class Personne:
    def __init__(self, nom):
        # private
        self._nom = nom

    def se_presenter(self):
        print(f"Je m'appelle {self._nom}")


class Etudiant(Personne):
    def se_presenter(self):
        print(f"Je suis étudiant, je m'appelle {self._nom}")

personne1 = Etudiant("Jean")
personne1.se_presenter()

print(personne1.__dict__)

