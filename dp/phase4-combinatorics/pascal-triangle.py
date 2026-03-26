def pascal(n):
    n -= 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    for i in range(n + 1):
        for j in range(i + 1):
            print(dp[i][j], end=" ")
        print()

    return dp[n][n]


# Without dp
# Python program for Pascal’s Triangle
# in O(n^2) time and O(1) extra space

# function for Pascal's Triangle
def pascal2(n):
    for row in range(1, n + 1):      
        # nC0 = 1
        c = 1
        for i in range(1, row + 1):

            # The first value in a row is always 1
            print(c, end=" ")
            c = c * (row - i) // i
        print()

n = 5
pascal(5)
pascal(5)