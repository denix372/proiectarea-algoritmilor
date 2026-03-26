import sys
sys.setrecursionlimit(10**6)

def solve(n, adj):
    visited = [False] * (n + 1)
    reps = []

    def dfs(u):
        visited[u] = 1
        for v in adj[u]:
            if not visited[v]:
                dfs(v)    

    for u in range(1, n + 1):
        if visited[u] == 0:
            reps.append(u)
            dfs(u)

    print(len(reps) - 1)
    for i in range(1, len(reps)):
        print(reps[i - 1], reps[i])

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

solve(n, adj)

