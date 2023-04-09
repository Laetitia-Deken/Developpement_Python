# Cuisson des oeufs, correction

"""
- Oeufs à la coque : 3 minutes
- Oeufs mollets : 6 minutes
- Oeufs durs : 9 minutes

import time
time.sleep(1)
print(".", end="", flush=True)

d = 100
min = d//60 # division entière (pas de virgules)
sec = d-min*60

print(f"{min:02d}")

"""
DUREE_PROGRESSION = 10

import time
import beepy # pour installer un son

# Afficher le menu :
print("Cuisson des oeufs")
print("1 - Oeufs à la coque : 3 minutes")
print("2 - Oeufs mollets : 6 minutes")
print("3 - Oeufs durs : 9 minutes")
while True :
    choix = input("Votre choix : ") # format str
    if choix == "1" or choix == "2" or choix == "3": # si tout est bon, on break et on passe à la suite du code
         break
    print("ERREUR: Vous devez choisir 1, 2 ou 3\n") # on retourne au début de la boucle

duree = 0
if choix == "1": # en fonction du choix utilisateur
    duree = 3 * 60 # convertir minutes en secondes
if choix == "2":
    duree = 6 * 60
if choix == "3":
    duree = 9 * 60

while True:
    for i in range(DUREE_PROGRESSION): # boucler pendant le temps de progression, ici = 10 secondes
        time.sleep(1) # bloquer le temps pendant 1 seconde
        print(".", end="", flush=True) # on force l'affichage de ce print - pour afficher des points
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

