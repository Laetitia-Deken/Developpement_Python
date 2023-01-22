# LISTES - ALGO : VALEUR LA PLUS PETITE


nom_chauffeur =       ["Patrick", "Paul", "Marc", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5,      2.2,    0.4,    0.9,    7.1,     1.1,      0.6]


# index_min
# V1
index_min = 0
distance_min = distance_chauffeur_km[0]
for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i

print("Distance minimale:", distance_min, "km")
print("Index de la distance minimale:", index_min)
print("Nom du chauffeur:", nom_chauffeur[index_min])

'''distance_chauffeur_km.sort()
print(distance_chauffeur_km[0])
print(distance_chauffeur_km)'''

'''noms_et_distances = [("Patrick", 1.5), ("Paul", 2.2), ("Marc", 0.4)]

#V2
nom_et_distance_min = noms_et_distances[0]
for nom_et_distance in noms_et_distances:
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print("Distance minimale:", nom_et_distance_min[1], "nom du chauffeur:", nom_et_distance_min[0])'''