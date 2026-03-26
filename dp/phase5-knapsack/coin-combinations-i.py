import sys

# Unoptimized approach
def coin_comb(n, x, coins):
    MOD = 10**9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1
    for i in range(1, x + 1):
        for j in range(n):
            dp[i] = (dp[i] + dp[i - coins[j]]) % MOD
    return dp[x] % MOD

# Same solution but speed optimized to pass al the tests on cses
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    x = int(data[1])
    coins = sorted([int(c) for c in data[2:] if int(c) <= x])
    
    if not coins:
        print(0)
        return

    dp = [0] * (x + 1)
    dp[0] = 1
    
    MOD = 1000000007
    max_coin = coins[-1]
    coin_tuple = tuple(coins)
    
    limit = min(x + 1, max_coin)
    for i in range(coins[0], limit):
        s = 0
        for c in coin_tuple:
            if c <= i:
                s += dp[i - c]
            else:
                break
        dp[i] = s % MOD
        
    for i in range(limit, x + 1):
        s = 0
        for c in coin_tuple:
            s += dp[i - c]
        dp[i] = s % MOD
                
    sys.stdout.write(str(dp[x]) + '\n')

if __name__ == "__main__":
    solve()