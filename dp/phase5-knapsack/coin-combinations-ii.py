
# Unoptimized approach
def coin_comb(n, x, coins):
    MOD = 10**9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], x + 1):
            dp[j] = (dp[j] + dp[j - coins[i]]) % MOD
    return dp[x] % MOD


import sys
import array


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

    # 3. Using array.array('I', ...) is more memory-efficient 
    # and faster for PyPy's JIT than a standard list.
    dp = array.array('I', [0] * (x + 1))
    dp[0] = 1
    
    # 4. The Hot Loop
    # We use a local reference to dp to speed up lookups
    # and hardcode the MOD to avoid variable lookup overhead.
    for coin in coins:
        for i in range(coin, x + 1):
            # Using the % operator with a literal is often 
            # highly optimized by PyPy.
            dp[i] = (dp[i] + dp[i - coin]) % 1000000007
                
    sys.stdout.write(str(dp[x]) + '\n')

if __name__ == "__main__":
    solve()