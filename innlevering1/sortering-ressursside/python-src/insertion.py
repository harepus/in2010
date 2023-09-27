def sort(A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i-1
        while j >= 0 and temp < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = temp
    return A


'''
Testing code for insertion sort :D
A = [80, 91, 7, 33, 50, 70, 13, 321, 12]
sort(A)
print(A)
'''
