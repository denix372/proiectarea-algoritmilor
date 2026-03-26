
INF = 10**9

def solve(n, a):
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                m[i][j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g[i][j] > g[i][k] + g[k][j]:
                    g[i][j] = g[i][k] + g[k][j]
                    m[i][j] = max(m[i][j], m[i][k] + m[k][j])
                elif g[i][j] == g[i][k] + g[k][j]:
                    m[i][j] = max(m[i][j], m[i][k] + m[k][j])

    for r in g:
        print(*r)
    for r in m:
        print(*r)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
solve (n, g)