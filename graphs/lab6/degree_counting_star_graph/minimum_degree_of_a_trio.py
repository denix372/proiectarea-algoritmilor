from typing import List
from collections import defaultdict
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        degree = [0] * (n + 1)
        
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            degree[u] += 1
            degree[v] += 1

        min_deg = float('inf')
  
        for u, v in edges:
            # A node 'w' forms a trio with 'u' and 'v' if it is a neighbor to BOTH.
            # We can find this by intersecting the neighbor sets of 'u' and 'v'.
            common_neighbors = adj[u].intersection(adj[v])
            
            for w in common_neighbors:
                # Calculate the degree using the formula
                trio_degree = degree[u] + degree[v] + degree[w] - 6
                min_deg = min(min_deg, trio_degree)

        return min_deg if min_deg != float('inf') else -1

n = 6
edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
print(Solution().minTrioDegree(n, edges))