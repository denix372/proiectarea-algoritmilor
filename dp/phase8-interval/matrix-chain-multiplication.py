def matrixMultiplication(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')

            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], 
                               dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j])
    return dp[0][n - 1]


arr = [2, 1, 3, 4]
print(matrixMultiplication(arr))