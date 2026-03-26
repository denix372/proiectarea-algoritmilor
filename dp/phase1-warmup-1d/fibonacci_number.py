class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return n
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
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b

n = 13
print(Solution().fib(n))
print(fib2(n))