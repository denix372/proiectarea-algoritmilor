def tarjan_scc(n, adj):
    disc = [-1] * n
    low = [-1] * n
    in_stack = [False] * n
    stack = []

    timer = 0
    sccs = []

    def dfs(u):
        # 1) discover nodes
        nonlocal timer
        timer += 1
        disc[u] = low[u] = timer

        stack.append(u)
        in_stack[u] = True

        # 2) explore neighbors
        for v in adj[u]:
            if disc[v] == -1: # tree-edge
                dfs(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]: # back-edge
                low[u] = min(low[u], disc[v])

        # 3) if u is root of SCC
        if low[u] == disc[u]:
            comp = []
            while True:
                x = stack.pop()
                in_stack[x] = False
                comp.append(x)
                if x == u:
                    break
            sccs.append(comp)

    # run DFS from all the unexplored nodes
    for i in range(n):
        if disc[i] == -1:
            dfs(i)

    return sccs

adj = [
    [1],
    [2],
    [0, 3],
    [4],
    [3, 5],
    []
]
n = len(adj)
print(tarjan_scc(n, adj))
