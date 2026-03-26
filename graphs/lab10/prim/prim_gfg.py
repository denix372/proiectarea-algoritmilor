from heapq import heappush, heappop
class Solution:
    def spanningTree(self, n, edges):
        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))

        visited = [False] * n
        visited[0] = True
        q = []
        cnt = 0
        cost = 0
        for v, w in adj[0]:
            heappush(q, (w, v))

        while q and cnt < n - 1:
            c, u = heappop(q)
            if visited[u]:
                continue
            visited[u] = True
            cnt += 1
            cost += c
            for v, w in adj[u]:
                if not visited[v]:
                    heappush(q, (w, v))
        return cost

n = 3
E = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print(Solution().spanningTree(n, Edges))