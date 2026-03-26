# Interval DP in O(n ^ 3)
def solve(n, arr, k):
    dp = [[float('inf')] * n for _ in range(n)]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Option 1: Can we fit this entire interval [i, j] on ONE line?
            # Total length = sum of characters + the spaces between them
            total_len = sum(arr[i:j+1]) + (j - i) 
            
            if total_len <= k:
                if j == n - 1:
                    dp[i][j] = 0 # Last line rule
                else:
                    dp[i][j] = (k - total_len) ** 2
                    
            # Option 2: Split the text block at some point 'm'
            # We add the cost of two perfectly wrapped smaller blocks together.
            for m in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
                
    return dp[0][n - 1]

# Partition DP in O(N ^ 2) time
def solve2(n, arr, k):
    # cost[i][j] = the cost to put words from i to j on a SINGLE line.
    cost = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        current_len = -1 # -1 offsets the first word not needing a leading space
        for j in range(i, n):
            current_len += arr[j] + 1
            if current_len > k:
                break # Too long to fit on one line
                
            if j == n - 1:
                cost[i][j] = 0 # Last line rule
            else:
                cost[i][j] = (k - current_len) ** 2

    # 2. The 1D Partition DP (Using the 2D Cost Matrix)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for j in range(i):
            # dp[i] looks at every possible previous cut 'j'.
            # We take the cost of the first 'j' words, plus the 2D cost 
            # of putting words [j to i-1] on a single line.
            dp[i] = min(dp[i], dp[j] + cost[j][i - 1])

    return dp[n]

arr = [3, 2, 2, 5]
k = 6
print(solve(len(arr), arr, k))
print(solve2(len(arr), arr, k))