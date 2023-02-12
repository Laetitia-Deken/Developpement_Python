# LES COLLECTIONS : LISTES / TUPLES
# Tris : Sort / Sorted
# sort() --> tri dans l'ordre alphabétique, directement dans une liste, ici noms. On n'a pas copié la liste. C'est une opération "in place".
# sorted --> prend une collection, ici noms et créé une nouvelle liste, qui va être triée. La liste originale est préservée.

def tri_longeur_caracteres(nom):
    return len(nom)

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# tri par ordre alphabetique STR
# du plus petit au plus grand INT
#noms.sort(key=tri_longeur_caracteres, reverse=True)  # inplace
noms_tries = sorted(noms, key=tri_longeur_caracteres, reverse=True)  # créer une nouvelle liste
# reverse = True --> ordre dans l'ordre alphabétique inversé

print(noms)
print(noms_tries)


