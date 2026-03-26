def solve(n, m, x, y):
    dp = [[0] * (m + 2) for _ in range(n + 2)]
    dp[0][0] = 0

    for j in range(1, m + 1):
        dp[n + 1][j] = x[j]
    for i in range(1, n + 1):
        dp[i][m + 1] = y[i]

    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])
    print(dp[1][1])

n, m = map(int, input().split())
x = [0] + list(map(int, input().split()))
y = [0] + list(map(int, input().split()))
solve(n, m, x, y)