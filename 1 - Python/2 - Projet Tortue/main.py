# Modules = programmes qui contiennent des fonctions réutilisables. Appelées aussi "bibliothèques" ou "librairies".
# Certaines existent dans Python (c'est le cas de "tortue", d'autres sont à telecharger.

"""
# Importer le module "Turtle", deja existant dans Python
import turtle

t = turtle.Turtle() # ici on crée une variable objet

#Deplacer la tortue
t.forward(100) # Permet à la tortue de se déplacer en avant, de (xxx) pixels.
t.left(90) # Tortue pivote a gauche de (xxx) degrés sur elle-meme (elle ne se deplace pas !)
t.forward(50)
t.backward(100) # Tortue se deplcae en arriere de (xxx) pixels
t.right(45) # Tortue pivote a droite de (xxx) degrés sur elle-meme (elle ne se deplace pas !)
t.forward(200)


turtle.done() # garder la fenetre active tant qu'on ne la ferme pas nous-memes
"""

#Exercice : faire un escalier de 5 marches de 30 pixels
import turtle

# Definition de la fonction escalier
def escalier(taille, nb):
    for i in range(0, nb):  # boucle for pour dupliquer les marches sans copier/coller les 4 lignes ci-dessous :
        t.forward(taille)  # 4 etapes pour creer 1 marche de l'escalier
        t.left(90)
        t.forward(taille)
        t.right(90)
        # taille = taille - 10 # fait evoluer la valeur de la variable taille
        # taille -= 10 -> decremente la valeur de taille par 10 a chaque marche (pareil mais + simple que ligne ci-dessus)
    t.forward(taille)  # pas dans la boucle -> fait juste pour terminer l'escalier

# Exercice : dessiner un carre
def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

#Exercice : dessiner plusieurs carres
def carres(taille_depart, nb): # dessiner plusieurs carres
    for i in range(0, nb):
        taille = (i+1)*taille_depart # -> taille du carre
        carre(taille) # tracé du carre

t = turtle.Turtle()

# Appel de la fonction pour creer les 5 marches de 30 pixels :
# escalier(30, 5)
# carre(50) # dessiner plusieurs carres colles (+ ligne ci-dessous)
# carre(100)
carres(10, 10)

turtle.done()