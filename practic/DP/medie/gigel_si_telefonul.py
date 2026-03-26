INF = 10**9
def solve(n, x, v):
    cost = 0
    battery = 0
    
    for i in range(n):
        nxt = -1
        for j in range(i + 1, n):
            if v[j] < v[i]:
                nxt = j
                break

        if nxt != -1:
            best = nxt - i
        else:
            best = n - i
        
        if battery < best:
            charge = min(x, best) - battery
            cost += charge * v[i]
            battery += charge
        battery -= 1
    print(cost)

n, x = map(int, input().split())
v = list(map(int, input().split()))
solve(n, x, v)