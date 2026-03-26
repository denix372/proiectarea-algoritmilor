from typing import List
INF = 10**6

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [INF] * n
        dist[src] = 0
        
        # because the problem limit with exactly k stops
        # we must to have a temporary array with the exactly k iterations
        for _ in range(k + 1):
            new_dist = dist.copy()
            for u, v, w in flights:
                if dist[u] != INF and dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist
    
        if dist[dst] == INF:
            return -1
        return dist[dst]

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))