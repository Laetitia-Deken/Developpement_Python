# LES COLLECTIONS : LISTES / TUPLES
# Slices = sélectionnent certains éléments dans une liste.

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

slices_noms = noms[-2:] # [inclus:exclu]
slices_noms = noms[1:] # démarre à 1 jusqu'à la fin de la liste. Et on fait une copie de la liste noms avec les mêmes valeurs en mémoire. On a donc 2 listes = la liste noms et la liste recopiée sclices_noms.

#noms[0] = "Toto"

print(slices_noms)
#print(noms)

# QUAND ON FAIT UN SLICE, ON CREE UNE NOUVELLE LISTE !!



