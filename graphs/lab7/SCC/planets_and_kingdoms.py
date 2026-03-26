import sys
sys.setrecursionlimit(10**5)

def planet_and_kingdoms(n, adj):
    timer = 0
    disc = [-1] * n
    low = [-1] * n
    stack = []
    in_stack = [False] * n
    sccs = []

    def dfs(u):
        nonlocal timer
        timer += 1
        disc[u] = low[u] = timer
        stack.append(u)
        in_stack[u] = True

        for v in adj[u]:
            if disc[v] == -1: #tree-edge
                dfs(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]: #back_edge
                low[u] = min(low[u], disc[v])
        
        if low[u] == disc[u]: #scc root
            scc = []
            while True:
                x = stack.pop()
                in_stack[x] = False
                scc.append(x)
                if x == u:
                    break
            sccs.append(scc)
        
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
    kingdoms = [0] * n
    for i, scc in enumerate(sccs, start=1):
        for u in scc:
            kingdoms[u] = i
    return len(sccs), kingdoms

n, m = map(int, input().split())
graph =[[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)

k, res = planet_and_kingdoms(n, graph)
print(k)
print(*res)