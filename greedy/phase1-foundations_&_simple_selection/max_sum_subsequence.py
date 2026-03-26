

def max_sum(arr):
    n = len(arr)
    m = max(arr)
    if m <= 0:
        return m

    res = 0
    for x in arr:
        if x > 0:
            res += x
    return res


arr = [ -2, 11, -4, 2, -3, -10 ]
print(max_sum(arr))