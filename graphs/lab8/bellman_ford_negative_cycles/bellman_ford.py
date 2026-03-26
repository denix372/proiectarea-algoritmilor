#User function Template for python3
INF = 10**8
class Solution:
    def bellmanFord(self, n, edges, src):
        #code here
        dist = [INF] * n
        dist[src] = 0
        
        for i in range(n):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    if i == n - 1:
                        return [-1]
                    dist[v] = dist[u] + w
        return dist

V = 5
edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0
print(Solution().bellmanFord(V, edges, src))