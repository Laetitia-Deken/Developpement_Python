# LES COLLECTIONS : LISTES / TUPLES
# index, find et count
# Index : savoir où, à quel index, se situe un élément dans une collection. Donne toujours l'index de la première valeur trouvée.
# Count : trouver le nombre d'occurences dans une liste
# Find : même esprit que index, mais fonctionne sur les chaînes de caractères, pas sur des collections (listes)


#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]


element_cherche = "Martin"
nb_occurences = noms.count(element_cherche)
print("nb_occurences", nb_occurences)
if nb_occurences > 0:
    index_occurence = 0
    for i in range(nb_occurences):
        index_occurence = noms.index(element_cherche, index_occurence)
        print(element_cherche, "trouvé à", index_occurence)
        index_occurence += 1
else:
    print("L'élément n'est pas dans la collection")

