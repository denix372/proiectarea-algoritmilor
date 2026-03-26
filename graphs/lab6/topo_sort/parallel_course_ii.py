from typing import List
from itertools import combinations
from typing import List

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # Convert courses to 0-indexed and store prerequisites as bitmasks
        prereq = [0] * n
        for prev, nxt in relations:
            prereq[nxt - 1] |= (1 << (prev - 1))
            
        # dp[mask] = min semesters to complete the courses represented by mask
        # Initialize all states to infinity, except state 0 (0 courses taken = 0 semesters)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        
        # Iterate through every possible combination of completed courses
        for mask in range(1 << n):
            # Skip states we haven't reached yet
            if dp[mask] == float('inf'):
                continue
                
            # Find all available courses we can take NEXT.
            # A course is available if we HAVEN'T taken it yet, AND we HAVE taken all its prereqs.
            available = []
            for i in range(n):
                if (mask & (1 << i)) == 0 and (mask & prereq[i]) == prereq[i]:
                    available.append(i)
            
            # If the number of available courses is <= k, we just take all of them.
            if len(available) <= k:
                nxt_mask = mask
                for i in available:
                    nxt_mask |= (1 << i)
                dp[nxt_mask] = min(dp[nxt_mask], dp[mask] + 1)
                
            # If there are more than k available courses, we have to try every combination of size k
            else:
                for combo in combinations(available, k):
                    nxt_mask = mask
                    for i in combo:
                        nxt_mask |= (1 << i)
                    dp[nxt_mask] = min(dp[nxt_mask], dp[mask] + 1)
                    
        # Return the min semesters required to reach the state where all 'n' bits are 1
        return dp[(1 << n) - 1]

n = 4
relations = [[2,1],[3,1],[1,4]]
k = 2
print(Solution().minNumberOfSemesters(n, relations, k))