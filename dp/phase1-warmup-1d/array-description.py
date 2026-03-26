MOD = 10**9 + 7

def countArray(arr, n, m):
    dp = [[0] * (m + 3) for _ in range(n)]
 
    if arr[0] == 0:
        for j in range(1, m + 1):
            dp[0][j] = 1
    else:
        dp[0][arr[0]] = 1
 
    for i in range(1, n):
        if arr[i] != 0:
            j = arr[i]
            dp[i][j] = (dp[i - 1][j - 1] +
                        dp[i - 1][j] +
                        dp[i - 1][j + 1]) % MOD
        else:
            for j in range(1, m + 1):
                dp[i][j] = (dp[i - 1][j - 1] +
                            dp[i - 1][j] +
                            dp[i - 1][j + 1]) % MOD
 
    return sum(dp[n - 1][1:m + 1]) % MOD
 
 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(countArray(arr,n, m))