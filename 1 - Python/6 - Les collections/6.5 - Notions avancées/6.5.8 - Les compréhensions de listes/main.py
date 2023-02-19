# LES COLLECTIONS : LISTES / TUPLES
# Les compréhensions de listes = syntaxe différente pour remplir des éléments avec certaines conditions ?


#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

# Liste avec le nbre de caractères pour chaque nom :
'''longeur_noms = []
for nom in noms:
    longeur_noms.append(len(nom))'''

# On peut arriver au même résultat bcp + rapidement avec une compréhension de liste :

# longeur_noms = [len(nom) if len(nom) < 10 else 0 for nom in noms] --> On peut rajouter des conditions
# noms_avec_e = [nom for nom in noms if "e" in nom]

#a = [i for i in range(11) if (i//2)*2 != i]
b = [(i, True if (i//2)*2 == i else False) for i in range(11)]

print(b)