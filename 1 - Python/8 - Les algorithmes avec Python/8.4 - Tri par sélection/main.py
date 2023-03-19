import random
# tri par sélection

# l = [5, 8, 1, 4]

#  V # unsorted_index 
# [1, 5, 8, 10, 2] # Le 1 est trié donc on itère à partir du 2 dans la liste
# sorted / unsorted

#     V
# [1, 2, 5, 8, 10] # Le 1 et le 2 sont triés donc on itère  à partir du 5...

#           V
# [1, 2, 5, 8, 10] # et ainsi de suite

# O(N^2)

# print("UNSORTED:", l)

# generate_random_list(n, min, max)  3, 0, 10  [7, 10, 5]
# selection_sort(l)

def generate_random_list(n, min, max):
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

def selection_sort(l):
    for unsorted_index in range(0, len(l)-1): # unsorted_index : index à partir duquel la suite du tableau n'est pas trié
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i          #   V            m
        l[min_index] = l[unsorted_index]   #  [5, 8, 10, 2, 5]
        l[unsorted_index] = min            #  [1, 8, 10, 2, 5]

l = generate_random_list(100, -1000, 1000)
print("UNSORTED:", l)

selection_sort(l)

print("SORTED:  ", l)

