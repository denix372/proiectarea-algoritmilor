
def solve(n, edges, k):
    adj = [[] for _ in range(n)]
    for a, b, w in edges:
        adj[a].append((b, w))
        adj[b].append((a, w))
    visited = [False] * n

    def back(u, total):
        if total >= k:
            return True

        visited[u] = True
        for v, w in adj[u]:
            if not visited[v]:
                if back(v, total + w):
                    return True
        visited[u] = False
        return False

    return back(0, 0)

V = 5

edges = [
    [0, 1, 4],
    [0, 2, 8],
    [1, 4, 6],
    [2, 3, 2],
    [4, 3, 10]
]
k = 8
print(solve(V, edges, k))