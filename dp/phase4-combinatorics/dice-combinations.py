MOD = 10**9 + 7

def dice_combinations(n):
    
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % MOD # dp[i -1] + dp[i -2] + ...dp[i -6]
    return dp[n] % MOD

n = int(input())
print(dice_combinations(n))
