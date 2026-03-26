INF = 10**9
def solve(n, m):
    if n > m:
        n, m, = m, n
    dp = [[INF] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j:
                dp[i][j] = 0
            else:
                best = INF
                for k in range(1, i // 2 + 1):
                    best = min(best, 1 + dp[k][j] + dp[i - k][j])
                for k in range(1, j // 2 + 1):
                    best = min(best, 1 + dp[i][k] + dp[i][j - k])
                dp[i][j] = best
    print(dp[n][m])

n, m = map(int, input().split())
solve(n, m)