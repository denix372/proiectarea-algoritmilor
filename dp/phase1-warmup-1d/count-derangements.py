def derangeCount(n):
  
    # Create a DP array to store results
    dp = [0] * (n + 1)

    # Base cases
    dp[1] = 0
    dp[2] = 1

    # Fill the DP array using the 
    # recursive relation
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
    
    return dp[n]

if __name__ == "__main__":
    n = 5
    print(derangeCount(n))