from collections import deque

def solve(n, edges, src, dst):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)

    cnt = 0
    visited = [-1] * n

    def back(u):
        nonlocal cnt
        if u == dst:
            return 1
        if visited[u] != -1:
            return visited[u]

        total = 0
        for v in adj[u]:
            total += back(v)

        visited[u] = total
        return total

    return back(src)

def solve2(n, edges, src, dst):
    adj = [[] for _ in range(V)]
    indegree = [0] * V

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    q = deque()
    topo = []

    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    while q:
        u = q.popleft()
        topo.append(u)

        for v in adj[u]:
            indegree[v] -= 1

            if indegree[v] == 0:
                q.append(v)

    dp = [0] * V
    dp[dest] = 1

    for u in reversed(topo):
        for v in adj[u]:
            dp[u] += dp[v]

    return dp[src]


V = 5
edges = [[0, 1], [0, 2], [0, 4], [1, 3], [1, 4], [2, 4], [3, 2]]
src = 0
dest = 4
print(solve(V, edges, src, dest))
print(solve2(V, edges, src, dest))
