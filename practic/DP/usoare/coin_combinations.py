import sys
input = sys.stdin.readline
MOD = 10**9 + 7

n, x = map(int, input().split())
coins = list(map(int, input().split()))
dp = [0] * (x + 1)
dp[0] = 1
for i in range(1, x + 1):
    for j in range(n):
        if i - coins[j] >= 0:
            dp[i] = (dp[i] + dp[i - coins[j]]) % MOD
print(dp[x] % MOD)