from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0] * (n + 1)
        edge_count = defaultdict(int)
        
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            edge_count[(min(u, v), max(u, v))] += 1

        sorted_degrees = sorted(degree[1:])
        
        ans = []
        for q in queries:
            count = 0
            
            # Step 1: Fast Two-Pointer count assuming NO shared edges
            left = 0
            right = n - 1
            
            while left < right:
                if sorted_degrees[left] + sorted_degrees[right] > q:
                    # If left + right is greater than q, then right paired with 
                    # ANY node between left and right is also greater than q.
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
                    
            # Step 2: Correct the overcounts caused by shared edges
            for (u, v), shared in edge_count.items():
                total_deg = degree[u] + degree[v]
                
                # If they were counted by the two-pointer step (total_deg > q)
                # BUT subtracting their actual shared edges drops them below the threshold,
                # we need to remove them from our count.
                if total_deg > q and total_deg - shared <= q:
                    count -= 1
                    
            ans.append(count)
            
        return ans

n = 4
edges = [[1,2],[2,4],[1,3],[2,3],[2,1]]
queries = [2,3]
print(Solution().countPairs(n, edges, queries))