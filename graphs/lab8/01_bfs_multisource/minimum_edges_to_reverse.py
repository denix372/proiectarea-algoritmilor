
INF = 10**5 + 1
from collections import deque 

class Solution:
    def minimumEdgeReversal(self, edges, n, src, dst):
        # code here
        adj = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append((b, 0))
            adj[b].append((a, 1))

        dist = [INF] * (n + 1)
        dist[src] = 0
        q = deque([(src, 0)])

        while q:
            u, d = q.popleft()
            if d > dist[u]:
                continue

            for v, w in adj[u]:
                cost = d + w
                if cost < dist[v]:
                    dist[v] = cost
                    if w == 0:
                        q.appendleft((v, dist[v]))
                    else:
                        q.append((v, dist[v]))

        if dist[dst] == INF:
            return -1
        return dist[dst]

n = 3
edges = [[1, 2], [3, 2]]
src = 1
dst = 3
print(Solution().minimumEdgeReversal(edges, n, src, dst))