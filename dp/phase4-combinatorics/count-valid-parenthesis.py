# Approach 1 using DP
def count(n):
    # Example
    #            open →
    #close ↓   0   1   2   3   4
    #        +------------------------
    #0       |  1   1   1   1   1
    #1       |      1   2   3   4
    #2       |          2   5   9
    #3       |              5  14
    #4       |                 14
    if n % 2 == 1:
        return 0
    pairs = n // 2
    dp = [[0] * (pairs + 1) for _ in range(pairs + 1)]

    dp[0][0] = 1

    for i in range(pairs + 1):
        for j in range(pairs + 1):

            if j <= i:  # singura condiție necesară

                if i > 0:
                    dp[i][j] += dp[i-1][j]

                if j > 0:
                    dp[i][j] += dp[i][j-1]

    return dp[pairs][pairs]

# Approach 2, using Catalan Numbers


# function to find of Binomial Coefficient C(n, k)
def binomialCoeff(n, k):
    res = 1

    # Since C(n, k) = C(n, n-k)
    if k > n - k:
        k = n - k

    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res

# A Binomial coefficient based function to
# find nth catalan number in O(n) time
def catalan(n):

    # Calculate value of 2nCn
    c = binomialCoeff(2 * n, n)

    # return 2nCn/(n+1)
    return c // (n + 1)

# Function to find possible ways
def findWays(n):
    if n % 2 != 0:
        return 0
    return catalan(n // 2)
    
print(count(9))
print(findWays(9))
