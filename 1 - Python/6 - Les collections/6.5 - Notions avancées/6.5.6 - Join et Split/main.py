# LES COLLECTIONS : LISTES / TUPLES
# join et split

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# Join : Rejoindre -> coller les éléments de la collection. Prend les différents éléments d'une collection et vient les coller ensemble, grâce à un caractère comme le "-" par exemple. Cette fonction concatène chaque chaîne de caractères, avec le "-", par exemple.

noms_join = ", ".join(noms)
print(noms_join)

# Split : Séparer, en liste avec les éléments séparés.
# a = "Paul-Marc-Emilie"
#a_split = a.split("-")
#print(a_split)

noms_resconstruits = noms_join.split(", ")
print(noms_resconstruits)

# Split est l'inverse du join.