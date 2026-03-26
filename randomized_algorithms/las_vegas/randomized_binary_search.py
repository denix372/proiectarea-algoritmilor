import random
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = random.randint(left, right)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))

'''
TIME COMPLEXITY ANALYSIS (Randomized Binary Search - Las Vegas Algorithm)

A) Algorithm Idea:
   Instead of always picking the exact median element (left + right) // 2, 
   we pick a random pivot index within the current search space [left, right].

B) Classification: Las Vegas Algorithm.
   It always finds the correct index (or -1 if not found), but its execution 
   time depends on the random choices made during execution.

C) Mathematical Complexity Proof (Expected O(log N)):
   Let T(n) be the expected time required to search an array of size n.
   When we pick a random pivot, the probability of choosing any specific pivot is 1/n.
   The expected time is the sum of times for all possible remaining subarray sizes 
   after the pivot is chosen, multiplied by their probability, plus O(1) for the pivot choice.

   T(n) = (1/n) * [T(1) + T(2) + ... + T(n-1)] + 1
   Multiply by n:
   n * T(n) = T(1) + T(2) + ... + T(n-1) + n          (Eq. 1)

   Substitute n with n-1:
   (n-1) * T(n-1) = T(1) + T(2) + ... + T(n-2) + n-1  (Eq. 2)

   Subtract Eq. 2 from Eq. 1:
   n * T(n) - (n-1) * T(n-1) = T(n-1) + 1
   n * T(n) = n * T(n-1) + 1
   T(n) = T(n-1) + 1/n

   Expanding this recurrence gives:
   T(n) = 1/n + 1/(n-1) + 1/(n-2) + ... + 1/2 + 1
   
   This is the n-th Harmonic number (H_n). 
   Mathematically, the Harmonic series H_n is bounded by O(log n).
   Therefore, Expected Time Complexity = O(log N).

D) Worst-Case Time Complexity: O(N)
   If we are extremely unlucky and always randomly pick the worst possible boundary 
   (e.g., the target is at the end, and we always pick the first element), the search 
   space shrinks by only 1 element per step. However, the probability of this happening 
   is exponentially small.
'''