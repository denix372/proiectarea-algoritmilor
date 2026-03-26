def unbounded_knapsack(p, w, W):
    n = len(p)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if j - w[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j],
                                dp[i][j - w[i - 1]] + p[i - 1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][W]



val = [1, 1]
wt = [2, 1]
capacity = 3

print(unbounded_knapsack(val, wt, capacity))