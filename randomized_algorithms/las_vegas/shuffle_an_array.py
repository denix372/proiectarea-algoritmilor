import random

# Fisher-Yates Algorithm
class Solution:

    def __init__(self, nums: list[int]):
        self.original = nums.copy()
        self.array = nums.copy()

    def reset(self) -> list[int]:
        self.array = self.original.copy()
        return self.array

    def shuffle(self) -> list[int]:
        n = len(self.array)
        for i in range(n):
            # choose a arrayomly index
            j = random.randint(i, n - 1)

            self.array[i], self.array[j] = self.array[j], self.array[i]

        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

solution = Solution([1, 2, 3])
print(solution.shuffle())    # Shuffle the array [1,2,3] and return its result.
                       # Any permutation of [1,2,3] must be equally likely to be returned.
                       # Example: return [3, 1, 2]
print(solution.reset())      # Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
print(solution.shuffle())    # Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]


'''
PROBABILISTIC ANALYSIS (Fisher-Yates Shuffle)

A) Algorithm Idea:
   At step i, we randomly select one element from the remaining (n - i) elements 
   (including the element currently at index i) and place it at index i.

B) Uniform Distribution Proof:
   We must prove that the probability of generating any specific permutation 
   is exactly 1 / n!.
   - At index 0: probability of picking a specific element is 1 / n.
   - At index 1: probability of picking the next specific element is 1 / (n - 1).
   - At index 2: probability is 1 / (n - 2).
   ...
   - At index n-1: only 1 element remains, so the probability is 1 / 1.

   According to the product rule (independent events at each draw), 
   the probability of obtaining a specific arrangement is:
   P = (1 / n) * (1 / (n - 1)) * (1 / (n - 2)) * ... * 1 = 1 / n!

C) The Naive Approach Flaw (Common Interview Trap):
   If we always picked j = random.randint(0, n - 1) at each step, the algorithm 
   would generate n^n possible draw sequences. Since n^n is not cleanly divisible 
   by n! (for n > 2), it is mathematically impossible for all n! permutations 
   to have the same probability. Fisher-Yates avoids this by shrinking 
   the selection pool to n - i elements (generating exactly n! decision paths).

D) Complexity:
   - Time Complexity: O(N) because we perform exactly N steps, and swapping is O(1).
   - Space Complexity: O(N) to store the copy of the original array.
'''