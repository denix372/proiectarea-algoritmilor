import random
from collections import defaultdict

class RandomMaxIndex:
    def find_random_index(self, arr: list[int]) -> int:
        if not arr:
            return -1
            
        # 1. Map each element to a list of its exact indices
        # Space Complexity: O(N) because we store N indices overall
        indices_map = defaultdict(list)
        for i, num in enumerate(arr):
            indices_map[num].append(i)
            
        # 2. Find the element with the longest list of indices (max frequency)
        max_freq = 0
        max_element = None
        
        for num, indices in indices_map.items():
            if len(indices) > max_freq:
                max_freq = len(indices)
                max_element = num
                
        # 3. Uniformly pick one random index from the max element's list
        # random.choice automatically guarantees perfectly equal probability (1 / max_freq)
        return random.choice(indices_map[max_element])


# --- DRIVER CODE (EXAMPLE USAGE & EMPIRICAL PROOF) ---
finder = RandomMaxIndex()
arr = [-1, 4, 9, 7, 7, 2, 7, 3, 0, 9, 6, 5, 7, 8, 9]

print("--- Random Index of Maximum Occurring Element ---")
# 7 occurs 4 times at indices: 3, 4, 6, 12.
print(f"Random index of max element: {finder.find_random_index(arr)}")

# Let's prove it distributes evenly over 100,000 runs
iterations = 100000
results_count = defaultdict(int)

for _ in range(iterations):
    idx = finder.find_random_index(arr)
    results_count[idx] += 1

print("\nEmpirical Distribution over 100,000 runs:")
for idx, count in sorted(results_count.items()):
    print(f"Index {idx}: {count} times ({(count / iterations) * 100:.2f}%) - Expected: 25.00%")
print()

'''
PROBABILISTIC ANALYSIS & ALGORITHM PROOF

A) Core Mathematical Idea:
   Let 'E' be the element with the maximum frequency 'k' in an array of size 'N'.
   The element 'E' appears at exactly 'k' distinct indices: {i_1, i_2, ..., i_k}.
   The problem requires us to return any of these 'k' indices with perfectly 
   equal probability.

B) Probability of Selection:
   By mapping the element to a list of its indices, we isolate the exact 'k' 
   valid positions.
   Using a uniform random generator (like Python's random.choice), we select 
   one element from this list of size 'k'.
   Therefore, the probability of returning any valid index i_j is exactly:
   P(returning i_j) = 1 / k.
   
   This guarantees a perfectly uniform distribution, avoiding the severe flaw 
   in the original GeeksforGeeks implementation (which biased towards odd indices).

C) Handling Ties:
   If multiple elements share the exact same maximum frequency (e.g., both 7 and 9 
   appear 4 times), this implementation strictly selects the FIRST element that 
   achieved that frequency (due to the `>` operator). If a strictly global random 
   choice across ALL max elements was required, we would pool their index lists 
   before selecting.

D) Complexity:
   - Time Complexity: O(N) 
     We iterate through the array of size N exactly once to build the map, and 
     iterate through the unique elements (at most N) to find the max.
   - Space Complexity: O(N) 
     The hash map stores the distinct elements as keys and exactly N integers 
     (the indices) across all lists combined.
'''