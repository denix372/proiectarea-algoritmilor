

def solve(n):
    dp = [0] * (n + 1)
    dp[0] = 2
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = 7
print(solve(n))