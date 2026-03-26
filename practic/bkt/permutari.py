

def solve(nums):
    res = []
    n = len(nums)

    def bkt(domain, sol):
        if len(sol) == n:
            res.append(sol.copy())
            return

        for i in range(len(domain)):
            new_sol = sol.copy()
            new_domain = domain.copy()
            new_sol.append(domain[i])
            new_domain.pop(i)
            bkt(new_domain, new_sol)
    bkt(nums, [])
    return res

n = int(input())

for r in solve([i for i in range(1, n + 1)]):
    print(*r)