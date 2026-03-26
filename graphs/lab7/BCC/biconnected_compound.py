
def biconnectedComponents(n, adj):
    disc = [-1] * n
    low = [-1] * n
    timer = 0
    stack = []
    bccs = []
    
    def dfs(u, p):
        nonlocal timer
        disc[u] = low[u] = timer
        timer += 1

        for v in adj[u]:
            if v == p:
                continue
        
            if disc[v] == -1: #tree-edge
                stack.append((u, v))
                dfs(v, u)
                low[u] = min(low[u], low[v])

                if low[v] >= disc[u]: #BCC
                    bcc = []
                    while stack and stack[-1] != (u, v):
                        bcc.append(stack.pop())
                    bcc.append(stack.pop())
                    bccs.append(bcc)
            elif disc[v] < disc[u]: # back-edge
                stack.append((u, v))
                low[u] = min(low[u], disc[v])
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
            if stack:
                bccs.append(stack.copy())
                stack.clear()
    return bccs

n = 5
adj = [
    [1,3],     # 0
    [0,2,3,4], # 1
    [1,4],     # 2
    [1,0],     # 3
    [1,2]      # 4
]
bcc = biconnectedComponents(n, adj)
print(bcc)