import random

class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            i = self.partition(arr, low, high)
            self.quickSort(arr, low, i - 1)
            self.quickSort(arr, i + 1, high)

    def partition(self, arr, low, high):
        # 1. Generate a random index between low and high

        rand_idx = random.randint(low, high)
        # 2. Swap the random element with the last element to reuse your exact Lomuto logic
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
        
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


sol = Solution()
arr = [4, 1, 3, 8, 7]
sol.quickSort(arr, 0, len(arr) - 1)
print(arr)

'''
TIME COMPLEXITY ANALYSIS (Las Vegas Algorithm)

A) Algorithm Idea: 
   Sorting by partitioning the array around a pivot. Smaller elements go left, 
   larger go right. Efficiency critically depends on how "balanced" the partition is.

B) Randomized Component: 
   Pivot selection. Instead of a fixed position (e.g., first or last), we select an 
   index i = random(low, high) and swap it with the control element.

C) Classification: Las Vegas Algorithm.
   It always returns the correct solution (the sorted array), but its execution 
   time is a random variable.

D) Complexity Mini-Proof:
   - Recurrence Relation: T(n) = n + T(k) + T(n-k-1)
     In the worst-case scenario (extreme pivot chosen every time), T(n) = O(n^2).
   - "Good" Pivot: A pivot is considered "good" if its rank falls in the central 
     interval [n/4, 3n/4]. The probability of selecting a good pivot is 1/2.
   - Impact: Choosing a good pivot reduces the maximum subproblem size to at most 3n/4.
   - Probabilistic Analysis: The probability of NOT choosing a good pivot in k steps 
     is (1/2)^k, which decays exponentially.
   - High Probability Bound (w.h.p.): We state that Randomized Quicksort has a time 
     complexity of O(n log n) with a probability of at least 1 - n^(-α). The recursion 
     tree depth is strictly bounded to O(log n) because the majority of partitions 
     will be "good enough" within a small, limited number of trials.

E) Key Takeaways:
   - Vulnerability: Classic deterministic Quicksort degrades to O(n^2) on sorted or 
     reverse-sorted data. Randomization completely eliminates the correlation between 
     the input data's initial order and the algorithm's performance.
   - Practicality: The "High Probability" bound (1 - n^(-α)) mathematically guarantees 
     that in practical scenarios, the O(n^2) worst-case will virtually never occur.
   - Optimization (Median-of-3): Choosing the median of 3 random elements increases 
     the probability of a "good" pivot from 1/2 to 11/16, successfully decreasing the 
     hidden constant factor in the O(n log n) complexity.
'''