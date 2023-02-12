# LES COLLECTIONS : LISTES / TUPLES
# Operations sur les éléments : min, max, in, sum
# in -> permet de savoir su une valeur est à l'intérieur d'une collection
# sum : somme --> uniqueent sur les collections qui contiennent des valeurs numériques

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

print(min(noms)) --> # Christophe, car commence par un "C", c'est le min dans l'ordre alphabétique des noms, et non pas Zoé, qui possède le - de caractères. Il vaut mieux utiliser min et max pour ces valeurs numériques.

ages = [21, 20, 30, 25, 22]

'''if 31 in ages:
    print("Présent")
else:
    print("Abscent")'''

'''found = False
for nom in noms:
    if nom == "Martin":
        found = True
        break
if found:
    print("Présent")
else:
    print("Abscent")'''

print(sum(ages))
