
def solve(adj):
    n = len(adj)
    for i in range(n):
        adj[i][i] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj[i][k] != 0 and adj[k][j] != 0:
                    adj[i][j] = 1
    return adj


adj = [[1, 1, 0, 1],
       [0, 1, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]
res = solve(adj)
for r in res:
    print(*r)