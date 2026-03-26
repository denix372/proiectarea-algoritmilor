# Interval DP solution in O(n * k ^ 2)
def solve(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base Case 1: If we have 1 egg, we have to check every floor one by one
    for f in range(1, k + 1):
        dp[1][f] = f

    # Base Case 2: If we have 1 floor, it takes 1 move. 0 floors takes 0 moves.
    for e in range(1, n + 1):
        dp[e][1] = 1
        dp[e][0] = 0
        
    # Fill the table
    for e in range(2, n + 1):
        for f in range(2, k + 1):
            dp[e][f] = float('inf')
            
            # Try dropping from every floor x from 1 to f
            for x in range(1, f + 1):
                worst_case = 1 + max(dp[e - 1][x - 1], dp[e][f - x])
                dp[e][f] = min(dp[e][f], worst_case)

    return dp[n][k]

# More Optimized solution O(n * k)
def eggDrop(n, k):
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    
    cnt = 0
    
    while dp[cnt][n] < k:
        cnt += 1

        for i in range(1, n + 1):
            dp[cnt][i] = 1 + dp[cnt - 1][i - 1] + dp[cnt - 1][i]
    return cnt

n = 2
k = 36
print(solve(n, k))
print(eggDrop(n, k))