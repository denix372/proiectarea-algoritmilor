
def matrixMultiplication_reconstruction(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    # 1. Create a table to store the optimal split point 'k'
    bracket = [[0] * n for _ in range(n)]

    # 2. Base case: Fill the expressions for single matrices
    for i in range(n - 1):
        bracket[i][i + 1] = chr(65 + i) # A, B, C, etc.

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')

            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                
                if cost < dp[i][j]:
                    dp[i][j] = cost
            
                    # 3. Concatenate the already-built smaller strings directly!
                    bracket[i][j] = f"({bracket[i][k]} * {bracket[k][j]})"
    
    return dp[0][n - 1], bracket[0][n - 1]

arr = [2, 1, 3, 4]
print(matrixMultiplication_reconstruction(arr)[1])