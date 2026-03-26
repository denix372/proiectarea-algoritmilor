def maximizeCuts(n, x, y, z):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):

        if i >= x and dp[i - x] != -1:
            dp[i] = max(dp[i], dp[i - x] + 1)

        if i >= y and dp[i - y] != -1:
            dp[i] = max(dp[i], dp[i - y] + 1)

        if i >= z and dp[i - z] != -1:
            dp[i] = max(dp[i], dp[i - z] + 1)

        if dp[i] == 0:
            dp[i] = -1

    if dp[n] == -1:
        return 0
    return dp[n]

if __name__ == "__main__":

    n = 11
    x = 2
    y = 3
    z = 5

    print(maximizeCuts(n, x, y, z))