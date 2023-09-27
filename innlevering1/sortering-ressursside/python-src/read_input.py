import sys


def read_input(filename):
    try:
        with open(filename, 'r') as file:
            data = [int(line.strip()) for line in file]
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)


def insertion(A):
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if A[j] < A[j-1]:
                A.swap(j, j-1)
    return A


# Implementer Merge Sort
def merge(A):
    if len(A) <= 1:
        return A

    # Divide
    mid = len(A) // 2
    left_half = A[:mid]
    right_half = A[mid:]

    # Recursive calls
    left_half = merge(left_half)
    right_half = merge(right_half)

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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort.py <input_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    input_data = read_input(input_filename)

    # Sorter dataene med Insertion Sort
    insertion_sorted_data = insertion(input_data.copy())

    # Sorter dataene med Merge Sort
    merge_sorted_data = merge(input_data.copy())

    # Skriv resultatene til filen
    with open("insertion_sorted.txt", "w") as insertion_file:
        for num in insertion_sorted_data:
            insertion_file.write(str(num) + '\n')

    with open("merge_sorted.txt", "w") as merge_file:
        for num in merge_sorted_data:
            merge_file.write(str(num) + '\n')
