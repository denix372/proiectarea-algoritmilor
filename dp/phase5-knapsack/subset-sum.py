def isSubsetSum(arr, sum):
    n = len(arr)

    dp = [[False] * (sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][sum]

def isSubsetSum_optimized(arr, sum):
    dp = [False] * (sum + 1)
    dp[0] = True

    for num in arr:
        for j in range(sum, num - 1, -1):
            if j - num >= 0:
                dp[j] = dp[j] or dp[j - num]

    return dp[sum]

def isSubsetSum_reconstruction(arr, sum):
    n = len(arr)
    dp = [[False] * (sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    res = []
    i, j = n, sum

    while i > 0 and j > 0:
        if dp[i - 1][j]:
            i -= 1
        else:
            res.append(arr[i - 1])
            j -= arr[i - 1]
            i -= 1

    return res[::-1]

arr = [3, 34, 4, 12, 5, 2]
sum = 9
print(isSubsetSum(arr, sum))
print(isSubsetSum_optimized(arr, sum))
print(isSubsetSum_reconstruction(arr, sum))