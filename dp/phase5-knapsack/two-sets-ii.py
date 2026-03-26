MOD = 10**9 + 7

def solve(n):
    target = n * (n + 1) // 2
    if target % 2 == 1:
        return 0
    target //= 2
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j - i >= 0:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - i]) % MOD
            else:
                dp[i][j] = dp[i - 1][j] % MOD
    return dp[n][target] * pow(2, MOD - 2, MOD) % MOD
n = int(input())
print(solve(n))