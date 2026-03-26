from collections import deque

def longest_path(n, edges):
    graph = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)

    for a, b in edges:
        graph[a].append(b)
        indeg[b] += 1

    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    dp = [-10**18] * (n + 1)
    parent = [-1] * (n + 1)
    dp[1] = 1

    for u in topo:
        if dp[u] < 0:
            continue
        for v in graph[u]:
            if  dp[v] < dp[u] + 1:
                dp[v] = dp[u] + 1
                parent[v] = u

    if dp[n] < 0:
        return None

    path = []
    i = n
    while i != -1:
        path.append(i)
        i = parent[i]

    path.reverse()
    return path

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b))

path = longest_path(n, edges)

if path is None:
    print("IMPOSSIBLE")
else:
    print(len(path))
    print(*path)
