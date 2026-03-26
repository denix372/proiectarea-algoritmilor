from typing import List
from heapq import heappush, heappop
INF = 10**9

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        dist1 = [INF] * (n + 1)
        dist2 = [INF] * (n + 1)
        dist1[1] = 0
        q = []
        heappush(q, (0, 1))

        while q:
            d, u = heappop(q)
            if d > dist2[u]:
                continue

            cycle = d // change
            if cycle % 2 == 0:
                # Green light: leave immediately
                leave_time = d
            else:
                # Red light: wait until the start of the next cycle
                leave_time = (cycle + 1) * change

            # The exact time we will arrive at any neighbor
            cost = leave_time + time
            
            for v in adj[u]:
                if cost < dist1[v]:
                    dist2[v] = dist1[v]
                    dist1[v] = cost
                    heappush(q, (dist1[v], v))
                    
                elif dist1[v] < cost < dist2[v]:
                    dist2[v] = cost
                    heappush(q, (dist2[v], v))
        
        return dist2[n]


n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5
print(Solution().secondMinimum(n, edges, time, change))