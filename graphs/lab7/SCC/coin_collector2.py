from collections import deque
import sys
sys.setrecursionlimit(10**7)
def coin_collector(n, coins, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
    
    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    timer = 1
    sccs = [0] * (n + 1)
    stack = []
    on_stack = [False] * (n + 1)
    scc_cnt = 0
    def dfs(u):
        nonlocal timer, scc_cnt
        disc[u] = low[u] = timer
        timer += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if disc[v] == 0:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])

        if disc[u] == low[u]:
            scc_cnt += 1
            while True:
                x = stack.pop()
                on_stack[x] = False
                sccs[x] = scc_cnt
                if x == u:
                    break
    
    for i in range(1, n + 1):
        if disc[i] == 0:
            dfs(i)
    
    scc_sum = [0] * (scc_cnt + 1)
    for i in range(1, n + 1):
        scc_sum[sccs[i]] += coins[i]
    
    dag = [[] for _ in range(scc_cnt + 1)]
    indeg = [0] * (scc_cnt + 1)

    for u in range(1, n + 1):
        for v in adj[u]:
            if sccs[u] != sccs[v]:
                dag[sccs[u]].append(sccs[v])
                indeg[sccs[v]] += 1
    dp = scc_sum.copy()
    q = deque()
    for i in range(1, scc_cnt + 1):
        if indeg[i] == 0:
            q.append(i)
    
    while q:
        u = q.popleft()
        for v in dag[u]:
            dp[v] = max(dp[v], dp[u] + scc_sum[v])
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return max(dp)


n, m = map(int, input().split())
coins = [0] + list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(coin_collector(n, coins, edges))