def knapsack(W, p, w):
    n = len(p)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if j - w[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], 
                            dp[i - 1][j - w[i - 1]] + p[i - 1])
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][W]

def knapsack_reconstruction(W, p, w):
    n = len(p)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if j - w[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], 
                            dp[i - 1][j - w[i - 1]] + p[i - 1])
            else:
                dp[i][j] = dp[i-1][j]

    solution = []
    i, j = n, W

    while i > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            solution.append(i - 1)
            j -= w[i - 1]
            i -= 1

    solution.reverse()
    return solution


p = [1, 2, 3]
w = [4, 5, 1]
W = 4
    
print(knapsack(W, p, w))