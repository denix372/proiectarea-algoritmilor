# Python program to find number of ways to
# make stable towers of given height.

def possibleWays(n, m, k):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Base case for height 0
    for j in range(m + 1):
        dp[0][j] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            
            # Not using the jth tile at all
            dp[i][j] = dp[i][j - 1]
            
            for cnt in range(1, min(k, i) + 1):
                dp[i][j] += dp[i - cnt][j - 1]
    
    return dp[n][m]

if __name__ == "__main__":
    n, m, k = 3, 3, 2
    print(possibleWays(n, m, k))