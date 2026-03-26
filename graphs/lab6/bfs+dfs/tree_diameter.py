from typing import List
from collections import defaultdict
from collections import deque

INF = 10**9

from collections import deque
INF = 10**9
def tree_diameter(edges: list[list[int]]) -> int:
    if not edges:
        return 0
    n = max((max(u, v) for u, v in edges)) + 1

    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def bfs(start):
        q = deque([start])
        dist = [INF] * n
        dist[start] = 0
        best = 0
        i = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == INF:
                    dist[v] = dist[u] + 1
                    if best < dist[v]:
                        best = dist[v]
                        i = v
                    q.append(v)
        return (i, best)
    u, _ = bfs(0)
    _, best = bfs(u)
    return best

edges = [[0,1], [1,2], [1,3], [3,4]]
print(tree_diameter(edges))