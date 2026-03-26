def knapsack(W, p, w):
    n = len(p)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if j - w[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], 
                            dp[i - 1][j - w[i - 1]] + p[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
                
    return dp[n][W]


p = [1, 2, 3]
w = [4, 5, 1]
W = 4

print(knapsack(W, p, w))