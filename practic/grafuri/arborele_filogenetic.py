n = int(input())
visited = [False] * n
res = 0

adj = [[] for _ in range(n)]
roots = []
for i in range(n):
    x = int(input())
    if x != -1:
        adj[x - 1].append(i)
    else:
        roots.append(i)

def dfs(u, d):
    global res
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            res = max(res, d + 1)
            dfs(v, d + 1)

for u in roots:
    if not visited[u]:
        dfs(u, 0)

print(res + 1)