from collections import defaultdict

def solve(nums, k):
    d = {0 : -1}
    res = prefix = 0

    for i, x in enumerate(nums):
        prefix += x
        if prefix - k in d:
            res = max(res, i - d[prefix - k])
        if prefix not in d:
            d[prefix] = i

    return res

nums = [1,-1,5,-2,3]
k = 3
print(solve(nums, k))