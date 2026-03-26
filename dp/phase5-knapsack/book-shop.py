import sys
input = sys.stdin.readline

def book_shop(n, x, h, s):
    dp = [0] * (x + 1)
    for i in range(n):
        hi = h[i]
        si = s[i]
        dpi = dp  # local binding
        for j in range(x, hi - 1, -1):
            dp[j] = max(dp[j], dp[j - hi] + si)
    return dp[x]

n, x = map(int, input().split())
h = list(map(int, input().split()))
s = list(map(int, input().split()))
print(book_shop(n, x, h, s))
