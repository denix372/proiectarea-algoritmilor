
def number_of_cc(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    visited = set()
    def dfs(u):
        if u in visited:
            return 0
        visited.add(u)
        for v in adj[u]:
            dfs(v)
        return 1

    s = 0
    for u in range(n):
        s += dfs(u)
    return s


def ccs(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    visited = set()

    def dfs(u, sol):
        visited.add(u)
        sol.append(u)
        for v in adj[u]:
            if v not in visited:
                dfs(v, sol)

    res =[]
    for u in range(n):
        if u not in visited:
            sol = []
            dfs(u, sol)
            res.append(sol)
    return res

n = 5 
edges = [[0,1], [2,3]]
print(number_of_cc(n, edges))
print(ccs(n, edges))