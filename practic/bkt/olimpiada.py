

n, k = map(int, input().split())
pb = [float(input()) for _ in range(n)]

def solve(n, k, nums):
    res = []
    s = 0
    cnt =0

    def back(sol, prod, index):
        nonlocal s, cnt
        if len(sol) == k:
            s += prod
            cnt += 1

        for i in range(index, n):
            sol.append(nums[i])
            back(sol, nums[i] * prod, i + 1)
            sol.pop()
    back([], 1.0, 0)
    print(f"{s/cnt:.5f}")

solve(n, k, pb)