MOD = 10**9 + 7

def grid_paths_i(n, matrix):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    if matrix[0][0] == '*':
        return 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if not (i == 1 and j == 1):
                if matrix[i - 1][j - 1] != '*':
                    dp[i][j] = dp[i - 1][j] % MOD + dp[i][j - 1] % MOD

    return dp[n][n] % MOD

n = int(input())
matrix = [['.'] * n for _ in range(n)]
for i in range(n):
    matrix[i] = input()
print(grid_paths_i(n, matrix))