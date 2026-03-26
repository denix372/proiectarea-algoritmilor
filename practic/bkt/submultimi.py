
def solve(nums):
    res = []
    sol = []
    def bkt(i):
        if i >= len(nums):
            if sol:
                res.append(sol.copy())
            return
            
        sol.append(nums[i])
        bkt(i + 1)
        sol.pop()
        bkt(i + 1)
    bkt(0)
    res.sort()
    return res

n = int(input())
for r in solve([i for i in range(1, n + 1)]):
    print(*r)