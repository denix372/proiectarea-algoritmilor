from typing import List
INF = 10**6
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[INF] * n for _ in range(n)]
        for a, b, w in edges:
            dist[a][b] = w
            dist[b][a] = w
        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j],
                                        dist[i][k] + dist[k][j])

        cities = INF
        opt = -1
        for i in range(n):
            c = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    c += 1
            if c <= cities:
                cities = c
                opt = i
        return opt
            
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(Solution().findTheCity(n, edges, distanceThreshold))