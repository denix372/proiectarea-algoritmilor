def palindromePartition(s):
    n = len(s)
    pal = [[False] * n for _ in range(n)]

    for i in range(n):
        pal[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or pal[i + 1][j - 1]):
                pal[i][j] = True     

    dp = [n] * n
    dp[0] = 0

    for i in range(1, n):
        if pal[0][i]:
            dp[i] = 0
        else:
            for j in range(i + 1):
                if pal[j][i]:
                    dp[i] = min(dp[i], 1 + dp[j - 1])
    return dp[n - 1]

s = "anacaere"
print(palindromePartition(s))