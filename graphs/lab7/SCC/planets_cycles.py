import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def planets_cycles(n, t):
    color = [0] * (n + 1)
    ans = [0] * (n + 1)
    def dfs(u):
        stack = []
        while True:
            stack.append(u)
            color[u] = 1
            v = t[u]

            if color[v] == 0:
                u = v
                continue
        
            if color[v] == 1:
                cycle = []
                while True:
                    x = stack.pop()
                    cycle.append(x)
                    if x == v:
                        break
                cycle_len = len(cycle)
                for x in cycle:
                    ans[x] = cycle_len
                    color[x] = 2

                while stack:
                    x = stack.pop()
                    ans[x] = ans[t[x]] + 1
                    color[x] = 2
                return     
            if color[v] == 2:
                while stack:
                    x = stack.pop()
                    ans[x] = ans[t[x]] + 1
                    color[x] = 2
                return
    for i in range(1, n + 1):
        if color[i] == 0:
            dfs(i)
    return ans[1:]


n = int(input())
t = [0] + list(map(int, input().split()))

result = planets_cycles(n, t)
print(*result)
