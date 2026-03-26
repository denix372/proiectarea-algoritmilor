def lcis(a, b):
    n, m = len(a), len(b)
    dp = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                best = 0

                for p in range(i):
                    for q in range(j):
                        if a[p] == b[q] and a[p] < a[i]:
                            best = max(best, dp[p][q])
                dp[i][j] = best + 1
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0
    return ans

# Optimized
def lcis2(a, b):
    n, m = len(a), len(b)
    dp = [0] * m 
    for i in range(n):
        best = 0
        for j in range(m):
            if a[i] == b[j]:
               dp[j] = best + 1
            elif a[i] > b[j]:
                best = max(best, dp[j])
    return max(dp)

def lcis3(a, b):
    n, m = len(a), len(b)
    dp = [0] * m 
    p = [-1] * m
    for i in range(n):
        best = 0
        idx = -1
        for j in range(m):
            if a[i] == b[j]:
               dp[j] = best + 1
               p[j] = idx
            elif a[i] > b[j]:
                if dp[j] > best:
                    best = dp[j]
                    idx = j
    j = dp.index(max(dp))
    sol = []
    while j != -1:
        sol.append(b[j])
        j = p[j]
    sol.reverse()
    return sol

a = [3, 4, 9, 1]
b = [5, 3, 8, 9, 10, 2, 1]
    
print(lcis(a, b))
print(lcis2(a, b))
print(lcis3(a, b))
