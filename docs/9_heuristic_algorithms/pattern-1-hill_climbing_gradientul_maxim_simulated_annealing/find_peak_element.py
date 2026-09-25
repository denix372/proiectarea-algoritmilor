from typing import List
import random

class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Drop the "climber" at a completely random position in the array
        current = random.randint(0, n - 1)
        
        while True:
            # Treat out-of-bounds as negative infinity (base of the mountain)
            left_val = nums[current - 1] if current > 0 else float('-inf')
            right_val = nums[current + 1] if current < n - 1 else float('-inf')
            
            # 2. Local Maximum found! The climber has reached a peak.
            if nums[current] > left_val and nums[current] > right_val:
                return current
                
            # 3. HILL CLIMBING: Always step towards the strictly higher neighbor
            if right_val > nums[current]:
                current += 1
            else:
                current -= 1

nums =[1,2,3,1]
print(Solution().findPeakElement(nums))
'''
HEURISTIC SEARCH ANALYSIS & PROOF (1D Hill Climbing vs Gradient Ascent)

A) Core Concept (The Landscape):
   Imagine the array values as a physical mountain range. Since nums[-1] and 
   nums[n] are -infinity, any path that strictly goes UP must eventually 
   hit a peak. It is mathematically impossible to walk uphill forever in a 
   finite sequence bounded by -infinity.

B) Hill Climbing (The Euristic Approach):
   The climber drops at a random index. They look left and right. If a neighbor 
   is higher, they take one step in that direction. Because they never step 
   down, they are mathematically guaranteed to find a local maximum (a peak).
   However, this pure heuristic approach has a worst-case Time Complexity of O(N) 
   (e.g., dropping at index 0 in a strictly increasing array and walking to N-1).

C) Binary Search (The LeetCode O(log N) Requirement):
   The Binary Search solution is just Hill Climbing that takes massive jumps. 
   By checking nums[mid] < nums[mid+1], you calculate the derivative (the slope). 
   If the slope is positive, there MUST be a peak to the right. You discard the 
   entire left half. This reduces the search space by half each time, giving 
   the required O(log N) complexity.
'''