MOD = 666013

def matmul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] != 0:
                for j in range(n):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def matpow(M, e):
    n = len(M)
    R = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while e:
        if e % 2 == 1:
            R = matmul(R, M)
        M = matmul(M, M)
        e = e // 2
    return R


def solve(n):
    if n == 1:
        return 2
    if n == 2:
        return 3

    M = [[1,1],
         [1,0]]
    R = matpow(M, n - 2)

    dp2 = 3
    dp1 = 2

    return (R[0][0]*dp2 + R[0][1]*dp1) % MOD

n = int(input())
print(solve(n))
