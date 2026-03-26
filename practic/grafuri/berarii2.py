def dfs(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

n, m, p = map(int, input().split())
visited = [False] * n
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[b - 1].append(a - 1)

for _ in range(p):
    b = int(input())
    dfs(b - 1)

bers = []
for i in range(n):
    if not visited[i]:
        bers.append(i)
print(len(bers))
for b in bers:
    print(b + 1)