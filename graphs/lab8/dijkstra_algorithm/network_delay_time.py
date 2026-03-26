from typing import List
import heapq
INF = 10**9
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj =[[] for _ in range(n + 1)]
        for a, b, w in times:
            adj[a].append((b, w))

        q =[]
        dist = [INF] * (n + 1)
        dist[k] = 0
        heapq.heappush(q, (0, k))

        while q:
            d, u = heapq.heappop(q)
            if d > dist[u]:
                continue
            
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w 
                    heapq.heappush(q, (dist[v], v))
        res = max(dist[1:])
        if res == INF:
            return -1
        return res

sol = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(sol.networkDelayTime(times, n, k))