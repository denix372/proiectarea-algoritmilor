from heapq import heappush, heappop
def prim(n, edges):
    adj = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a - 1].append((b - 1, w))
        adj[b - 1].append((a - 1, w))
    cost = 0
    visited = [False] * n
    q = []
    heappush(q, (0, 0)) # weight = 0, start=0

    while q:
        d, u = heappop(q)
        if visited[u]:
            continue
        visited[u] = True
        cost += d

        for v, w in adj[u]:
            if not visited[v]:
                heappush(q, (w, v))
    return cost

edges = [[1, 2, 1],
         [1, 3, 2],
         [1, 4, 3],
         [1, 5, 4],
         [2, 3, 5],
         [3, 5, 7],
         [3, 5, 6]]
n = 6
print(prim(n, edges))