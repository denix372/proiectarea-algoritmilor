import bisect

def lis(n, nums):
    sol = []
    for i in range(n):
        j = bisect.bisect_left(sol, nums[i])
        if j == len(sol):
            sol.append(nums[i])
        else:
            sol[j] = nums[i]
    return len(sol)


n = int(input())
nums = list(map(int, input().split()))
print(lis(n, nums))