INF = 10**9 

# O(n^2 * m^2 solution) time
def solve(a):
    n = len(a)
    m = len(a[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = a[i - 1][j - 1] + (dp[i - 1][j] +
                                          dp[i][j - 1] 
                                          - dp[i - 1][j - 1])

    res = -INF
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(i, n + 1):
                for l in range(j, m + 1):
                    res = max(res, dp[k][l] - dp[i - 1][l] - dp[k][j - 1] + dp[i - 1][j - 1])
    return res

# Kadane 2D, O(n * m^2) time solution
def solve2(a):
    def kadane(arr):
        current_sum = arr[0]
        local_max = arr[0]
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            local_max = max(local_max, current_sum)
        return local_max

    n = len(a)
    m = len(a[0])
    max_sum = -INF

    # Fix the left and right columns
    for left in range(m):
        temp = [0] * n
        for right in range(left, m):
            # Accumulate row sums for the current column bounds
            for i in range(n):
                temp[i] += a[i][right]
            
            # Apply 1D Kadane's on the temp array using the internal function
            max_sum = max(max_sum, kadane(temp))

    return max_sum

mat = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6]
    ]
print(solve(mat))
print(solve2(mat))