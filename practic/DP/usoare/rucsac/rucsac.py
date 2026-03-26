

def solve(n, g, w, p):
    dp = [[0] * (g + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, g + 1):
            if j - w[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + p[i - 1])
    return dp[n][g]

with open("rucsac.in", "r") as fin:
    n, g = map(int, fin.readline().split())
    w = [0] * n 
    p = [0] * n
    for i in range(n):
        w[i], p[i] = map(int, fin.readline().split())

with open("rucsac.out", "w") as fout:
    fout.write(str(solve(n, g, w, p)))
