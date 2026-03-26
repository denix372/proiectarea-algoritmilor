import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def coin_collector(n, m, coins, edges):
    g = [[] for _ in range(n + 1)]
    for a, b in edges:
        g[a].append(b)

    # tarjan SCC to find sccs
    index = 1
    stack = []
    onstack = [False] * (n + 1)
    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    comp = [0] * (n + 1)
    scc_count = 0

    def dfs(u):
        nonlocal index, scc_count
        disc[u] = low[u] = index
        index += 1
        stack.append(u)
        onstack[u] = True

        for v in g[u]:
            if disc[v] == 0:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif onstack[v]:
                low[u] = min(low[u], disc[v])

        if disc[u] == low[u]:
            scc_count += 1
            while True:
                x = stack.pop()
                onstack[x] = False
                comp[x] = scc_count
                if x == u:
                    break

    for i in range(1, n + 1):
        if disc[i] == 0:
            dfs(i)

    # compressing SCCs intro one node resulting into a DAG
    scc_sum = [0] * (scc_count + 1)
    for i in range(1, n + 1):
        scc_sum[comp[i]] += coins[i]

    dag = [[] for _ in range(scc_count + 1)]
    indeg = [0] * (scc_count + 1)

    for u in range(1, n + 1):
        for v in g[u]:
            if comp[u] != comp[v]:
                dag[comp[u]].append(comp[v])
                indeg[comp[v]] += 1

    # having now a dag, find the longest weighted path in dag
    from collections import deque
    dp = scc_sum[:]

    q = deque()
    for i in range(1, scc_count + 1):
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

print(coin_collector(n, m, coins, edges))
