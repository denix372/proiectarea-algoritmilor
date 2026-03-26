
def solve(n, m, a, b):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1] 
            else:
                dp[i][j] =  max(dp[i -1][j],
                                dp[i][j -1],)
    res = dp[n][m]
    i = n
    j = m
    sol = []
    while i != 0 and j != 0:
        if a[i - 1] == b[j - 1]:
            sol.append(a[i - 1])
            i -=1
            j -=1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    sol.reverse()
    print(res)
    print(*sol)
   
n, m = map(int, input().split())
a = list(map(int, input().split()))
b =  list(map(int, input().split()))
solve(n, m, a, b)