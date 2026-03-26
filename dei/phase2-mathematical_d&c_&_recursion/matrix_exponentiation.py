

def multiply(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])

    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][k] = A[i][j] * B[j][k]
    return C

def add(A, B):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            A[i][j] += B[i][j]
    return A

def exp(A, e):
    n = len(A)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1

    while e > 0:
        if e & 1:
            res = multiply(res, A) 
        A = multiply(A, A)
        e >>= 1
    return res


mat1 = [
        [1, 2],
        [4, 5]
    ]

print(exp(mat1, 5))