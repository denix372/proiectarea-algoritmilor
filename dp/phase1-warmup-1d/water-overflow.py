# Python program to find amount  
# of water in a given glass Using Dynamic Programming

def waterOverflow(k, n, m):
    
    # DP matrix to simulate water flow in glasses
    dp = [[0.0 for _ in range(n)] for _ in range(n)]
    
    # Initial water in top glass
    dp[0][0] = k
    
    # Simulate water flow through triangle
    for i in range(n - 1):
        for j in range(i + 1):
            
            # Calculate water overflow
            excess = max(0.0, dp[i][j] - 1.0)
            
            # Distribute excess water
            if excess > 0:
                
                # Cap current glass
                dp[i][j] = 1.0
                
                # Flow to bottom glasses
                dp[i + 1][j] += excess / 2.0
                dp[i + 1][j + 1] += excess / 2.0
    
    # Return water in target glass
    return min(1.0, dp[n - 1][m - 1])


if __name__ == "__main__":
    k = 3
    r = 2
    c = 1
    
    waterAmount = waterOverflow(k, r, c)
    print(waterAmount)