def solve(n, nums):
    res = []
    
    def bkt(domain, sol):
        if len(sol) == n:
            res.append(sol.copy())
        
        for i in range(len(domain)):
            if sol and domain[i] % 2 == sol[-1] % 2:
                continue
            new_sol = sol.copy()
            new_domain = domain.copy()
            new_sol.append(domain[i])
            new_domain.pop(i)
            bkt(new_domain, new_sol)
    
    bkt(nums, [])
    for r in res:
        print(*r)


n = int(input())
if n == 0:
    print(-1)
else:
    solve(n, [i for i in range(1, n + 1)])