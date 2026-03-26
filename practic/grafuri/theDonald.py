

def dfs(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visited = [False] * n
cnt = 0
for i in range(n):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt - 1)