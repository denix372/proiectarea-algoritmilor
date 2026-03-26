# Solve with Interval DP
def solve(n, arr, k):
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    # 1. Base case: 1 painter must paint the whole interval [i, j].
    # The time is just the sum of the boards from i to j.
    for i in range(n):
        for j in range(i, n):
            dp[i][j][1] = sum(arr[i : j + 1])

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            for p in range(2, k + 1):
                
                for m in range(i, j):
                    # We give the left part [i, m] to p-1 painters
                    left_time = dp[i][m][p - 1]
    
                    # We give the right part [m+1, j] to exactly 1 painter
                    # (which means it's just the sum of those boards)
                    right_time = dp[m + 1][j][1] 

                    dp[i][j][p] = min(dp[i][j][p], max(left_time, right_time))

    return dp[0][n - 1][k]

# Solve with Partition DP
def solve2(n, arr, k):
    # Optimization: You never need more painters than there are boards
    k = min(n, k)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    # dp[i][p] = min-max time to paint the first 'i' boards using 'p' painters
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

    for p in range(1, k + 1):
        dp[0][p] = 0

    # Base Case 2: If you only have 1 painter, they MUST paint all 'i' boards.
    for i in range(1, n + 1):
        dp[i][1] = prefix[i]

    for p in range(2, k + 1):           # Loop over number of painters
        for i in range(1, n + 1):       # Loop over number of boards

            # Try placing the last divider after board 'j'
            # 'j' represents the number of boards given to the first p-1 painters
            for j in range(i):
                # The time it takes the last painter to paint the rest
                last_painter_time = prefix[i] - prefix[j]

                # We want the minimum possible time across all valid splits
                dp[i][p] = min(dp[i][p],
                               max(dp[j][p - 1], last_painter_time))

    return dp[n][k]


arr = [5, 10, 30, 20, 15]
print(solve(len(arr), arr, 3))
print(solve2(len(arr), arr, 3))