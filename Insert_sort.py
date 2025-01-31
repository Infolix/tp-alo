import random

def tri_insert(A):  
    for j in range(1, len(A)):  
        k = A[j]
        i = j - 1
        while i >= 0 and A[i] > k:  
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = k


A = [random.randint(1, 100) for _ in range(100000)]

tri_insert(A)  


print(A[:10])
