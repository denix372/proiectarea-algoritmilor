#User function Template for python3

#User function Template for python3


class Solution:
    def arrangeTiles(self, n):
        if n <= 3:
            return 1
        elif n <= 4:
            return 2
            
        dp = [1] * n
        dp[3] = 2
        for i in range(4, n):
           dp[i] = dp[i - 1] + dp[i - 4]
        return dp[n - 1]
    

def arrangeTiles_in_logn(n):
    if n <= 3:
        return 1
    elif n <= 4:
        return 2
        
        
    A = [[1, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]]
    v = [2, 1, 1, 1]
        
    # multiplying 2 matrixes A * B
    def matmul(A, B):
        m, n, p = len(A), len(B), len(B[0])
        C = [[0] * p for _ in range(m)]
        for i in range(m):
            for k in range(n):
                for j in range(p):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    # multipling a matrix A with a vector
    def matvec(A, v):
        m, n = len(A), len(v)
        res = [0] * m
        for i in range(m):
            for j in range(n):
                res[i] += A[i][j] * v[j]
        return res
        
    def identity(n):
        I = [[0]*n for _ in range(n)]
        for i in range(n):
            I[i][i] = 1
        return I

    # Log n exponention
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
        
    res = matvec(matpow(A, n - 4), v)
    return res[0]
    

sol = Solution()
print(sol.arrangeTiles(19))
print(arrangeTiles_in_logn(19))