# Epreuve de code "Convertisseur"




"""
A -> B
  x2
5a -> 10b

B -> A
  x0.5  (1/2)
10b -> 5a

- Idée
- Collections
- Orienté objet
- Analyse (collections)
"""

#Définir le sens de la conversion :
def demander_et_afficher_conversion(unit1: str, unit2: str, facteur: float, reverse: bool = False): # reverse --> en mode inversé
    if reverse: # On inverse les unités
        unit1, unit2 = unit2, unit1
        facteur = 1 / facteur

    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quitter) : ")
    if valeur_str == "q":
        return True
    try:
        valeur_float = float(valeur_str)
    except ValueError:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        print("(utilisez le point et non la virgule pour les décimales)")
        return demander_et_afficher_conversion(unit1, unit2, facteur)

    valeur_convertie = round(valeur_float * facteur, 2)
    print(f"Résultat de la conversion : {valeur_float} {unit1} = {valeur_convertie} {unit2}")
    return False


while True:
    # Menu : choix de la conversion
    print("Ce programme vous permet d'effectuer des conversions d'unités")
    print("1 - Pouces vers cm")
    print("2 - cm vers pouces")
    choix = input("Votre choix (1 ou 2): ")
    if choix == "1" or choix == "2":
        break
    print("ERREUR : Vous devez choisir 1 ou 2")

while True:
    # Demander les valeurs à convertir à l'utilisateur
    if demander_et_afficher_conversion("pouces", "cm", 2.54, reverse=False if choix == "1" else True): # reverse = False --> voir au-dessus
        break




