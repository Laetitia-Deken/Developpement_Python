# LES COLLECTIONS : LISTES / TUPLES
# Swapper deux éléments (échanger deux éléments dans une liste)
# Attention au rique d'écrasement ! Conseillé de créer une variable intermédiare pour sauvegarder la liste originale avant de swapper

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

'''t = noms[0]  # Jean
noms[0] = noms[4]  # Jean <- Zoe
noms[4] = t'''

#                     Zoe      Jean
noms[0], noms[4] = noms[4], noms[0] # récupère les valeurs en une fois, on n'écrase plus une valeur qu'on va perdre

print(noms)
