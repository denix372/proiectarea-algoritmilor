from typing import List
from heapq import heappop, heappush

INF = 10**6
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))
        
        dist = [[INF] * (maxTime + 1) for _ in range(n)]
        dist[0][0] = passingFees[0]
        q =[]
        heappush(q, (passingFees[0], 0, 0))
        while q:
            cost, time, u = heappop(q) 
            if cost > dist[u][time]:
                continue

            if u == n - 1:
                return cost

            for v, t in adj[u]:
                
                if time + t <= maxTime:
                    if cost + passingFees[v] < dist[v][time + t]:
                        dist[v][time + t] = cost + passingFees[v]
                        heappush(q, (dist[v][time + t],time + t, v))
        
        return -1
        
maxTime = 30
edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]]
passingFees = [5,1,2,20,20,3]
print(Solution().minCost(maxTime, edges, passingFees))
