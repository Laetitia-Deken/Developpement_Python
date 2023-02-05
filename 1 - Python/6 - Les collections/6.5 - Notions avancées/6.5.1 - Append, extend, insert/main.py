# LES COLLECTIONS : LISTES / TUPLES
# Append / Extend / += / Insert

# Append = ajouter un seul élément à la fin. Il ajouter telle quelle. Si on met une liste, comme ci-dessous, il ajoute cette liste sans réfléchir. Pour ajouter les deux éléments en tant que chaînes de caractères, de manière individuelle, boucler !
# --> Pour faire cela plus rapdement qu'une boucle, utiliser "extend" au lieu de boucler.
# --> += se comporte comme "extend" : il ajoute les éléments les uns après les autres
# --> Insert[index] : insérer un élément au début ou au milieu d'une liste, au lieu de la fin, comme c'est le cas avec append

noms = ["Jean", "Sophie", "Martin"]

noms_supplementaires = ["Christophe", "Zoe"]

#noms.append(noms_supplementaires)
# for e in noms_supplementaires:
#    noms.append(e)
#noms.extend(noms_supplementaires)
# noms += noms_supplementaires
# noms = noms + noms_supplementaires  --> le +, c'est comme "extend". Attention, on concatène des éléments de même type, sinon ça ne marche pas ! Sur les listes, le + se comporte comme extend.

# noms.append("Toto")
# noms.insert(1, "Toto")

noms = noms + noms_supplementaires

print(noms)




