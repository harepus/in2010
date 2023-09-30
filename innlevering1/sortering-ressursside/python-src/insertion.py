from countswaps import CountSwaps


def sort(A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i-1
        while j >= 0 and temp < A[j]:
            A.swap(j, j+1)
            j -= 1
        A[j+1] = temp
    return list(A)
