from typing import List
from collections import defaultdict

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(vals[v])
            adj[v].append(vals[u])

        best = float('-inf')

        for u in range(len(vals)):
            
            adj[u].sort(reverse=True)
            current_sum = vals[u]
            
            for j in range(min(k, len(adj[u]))):
                if adj[u][j] > 0:
                    current_sum += adj[u][j]
                else:
                    # Because the list is sorted, once we hit a negative 
                    # number, we know the rest are negative too.
                    break 

            best = max(best, current_sum)

        return best

vals = [1,2,3,4,10,-10,-20]
edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
k = 2
print(Solution().maxStarSum(vals, edges, k))