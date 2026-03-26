INF = 10**9
import bisect
def solve(n, projects):
    dp = [0] * (n + 1)
    projects.sort(key = lambda x: x[1])
    ends = [p[1] for p in projects]

    for i in range(1, n + 1):
        a, b, m = projects[i - 1]
        j = bisect.bisect_left(ends, a)
        dp[i] = max(dp[i - 1], dp[j] + m)
    print(dp[n])

n = int(input())
projects = []
for _ in range(n):
    a, b, p = map(int, input().split())
    projects.append((a, b, p))
solve(n, projects)