def solve(n, g):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = max(g[i][j], g[i][k] * g[k][j])

    for i in range(n):
        for j in range(n):
            if g[i][j] == 0:
                print(f"{-1:.10f}", end = " ")
            else:
                print(f"{g[i][j]:.10f}", end = " ")
        print()


n, m = map(int, input().split())
g = [[0.0] * n for _ in range(n)]
for _ in range(m):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = float(c)
    g[a - 1][b - 1] = c

for i in range(n):
    g[i][i] = 1.0
solve(n, g)