# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Nombre total de caractères"

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# 1 - for / len # Boucle
'''s = 0
for nom in noms:
    s += len(nom)
print("Nombre total de caractères:", s)''' # Prend le - de mémoire, on prend les valeurs telles quelles puis compteur

# 2 - Completion de liste + sum # Reconstruit une liste, puis sum
# longeur_noms = [len(nom) for nom in noms]
# print("Nombre total de caractères:", sum(longeur_noms)) # Prend le + de mémoire

# 3 - Join / len # Silple --> concatène les résultats en une chaine de caractères puis récup la longueur de cette chaine
print("Nombre total de caractères:", len("".join(noms))) # Meilleure méthode, + pratique car en faisant un join, on cécrit un code très court. 
