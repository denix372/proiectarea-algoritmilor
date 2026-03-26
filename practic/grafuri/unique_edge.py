import sys
sys.setrecursionlimit(10**7)

def tarjan_bridges(n, adj):
    tin = [0]*n
    low = [0]*n
    timer = 0
    bridges = set()

    def dfs(u, p):
        nonlocal timer
        timer += 1
        tin[u] = low[u] = timer

        for v in adj[u]:
            if v == p:
                continue
            if tin[v] == 0:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.add((min(u,v), max(u,v)))
            else:
                low[u] = min(low[u], tin[v])

    for i in range(n):
        if tin[i] == 0:
            dfs(i, -1)

    return bridges


def find_path(A, B, adj):
    visited = [False]*len(adj)
    path = []

    def dfs(u):
        if u == B:
            return True
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                path.append((min(u,v), max(u,v)))
                if dfs(v):
                    return True
                path.pop()
        return False

    dfs(A)
    return path

def solve_one(n, edges, A, B):
    A -= 1
    B -= 1
    adj = [[] for _ in range(n)]
    for x, y in edges:
        x -= 1
        y -= 1
        adj[x].append(y)
        adj[y].append(x)

    bridges = tarjan_bridges(n, adj)
    path = find_path(A, B, adj)

    for e in path:
        if e in bridges:
            return 1
    return 0

F = int(sys.stdin.readline())
for _ in range(F):
    n, m = map(int, sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    print(solve_one(n, edges, A, B))
