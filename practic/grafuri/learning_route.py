
def dfs(u, local):
    local[u] = 1
    visited[u] = True
    for v in adj[u]:
        if local[v] == 0:
            dfs(v, local)

n = int(input())
adj = [[] for _ in range(n)]
v = list(map(int, input().split()))
for i in range(n):
    adj[i].append(v[i] - 1)

visited = [False] * n

res = 0
for i in range(n):
    if not visited[i]:
        local = [0] * n
        dfs(i, local)
        sol = sum(local)
        res= max(res, sol)
print(res)