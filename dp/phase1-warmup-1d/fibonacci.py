def fib(n):
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def fib2(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    c = 0
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b

print(fib(13))