# post-order, find finish-time
def dfs1(u, adj, visited, stack):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs1(v, adj, visited, stack)
    stack.append(u)

def dfs2(u, revadj, visited, scc):
    visited[u] = True
    scc.append(u)
    for v in revadj[u]:
        if not visited[v]:
            dfs2(v, revadj, visited, scc)
    
def kosaraju(n, adj):
    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            dfs1(i, adj, visited, stack)

    revAdj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            revAdj[v].append(u)
    
    visited = [False] * n
    sccs = []

    while stack:
        u = stack.pop()
        if not visited[u]:
            scc = []
            dfs2(u, revAdj, visited, scc)
            sccs.append(scc)
    return sccs

n = 5
edges = [ [1, 3], [1, 4], [2, 1], [3, 2], [4, 5] ]
adj =[[] for _ in range(n + 1)]
for u, v in edges:
    adj[u].append(v)

sccs = kosaraju(n + 1, adj)
print("Strongly Connected Components:")
print(*sccs[:len(sccs) - 1])