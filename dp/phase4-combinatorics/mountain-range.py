import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    h = [int(x) for x in input_data[1:]]

    L = [-1] * n
    stack = []
    for i in range(n):
        while stack and h[stack[-1]] <= h[i]:
            stack.pop()
        if stack:
            L[i] = stack[-1]
        stack.append(i)

    R = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and h[stack[-1]] <= h[i]:
            stack.pop()
        if stack:
            R[i] = stack[-1]
        stack.append(i)
        
    dp = [1] * n
    indices = sorted(range(n), key=lambda x: h[x])
    
    for i in indices:
        if L[i] != -1:
            if dp[i] + 1 > dp[L[i]]:
                dp[L[i]] = dp[i] + 1
                
        if R[i] != -1:
            if dp[i] + 1 > dp[R[i]]:
                dp[R[i]] = dp[i] + 1
                
    print(max(dp) if n > 0 else 0)

if __name__ == '__main__':
    solve()