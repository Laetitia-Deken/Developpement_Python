# Cuisson des oeufs, correction
# Les collections permettent de rendre le programme + flexible
DUREE_PROGRESSION = 10

import time
import beepy

# titre : "Oeufs à la coque"
# duree : 3*60

CHOIX_CUISSON = (
    ("Oeufs à la coque", 3*60),
    ("Oeufs mollets", 6*60),
    ("Oeufs durs", 9*60),
    ("Steak à point", 4*60 + 30),
    ("Test1", 5),
    ("Test2", 11),
    ("Test3", 15),
)

def temps_sec_en_str(t):
    min = t//60 # division entière (pas de virgules)
    sec = t-min*60
    min_unit = "minutes"
    sec_unit = "secondes"
    if min == 1:
        min_unit = "minute"
    if sec == 1:
        sec_unit = "seconde"
    r = ""
    if min > 0:
        r += f"{min} {min_unit}"
    if sec > 0:
        if len(r) > 0:
            r += " "
        r += f"{sec} {sec_unit}"
    return r
     
def demander_valeur_numerique_min_max(min, max):
    valeur = input(f"Rendrez une valeur entre {min} et {max} : ")
    try:
        valeur_int = int(valeur)
    except:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        return demander_valeur_numerique_min_max(min, max)
    if not (min <= valeur_int <= max):
        print(f"ERREUR : Vous devez rentrer une valeur numérique entre {min} et {max}")
        return demander_valeur_numerique_min_max(min, max) # fonction récusive, se rappelle elle-même
    return valeur_int

# Affichage du menu
print("Choix de la cuisson")
index_choix = 1
for choix_cuisson in CHOIX_CUISSON: # on boucle sur les choix de cuissons :
    print(f"{index_choix} - {choix_cuisson[0]} : {temps_sec_en_str(choix_cuisson[1])}")
    index_choix += 1

choix = demander_valeur_numerique_min_max(1, len(CHOIX_CUISSON))

choix_cuisson = CHOIX_CUISSON[choix-1] # choix 1 = index 0, d'où le -1
duree = choix_cuisson[1]
print(f"{choix_cuisson[0]} : {temps_sec_en_str(choix_cuisson[1])}", end="", flush=True)

while True:
    for i in range(DUREE_PROGRESSION):
        time.sleep(1)
        print(".", end="", flush=True)
        duree -= 1
        if duree <= 0:
            break

    if duree <= 0:
        break
    min = duree//60 # division entière (pas de virgules)
    sec = duree-min*60
    print()
    print(f"Temps restant : {min:02d}:{sec:02d}", end="", flush=True)

print()
print("Cuisson terminée")
beepy.beep(sound="ping")

