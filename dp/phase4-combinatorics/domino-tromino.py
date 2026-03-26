MOD = 10**9 + 7
class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1] * n
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        for i in range(3, n):
            dp[i] = (2 * dp[i - 1] % MOD) + (dp[i - 3] % MOD)
        return dp[n - 1] % MOD
    
# Optimized
MOD = 10**9 + 7

def matmul(A, B):
    m, n, p = len(A), len(B), len(B[0])
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for k in range(n):
            for j in range(p):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def matvec(A, v):
    m, n = len(A), len(v)
    res = [0] * m
    for i in range(m):
        for j in range(n):
            res[i] = (res[i] + A[i][j] * v[j]) % MOD
    return res

def identity(n):
    I = [[0]*n for _ in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I

def matpow(A, exp):
    if exp == 0:
        return identity(len(A))
    if exp == 1:
        return A
    half = matpow(A, exp // 2)
    half_sq = matmul(half, half)
    if exp % 2 == 0:
        return half_sq
    else:
        return matmul(A, half_sq)

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        M = [
            [2, 0, 1],
            [1, 0, 0],
            [0, 1, 0]
        ]

        Mn = matpow(M, n - 3)
        V3 = [5, 2, 1]
        result = matvec(Mn, V3)
        return result[0] % MOD
        

sol = Solution()
print(sol.numTilings(7))