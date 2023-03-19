# Inverser une chaine (Reverse)
#
# "Bonjour toto"
# "otot ruojnoB"
#
# Boucle
# Slice

# Boucle

def reverse_string1(str):
    r = ""
    for c in str:
        r = c + r
    return r

# Slice

def reverse_string2(str):
    return s[::-1] # + rapide à exécuter car - d'instructions


s = "Bonjour toto"
# print(reverse_string1(s))

print(reverse_string2(s))
