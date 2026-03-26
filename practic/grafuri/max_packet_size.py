INF = 10**9
def dfs(u, p):
    if adj[u] == []:
        return (u, p)
    for v, c in adj[u]:
        return dfs(v, min(p, c))

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
indeg = [0] * n
outdeg = [0] * n
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    indeg[b] += 1
    outdeg[a] += 1
    adj[a].append((b, c))

paths = []
cnt = 0
for i in range(n):
    if indeg[i] == 0:
        dst, p = dfs(i, INF)
        if p >= INF:
            paths.append((i + 1, dst + 1, 0))
        else:
            paths.append((i + 1, dst + 1, p))
    
print(len(paths))
for p in paths:
    print(*p)

