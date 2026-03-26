
# O(4 ^ n) approach
def SumOverSubsets(n, a):
    m = 1 << n
    dp = [0] * m
    
    for x in range(m): 
        # iterate for all possible bitwise subsets
        for i in range(m):
            if ((x & i) == i):
                dp[x] += a[i]

    print(*dp)

# O (n * 2 ^ n) approach
def SumOverSubsets2(n, a):
    m = (1 << n)
    dp = [0]* m

    # iterate for all possible x
    for x in range(m):
        dp[x] = a[0]
        
        # iterate for the bitwise subsets only
        i = x

        while i > 0:
          dp[x] += a[i]
          i = ((i - 1) & x)

    print(*dp)

a = [7, 12, 14, 16]
n = 2
SumOverSubsets(n, a)
SumOverSubsets2(n, a)