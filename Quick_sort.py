import random

def quicksort(tab, p, r):
    if p < r:
        q = partition(tab, p, r)
        quicksort(tab, p, q - 1)
        quicksort(tab, q + 1, r)

def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= x:
            i += 1
            exchange(tab, i, j)
    
    exchange(tab, i + 1, r)
    return i + 1   

def exchange(A, i, j):
    Buf = A[i]
    A[i] = A[j]
    A[j] = Buf        

A = []  # Initialiser une liste vide
for i in range(1000):
    n = random.randint(1, 500)
    A.append(n)  # Ajouter n à la liste

quicksort(A, 0, len(A) - 1)

print(A)
