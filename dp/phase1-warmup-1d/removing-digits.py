#greedy 
def remove_digits(n):
    cnt = 1
    while(n > 9):
        digits = map(int, list(str(n)))
        n = n - max(digits)
        cnt += 1
    return cnt

def remove_digits2(n):
    dp = [10**9] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for d in str(i):
            dp[i] = min(dp[i], dp[i - int(d)] + 1)

    return dp[n]


n = int(input())
print(remove_digits2(n))