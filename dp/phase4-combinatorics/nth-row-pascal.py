def nth_row_pascal(n):
    n -= 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n]

def nth_row_pascal(n):
    row = [0] * n
    row[0] = 1

    for i in range(1, n):
        for j in range(i, 0, -1):
            row[j] += row[j - 1]

    return row


n = 5
print(nth_row_pascal(n))
