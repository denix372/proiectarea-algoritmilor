MOD = 10**9 + 7
from collections import deque
def game_routes(n, adj, indeg):
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    #DP????
    dp = [0] * (n + 1)
    dp[1] = 1
    for u in order:
        for v in adj[u]:
            dp[v] = (dp[v] + dp[u]) % MOD
    return dp[n]

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indeg[b] += 1

print(game_routes(n, adj, indeg))
