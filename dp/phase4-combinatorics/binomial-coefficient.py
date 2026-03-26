# C(n, k) = C(n -1, k - 1) + C(n - 1, k)

def binomial_coef(n, k):
    # C(n, k) = C(n -1, k - 1) + C(n - 1, k)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]

n = 4
k = 2
print(binomial_coef(n, k))