def sort(A):
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j] < A[j-1]:
                A.swap(j, j-1)
    return A
