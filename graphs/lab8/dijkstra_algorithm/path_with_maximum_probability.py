from typing import List
from heapq import heappush, heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        for (a, b), w in zip(edges, succProb):
            adj[a].append((b, w))
            adj[b].append((a, w))
        
        dist = [0.0] * n
        dist[start_node] = 1.0
        q = []
        heappush(q, (-1.0, start_node))

        while q:
            d, u = heappop(q)
            if -d < dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] * w > dist[v]:
                    dist[v] = dist[u] * w
                    heappush(q, (-dist[v], v))
        return dist[end_node]
        
sol = Solution()
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
print(sol.maxProbability(n, edges, succProb, start, end))