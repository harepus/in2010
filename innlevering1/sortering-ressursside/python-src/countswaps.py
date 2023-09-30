class CountSwaps(list):
    swaps = 0

    def swap(self, i, j):
        # print(f"Swapping elements at indices {i} and {j}")
        self.swaps += 1
        # print(f"Number of swaps so far: {self.swaps}")
        self[i], self[j] = self[j], self[i]
