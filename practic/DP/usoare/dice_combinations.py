MOD = 10**9 + 7
def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for k in range(1, 7):
            if i - k >= 0:
                dp[i] += dp[i - k] % MOD
    return dp[n] % MOD

n = int(input())
print(solve(n))