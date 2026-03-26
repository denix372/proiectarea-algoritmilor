from typing import List
from heapq import heappush, heappop
MOD = 10**9 + 7
INF = 10**18
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b, w in roads:
            adj[a].append((b, w))
            adj[b].append((a, w))
        
        dist = [INF] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        q = []
        heappush(q, (dist[0], 0))
        nr = 0
        while q:
            d, u = heappop(q)
            if d > dist[u]:
                continue

            for v, w in adj[u]:
                m = dist[u] + w
                if m < dist[v]:
                    dist[v] = m
                    ways[v] = ways[u]
                    heappush(q, (dist[v], v))
                elif dist[u] + w == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n - 1] % MOD

n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(Solution().countPaths(n, roads))