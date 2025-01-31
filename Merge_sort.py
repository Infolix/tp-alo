import random 
def fusion(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    # Création des sous-tableaux gauche (L) et droit (R)
    L = [A[i] for i in range(p, q + 1)] + [float('inf')]  # Ajouter un élément sentinelle
    R = [A[i] for i in range(q + 1,r + 1)] + [float('inf')]

    i = 0  # Indice du sous-tableau gauche
    j = 0  # Indice du sous-tableau droit

    # Fusion des deux sous-tableaux dans A[p:r]
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def tri_fusion(A, p, r):
    """  trier recursivement et faire la fusion """
    if p < r:
        q = (p + r) // 2  # Trouver le milieu du tableau
        tri_fusion(A, p, q)  # Trier la première moitié
        tri_fusion(A, q + 1, r)  # Trier la deuxième moitié
        fusion(A, p, q, r)  # Fusionner les deux moitiés triées

import random

A = []  # Initialiser une liste vide
for i in range(1000):
    n = random.randint(1, 500)
    A.append(n)  # Ajouter n à la liste

tri_fusion(A, 0, len(A) - 1)  # Appliquer le tri fusion
print(A)  # Affiche un tableau trié
