# création de la definition de la fonction "demander le nom"
def demander_nom():
    reponse_nom = ""  # Nom de la variable locale a cette fonction. Meme si vide, Python comprend variable de type "chaine de caracteres"
    while reponse_nom == "":
       reponse_nom = input("Quel est votre nom ? ")  # si l'utilisateur ne rentre rien, ça boucle
        # la fonction input est bloquante, on attend une reponse de l'utilisateur
    return reponse_nom # on retourne la valeur du nom

"""
Creation d'une fonction "demander_age" pour structurer le code : on utilise def pour définir la fonction.
Attention, tout ce qui est a l'interieur de def n'existe que a l'interieur de la fonction def et pas sur le reste du code.
Les fonctions possedent donc un contexte.
"""

# Creation de la definition de la fonction "demander age"
def demander_age(nom_personne): # entre () -> paramètre de cette fonction, qui permet de rendre une fonction independante
    age_int = 0
    # autre possibilite : global age -> age dans le contexte global et pas local a la fonction. Ici renvoie a age = 0.
    while age_int == 0: # while est une boucle. Signifie "tant que..."
        age_str = input(nom_personne + " Quel est votre age ? ")  # -> age reçu de l'utilisateur
        # age_str -> age au format "chaîne de caractères"
        try: # permet "d'essayer"
            age_int = int(age_str)  # -> conversion en nombre
        except: # si try ne fonctionne pas, afficher l'exception ci-dessous :
            print("ERREUR: Vous devez rentrer un nombre pour l'age.")
    return age_int

# Afficher les informations d'une personne
def afficher_informations_personne(nom, age, taille=0):
    # taille=0 -> paramètre optionnel car on a rentré une valeur par défaut : ici, 0.
    print()  # permet de créer une ligne d'espace
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans.")
    print("L'an prochain vous aurez " + str(age + 1) + " ans.")

    # 2 Autres facons de concatener des chaines de caractères -> chaines formatees :
    # print(f"Vous vous appelez {nom}, vous avez {age} ans.") / f -> formater + {} qui prennent le nom de la variable
    # print("L'an prochain vous aurez %s ans." % (age + 1)) / %s + donner 1 valeur de %s
    # print("Vous vous appelez %s, vous avez %s ans." (nom, age)) / remplacer plusieurs valeurs dans %s


    # Conditions
    # condition = age >= 18 (creation d'une condition avec resultat de type booleen -> True / False)
    # print(condition)
    if age == 1 or age == 2: # if -> si (+ condition). Place toujours en 1er dans les conditions. / or -> ou
        print("Vous êtes un bébé.")
    elif age < 10:
        print("Vous êtes enfant.")
    elif age == 1 or age == 2: # or -> ou
        print("Vous êtes un bébé.")
    elif 12 <= age < 18: # autre possibilité : elif >= 12 and age < 18:
        print ("Vous êtes adolescent.")
    elif age == 17: # elif -> sinon si (+ condition). Toujours place entre "if" et "else".
        print("Vous êtes presque majeur.")
    elif age == 18:
        print("Tout juste majeur : Félicitations !")
    elif age > 60:
        print("Vous êtes sénior.") # a mettre avant age >= 18 car cas particulier : 60 > 18 !
    elif age >= 18:
        print("Vous êtes majeur.")
    else: # else -> sinon. Place toujours en bas dans les conditions. Si aucune condition ci-dessus n'est respectée, c'est celle-ci qui s'affiche.
        print("Vous êtes mineur.")
    """
    Attention à l'ordre dans la creation des conditions vu que le code est teste de haut en bas !
    Une condition valable en haut pourrait bloquer une de celles en bas !
    Conseil : privilegier d'abord les cas particuliers avant de taper les cad generaux.
    """

    # Afficher la taille
    # taille = 1.75 # variable de type "nombre à virgule" (float) mais tout le monde ne mesure pas 1.15m.
    if not taille == 0: # si la taille n'est PAS 0 (valeur rentrée par défaut dans def afficher_informations_personne)
        print("Votre taille est : " + str(taille) + " m.")

# demander le nom
# Ce sont des appels à la foncrion demander_nom
nom1 = demander_nom()
nom2 = demander_nom() #creation de la variable nom pour recuperer un resultat, comme pour input
# appel de la fonction créée ci-dessus

# demander l'age
#Ce sont des appels à la fonction demander_age
age1 = demander_age(nom1) # nom1 -> argument
age2 = demander_age(nom2) # creation de la variable nom pour recuperer un resultat, comme pour input
# appel de la fonction créée ci-dessus
# ne pas oublier de lier nom1 -> age 1 / nom2 -> age2

#Afficher les résultats :
afficher_informations_personne(nom1, age1) # attention ! Oredre des paramètres important
afficher_informations_personne(nom2, age2)

NB_PERSONNES = 1
""" Variable constante -> permet de mieux comprendre le code.
Les constantes n'existent pas vraiment dans Python, c'est plus une convention pour mieux reconfigurer le code.
"""

# la boucle for -> permet de boucler un certain nombre de fois / d'éléments concernant les listes
for i in range(0, NB_PERSONNES): # i -> nom de la variable -> declare la variable -> index / Range -> dans l'ensemble.
# for i in range -> pour i dans l'ensemble
    nom = "personne" + str(i+1)
    age = demander_age(nom) # Attention ! On ne peut pas concatener des noms de variable !
    afficher_informations_personne(nom, age) # ici, les arguments nom et age se rapportent aux deux lignes ci-dessus

# print sur plusieurs lignes -> même principe que les commentaires sur plusieurs lignes.
# print("""
# Mettre
    # ce que
        # l'on veut
# """)

# Ajouter d'autres arguments à la fonction print :
print("toto", 20, "ans", "taille:", 1.70) # -> affiche les uns après les autres séparés par un espace.
# ici, on a pas converti les str et int car on a pas de "+" mais des ",". On a pas concatene.

