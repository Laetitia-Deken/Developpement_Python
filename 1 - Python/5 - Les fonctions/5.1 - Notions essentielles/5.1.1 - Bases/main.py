# Les fonctions



'''nom = "toto"
print("Je m'appelle " + nom) # concaténé la chaine # <- 1 seul paramètre
print()
print("Je m'appelle", nom) # <- 2 paramètres
'''

'''nom = input("Votre nom :")  # <- Retourne une valeur (fonction bloquante)
print("Votre nom est:", nom)'''


'''
recuperer_et_afficher_infos_personne
    -> recuperer_infos_personne()
    -> afficher_infos_personne(nom, age)
        -> est_majeur()

'''
# str : chaines de caractères
# int : nombre entiers
def est_majeur(age: int):
    if age <= 0:  # "40" <= 0
        return False
    # Vrai ou Faux (True / False)
    # si l'age >= 18 => True sinon False
    if age >= 18:
        return True
    return False
    
def recuperer_infos_personne(numero_personne):
    nom_personne = input("Nom de la personne " + str(numero_personne) + ": ")
    age_personne = input("Age de la personne " + str(numero_personne) + ": ")
    return nom_personne, int(age_personne)


def afficher_infos_personne(numero_personne, nom, age: int):
    print("La personne", numero_personne, "est", nom, "son age est", age, "ans")
    print("le nom possède", len(nom), "caractères")
    if est_majeur(age):
        print("il est majeur")
    else:
        print("il est mineur")

# implémenter recuperer_et_afficher_infos_personne
# parametre : numero_personne
# rien retourner
# input / print
# nom / age
def recuperer_et_afficher_infos_personne(numero_personne):
    nom, age = recuperer_infos_personne(numero_personne)
    afficher_infos_personne(numero_personne, nom, age)

nb_personnes = 2

for i in range(nb_personnes):  # 0 1 2
    recuperer_et_afficher_infos_personne(i+1)

afficher_infos_personne("007", "James", 40)


# return (pas obligatoire)
# -> sortir de la fonction
# -> renvoyer une valeur (pas obligatoire)
'''


# définition de la fonction
def afficher_infos_personne(nom="", age=0):
    if nom == "":
        print("Vous n'avez pas donné de nom, l'age vaut", age)
        return
    
    if age == 0:
        print("La personne est", nom)
    else:
        print("La personne est", nom + ", son age est", age, "ans")

    print("Le nom comporte", len(nom), "caractères")
    if est_majeur(age):
        print("il est majeur")
    else:
        print("il est mineur")


print("Début du programme")

#afficher_infos_personne(age="20")

age = 10

if age == 0:
    exit(0)

print("La personne a", age, "ans")
majeur_ou_non = est_majeur(age)
if majeur_ou_non:
    print("il est majeur")
else:
    print("il est mineur")

print("Fin du programme")
'''