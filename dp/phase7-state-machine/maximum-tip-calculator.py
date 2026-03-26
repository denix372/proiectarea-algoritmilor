N = 0
X = 0
Y = 0

A_right_sum = []
B_right_sum = []
# vector<unordered_map<int, unordered_map<int, int> > > mem;
# vector<unordered_map<int, unordered_map<int, bool> > > vis;
dp = []
vis = []

## Function to check if visited before
def get_vis_val(i, x, y):
    if (i == N):
        return True
    if(x not in vis[i]):
        return False
    if(y not in vis[i][x]):
        return False
    return vis[i][x][y]

## Function to return the tip value
def get_mem_val(i, x, y):
    if (i == N):
        return 0
    if(x not in dp[i]):
        return 0
    if(y not in dp[i][x]):
        return 0
    return dp[i][x][y]

## Function to calculate the maximum tip possible
def find_ans(i, x, y, A, B):

    ## If already visited
    if (get_vis_val(i, x, y)):
        return;

    if(x not in vis[i]):
        vis[i][x] = {}
    vis[i][x][y] = True

    ## If X cannot take more orders
    if (x == 0):
        if(x not in dp[i]):
            dp[i][x] = {}
        dp[i][x][y] = B_right_sum[i]

    ## If Y cannot take more orders
    elif (y == 0):
        if(x not in dp[i]):
            dp[i][x] = {}
        dp[i][x][y] = A_right_sum[i]

    ## If both can take orders then
    ## calculate the maximum of two
    else:
        find_ans(i + 1, x - 1, y, A, B)
        find_ans(i + 1, x, y - 1, A, B)
        if(x not in dp[i]):
            dp[i][x] = {}
        dp[i][x][y] = max(get_mem_val(i + 1, x - 1, y) + A[i], get_mem_val(i + 1, x, y - 1) + B[i])

## Driver code
if __name__=='__main__':

    a = [ 1, 2, 3, 4, 5 ]
    b = [ 5, 4, 3, 2, 1 ]
    N = len(a)
    X = 3
    Y = 3

    ## Vector containing the tips of waiter X
    A = []
    for i in range(0, N):
        A.append(a[i])

    ## Vector containing the tips of waiter Y
    B = []
    for i in range(0, N):
        B.append(b[i])

    ## Memory allocation and clearing
    ## of previous caches
    dp.clear();
    for i in range(0, N+1):
        dp.append({})

    vis.clear();
    for i in range(0, N+1):
        vis.append({})

    for i in range(0, N):
        A_right_sum.append(0)
        B_right_sum.append(0)

    A_right_sum[N - 1] = A[N - 1]
    B_right_sum[N - 1] = B[N - 1]

    ## Precalculation of sums
    ## of tip at each ith order
    for i in range(N-2, -1, -1):
        A_right_sum[i] = A_right_sum[i + 1] + A[i]
        B_right_sum[i] = B_right_sum[i + 1] + B[i]

    ## Bottom up dp based solution
    find_ans(0, X, Y, A, B)

    ## Final ans stored in mem[0][X][Y]
    print(get_mem_val(0, X, Y))
