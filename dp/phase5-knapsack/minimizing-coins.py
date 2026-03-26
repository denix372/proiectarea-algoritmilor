def coinChange(n, coins, amount):
        n = len(coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(n):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        if dp[amount] != amount + 1:
            return dp[amount]
        return -1

n, amount = map(int, input().split())
coins = list(map(int, input().split()))
print(coinChange(n, coins, amount))