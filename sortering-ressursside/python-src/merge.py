def merge_sort(A):
    if len(A) <= 1:
        return A

    # Divide
    mid = len(A) // 2
    left_half = A[:mid]
    right_half = A[mid:]

    # Recursive calls
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge
    result = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            A.swap(i, i + j)  # Swap and count
            result.append(left_half[i])
            i += 1
        else:
            A.swap(i + j, i + j)  # Swap and count
            result.append(right_half[j])
            j += 1

    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result

# Usage:
# Call merge_sort(A) with your custom A data structure to sort an array.
