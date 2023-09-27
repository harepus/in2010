def merge(A):
    if len(A) <= 1:
        return  # Base case: single-element array is already sorted

    mid = len(A) // 2
    left_half = A[:mid]
    right_half = A[mid:]

    # Sort the halves
    merge(left_half)
    merge(right_half)

    # Merge the sorted halves
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            A[k] = left_half[i]
            i += 1
        else:
            A[k] = right_half[j]
            j += 1
        k += 1

    # If there are remaining elements in left_half
    while i < len(left_half):
        A[k] = left_half[i]
        i += 1
        k += 1

    # If there are remaining elements in right_half
    while j < len(right_half):
        A[k] = right_half[j]
        j += 1
        k += 1

    return A  # Return the sorted list

# Run all sorting algorithms and create .out files
# def run_algs_part2(A, infilename):
