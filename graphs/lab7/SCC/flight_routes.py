import sys
sys.setrecursionlimit(10**7)
def flight_routes(n, edges):
    adj =[[] for _ in range(n + 1)]
    rev =[[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        rev[b].append(a)
    
    def dfs(u, adj, visited):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v, adj, visited)
    visited1 = [False] * (n + 1)
    visited2 = [False] * (n + 1)

    dfs(1, adj, visited1)
    dfs(1, rev, visited2)

    for i in range(1, n + 1):
        if not visited1[i]:
            print("NO")
            print(1, i)
            exit()
    for i in range(1, n + 1):
         if not visited2[i]:
            print("NO")
            print(i, 1)
            exit()

    print("YES")

n , m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
flight_routes(n, edges)
