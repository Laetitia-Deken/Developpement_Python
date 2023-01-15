# EXERCICE FONCTIONS
# Tables de multiplication
#
#
# 1 x 4 = 4
# 2 x 4 = 8
# 3 x 4 = 12
# ...
# 10 x 4 = 40
#
# afficher_table_multiplication(n)
# min / max
# erreur : si min > max => erreur


def afficher_table_multiplication(n, min=1, max=10):
    if min > max:
        print("ERREUR : Le min est supéreur au max")
        return

    for i in range(min, max+1):
        print(i, "x", n, "=", i*n)


afficher_table_multiplication(5, 10, 1)


