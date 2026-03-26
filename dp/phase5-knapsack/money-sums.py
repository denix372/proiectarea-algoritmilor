
def solve(n, arr):
    s = sum(arr)
    dp =[[False] * (s + 1) for _ in range(n + 1)]
    cnt = 0
    res = []

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if j - arr[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]] 
            else:
                dp[i][j] = dp[i - 1][j]

    for j in range(1, s + 1):
        if dp[n][j]:
            cnt += 1
            res.append(j)

    print(cnt)
    print(*res)

n = int(input())
arr = list(map(int, input().split()))
solve(n, arr)

