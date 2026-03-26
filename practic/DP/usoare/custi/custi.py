def solve(n, a):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    ap = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1][j - 1] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j],
                               dp[i][j - 1],
                               dp[i - 1][j - 1]) + 1
            if dp[i][j] != 0:
                for k in range(1, dp[i][j] + 1):
                    ap[k] += 1

    with open("custi.out", "w") as fout:
        for i in range(1, n + 1):
            fout.write(str(ap[i]) + "\n")

with open("custi.in", "r") as fin:
    n = int(fin.readline())
    a = [[0] * n for _ in range(n)]
    a = [list(map(int, fin.readline().split())) for _ in range(n)]

solve(n, a)