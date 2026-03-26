
def countWays(n, k):
    
    # base cases
    if n == 1:
        return k
    if n == 2:
        return k * k
    
    dp = [0] * (n + 1)
    
    # Fill value for 1 and 2 fences
    dp[1] = k
    dp[2] = k * k
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] * (k - 1) + dp[i - 2] * (k - 1)
    
    return dp[n]

n = 6
k = 8
print(countWays(n, k))