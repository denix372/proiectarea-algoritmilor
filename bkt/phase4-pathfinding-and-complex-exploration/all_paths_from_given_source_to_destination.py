
from collections import deque

def solve(n, edges, src, dst):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)

    res = []
    visited = [False] * n

    def back(u, sol):
        if u == dst:
            res.append(sol.copy())
            return

        visited[u] = True

        for v in adj[u]:
            if not visited[v]:
                back(v, sol + [v])

        visited[u] = False

    back(src, [src])
    return res

V = 4
edges = [[0, 3], [0, 1], [1, 3], [2, 1], [2, 0]]
src = 2
dest = 3
print(solve(V, edges, src, dest))
