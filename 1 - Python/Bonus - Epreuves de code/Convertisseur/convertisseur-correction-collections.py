# Epreuve de code "Convertisseur"

"""
Collections
    - liste de conversions possibles

    - pouces -> cm (...)
    - cm -> m
    - km -> miles
"""

# unité de départ, unité d'arrivée, facteur de conversion
CONVERSIONS = (                #   choix   index      pair     (choix-1)//2
    ("pouces", "cm", 2.54),        # 1      0          F         0
                                   # 2      0 + R      T         0
    ("m", "cm", 100),              # 3      1                    1
                                   # 4      1 + R                1
    ("km", "miles", 0.621371),     # 5      2                    2
                                   # 6      2 + R                2
    ("yard", "m", 0.9144), 
    ("kg", "livres", 2.20462),    
)

#Définir le sens de la conversion :
def demander_et_afficher_conversion(unit1: str, unit2: str, facteur: float, reverse: bool = False):
    if reverse: # reverse --> en mode inversé
        unit1, unit2 = unit2, unit1 # On inverse les unités
        facteur = 1 / facteur # il faut aussi inverser le facteur

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

# Fonction récursive :
def demander_valeur_numerique_utilisateur(valeur_min, valeur_max):
    v = input(f"Donnez une valeur entre {valeur_min} et {valeur_max} : ")
    try:
        v_int = int(v)
    except:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        return demander_valeur_numerique_utilisateur(valeur_min, valeur_max)

    if not (valeur_min <= v_int <= valeur_max):
        print(f"ERREUR : Votre valeur doit être entre {valeur_min} et {valeur_max}")
        return demander_valeur_numerique_utilisateur(valeur_min, valeur_max)

    return v_int # tout est bon
    

# Menu : choix de la conversion
print("Ce programme vous permet d'effectuer des conversions d'unités")
i = 1
for c in CONVERSIONS:
    unit1 = c[0]
    unit2 = c[1]
    print(f"{i} - {unit1} vers {unit2}")
    i += 1
    print(f"{i} - {unit2} vers {unit1}")
    i += 1

valeur_choix_maximale = i-1 # variable intermédiaire

choix_int = demander_valeur_numerique_utilisateur(1, valeur_choix_maximale)


while True:
    # Demander les valeurs à convertir à l'utilisateur

    # Si le choix utilisateur est 1 alors l'index est 0 (premier idem de CONVERSIONS)
    # Divisé par 2, car on génére des options intermédiaires de conversions inverse
    #   choix = 2 -> index = 0 mais reverse = True (converison inverse)
    index = (choix_int-1)//2
    # True si la valeur est pair
    reverse = choix_int % 2 == 0
    # 1 % 2 = 0 x 2 + 1
    # 2 % 2 = 1 x 2 + 0
    # 3 % 2 = 1 x 2 + 1
    # 4 % 2 = 2 x 2 + 0
    unit1, unit2, facteur = CONVERSIONS[index]

    if demander_et_afficher_conversion(unit1, unit2, facteur, reverse):
        break




